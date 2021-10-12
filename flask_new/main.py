from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret'
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


def get_categories():
    return [i[0] for i in Product.query.with_entities(Product.category).distinct()]


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products, categories=get_categories())


@app.route('/product')
def product():
    return render_template('product.html', categories=get_categories())


@app.route('/checkout')
def checkout():
    return render_template('checkout.html', categories=get_categories())


@app.route('/cart')
def cart():
    return render_template('cart.html', categories=get_categories())


@app.route('/contact')
def contact():
    return render_template('contact.html', categories=get_categories())


@app.route('/categories/<string:category>')
def exist_category(category):
    if category in get_categories():
        products = Product.query.filter_by(category=category)
        return render_template('categories.html', categories=get_categories(), cur_category=category, products=products)
    else:
        return redirect('/')


@app.route('/categories')
def categories():
    return render_template('categories.html', categories=get_categories())


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
