# import pickle
# import numpy as np
# from flask import Flask, render_template, request

# app = Flask(__name__)

# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST', 'GET'])
# def predict():
#     float_features = [float (x) for x in request.form.values()] 
#     final = [np.array(float_features)]
#     prediction = model.predict(final)
#     output = format(prediction[0])
    


#     if output == str("1"):
#         print(output)
#         return render_template('pop.html')

#     else:
#         return render_template('pop2.html')


# if __name__ == '__main__':
#     app.run()

import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values by field names
        age = float(request.form['Age'])
        anaemia = int(request.form['Anaemia'])
        cpk = float(request.form['Creatinine_phosphokinase'])
        diabetes = int(request.form['Diabetes'])
        ef = float(request.form['Ejection_fraction'])
        hbp = int(request.form['High_blood_pressure'])
        platelets = float(request.form['Platelets'])
        sc = float(request.form['Serum_creatinine'])
        ss = float(request.form['Serum_sodium'])
        sex = int(request.form['sex'])
        smoke = int(request.form['smoke'])
        fup = float(request.form['fup'])

        # Feature order must match training
        features = np.array([[age, anaemia, cpk, diabetes, ef, hbp, platelets,
                              sc, ss, sex, smoke, fup]])

        prediction = model.predict(features)[0]

        if prediction == 1:
            return render_template('pop.html')
        else:
            return render_template('pop2.html')

    except Exception as e:
        return f"Something went wrong: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
