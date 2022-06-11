from flask import Flask,request, render_template, jsonify
from api import API_translate
from question_choice import Question
import os 
from flask_cors import CORS


app = Flask(
            __name__, 
            static_folder= os.getcwd() +'/../frontend/dist/static', 
            template_folder= os.getcwd() + '../frontend/dist'
            )
CORS(
    app,
    origins=["*"]
)

app.config['JSON_AS_ASCII'] = False

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/api')
def respond():
    try:
        count = int(request.args.get("count"))
    except Exception as e:
        print(e)
        count = 3
    binary_str = request.args.get("b")
    q = Question(binary_str, os.getcwd() + "/backend/source.json")
    translated_text = API_translate(q.question["content"]).translate_text(count)
    print(q.wrongs)
    res = {
        "source": q.question["content"],
        "translated": translated_text[0], 
        "choices": {
            "correct": q.question["title"],
            "wrong": q.wrongs,
        }, 
        "finish": q.binary_str
    }
    
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)