# Simple-Flask-WebApp
Simple Flask application displaying "hello world" in your browser

## Dependencies required:
Flask

## How to setup:
You need to install flask via the following command
`pip install flask --break-system-packages`

## How to run:
Create a file named app.py
`nano app.py`
Copy the contents and paste it
Install Flask
`pip install flask --break-system-packages`
Run the application
`python3 app.py`
Access the application
Open browser: http://localhost:5000
Or if from outside container: http://YOUR_CONTAINER_IP:5000

## Dependencies Explained
For this basic app:
- flask - The only required dependency
Flask automatically installs these sub-dependencies:
- Werkzeug - WSGI utility library
- Jinja2 - Template engine
- click - Command-line interface
- itsdangerous - Secure signing
- MarkupSafe - String handling

## Create a requirements.txt (Best Practice)
`echo "flask==3.0.0" > requirements.txt`

Then you can install with
`pip install -r requirements.txt --break-system-packages`

## If Running in Docker Container
`docker run -p 5000:5000 -it ubuntu bash`

