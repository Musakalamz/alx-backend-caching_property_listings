# Caching in Django

This project implements a Django-based property listing application with Redis caching at multiple levels. The system demonstrates various caching strategies including view-level caching, low-level queryset caching, and proper cache invalidation techniques.

## Project Structure

- **alx_backend_caching_property_listings**: Main Django project directory.
- **properties**: Django app for managing property listings.
- **docker-compose.yml**: Docker configuration for PostgreSQL and Redis services.
- **requirements.txt**: Python dependencies.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd alx-backend-caching_property_listings
    ```

2.  **Start Docker containers:**
    ```bash
    docker-compose up -d
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **GET /properties/**: List all properties (Cached for 15 minutes).

## Caching Strategy

- **View-Level Caching**: The property list view is cached for 15 minutes using `@cache_page`.
- **Backend**: Redis is used as the caching backend.

## Database

- **PostgreSQL**: Used for persistent data storage.
