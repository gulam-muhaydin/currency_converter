from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_rate')
def get_rate():
    # Replace with a real API that provides currency rates
    url = "https://api.exchangerate-api.com/v4/latest/OMR"
    response = requests.get(url)
    data = response.json()
    rate = data['rates']['PKR']  # Get the PKR rate from the data
    return jsonify(rate=rate)

if __name__ == '__main__':
    app.run(debug=True)
