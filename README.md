# Flask Blog API

This project is a simple blog application built using Flask and SQLAlchemy, including features such as user authentication, CRUD operations for blog posts, and pagination. 

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Display a list of all blog posts with pagination
- Display a single blog post on a separate page

## Technologies Used

- Flask
- SQLAlchemy
- SQLite/MySQL/PostgreSQL
- Flask-JWT-Extended for JWT-based authentication
- Flask-Paginate for pagination

## Project Structure

\`\`\`
blog_api/
├── __init__.py
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── wsgi.py
└── create_db.py
\`\`\`

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:

    \`\`\`bash
    git clone https://github.com/your-username/flask-blog-api.git
    cd flask-blog-api
    \`\`\`

2. **Create a virtual environment**:

    \`\`\`bash
    python -m venv venv
    \`\`\`

3. **Activate the virtual environment**:

    - On Windows:

        \`\`\`bash
        venv\Scripts\activate
        \`\`\`

    - On macOS/Linux:

        \`\`\`bash
        source venv/bin/activate
        \`\`\`

4. **Install the dependencies**:

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

### Configuration

Configure your application settings in \`config.py\`. By default, the application uses SQLite. You can switch to MySQL or PostgreSQL by changing the \`SQLALCHEMY_DATABASE_URI\`.

**\`config.py\`**:

\`\`\`python
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret_key')
\`\`\`

### Database Setup

1. **Initialize the database**:

    \`\`\`bash
    python create_db.py
    \`\`\`

This will create the database tables defined in your \`models.py\` file.

### Running the Application

1. **Set the FLASK_APP environment variable**:

    - On Windows:

        \`\`\`bash
        set FLASK_APP=blog_api
        \`\`\`

    - On macOS/Linux:

        \`\`\`bash
        export FLASK_APP=blog_api
        \`\`\`

2. **Run the Flask application**:

    \`\`\`bash
    flask run
    \`\`\`

The application should now be running at \`http://127.0.0.1:5000\`.

## API Endpoints

### User Authentication

- **Register a new user**:

    \`\`\`http
    POST /register
    \`\`\`

    **Request body**:
    
    \`\`\`json
    {
        "username": "your_username",
        "email": "your_email",
        "password": "your_password"
    }
    \`\`\`

- **Login**:

    \`\`\`http
    POST /login
    \`\`\`

    **Request body**:

    \`\`\`json
    {
        "username": "your_username",
        "password": "your_password"
    }
    \`\`\`

- **Logout**:

    \`\`\`http
    POST /logout
    \`\`\`

    **Headers**:

    \`\`\`http
    Authorization: Bearer <access_token>
    \`\`\`

### Blog Posts

- **Get all posts with pagination**:

    \`\`\`http
    GET /posts
    \`\`\`

    **Query parameters**:

    - \`page\`: The page number (default is 1)
    - \`per_page\`: Number of posts per page (default is 10)

- **Get a single post**:

    \`\`\`http
    GET /posts/<id>
    \`\`\`

- **Create a new post**:

    \`\`\`http
    POST /posts
    \`\`\`

    **Headers**:

    \`\`\`http
    Authorization: Bearer <access_token>
    \`\`\`

    **Request body**:

    \`\`\`json
    {
        "title": "Post title",
        "content": "Post content"
    }
    \`\`\`

- **Update a post**:

    \`\`\`http
    PUT /posts/<id>
    \`\`\`

    **Headers**:

    \`\`\`http
    Authorization: Bearer <access_token>
    \`\`\`

    **Request body**:

    \`\`\`json
    {
        "title": "Updated title",
        "content": "Updated content"
    }
    \`\`\`

- **Delete a post**:

    \`\`\`http
    DELETE /posts/<id>
    \`\`\`

    **Headers**:

    \`\`\`http
    Authorization: Bearer <access_token>
    \`\`\`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to me at [shubhu2961@gmail.com].
