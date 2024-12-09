from flask import Flask  # Import the Flask class to create an application instance
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database management
from flask_login import LoginManager  # Import LoginManager for handling user sessions

# Initialize extensions
db = SQLAlchemy()  # Create an instance of SQLAlchemy for the database
login_manager = LoginManager()  # Create an instance of LoginManager for authentication

def create_app():
    """
    Factory function to initialize and configure the Flask app.
    This function is called to create a new instance of the app.
    """
    app = Flask(__name__)  # Create the Flask application object
    app.config.from_object('config.Config')  # Load configuration settings from config.py

    # Initialize extensions with the app
    db.init_app(app)  # Bind the database to the Flask app
    login_manager.init_app(app)  # Bind LoginManager to the Flask app

    # Import and register blueprints
    from .routes.main_routes import main_bp  # Import the main blueprint
    from .routes.admin_routes import admin_bp  # Import the admin blueprint
    app.register_blueprint(main_bp)  # Register the main blueprint
    app.register_blueprint(admin_bp)  # Register the admin blueprint

    return app  # Return the configured Flask app instance
