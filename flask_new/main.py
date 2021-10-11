from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
admin = Admin(app)


class User(db.Model, UserMixin):
    def __repr__(self):
        return self.title

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)


class Product(db.Model):
    def __repr__(self):
        return self.title

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, default=0)


admin.add_view(ModelView(Product, db.session))


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


# @app.route('/create', methods=['POST', 'GET'])
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         price = request.form['price']
#
#         item = Item(title=title, price=price)
#         try:
#             db.session.add(item)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'Ошибка'
#     else:
#         return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
