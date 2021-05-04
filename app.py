import numpy as np
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
model = pickle.load(open('modl.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    print(final)
    data_unseen = pd.DataFrame([final], columns = ['main_category', 'country', 'name_wcount', 'campaing_len',
                                                'launched_hour', 'launched_month', 'launched_year', 'launched_weekend',
                                                'deadline_weekend', 'goal_usd'])

    prediction = model.predict(data_unseen)
    output = prediction

    if output == 1:
        label = 'Successful!'
    else:
        label = 'Failed!'

    return render_template('index.html', prediction_text=' The campaign is predicted as {}'.format(label))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    dataset = pd.DataFrame(data, index=[0])
    prediction = model.predict(dataset)

    #output = prediction[0]
    bol = 1 if prediction[0] == True else 0
    return jsonify(bol)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=port)
