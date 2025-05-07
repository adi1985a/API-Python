from flask import Flask, render_template, jsonify, request, redirect, session,flash, url_for



app = Flask(__name__)
app.secret_key = '123312334512334545123345'

# Lista produktów jako dane testowe
products = [
    {"id": 1, "name": "Cola-Cola", "description": "Napój Cola-Cola, 0.5l"},
    {"id": 2, "name": "Pepsi", "description": "Napój Pepsi, 0.5l"},
    {"id": 3, "name": "Fanta", "description": "Napój Fanta, 0.5l"},
    {"id": 4, "name": "Sprite", "description": "Napój Sprite, 0.5l"},
    {"id": 5, "name": "Cola-zero", "description": "Napój Cola-zero, 0.5l"},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dodaj logikę logowania
        # Przykładowo:
        email = request.form.get('email')
        # Sprawdź poprawność loginu i hasła, np. w bazie danych
        # Jeśli poprawne, ustaw użytkownika w sesji
        session['user'] = 'example_user'
        return redirect('/dashboard')  # Zmiana ścieżki przekierowania

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Dodaj logikę rejestracji
        # Przykładowo:
        email = request.form.get('email')
        # Sprawdź poprawność danych rejestracyjnych i zarejestruj użytkownika, np. w bazie danych
        # Jeśli poprawne, ustaw użytkownika w sesji
        session['user'] = email
        flash('Zarejestrowano pomyślnie!', 'success')
        return redirect('/dashboard')  # Zmiana ścieżki przekierowania

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', products=products, user='example_user')  # Dodaj użytkownika z sesji

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Dodaj logikę dodawania produktu
        # Przykładowo:
        return redirect('/dashboard')  # Zmiana ścieżki przekierowania

    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if request.method == 'POST':
        # Dodaj logikę edycji produktu
        # Przykładowo:
        return redirect('/dashboard')  # Zmiana ścieżki przekierowania

    return render_template('edit_product.html', product=product)

@app.route('/logout')
def logout():
    # Dodaj logikę wylogowania
    return redirect('/login')  # Zmiana ścieżki przekierowania

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/api/add_product', methods=['POST'])
def add_product_api():
    if request.method == 'POST':
        # Dodaj logikę dodawania produktu
        # Przykładowo:
        data = request.json
        new_product = {
            'id': len(products) + 1,
            'name': data['name'],
            'description': data['description']
        }
        products.append(new_product)
        return jsonify(new_product)

@app.route('/api/edit_product/<int:id>', methods=['PUT'])
def edit_product_api(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        if request.method == 'PUT':
            # Dodaj logikę edycji produktu
            # Przykładowo:
            data = request.json
            product['name'] = data['name']
            product['description'] = data['description']
            return jsonify(product)

@app.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    global products
    products = [p for p in products if p['id'] != id]
    return redirect('/dashboard')


@app.route('/api/delete_product/<int:id>', methods=['DELETE'])
def delete_product_api(id):
    global products
    products = [p for p in products if p['id'] != id]
    return jsonify({'message': 'Product deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
