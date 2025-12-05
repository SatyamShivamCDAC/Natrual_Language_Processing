from flask import Flask,render_template,redirect,url_for,request
import joblib
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sword = stopwords.words('english')
ps = PorterStemmer()


def clean_text_stem(sent):
    tokens1 = word_tokenize(sent)
    tokens2 = [token for token in tokens1 if token.isalpha()]
    tokens3 = [ps.stem(token) for token in tokens2 if token.lower() not in sword]
    return tokens3

model = joblib.load('spam_detector.model')
preprocessor = joblib.load('spam_detector_preprocessor.model')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('spamdetector.html')

@app.route('/spamfinder', methods = ['POST', 'GET'])
def spamfinder():
    if request.method == 'POST':
        message = request.form['message']
        new_mes = preprocessor.transform([message])

        pred = model.predict(new_mes)
        return render_template('result.html',result = pred[0])



if __name__ == '__main__':
    app.run(debug=True)