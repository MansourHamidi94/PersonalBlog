from flask import Flask  # Import Flask to create the app

def create_app():
    """
    Factory function to initialize and configure the Flask app.
    """
    app = Flask(__name__)  # Create a Flask app instance

    # Import and register the main blueprint
    from .routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app  # Return the configured app
