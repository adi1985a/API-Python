# Product Management Application

## Overview
Product Management Application is a Flask-based web app for managing a product catalog. It supports user authentication (login/register), a dashboard to view products, and CRUD operations (add, edit, delete) through a web interface and REST API. Uses session management and test data for products.

## Features
- **User Authentication**: Login and registration with session management.
- **Product Management**: View, add, edit, and delete products via dashboard or API.
- **REST API**: Endpoints for listing, adding, editing, and deleting products (`/api/products`, `/api/add_product`, `/api/edit_product/<id>`, `/api/delete_product/<id>`).
- **Dashboard**: Displays product list with options to manage entries.
- **Flash Messages**: Provides feedback for actions like successful registration.

## Requirements
- Python 3.6+
- Libraries:
  - `Flask`

Install dependencies using:
```bash
pip install Flask
```

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required library (see Requirements).
3. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Launch the app and navigate to `http://localhost:5000` in a browser.
2. **Interface**:
   - **Home**: Access login or registration pages.
   - **Login/Register**: Enter credentials to access the dashboard (uses placeholder logic).
   - **Dashboard**: View products, add new ones, edit, or delete existing ones.
   - **Add/Edit Product**: Use forms to create or modify product details.
   - **Logout**: End the session and return to the login page.
3. **API Endpoints**:
   - `GET /api/products`: Retrieve all products.
   - `POST /api/add_product`: Add a new product (JSON payload).
   - `PUT /api/edit_product/<id>`: Update a product (JSON payload).
   - `DELETE /api/delete_product/<id>`: Delete a product.
4. Test data includes products like Cola-Cola, Pepsi, etc.

## File Structure
- `app.py`: Main Flask application script with routes, API endpoints, and logic.
- `templates/`: Directory containing HTML templates:
  - `home.html`: Homepage.
  - `login.html`: Login page.
  - `register.html`: Registration page.
  - `dashboard.html`: Product management dashboard.
  - `add_product.html`: Form for adding products.
  - `edit_product.html`: Form for editing products.
- `README.md`: This file, providing project documentation.

## Notes
- Authentication logic (login/register) is placeholder and needs integration with a database for production use.
- Product data is stored in memory (`products` list); a database (e.g., SQLite) is recommended for persistence.
- HTML templates are assumed to exist and include forms for user input and product management.
- The app runs in debug mode by default; disable it in production (`debug=False`).

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, open an issue on GitHub or contact the repository owner.