from flask import Flask,request
from api import API_translate
import random


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/api')
def respond():
    count = request.args.get("count")
    with open("./question_list.txt","r") as f:
        question_list = f.read()
        question_list = question_list.split("\n")
    question = random.choice(question_list)
    sample = API_translate(question)
    sample = sample.translate_text(count)
    return sample.json()

if __name__ == "__main__":
    app.run(debug=True)