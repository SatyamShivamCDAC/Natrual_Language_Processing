from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return f'hello {name}'



if __name__ == '__main__':
    app.run(debug=True)