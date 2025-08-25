

#!/usr/bin/env python3
import sys
import logging
from datetime import datetime, timedelta

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Setup logging
LOG_FILE = "/tmp/order_reminders_log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    try:
        # GraphQL endpoint
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Calculate date range (last 7 days)
        today = datetime.now()
        last_week = today - timedelta(days=7)
        today_str = today.strftime("%Y-%m-%d")
        last_week_str = last_week.strftime("%Y-%m-%d")

        # GraphQL query for orders in last 7 days
        query = gql("""
        query GetRecentOrders($startDate: Date!, $endDate: Date!) {
            orders(orderDate_Gte: $startDate, orderDate_Lte: $endDate) {
                id
                customer {
                    email
                }
            }
        }
        """)

        variables = {"startDate": last_week_str, "endDate": today_str}
        result = client.execute(query, variable_values=variables)

        # Log each reminder
        orders = result.get("orders", [])
        if orders:
            for order in orders:
                log_message = f"Reminder: Order {order['id']} for {order['customer']['email']}"
                logging.info(log_message)
        else:
            logging.info("No recent orders found.")

        print("Order reminders processed!")

    except Exception as e:
        logging.error(f"Error processing order reminders: {e}")
        print("Error occurred. Check logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()