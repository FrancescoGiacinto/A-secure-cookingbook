from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, jsonify, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField
from .models import User, Recipe
from . import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import re
import jwt
import datetime
from functools import wraps

# Creating a blueprint for user-related routes
user_manager = Blueprint('user_manager', __name__)

class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired()])
    surname = StringField('Surname', [validators.InputRequired()])
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    password1 = PasswordField('Password', [validators.InputRequired()])
    password2 = PasswordField('Confirm Password', [validators.InputRequired(), validators.EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField('Remember Me')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')  # Get the token from cookies

        if not token:
            return jsonify({'message':'Token is missing'}), 401
        try :
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401
        
        return f( current_user, *args, **kwargs )
    
    return decorated



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



@user_manager.route('/singup', methods=['GET', 'POST'])
def create_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        user_name = form.name.data
        user_surname = form.surname.data
        user_email = form.email.data
        password1 = form.password1.data
        # Nota: non hai bisogno di verificare la password2 poiché Flask-WTF lo farà per te con validators.EqualTo

        if not validate_password(password1):
            flash('Password must be at least 6 characters and include a special character.', 'danger')
            return redirect(url_for('user_manager.create_user'))

        existing_user = User.query.filter_by(email=user_email).first()
        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('user_manager.create_user'))

        hashed_password = generate_password_hash(password1, method='scrypt')

        new_user = User(public_id=str(uuid.uuid4()),
                        name=user_name,
                        surname=user_surname,
                        email=user_email,
                        password=hashed_password,
                        admin=False)
        db.session.add(new_user)

        
        try:
            db.session.commit()
            flash('Successfully registered!', 'success')
            return redirect(url_for('views.home_page', public_id=new_user.public_id))
        except:
            flash('There was an error creating your account!', 'danger')
            return redirect(url_for('user_manager.create_user'))
        


    return render_template('singup.html', form=form)


# Sample route for user login
@user_manager.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user_email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=user_email).first()

        if not user:
            flash('User not found', 'danger')
            return render_template('login.html', form=form)  # Render the template again with the error message

        if not check_password_hash(user.password, password):
            flash('Incorrect password', 'danger')
            return render_template('login.html', form=form)  # Render the template again with the error message

        # Generate the JWT token
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        }, current_app.config['SECRET_KEY'])

        # Typically, you'd redirect to a dashboard or home page after login
        # For this example, I'm assuming a 'dashboard' route. Adjust as needed.
        response = make_response(redirect(url_for('views.home_page', public_id=user.public_id)))
        response.set_cookie('token', token)  # Set the JWT token as a cookie
        return response
    
    return render_template('login.html', form=form)





@user_manager.route('/user', methods=['GET'])
def get_all_user():
    users = User.query.all()
     
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
