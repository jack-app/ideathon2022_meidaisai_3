from flask import Flask,request, jsonify
from api import API_translate
from question_choice import Question


import random


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return 'Hello World'

@app.route('/api')
def respond():
    count = int(request.args.get("count"))
    binary_str = request.args.get("b")
    q = Question(binary_str, "./source.json")
    translated_text = API_translate(q.question["content"]).translate_text(count)
    print(q.wrongs)
    res = {
        "source": q.question["content"],
        "translated": translated_text, 
        "choices": {
            "correct": q.question["title"],
            "wrong": q.wrongs,
        }, 
        "finish": q.binary_str
    }
    
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)