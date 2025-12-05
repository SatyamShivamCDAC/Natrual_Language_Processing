from flask import Flask,url_for,redirect,request,render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['nm']
        return redirect(url_for('success',name = name))
    else:
        name = request.form['nm']
        return redirect(url_for('success',name = name))


#rendering custom made html
@app.route('/html')
def html():
    return '''
        <html>
        <title>My web page</title>
        <body>
        <h1><center>Welcome to Flask</center></h1>
        <h2><center>The language of Web</center></h2>
        </body>
        </html>
'''
#rendering predefined html
@app.route('/render_html')
def render():
    return render_template('welcome.html')

#passing data to html
@app.route('/redner_name/<name>')
def render_name(name):
    return render_template('name_render.html',user = name)


if __name__ == '__main__':
    app.run(debug=True)