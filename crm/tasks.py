

import logging
from datetime import datetime
from celery import shared_task
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


# Setup logger
logger = logging.getLogger(__name__)

@shared_task
def generate_crm_report():
    # GraphQL Transport
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql/",
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # GraphQL query
    query = gql(
        """
        query {
            allCustomers {
                totalCount
            }
            allOrders {
                totalCount
                totalAmount
            }
        }
        """
    )

    try:
        response = client.execute(query)

        customers = response["allCustomers"]["totalCount"]
        orders = response["allOrders"]["totalCount"]
        revenue = response["allOrders"]["totalAmount"]

        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Report: {customers} customers, {orders} orders, {revenue} revenue\n"

        with open("/tmp/crm_report_log.txt", "a") as log_file:
            log_file.write(log_entry)

        logger.info("CRM Report Generated: %s", log_entry)
    except Exception as e:
        logger.error("Failed to generate CRM report: %s", e)
