


import os
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport



def log_crm_heartbeat():
    # Log message with timestamp
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{timestamp} CRM is alive\n"

    log_file = "/tmp/crm_heartbeat_log.txt"

    # Append the log message
    with open(log_file, "a") as f:
        f.write(log_message)

    # --- Optional: Check GraphQL hello field ---
    try:
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql/",  # Update to your actual GraphQL endpoint
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        query = gql(
            """
            query {
                hello
            }
            """
        )

        result = client.execute(query)
        gql_message = f"{timestamp} GraphQL hello response: {result.get('hello')}\n"

        # Append GraphQL result to the log
        with open(log_file, "a") as f:
            f.write(gql_message)

    except Exception as e:
        error_message = f"{timestamp} GraphQL query failed: {str(e)}\n"
        with open(log_file, "a") as f:
            f.write(error_message)

def update_low_stock():
    # GraphQL endpoint
    transport = RequestsHTTPTransport(
        url="http://127.0.0.1:8000/graphql/",
        use_json=True,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define mutation
    mutation = gql(
        """
        mutation {
            updateLowStockProducts {
                updatedProducts {
                    id
                    name
                    stock
                }
                message
            }
        }
        """
    )

    # Execute mutation
    response = client.execute(mutation)

    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_file = "/tmp/low_stock_updates_log.txt"

    with open(log_file, "a") as f:
        f.write(f"\n[{timestamp}] {response['updateLowStockProducts']['message']}\n")
        for product in response["updateLowStockProducts"]["updatedProducts"]:
            f.write(f" - {product['name']} (New Stock: {product['stock']})\n")
