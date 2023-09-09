from flask import Flask
import os

def create_app(config_name=None):
    app.config['SECRET_KEY'] = os.environ.get('FLASK_COOKINGBOOk_SECERT_KET', 'fallback_key_if_not_found')
    
    app = Flask(__name__)


    from .views import views
    from .user_manager import user_manager

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(user_manager, url_prefix='/')

    return app

    # Import and register your views and blueprints
    from . import views, user_manager

    # For example, if user_manager is a blueprint:
    # app.register_blueprint(user_manager.bp)

    return app
