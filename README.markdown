# 📦🌐 Flask ProductManager: Web & API Catalog App 🛍️
_A Flask-based web application for managing a product catalog, featuring user authentication, a dashboard for CRUD operations, and a REST API, with session management and JSON file data storage._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

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

**Flask ProductManager** is a web application based on **Flask** (Python), designed for managing a product catalog. It enables user registration and login (with session support), as well as product management (CRUD) via a web panel and REST API. Product and user data are stored in JSON files. Project created by Adrian Leśniak.

<br> 
<p align="center">
  <img src="screenshots/1.gif" width="90%">
</p>
<br>

## ✨ Key Features

*   🔑 **User authentication and session management**:
    *   User registration and login.
    *   User sessions handled by Flask.
    *   User data stored in `users.json` (passwords in plain text – should be improved for production).
*   📦 **Product catalog management (CRUD)**:
    *   **View products**: Dashboard with a list of all products.
    *   **Add products**: Form for adding new products (name, description, price, category).
    *   **Edit products**: Ability to edit existing products.
    *   **Delete products**: Delete products with confirmation.
    *   All operations available via the web panel and REST API.
*   📡 **REST API**:
    *   `GET /api/products` – get a list of all products.
    *   `POST /api/add_product` – add a new product (JSON).
    *   `PUT /api/edit_product/<id>` – edit a product by ID (JSON).
    *   `DELETE /api/edit_product/<id>` – delete a product by ID.
*   🖥️ **Interactive dashboard**:
    *   Central panel for managing products (after login).
    *   Intuitive forms and buttons for CRUD operations.
*   💬 **Flash messages**:
    *   User feedback (e.g., "Registration successful!", "Product added!").
*   📝 **HTML templates (Jinja2)**:
    *   Dynamic page generation: home, login, register, dashboard, add/edit product, error.

## 🖼️ Screenshots (Conceptual)

_(login, registration, dashboard, product form, sample API request)_

<p align="center">
  <img src="screenshots\1.jpg" width="300"/>
  <img src="screenshots\2.jpg" width="300"/>
  <img src="screenshots\3.jpg" width="300"/>
  <img src="screenshots\4.jpg" width="300"/>
  <img src="screenshots\5.jpg" width="300"/>
  <img src="screenshots\6.jpg" width="300"/>
  <img src="screenshots\7.jpg" width="300"/>
  <img src="screenshots\8.jpg" width="300"/>
  <img src="screenshots\9.jpg" width="300"/>
  <img src="screenshots\10.jpg" width="300"/>
</p>

## ⚙️ System Requirements & Dependencies

### Software:
*   **Python**: 3.7 or newer
*   **Libraries**:
    *   `Flask` (core web application)
    *   (All dependencies in `requirements.txt`)

### Installing dependencies:
*   Install via `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Installation and Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
    *(Replace `<repository-url>` and `<repository-directory>` with appropriate values)*

2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application**:
    ```bash
    python app.py
    ```
    *   By default, the app runs at `http://127.0.0.1:5000`.

## 💡 Usage Guide (Web Interface & API)

### Web Interface:

1.  Run the app: `python app.py`.
2.  Open your browser and go to `http://127.0.0.1:5000`.
3.  **Home page (`/` or `home.html`)**: Links to login and registration.
4.  **Registration (`/register`)**: Fill out the registration form. On success, a flash message will appear.
5.  **Login (`/login`)**: Enter your login details. On success, you will be redirected to the dashboard.
6.  **Dashboard (`/dashboard`)**: List of products, options to add, edit, and delete.
7.  **Add/Edit product (`/add_product`, `/edit_product/<id>`)**: Forms for entering/editing product data.
8.  **Logout (`/logout`)**: End the session.

### REST API Endpoints (e.g., testing via Postman/curl):

*   `GET /api/products` – list of products (JSON)
*   `POST /api/add_product` – add a product (body: JSON)
*   `PUT /api/edit_product/<id>` – edit a product (body: JSON)
*   `DELETE /api/edit_product/<id>` – delete a product

#### Example POST request:
```http
POST /api/add_product
Content-Type: application/json
{
  "name": "New product",
  "description": "Description",
  "price": 19.99,
  "category": "Drinks"
}
```

## 🗂️ Project File Structure

```
Projekt1/
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
├── products.json          # Product data (JSON)
├── users.json             # User data (JSON)
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── img/
└── templates/             # HTML templates (Jinja2)
    ├── base.html
    ├── home.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── add_product.html
    ├── edit_product.html
    └── error.html
```

## 📝 Important Notes & Considerations

*   **Authentication and passwords**: User passwords are stored in the JSON file in plain text – in production, use secure hashing and a database.
*   **Data persistence**: Products and users are saved in JSON files (`products.json`, `users.json`).
*   **HTML templates**: All views use templates in the `templates/` directory.
*   **Debug mode**: By default, the app runs in debug mode (`debug=True`). In production, set `debug=False`.
*   **API security**: In production, add authentication to API endpoints and input validation.
*   **CSRF protection**: Forms should be protected against CSRF (e.g., via Flask-WTF).

## 🤝 Contributing

Contributions are welcome! If you want to:
*   Add a database (e.g., SQLite, SQLAlchemy)
*   Implement secure password hashing
*   Expand the API or user panel
*   Improve validation and error handling
*   Enhance the frontend (CSS/JS)

1.  Fork the repository
2.  Create a new branch (`git checkout -b feature/FeatureName`)
3.  Make your changes
4.  Commit (`git commit -m 'Change description'`)
5.  Push the branch (`git push origin feature/FeatureName`)
6.  Open a Pull Request

Code should follow PEP8 and Flask best practices.

## 📃 License

Project under the **MIT** license. See the `LICENSE` file for details.

## 📧 Contact

Project: **Adrian Leśniak**
For questions or suggestions – open an issue on GitHub or contact directly.

---
🚀 _Building dynamic web applications and APIs with Flask!_
