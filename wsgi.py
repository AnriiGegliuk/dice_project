from flask import Flask, jsonify
from dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    roll = dice.roll()
    return jsonify({'roll': roll})
