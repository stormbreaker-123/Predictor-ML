import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    float_features = [float (x) for x in request.form.values()] 
    final = [np.array(float_features)]
    prediction = model.predict(final)
    output = format(prediction[0])
    


    if output == str("1"):
        return render_template('pop.html')
    else:
        return render_template('pop2.html')


if __name__ == '__main__':
    app.run()
