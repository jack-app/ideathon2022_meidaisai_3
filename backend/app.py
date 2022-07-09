from flask import Flask,request, render_template, jsonify
from flask_socketio import SocketIO, send, emit
from api import API_translate
from question_choice import Question
import os 
from flask_cors import CORS
from constants import Constants

all_user = []
room_volume = [2] * 50 + [4] * 50
room_condition = [True] * 100
respondent = ''


c = Constants()

app = Flask(
            __name__, 
            static_folder= c.prefix_frontend_dir + '/dist/static', 
            template_folder= c.prefix_frontend_dir + '/dist'
            )
CORS(
    app,
    origins=["*"]
)

socketio = SocketIO(app, cors_allowed_origins='*')
app.config['JSON_AS_ASCII'] = False

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/prepare',methods = ['POST'])
@socketio.on('prepare')
def prepare():
    name = request.form.get('name')
    option = request.form.get('option')
    global all_user
    global room_condition
    global room_volume
    if option == 'two':
        i = 0
    else:
        i = 50
    while room_condition[i]:
        i += 1
    room = i
    all_user[room].append(name)
    emit('room_set', {'room' : room})
    if room_volume[i] == len(all_user[i]):
        room_condition[i] = False
        emit('battle_start', {'ok_num': room}, broadcast = True)
        res = { 
            'user' : all_user
        }
        return jsonify(res) 

@socketio.on('battle_end')
def end():
    room = request.form.get('room_unm') 
    global all_user
    global room_condition
    room_condition[room] = True
    del all_user[room]

@socketio.on('bottun_push')
def push():
    name = request.form.get('respondent')
    global respondent
    if respondent:
        respondent = name
    emit('respond',{'respondent': respondent})


@app.route('/api')
def respond():
    try:
        count = int(request.args.get("count"))
    except Exception as e:
        print(e)
        count = 3
    binary_str = request.args.get("b")
    q = Question(binary_str, c.prefix_source_dir + "/source.json")
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