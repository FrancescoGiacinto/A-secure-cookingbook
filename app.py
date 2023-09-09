# Import the custom function to create and configure the Flask application.
from modules import create_app 

# Initialize the Flask application with an optional configuration name.
# This structure allows flexibility to configure the app for different environments (e.g., 'development', 'production').
app = create_app('development')

# Check if this script is the main entry point.
# This pattern ensures the Flask app only runs when this script is executed directly.
# It doesn't run if the script is imported elsewhere.
if __name__ == "__main__":
    # Run the Flask app in debug mode for development.
    # NOTE: Always turn off debug mode in a production setting to maintain security.
    app.run(debug=True)


