# Phase-4-Code-Challenge-Superheroes

# Superheroes API

## Project Overview

The Superheroes API is a RESTful API that allows users to manage superheroes and their associated powers. This project is built using Flask and SQLAlchemy.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite

## Initial Setup

Follow these steps to set up the project on your local machine.

### Creating the Repository

2. **Clone the repository to your local machine**:
   ```bash
   git clone https://github.com/CGM123sherry/Phase-4-Code-Challenge-Superheroes
   cd superheroes-api
   ```

### Installation

1. **Create a virtual environment**:

   ```bash
   pyenv virtualenv 3.12.5 phase4env
   ```

2. **Activate the virtual environment**:

   ```bash
   pyenv activate phase4env
   ```

3. **Install the required dependencies**:

   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```

4. **Install Postman for API testing**:
   - Download Postman from [Postman's official website](https://www.postman.com/downloads/).

## Creating Models

In the `models.py` file, create the following models:

### Hero Model

### Power Model

### HeroPower Model

## Database Migration

1. **Initialize the migration repository**:

   ```bash
   flask db init
   ```

2. **Generate migration files**:

   ```bash
   flask db migrate -m "Initial migration."
   ```

3. **Apply the migration to the database**:
   ```bash
    flask db upgrade head
   ```

## Seeding the Database

To add initial data to your database, create a `seed.py` file:

```bash
 python seed.py
```

## Creating Routes

touch app.py to create the file.

create the necessary routes for the API. The routes should follow RESTful conventions:

- **home ('/')**
- **GET /heroes**: Retrieve all heroes.
- **GET /heroes/<id>**: Retrieve a specific hero by ID.
- **GET /powers**: Retrieve all powers.
- **GET /powers/<id>**: Retrieve a specific power by ID.
- **PATCH /powers/<id>**: Update a power's description.
- **POST /hero_powers**: Create a new HeroPower entry.

## Testing the Routes on browser

on the terminal, r:

**flask Run**
This will open:

- Serving Flask app 'app.py'
- Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
- Running on http://127.0.0.1:5555

follow the link.

## Testing Endpoints in Postman

Follow these steps to test your API endpoints using Postman:

1. **Open Postman** and create a new request.
2. Set the request type (GET, POST, etc.) and enter the appropriate URL.

GET Heroes: http://127.0.0.1:5555/heroes
GET Hero by ID: http://127.0.0.1:5555/heroes/1 (replace 1 with the actual hero ID you want to test)
GET Powers: http://127.0.0.1:5555/powers
GET Power by ID: http://127.0.0.1:5555/powers/1
PATCH Power: http://127.0.0.1:5555/powers/1 (to update a power with ID 1)
POST HeroPower: http://127.0.0.1:5555/hero_powers

3. If needed, set headers (e.g., `Content-Type: application/json`) and add a request body (for POST or PATCH requests).
4. Click **Send** and review the response in the lower section of the Postman window.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request.
