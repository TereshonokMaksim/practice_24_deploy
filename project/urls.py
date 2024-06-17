import home_page
import shop_page
from .settings import project_app

home_page.home_app.add_url_rule(rule = "/", view_func = home_page.render_home)
shop_page.shop_app.add_url_rule(rule = "/shop/", view_func = shop_page.render_shop, methods = ["GET", "POST"])

project_app.register_blueprint(blueprint = home_page.home_app)
project_app.register_blueprint(blueprint = shop_page.shop_app)