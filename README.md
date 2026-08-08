# Book Management System — Backend (Django + DRF + MySQL + JWT)

## Setup

1. Create & activate a virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Create a MySQL database
   ```sql
   CREATE DATABASE book_management_db CHARACTER SET utf8mb4;
   ```

4. Copy `.env.example` to `.env` and fill in your real values
   ```
   cp .env.example .env
   ```

5. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create an admin user (optional)
   ```
   python manage.py createsuperuser
   ```

7. Run the server
   ```
   python manage.py runserver
   ```
   API is now live at http://127.0.0.1:8000/api/

## API Endpoints

| Method | Endpoint                  | Description                  |
|--------|----------------------------|-------------------------------|
| POST   | /api/auth/register/       | Register a new user          |
| POST   | /api/auth/login/          | Login, returns JWT tokens    |
| POST   | /api/auth/refresh/        | Refresh access token         |
| GET    | /api/auth/me/             | Current logged-in user       |
| GET    | /api/books/                | List books (paginated)       |
| POST   | /api/books/                | Create a book (auth required)|
| GET    | /api/books/:id/            | Book details                 |
| PUT    | /api/books/:id/            | Update book (owner only)     |
| DELETE | /api/books/:id/            | Delete book (owner only)     |

Query params on `/api/books/`:
- `?search=harry` — search by title/author
- `?genre=Fiction` — filter by genre
- `?ordering=publication_date` or `?ordering=-publication_date` — sort
- `?page=2` — pagination
