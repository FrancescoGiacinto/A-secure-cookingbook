from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home.html')

@views.route('/recipes/<user_id>')
def home_page(user_id):
    return render_template('recipes.html')