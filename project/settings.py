import flask
import os
import flask_migrate
import flask_sqlalchemy

project_app = flask.Flask(
    import_name = "project",
    instance_path = os.path.abspath(__file__ + "/..")
)

project_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

DB = flask_sqlalchemy.SQLAlchemy(app = project_app)

MIGRATE = flask_migrate.Migrate(app = project_app, db = DB)