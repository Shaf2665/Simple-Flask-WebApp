# Simple-Flask-WebApp
A simple Flask web application that demonstrates the basics of creating a web server with Python Flask.
Description
This is a minimal Flask application that serves a "Hello, World!" message. It includes two routes:

A home route that displays a simple greeting
A dynamic route that greets users by name

Features

Simple and clean Flask implementation
RESTful routing
Dynamic URL parameters
Ready for Docker deployment
Debug mode enabled for development

Prerequisites

Python 3.6 or higher
pip (Python package manager)

Installation
1. Clone the Repository
`git clone https://github.com/Shaf2665/Simple-Flask-WebApp.git`
`cd Simple-Flask-WebApp`
2. Install Dependencies
`pip install -r requirements.txt`
Or install Flask directly:
`pip install flask`
Usage
Running the Application
Start the Flask development server:
`python3 app.py`
The application will start on http://localhost:5000

Accessing the Application
Open your web browser and navigate to:

Home page: http://localhost:5000/

Returns: Hello, World!


Personalized greeting: http://localhost:5000/greet/<name>

Example: http://localhost:5000/greet/John
Returns: Hello, John!

Running with Docker
Build the Docker Image
`docker build -t simple-flask-webapp .`
Run the Container
`docker run -p 5000:5000 simple-flask-webapp`

Access the application at http://localhost:5000

Simple-Flask-WebApp/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation

Configuration
The application runs with the following default settings:

Host: 0.0.0.0 (accessible from all network interfaces)
Port: 5000
Debug Mode: True (disable in production)

To change these settings, modify the app.run() parameters in app.py:
`app.run(host='0.0.0.0', port=5000, debug=True)`

Dependencies

Flask 3.0.0 - Web framework

All dependencies are listed in requirements.txt

Development
Running in Debug Mode
Debug mode is enabled by default, which provides:

Auto-reload on code changes
Detailed error messages
Interactive debugger

⚠️ Important: Disable debug mode in production by setting debug=False
Adding New Routes
Add new routes by defining functions with the @app.route() decorator:
`@app.route('/about')
def about():
    return 'About Page'`

Deployment
Production Considerations
For production deployment:

Disable debug mode:
`app.run(host='0.0.0.0', port=5000, debug=False)`

Use a production WSGI server:
`pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app`
   
Set environment variables:
`export FLASK_ENV=production`

Deployment Platforms
This application can be deployed on:

Heroku
AWS Elastic Beanstalk
Google Cloud Platform
Azure App Service
DigitalOcean
Docker containers

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Author
Shafiq - @Shaf2665
Project Link: https://github.com/Shaf2665/Simple-Flask-WebApp
Acknowledgments

Flask documentation: https://flask.palletsprojects.com/
Python community


Port Already in Use
If port 5000 is already in use, change the port in app.py:
`app.run(host='0.0.0.0', port=8080, debug=True)`

Module Not Found Error
Make sure Flask is installed:
pip install flask

Connection Refused (Docker)
Ensure the container port is properly mapped:
`docker run -p 5000:5000 simple-flask-webapp`


Support
If you have any questions or run into issues, please open an issue on GitHub.

Happy Coding! 🚀

