from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)  # Creating an instance of the Flask class.

@app.route('/', methods=["GET"])
def home():
    return "Welcome to the Compound Interest Calculator API."

@app.route('/calculate', methods=["POST"])
def calculate():
    if request.is_json:
        data = request.get_json()  # Get JSON data from the request.
        P = data['principal']
        r = data['rate']
        t = data['time']

        # Calculate the compound interest and total amount.
        A = P * (1 + r) ** t
        CI = A - P

        response = {
            "principal": P,
            "rate": r,
            "time": t,
            "compound_interest": CI,
            "total_amount": A
        }

        return jsonify(response)  # Return the calculation as JSON.
    else:
        return "Request content type must be application/json", 415

if __name__ == "__main__":
    app.run(debug=True, port=9000)  # Running the app in debug mode on port 9000.
