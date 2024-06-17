import flask
from .model import Product
from project.settings import DB
import os


def render_shop():
    if flask.request.method == "POST":
        product = Product(
            name = flask.request.form["name"]
        )
        flask.request.files["image"].save(os.path.abspath( __file__ + f"/../../static/shop_page/images/{product.name}.png"))

        DB.session.add(product)
        DB.session.commit()
        
    return flask.render_template("shop_page.html", products = Product.query.all())