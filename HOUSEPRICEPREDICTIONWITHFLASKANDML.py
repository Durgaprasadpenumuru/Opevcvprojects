""""
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def world():
    return render_template("index.html")
    #return "hidurgaprasad"
@app.route('/products')
def products():
    return "we have many products"
if __name__=='__main__':
    app.run()
"""
#https://github.com/ifrankandrade/ml-web-app,,,link for files
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])
    prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'A house with {rooms} rooms per dwelling and located {distance} km to employment centers has a value of ${output}K')

if __name__ == "__main__":
    app.run()