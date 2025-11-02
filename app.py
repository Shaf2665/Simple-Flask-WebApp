from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define route for home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define additional route (optional)
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

# Run the application
if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible from outside the container
    # debug=True enables auto-reload and detailed error messages
    app.run(host='0.0.0.0', port=5000, debug=True)
