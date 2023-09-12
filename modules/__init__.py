from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
DB_PATH = os.path.join("static", "database", DB_NAME)  # Define a full path to the database file

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Set up the app's secret key, using an environment variable if available
    app.config['SECRET_KEY'] = os.environ.get('FLASK_COOKINGBOOK_SECRET_KEY', 'fallback_key_if_not_found')
    
    # Use the full path to the database file
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    
    db.init_app(app)

    from .views import views
    from .user_manager import user_manager
    from .models import User, Recipe

    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(user_manager, url_prefix='/user')

    # Creation of the database has been moved to 'create_database' function
    # with app.app_context():
    #     db
