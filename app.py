"""
================================================================================
                    PRODUCT MANAGEMENT SYSTEM
================================================================================
Program enables product management through web interface.
Features: adding, editing, deleting products, login system,
file data save/load, error logging.

Author: Adrian Lesniak
Version: 2.0
Date: 2024
================================================================================
"""

import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional, Union
from flask import Flask, render_template, jsonify, request, redirect, session, flash, url_for, abort
from werkzeug.exceptions import HTTPException

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProductManager:
    """Class managing products with file save/load functionality"""
    
    def __init__(self, filename: str = 'products.json'):
        self.filename = filename
        self.products = self._load_products()
    
    def _load_products(self) -> List[Dict]:
        """Loads products from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    logger.info(f"Loaded {len(data)} products from file {self.filename}")
                    return data
            else:
                # Default products if file doesn't exist
                default_products = [
                    {"id": 1, "name": "Coca-Cola", "description": "Coca-Cola drink, 0.5l", "price": 3.50, "category": "Beverages"},
                    {"id": 2, "name": "Pepsi", "description": "Pepsi drink, 0.5l", "price": 3.20, "category": "Beverages"},
                    {"id": 3, "name": "Fanta", "description": "Fanta drink, 0.5l", "price": 3.00, "category": "Beverages"},
                    {"id": 4, "name": "Sprite", "description": "Sprite drink, 0.5l", "price": 3.00, "category": "Beverages"},
                    {"id": 5, "name": "Coca-Cola Zero", "description": "Coca-Cola Zero drink, 0.5l", "price": 3.50, "category": "Beverages"},
                ]
                self._save_products(default_products)
                return default_products
        except Exception as e:
            logger.error(f"Error loading products: {e}")
            return []
    
    def _save_products(self, products: List[Dict]) -> None:
        """Saves products to JSON file"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(products, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved {len(products)} products to file {self.filename}")
        except Exception as e:
            logger.error(f"Error saving products: {e}")
    
    def get_all_products(self) -> List[Dict]:
        """Returns all products"""
        return self.products
    
    def get_product_by_id(self, product_id: int) -> Optional[Dict]:
        """Returns product by ID"""
        return next((p for p in self.products if p['id'] == product_id), None)
    
    def add_product(self, name: str, description: str, price: float = 0.0, category: str = "Other") -> Dict:
        """Adds new product"""
        try:
            new_id = max([p['id'] for p in self.products], default=0) + 1
            new_product = {
                'id': new_id,
                'name': name,
                'description': description,
                'price': price,
                'category': category,
                'created_at': datetime.now().isoformat()
            }
            self.products.append(new_product)
            self._save_products(self.products)
            logger.info(f"Added new product: {name}")
            return new_product
        except Exception as e:
            logger.error(f"Error adding product: {e}")
            raise
    
    def update_product(self, product_id: int, name: str, description: str, price: float = 0.0, category: str = "Other") -> Optional[Dict]:
        """Updates product"""
        try:
            product = self.get_product_by_id(product_id)
            if product:
                product.update({
                    'name': name,
                    'description': description,
                    'price': price,
                    'category': category,
                    'updated_at': datetime.now().isoformat()
                })
                self._save_products(self.products)
                logger.info(f"Updated product ID {product_id}")
                return product
            return None
        except Exception as e:
            logger.error(f"Error updating product: {e}")
            raise
    
    def delete_product(self, product_id: int) -> bool:
        """Deletes product"""
        try:
            initial_count = len(self.products)
            self.products = [p for p in self.products if p['id'] != product_id]
            if len(self.products) < initial_count:
                self._save_products(self.products)
                logger.info(f"Deleted product ID {product_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting product: {e}")
            raise

class UserManager:
    """Class managing users with file save/load"""
    def __init__(self, filename: str = 'users.json'):
        self.filename = filename
        self.users = self._load_users()
        if not self.users:
            # Domyślni użytkownicy jeśli plik nie istnieje
            self.users = {
                'admin@example.com': {'password': 'admin123', 'name': 'Administrator', 'role': 'admin'},
                'user@example.com': {'password': 'user123', 'name': 'User', 'role': 'user'}
            }
            self._save_users()

    def _load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_users(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)

    def authenticate(self, email: str, password: str):
        if email in self.users and self.users[email]['password'] == password:
            user_data = self.users[email].copy()
            return {'email': email, 'name': user_data['name'], 'role': user_data['role']}
        return None

    def register_user(self, email: str, password: str, name: str) -> bool:
        if email not in self.users:
            self.users[email] = {'password': password, 'name': name, 'role': 'user'}
            self._save_users()
            return True
        return False

# Application initialization
app = Flask(__name__)
app.secret_key = '123312334512334545123345'

# Initialize managers
product_manager = ProductManager()
user_manager = UserManager()

def require_login(f):
    """Decorator requiring login"""
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('You must be logged in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def require_admin(f):
    """Decorator requiring admin privileges"""
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('You must be logged in to access this page.', 'error')
            return redirect(url_for('login'))
        
        if session['user'].get('role') != 'admin':
            flash('You need administrator privileges to perform this action.', 'error')
            return redirect(url_for('dashboard'))
        
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def is_admin():
    """Check if current user is admin"""
    return session.get('user', {}).get('role') == 'admin'

@app.errorhandler(404)
def not_found_error(error):
    """404 error handler"""
    logger.warning(f"404 error: {request.url}")
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    logger.error(f"500 error: {error}")
    return render_template('error.html', error_code=500, error_message="Server error"), 500

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            
            if not email or not password:
                flash('All fields are required.', 'error')
                return render_template('login.html')
            
            user = user_manager.authenticate(email, password)
            if user:
                session['user'] = user
                logger.info(f"User {email} logged in successfully")
                flash('Logged in successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password.', 'error')
                logger.warning(f"Failed login attempt for email: {email}")
        except Exception as e:
            logger.error(f"Error during login: {e}")
            flash('An error occurred during login.', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            name = request.form.get('name')
            
            if not email or not password or not name:
                flash('All fields are required.', 'error')
                return render_template('register.html')
            
            if user_manager.register_user(email, password, name):
                session['user'] = {'email': email, 'name': name, 'role': 'user'}
                logger.info(f"Registered new user: {email}")
                flash('Registered successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('User with this email already exists.', 'error')
        except Exception as e:
            logger.error(f"Error during registration: {e}")
            flash('An error occurred during registration.', 'error')
    
    return render_template('register.html')

@app.route('/dashboard')
@require_login
def dashboard():
    """Main dashboard with product list"""
    try:
        products = product_manager.get_all_products()
        categories = sorted(set(p['category'] for p in products if p.get('category')))
        return render_template('dashboard.html', products=products, user=session['user'], is_admin=is_admin(), categories=categories)
    except Exception as e:
        logger.error(f"Error loading dashboard: {e}")
        flash('An error occurred while loading products.', 'error')
        return render_template('dashboard.html', products=[], user=session['user'], is_admin=is_admin(), categories=[])

@app.route('/add_product', methods=['GET', 'POST'])
@require_admin
def add_product():
    """Add new product - admin only"""
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            description = request.form.get('description')
            price = float(request.form.get('price', 0))
            category = request.form.get('category', 'Other')
            
            if not name or not description:
                flash('Name and description are required.', 'error')
                return render_template('add_product.html')
            
            product_manager.add_product(name, description, price, category)
            flash('Product added successfully!', 'success')
            return redirect(url_for('dashboard'))
        except ValueError:
            flash('Invalid price.', 'error')
        except Exception as e:
            logger.error(f"Error adding product: {e}")
            flash('An error occurred while adding product.', 'error')
    
    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
@require_admin
def edit_product(id):
    """Edit product - admin only"""
    logger.info(f"Edit product request for ID: {id}")
    product = product_manager.get_product_by_id(id)
    logger.info(f"Found product: {product}")
    if not product:
        logger.warning(f"Product with ID {id} not found")
        flash('Product not found.', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            description = request.form.get('description')
            price = float(request.form.get('price', 0))
            category = request.form.get('category', 'Other')
            logger.info(f"Updating product {id}: name='{name}', description='{description}', price={price}, category='{category}'")
            if not name or not description:
                flash('Name and description are required.', 'error')
                return render_template('edit_product.html', product=product)
            product_manager.update_product(id, name, description, price, category)
            # Zapisz info o ostatniej edycji do session
            session['last_edit'] = {
                'product_name': name,
                'edit_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            flash('Product updated successfully!', 'success')
            return redirect(url_for('dashboard'))
        except ValueError:
            flash('Invalid price.', 'error')
        except Exception as e:
            logger.error(f"Error editing product: {e}")
            flash('An error occurred while editing product.', 'error')
    logger.info(f"Rendering edit form for product: {product}")
    return render_template('edit_product.html', product=product)

@app.route('/logout')
def logout():
    """User logout"""
    if 'user' in session:
        logger.info(f"User {session['user'].get('email', 'unknown')} logged out")
        session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

# API endpoints
@app.route('/api/products', methods=['GET'])
def get_products():
    """API - get all products"""
    try:
        products = product_manager.get_all_products()
        return jsonify(products)
    except Exception as e:
        logger.error(f"API error - getting products: {e}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/api/add_product', methods=['POST'])
def add_product_api():
    """API - add product (admin only)"""
    try:
        # Check if user is admin
        if 'user' not in session or session['user'].get('role') != 'admin':
            return jsonify({'error': 'Administrator privileges required'}), 403
        
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({'error': 'Missing required data'}), 400
        
        new_product = product_manager.add_product(
            name=data['name'],
            description=data['description'],
            price=data.get('price', 0.0),
            category=data.get('category', 'Other')
        )
        return jsonify(new_product), 201
    except Exception as e:
        logger.error(f"API error - adding product: {e}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/api/edit_product/<int:id>', methods=['PUT'])
def edit_product_api(id):
    """API - edit product (admin only)"""
    try:
        # Check if user is admin
        if 'user' not in session or session['user'].get('role') != 'admin':
            return jsonify({'error': 'Administrator privileges required'}), 403
        
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({'error': 'Missing required data'}), 400
        
        updated_product = product_manager.update_product(
            id, 
            name=data['name'],
            description=data['description'],
            price=data.get('price', 0.0),
            category=data.get('category', 'Other')
        )
        
        if updated_product:
            return jsonify(updated_product)
        else:
            return jsonify({'error': 'Product not found'}), 404
    except Exception as e:
        logger.error(f"API error - editing product: {e}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/delete_product/<int:id>', methods=['POST'])
@require_admin
def delete_product(id):
    """Delete product - admin only"""
    try:
        if product_manager.delete_product(id):
            flash('Product deleted successfully!', 'success')
        else:
            flash('Product not found.', 'error')
    except Exception as e:
        logger.error(f"Error deleting product: {e}")
        flash('An error occurred while deleting product.', 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/api/delete_product/<int:id>', methods=['DELETE'])
def delete_product_api(id):
    """API - delete product (admin only)"""
    try:
        # Check if user is admin
        if 'user' not in session or session['user'].get('role') != 'admin':
            return jsonify({'error': 'Administrator privileges required'}), 403
        
        if product_manager.delete_product(id):
            return jsonify({'message': 'Product deleted successfully'})
        else:
            return jsonify({'error': 'Product not found'}), 404
    except Exception as e:
        logger.error(f"API error - deleting product: {e}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/products')
def products_html():
    """Strona HTML z listą produktów"""
    products = product_manager.get_all_products()
    return render_template('products.html', products=products)

@app.route('/products_api')
def products_api_html():
    """Strona HTML z listą produktów (API view)"""
    products = product_manager.get_all_products()
    return render_template('products_api.html', products=products)

if __name__ == '__main__':
    logger.info("Starting Product Management System application")
    app.run(debug=True, host='0.0.0.0', port=5000)
