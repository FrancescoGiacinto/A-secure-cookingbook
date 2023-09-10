from flask import Blueprint, render_template, request, redirect, url_for

# Creating a blueprint for user-related routes
user_manager = Blueprint('user_manager', __name__)

# Sample route for user registration
@user_manager.route('/singin', methods=['GET', 'POST'])
def register():
    return render_template('singin.html') 

# Sample route for user login
@user_manager.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('home.html') 

