from flask import Blueprint, render_template

# Creating a blueprint for user-related routes
user_manager = Blueprint('user_manager', __name__)

# Sample route for user registration
@user_manager.route('/singin', methods=['GET', 'POST'])
def create_user():
    return render_template('singin.html') 

# Sample route for user login
@user_manager.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('home.html') 

@user_manager.route('/user', methods=['GET'])
def get_all_user():
    return ''

@user_manager.route('/user/<user_id>', methods=['GET'])
def get_one_user():
    return ''

@user_manager.route('/user/<user_id>', methods= ['PUT'])
def promote_user():
    return ''

@user_manager.route('/user/<user_id>', methods= ['DELETE'])
def delete_user():
    return ''
