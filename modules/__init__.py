from flask import Flask
import os  # Import the os library to access environment variables

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(config_name=None):
    # Initialize the Flask app instance
    app = Flask(__name__)
    
    # Configure the app's secret key using an environment variable.
    # If the environment variable isn't set, use a fallback key.
    app.config['SECRET_KEY'] = os.environ.get('FLASK_COOKINGBOOK_SECRET_KEY', 'fallback_key_if_not_found')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import blueprints from other modules and register them with the app
    from .views import views
    from .user_manager import user_manager

    from .models import User, Recipe

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(user_manager, url_prefix='/user')  # Changed prefix to '/user' to avoid route overlap

    # These lines are redundant since blueprints are already imported and registered above
    # from . import views, user_manager

    # Return the configured app instance
    return app

