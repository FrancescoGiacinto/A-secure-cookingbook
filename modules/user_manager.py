from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Recipe
from . import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import re

# Creating a blueprint for user-related routes
user_manager = Blueprint('user_manager', __name__)


def validate_password(password: str) -> bool:
    """
    Validate the password according to given rules.
    1. Minimum length of 6 characters.
    2. Contains at least one special character.
    """
    if len(password) < 6:
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True


# Sample route for user registration
@user_manager.route('/singup', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_surname = request.form.get('surname')
        user_email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not validate_password(password1):
            flash('Password must be at least 6 characters and include a special character.', 'danger')
            return redirect(url_for('create_user'))

        existing_user = User.query.filter_by(email=user_email).first()
        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('create_user'))

        if password1 != password2:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('create_user'))

        hashed_password = generate_password_hash(password1, method='sha256')


        new_user = User(public_id = uuid.uuid4(),
                name = user_name,
                surname = user_surname,
                email = user_email,
                password = hashed_password,
                admin = False)
        db.session.add(new_user)
        try:
            db.session.commit()
            flash('Successfully registered!', 'success')
            return redirect(url_for('views.home_page', user_id=new_user.public_id))  
        except:
            flash('There was an error creating your account!', 'danger')
            return redirect(url_for('user_manager.create_user'))

    return render_template('singup.html') 

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
