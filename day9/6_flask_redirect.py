from flask import Flask, redirect, url_for

app = Flask(__name__)



@app.route('/admin')
def hello_admin():
    return 'Hello Boss'


@app.route('/guest/<name>')
def hello_guest(name):
    return f'Hello {name}'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    
    else:
        return redirect(url_for('hello_guest',name = name))
    

if __name__ == '__main__':
    app.run(debug=True)