from flask import (
    Flask,
    request,
    jsonify,
    render_template
)

import joblib

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load(
    'churn_model.pkl'
)

# Home route
@app.route('/')
def home():

    return render_template(
        'index.html'
    )


# JSON API prediction route
@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    sample = data['features']

    prediction = model.predict([sample])

    return jsonify({
        "prediction": int(prediction[0])
    })


# HTML form route
@app.route('/predict_form', methods=['POST'])
def predict_form():

    tenure = float(
        request.form['tenure']
    )

    monthlycharges = float(
        request.form['monthlycharges']
    )

    contract = request.form['contract']

    contract_one_year = (
        True if contract == 'one_year'
        else False
    )

    contract_two_year = (
        True if contract == 'two_year'
        else False
    )

    totalcharges = tenure * monthlycharges

    sample = [[
        0,
        tenure,
        monthlycharges,
        totalcharges,
        False,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        True,
        True,
        contract_one_year,
        contract_two_year
    ]]

    prediction = model.predict(sample)

    if prediction[0] == 1:
        result = "Customer is likely to churn"

    else:
        result = "Customer is not likely to churn"

    return render_template(
    'result.html',
    tenure=tenure,
    monthlycharges=monthlycharges,
    totalcharges=totalcharges,
    contract=contract,
    result=result
)


# Run Flask app
if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )