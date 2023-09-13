from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home.html')

@views.route('/recipes/<public_id>')
def home_page(public_id):
    return render_template('recipes.html')