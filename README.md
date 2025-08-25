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

--- 

---

CRM GraphQL & Task Automation

This project extends the alx-backend-graphql_crm repository with GraphQL, scheduled cron jobs, and Celery tasks for CRM automation.

---

📌 Features Implemented
1. Add GraphQL to CRM

Installed graphene-django.

Added GraphQL endpoint at /graphql/.

Configured crm/schema.py with a root Query and mutations.

Verified with GraphiQL or Insomnia.

---

2. GraphQL Query for Hello Field

Defined a simple hello query in crm/schema.py that returns "Hello, world!".

Used to test the GraphQL endpoint responsiveness.

---

3. Scheduled GraphQL Mutation for Low Stock Products

Added UpdateLowStockProducts mutation in crm/schema.py.

Mutation finds products with stock < 10, increments by 10, and returns updated product list.

Created cron job in crm/cron.py with django-crontab to run every 12 hours.

Logs results in /tmp/low_stock_updates_log.txt.

CRONJOBS = [
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]

---

4. Celery Task for CRM Weekly Report

Installed celery and django-celery-beat.

Configured crm/celery.py with Redis broker.

Added crm/tasks.py with generate_crm_report task:

Queries GraphQL for total customers, orders, and revenue.

Logs to /tmp/crm_report_log.txt with timestamp.

Scheduled with Celery Beat to run every Monday at 06:00.

CELERY_BEAT_SCHEDULE = {
    'generate-crm-report': {
        'task': 'crm.tasks.generate_crm_report',
        'schedule': crontab(day_of_week='mon', hour=6, minute=0),
    },
}

---

5. Documentation & Setup Instructions
🔧 Installation
pip install -r requirements.txt
python manage.py migrate

🚀 Run GraphQL API
python manage.py runserver

⏰ Run Cron Jobs
# Add cron jobs
python manage.py crontab add  

# Show scheduled jobs
python manage.py crontab show  

# Remove cron jobs
python manage.py crontab remove

⚡ Run Celery & Celery Beat
# Start Redis (ensure redis-server is running)
redis-server

# Start Celery worker
celery -A crm worker -l info  

# Start Celery Beat
celery -A crm beat -l info

---

📜 Logs
Low stock updates → /tmp/low_stock_updates_log.txt
Weekly CRM report → /tmp/crm_report_log.txt