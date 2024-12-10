from app import create_app  # Import the app factory function

app = create_app()  # Create an app instance

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask development server
