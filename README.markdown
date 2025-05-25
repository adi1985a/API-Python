# 📦🌐 Flask ProductManager: Web & API Catalog App 🛍️
_A Flask-based web application for managing a product catalog, featuring user authentication, a dashboard for CRUD operations, and a REST API, with session management and in-memory test data._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
<!-- Add badges for HTML/CSS/JS if custom frontend work is significant -->

## 📋 Table of Contents
1.  [Overview](#-overview)
2.  [Key Features](#-key-features)
3.  [Screenshots (Conceptual)](#-screenshots-conceptual)
4.  [System Requirements & Dependencies](#-system-requirements--dependencies)
5.  [Installation and Setup](#️-installation-and-setup)
6.  [Usage Guide (Web Interface & API)](#️-usage-guide-web-interface--api)
7.  [Project File Structure](#-project-file-structure)
8.  [Important Notes & Considerations](#-important-notes--considerations)
9.  [Contributing](#-contributing)
10. [License](#-license)
11. [Contact](#-contact)

## 📄 Overview

**Flask ProductManager** is a web application built with the **Flask** Python microframework, designed for managing a product catalog. Developed by Adrian Lesniak, it provides a user-friendly web interface for user authentication (login/registration using session management) and a dashboard for performing CRUD (Create, Read, Update, Delete) operations on products. Alongside the web interface, it exposes a **REST API** for programmatic interaction with the product data. The application currently uses in-memory test data (e.g., Cola-Cola, Pepsi) for products, with placeholder logic for user authentication, highlighting areas for database integration in a production environment.

## ✨ Key Features

*   🔑 **User Authentication & Session Management**:
    *   User registration and login functionality.
    *   Utilizes Flask sessions to manage user authentication state.
    *   *(Note: Authentication logic is currently placeholder and requires database integration for secure, persistent user accounts).*
*   📦 **Product Catalog Management (CRUD)**:
    *   **View Products**: A dashboard displays a list of all products.
    *   **Add Products**: Users can add new products through a dedicated form.
    *   **Edit Products**: Existing product details can be modified.
    *   **Delete Products**: Products can be removed from the catalog.
    *   These operations are available via both the web dashboard and the REST API.
*   📡 **REST API Endpoints**:
    *   `GET /api/products`: Retrieve a list of all products.
    *   `POST /api/add_product`: Add a new product (expects JSON payload).
    *   `PUT /api/edit_product/<id>`: Update an existing product identified by its ID (expects JSON payload).
    *   `DELETE /api/delete_product/<id>`: Delete a product identified by its ID.
*   🖥️ **Interactive Web Dashboard**:
    *   A central dashboard for authenticated users to view and manage the product list.
    *   Provides intuitive forms and buttons for add, edit, and delete operations.
*   💬 **Flash Messaging**:
    *   Uses Flask's flash messaging system to provide user feedback for actions (e.g., "Registration successful!", "Product added!").
*   📝 **HTML Templating**:
    *   Utilizes Flask's templating engine (Jinja2 by default) to render dynamic HTML pages for home, login, registration, dashboard, and product forms.

## 🖼️ Screenshots (Conceptual)

**Coming soon!**

_This section would ideally show screenshots of: the login/registration pages, the main product dashboard, the form for adding/editing a product, and an example of an API request/response (e.g., using Postman or curl)._

## ⚙️ System Requirements & Dependencies

### Software:
*   **Python**: Version 3.6 or higher.
*   **Libraries**:
    *   `Flask`: The core web framework.
    *   (Typically `Flask-WTF` for forms, `Flask-SQLAlchemy` for database ORM, `Werkzeug` for password hashing would be used in a more complete version, but are not explicitly listed beyond Flask itself).

### Installation:
*   Dependencies are installed using `pip`.

## 🛠️ Installation and Setup

1.  **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
    *(Replace `<repository-url>` and `<repository-directory>` with your specific details).*

2.  **Set Up a Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Required Libraries**:
    ```bash
    pip install Flask
    # If a requirements.txt file is provided:
    # pip install -r requirements.txt
    ```

4.  **Prepare `app.py` and Templates**:
    *   Ensure `app.py` (containing the Flask application logic, routes, and API endpoints) is in the project root.
    *   Verify that the `templates/` directory exists and contains all necessary HTML template files (`home.html`, `login.html`, `register.html`, `dashboard.html`, `add_product.html`, `edit_product.html`).

5.  **Run the Flask Application**:
    Open a terminal in the project's root directory and execute:
    ```bash
    python app.py
    ```
    *   The application will typically start a development server (often on `http://localhost:5000`).
    *   The terminal will indicate the address where the application is running.

## 💡 Usage Guide (Web Interface & API)

### Web Interface:

1.  Launch the application by running `python app.py`.
2.  Open your web browser and navigate to `http://localhost:5000` (or the address shown in your terminal).
3.  **Homepage (`/` or `home.html`)**: Provides links to "Login" or "Register".
4.  **Registration (`/register`)**:
    *   Fill in the registration form (e.g., username, password).
    *   Upon submission, you should receive a flash message indicating success (or failure if validation is implemented).
5.  **Login (`/login`)**:
    *   Enter your registered credentials.
    *   Successful login will redirect you to the dashboard and establish a session.
6.  **Dashboard (`/dashboard`)**:
    *   View a list of current products (initially from test data like "Cola-Cola," "Pepsi").
    *   Options to "Add New Product," "Edit" an existing product, or "Delete" a product.
7.  **Add/Edit Product (`/add_product`, `/edit_product/<id>`)**:
    *   Use the provided forms to enter or modify product details (e.g., name, price, description).
8.  **Logout (`/logout`)**:
    *   Ends the current user session and typically redirects to the login or home page.

### REST API Endpoints (Test with tools like Postman, Insomnia, or `curl`):

*   **`GET /api/products`**:
    *   Retrieves a JSON list of all products.
*   **`POST /api/add_product`**:
    *   Adds a new product.
    *   **Request Body (JSON)**: e.g., `{"name": "New Product", "price": 19.99, "description": "A cool new item"}`
*   **`PUT /api/edit_product/<id>`**:
    *   Updates an existing product identified by its `<id>`.
    *   **Request Body (JSON)**: e.g., `{"name": "Updated Product Name", "price": 24.99}`
*   **`DELETE /api/delete_product/<id>`**:
    *   Deletes the product identified by `<id>`.

## 🗂️ Project File Structure

*   `app.py`: The main Flask Python script. Contains route definitions, view functions, API endpoint logic, and interaction with product data.
*   `templates/` (directory): Contains HTML templates rendered by Flask:
    *   `home.html`: The homepage.
    *   `login.html`: User login form.
    *   `register.html`: User registration form.
    *   `dashboard.html`: Main product management interface for authenticated users.
    *   `add_product.html`: Form for adding new products.
    *   `edit_product.html`: Form for editing existing products.
    *   (Potentially a `layout.html` or `base.html` for common template structure).
*   `README.md`: This documentation file.
*   (Potentially `static/` directory for CSS, JS, images if not using CDNs exclusively).

## 📝 Important Notes & Considerations

*   **Placeholder Authentication**: The user authentication logic (login/register) is noted as a **placeholder**. For a production application, this **must** be integrated with a secure database (e.g., using SQLAlchemy with Flask-Login or Flask-Security) to store hashed passwords and manage user accounts properly.
*   **In-Memory Product Data**: Product data is currently stored in an in-memory Python list (e.g., `products = [...]`). This data will be lost when the Flask application restarts. For persistence, a database (SQLite, PostgreSQL, MySQL) should be integrated, typically using an ORM like SQLAlchemy.
*   **HTML Templates**: The functionality relies on the existence and correct structure of the HTML templates within the `templates/` directory. These templates would use Jinja2 syntax for dynamic content.
*   **Debug Mode**: The Flask application runs in `debug=True` mode by default for development. **This must be set to `debug=False` in a production environment** for security and performance reasons.
*   **API Security**: For production APIs, consider adding authentication (e.g., token-based) and proper input validation/sanitization to all API endpoints.
*   **CSRF Protection**: While Flask provides CSRF protection (often via Flask-WTF), ensure it's correctly implemented for all forms that modify state.

## 🤝 Contributing

Contributions to **Flask ProductManager** are highly encouraged! If you have ideas for:

*   Implementing database persistence for users and products (e.g., using SQLite and SQLAlchemy).
*   Enhancing user authentication with secure password hashing and session management.
*   Adding more features to the product catalog (e.g., categories, images, search).
*   Improving the REST API with more robust validation and error handling.
*   Adding frontend styling or using a JavaScript framework for a richer UI.

1.  Fork the repository.
2.  Create a new branch for your feature (`git checkout -b feature/DatabaseIntegration`).
3.  Make your changes to the Python scripts and HTML templates.
4.  Commit your changes (`git commit -m 'Feature: Implement SQLite database for products'`).
5.  Push to the branch (`git push origin feature/DatabaseIntegration`).
6.  Open a Pull Request.

Please ensure your code is well-commented and follows Python (PEP 8) and Flask best practices.

## 📃 License

This project is licensed under the **MIT License**.
(If you have a `LICENSE` file in your repository, refer to it: `See the LICENSE file for details.`)

## 📧 Contact

Project concept by **Adrian Lesniak**.
For questions, feedback, or issues, please open an issue on the GitHub repository or contact the repository owner.

---
🚀 _Building dynamic web applications and APIs with Flask!_
