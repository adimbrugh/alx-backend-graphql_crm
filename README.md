📌 ALX Backend GraphQL CRM

This project is a step-by-step learning journey to understand GraphQL with Django using Graphene-Django.
It follows structured tasks to progressively build a CRM-style API with best practices.

---

🚀 Project Setup
1. Clone Repo
git clone https://github.com/adimbrugh/alx-backend-graphql_crm.git
cd alx-backend-graphql_crm

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Requirements
pip install -r requirements.txt

---

📖 Tasks
Task 0: Set Up GraphQL Endpoint

Objective:
Set up a GraphQL endpoint and define your first schema and query.

Steps:

Create Django project alx-backend-graphql_crm.

Create app crm.

Install required libraries:

pip install graphene-django django-filter


Define schema in alx_backend_graphql_crm/schema.py:

Query with field hello: String returning "Hello, GraphQL!".

Connect endpoint in urls.py:

path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),


Visit http://localhost:8000/graphql
 and run:

{
  hello
}


✅ Checkpoint: Should return:

{
  "data": {
    "hello": "Hello, GraphQL!"
  }
}

---

Task 1: Define CRM Models

Objective:
Create basic models for a CRM system.

Models:

Customer → name, email, phone, created_at

Order → product_name, amount, created_at, customer (FK)

✅ Checkpoint: Run python manage.py makemigrations && python manage.py migrate.

---

Task 2: Expose Models via GraphQL

Objective:
Expose CRM models in GraphQL schema.

Steps:

Use graphene_django.DjangoObjectType.

Add query fields for all_customers and all_orders.

Query example:

{
  allCustomers {
    id
    name
    email
  }
}

✅ Checkpoint: Returns list of customers.

---

Task 3: Add Filtering & Pagination

Objective:
Enhance queries with filters and pagination.

Steps:

Install django-filter.

Add filters for Customer (by name, email).

Add pagination (first, skip).

✅ Checkpoint: Query filtered customers by email substring.

---

Task 4: Create Mutations

Objective:
Allow creating and updating data via GraphQL mutations.

Steps:

Define CreateCustomer mutation.

Define UpdateCustomer mutation.

Example query:

mutation {
  createCustomer(name: "Alice", email: "alice@example.com", phone: "12345") {
    customer {
      id
      name
      email
    }
  }
}

✅ Checkpoint: Customer is saved in DB.

---

Task 5: Relationships in GraphQL

Objective:
Expose relationships between models.

Steps:

Add orders field inside CustomerType.

Query example:

{
  allCustomers {
    name
    orders {
      productName
      amount
    }
  }
}

✅ Checkpoint: Each customer shows related orders.

---

Task 6: Authentication & Permissions

Objective:
Secure GraphQL queries with authentication.

Steps:

Enable Django authentication.

Restrict mutations to logged-in users.

Example:

mutation {
  createOrder(productName: "Laptop", amount: 1200, customerId: 1) {
    order {
      id
      productName
    }
  }
}

✅ Checkpoint: Unauthorized users cannot create orders.

---

🛠 Tools & Libraries

Django 5.1

Graphene-Django

Django Filters

GraphiQL (Interactive Playground)

---

📌 Real-World Use Cases

CRM Systems (Customers & Orders)

Blog APIs (Posts, Comments, Tags)

Social Media Apps (Users, Posts, Likes)

E-commerce APIs (Products, Categories, Orders)

---

📜 License

MIT License