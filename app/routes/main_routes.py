from flask import Blueprint  # Import Blueprint from Flask

# Create a Blueprint object for main routes
main_bp = Blueprint('main', __name__)

# Define a simple route for testing
@main_bp.route('/')
def home():
    return "Welcome to the Personal Blog!"
