# Simple-Flask-WebApp
A simple Flask web application that demonstrates the basics of creating a web server with Python Flask.

## Features
- Simple Flask implementation
- Two routes: home page and personalized greeting
- Docker ready

## Prerequisites
- Python 3.6+
- pip

## Installation
- Clone the repository:
- `git clone https://github.com/Shaf2665/Simple-Flask-WebApp.git`
- `cd Simple-Flask-WebApp`
- Install dependencies:
`pip install flask`
## Usage
- Run the application:
`python3 app.py`
- Access at http://localhost:5000

## Routes
- / - Returns "Hello, World!"
- /greet/<name> - Returns "Hello, {name}!"

## Docker
- Build and run with Docker:
  `docker build -t simple-flask-webapp .`
  `docker run -p 5000:5000 simple-flask-webapp`

## Project Structure
- Simple-Flask-WebApp/
- ├── app.py
- ├── requirements.txt
- └── README.md

## Author
Shafiq - GitHub

## License
MIT License
