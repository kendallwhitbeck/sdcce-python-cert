"""
Name: flask_playground.py
Description:

Default path for Flask is located at: http://127.0.0.1:5000/
"""

from flask import Flask
app = Flask(__name__)

@app.route('/a')
def hello_world():
    print("in hello_world() funciton")
    return "Hello World 'a' page"

@app.route('/')
def main():
    print("in main() function")
    return hello_world() + " root page"

if __name__ == '__main__':
    # main()
    app.run()

