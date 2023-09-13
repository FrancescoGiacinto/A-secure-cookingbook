from flask import Blueprint, render_template
from .user_manager import token_required

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home.html')

@views.route('/recipes/<public_id>')
@token_required
def home_page(current_user, public_id):
    public_id = current_user.public_id
    return render_template('recipes.html')