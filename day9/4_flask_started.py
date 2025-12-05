from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Yolo'


@app.route('/index')
def index():
    return 'Welcome to Index Page'

if __name__ == '__main__':
    app.run(debug=True)