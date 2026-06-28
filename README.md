# Customer Support Ticket Management API

A backend system for managing customer support tickets — built for the Teyzix Core Internship (BE-2 Task).

Customers can raise support tickets, agents can manage and resolve them, and admins can monitor overall support operations through dashboard statistics.

## Features

- **Authentication** — JWT-based register/login with role support (Customer, Agent, Admin)
- **User Management** — Profile view/update
- **Ticket Management** — Create, update, delete, assign, and track ticket status
- **Ticket Status Workflow** — Open → In Progress → Resolved → Closed
- **Ticket Replies** — Threaded conversation history per ticket with timestamps
- **Search & Filtering** — Filter by status, assigned agent; search by title/customer
- **Dashboard Statistics** — Total/open/in-progress/resolved/closed ticket counts, active agent count
- **Ticket Priority Levels** — Low/Medium/High/Urgent priority, settable on creation and updatable by agents/admins
- **Role-Based Access Control** — Customers see only their tickets, agents see only assigned tickets, admins see everything

## Tech Stack

- **Framework:** Django + Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Filtering:** django-filter

## Project Structure

```
ticketsystem/
├── accounts/       # Custom User model, auth APIs, profile
├── tickets/        # Ticket model, CRUD, assign, status, permissions
├── replies/        # Ticket conversation/reply system
├── dashboard/      # Aggregate statistics API
└── ticketsystem/   # Project settings, root URLs
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd ticketsystem
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_NAME=ticket_management_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

> After creating the superuser, set their `role` field to `admin` via the Django admin panel (`/admin/`) — it defaults to `customer`.

### 7. Run the development server

```bash
python manage.py runserver
```

API will be available at `http://127.0.0.1:8000/`

## Live Deployment

This API is deployed and live at: **https://bilalshaf.pythonanywhere.com/**

> Note: The root URL (`/`) returns a 404 by design — this is a pure REST API with no frontend. Use the endpoints listed below (e.g. `/api/auth/register/`, `/api/tickets/`) directly, or import the Postman collection to test against the live server.

## User Roles

| Role | Permissions |
|------|-------------|
| **Customer** | Create tickets, view/reply to own tickets |
| **Agent** | View/reply to assigned tickets, update status |
| **Admin** | Full access — view all tickets, assign agents, view dashboard stats |

## API Endpoints

### Authentication

| Method | Endpoint | Description | Access |
|--------|----------|--------------|--------|
| POST | `/api/auth/register/` | Register a new user | Public |
| POST | `/api/auth/login/` | Login, returns access + refresh tokens | Public |
| POST | `/api/auth/login/refresh/` | Refresh access token | Public |
| GET | `/api/auth/profile/` | View own profile | Authenticated |
| PATCH | `/api/auth/profile/` | Update own profile | Authenticated |

### Tickets

| Method | Endpoint | Description | Access |
|--------|----------|--------------|--------|
| GET | `/api/tickets/` | List tickets (filtered by role) | Authenticated |
| POST | `/api/tickets/` | Create a new ticket | Authenticated |
| GET | `/api/tickets/<id>/` | Get ticket detail | Authenticated |
| PUT/PATCH | `/api/tickets/<id>/` | Update ticket | Authenticated |
| DELETE | `/api/tickets/<id>/` | Delete ticket | Authenticated |
| PATCH | `/api/tickets/<id>/assign/` | Assign an agent to a ticket | Agent/Admin |
| PATCH | `/api/tickets/<id>/status/` | Update ticket status | Agent/Admin |
| PATCH | `/api/tickets/<id>/priority/` | Update ticket priority | Agent/Admin |

**Query parameters:** `?status=open`, `?priority=high`, `?assigned_agent=<id>`, `?search=<keyword>`

### Ticket Replies

| Method | Endpoint | Description | Access |
|--------|----------|--------------|--------|
| GET | `/api/tickets/replies/<ticket_id>/` | View conversation history | Related users only |
| POST | `/api/tickets/replies/<ticket_id>/` | Add a reply | Related users only |

### Dashboard

| Method | Endpoint | Description | Access |
|--------|----------|--------------|--------|
| GET | `/api/dashboard/stats/` | Total/open/resolved/closed ticket counts + active agents | Agent/Admin |

## Authentication

All protected endpoints require a JWT access token in the request header:

```
Authorization: Bearer <access_token>
```

## Testing

A Postman collection (`Ticket_Management_API.postman_collection.json`) is included in this repository, covering all endpoints with example request bodies.

## Bonus Features Implemented

- **Ticket Priority Levels** — Tickets support `low`, `medium`, `high`, and `urgent` priority. Customers can set priority on creation; agents/admins can update it via `/api/tickets/<id>/priority/`. Tickets can also be filtered by priority.

## Author

Bilal Shafqat — Teyzix Core Internship, BE-2 Task