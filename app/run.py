from app import create_app

ap = create_app() # Creating an app instance using the factory function

if __name__== '__main__':
    app.run(debug=True) # Starting the development server.