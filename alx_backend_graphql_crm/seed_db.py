

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_backend_graphql_crm.settings')
django.setup()

from crm.models import Customer, Product

def run():
    # Customers
    Customer.objects.create(name="John Doe", email="john@example.com", phone="+1234567890")
    Customer.objects.create(name="Jane Smith", email="jane@example.com")

    # Products
    Product.objects.create(name="Laptop", price=999.99, stock=5)
    Product.objects.create(name="Phone", price=499.99, stock=10)
    Product.objects.create(name="Headphones", price=59.99, stock=25)

    print("Database seeded successfully!")

if __name__ == "__main__":
    run()
