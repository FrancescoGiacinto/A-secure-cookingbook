# Import necessary modules from Flask
from flask import Flask

# Import custom modules from the "modules" directory. 
# Here, 'views' could handle general routes like homepage, about page, etc.
# 'user_manager' might handle routes related to user authentication, recipe management, etc.
from modules import views, user_manager  

# Initialize the Flask application
app = Flask(__name__)

# Any specific configurations for the Flask app or extensions can be initialized here. 
# For instance, configurations for a database, secret keys, etc.

# This conditional ensures the app runs only when the script is executed directly, 
# not when it's imported elsewhere. This is a common pattern in Flask applications.
if __name__ == "__main__":
    # Run the Flask app in debug mode. 
    # WARNING: Debug mode should not be used in production as it can expose sensitive information and allow arbitrary code execution.
    app.run(debug=True)  
