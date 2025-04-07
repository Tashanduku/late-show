# Episodes API

A Flask RESTful API for managing  episodes, guests, and their appearances.


## Features

- SQLAlchemy ORM for database interactions
- Flask-Migrate for database migrations
- CRUD operations for podcast episodes
- Guest management
- Track appearances of guests on episodes with ratings


## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install flask flask-sqlalchemy flask-migrate flask-restful
   ```

4. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Running the Application

Run the application using Python directly:
```
python app.py
```

This will start the server on port 8080 with debug mode enabled.

Alternatively, use the Flask CLI (note: this will use the default port 5000 unless specified):
```
flask run --port=8080
```

## API Endpoints

### Root
- `GET /` - Welcome message and available endpoints

### Episodes
- `GET /episodes` - List all episodes
- `GET /episodes/<id>` - Get a specific episode by ID, including its appearances

### Guests
- `GET /guests` - List all guests

### Appearances
- `POST /appearances` - Create a new appearance with the following JSON structure:
  ```json
  {
    "rating": integer (1-5),
    "episode_id": integer,
    "guest_id": integer
  }
  ```

## Data Models

### Episode
- `id`: Integer (Primary Key)
- `date`: String (e.g., "2023-01-15")
- `number`: Integer (Episode number)

### Guest
- `id`: Integer (Primary Key)
- `name`: String
- `occupation`: String

### Appearance
- `id`: Integer (Primary Key)
- `rating`: Integer (1-5)
- `episode_id`: Foreign Key to Episode
- `guest_id`: Foreign Key to Guest

## Development

### Database Migrations
After making changes to the models:
```
flask db migrate -m "Description of changes"
flask db upgrade
```

