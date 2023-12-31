from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from os import path

db = SQLAlchemy() # Initialize SQLAlchemy database object
DB_NAME = "database.db" 
DB_PATH = os.path.join(os.getcwd(), "modules\static\database", DB_NAME)

def create_app(config_name=None):
    """
    Function to create and configure the Flask app instance.
    """
    # Initialize the Flask app instance
    app = Flask(__name__)
    
    # Configure the app's secret key using an environment variable.
    # If the environment variable isn't set, use a fallback key.
    app.config['SECRET_KEY'] = os.environ.get('FLASK_COOKINGBOOK_SECRET_KEY', 'fallback_key_if_not_found')
    
    # Configure the SQLAlchemy database URI using the absolute DB_PATH
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    
    # Initialize the database with the app
    db.init_app(app)

    # Import blueprints from other modules and register them with the app
    from .user_manager import user_manager
    from .views import views    
    from .models import User, Recipe # Import the required models

    with app.app_context():
        db.create_all() 

    # Register the blueprints with their respective url prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(user_manager, url_prefix='/user')

    # Return the configured app instance
    return app

def create_database(app):
    if not os.path.exists(DB_PATH):
        with app.app_context():
            db.create_all()
        print('DATABASE HAS BEEN CREATED')