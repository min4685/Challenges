from flask import Flask, render_template, request, jsonify, session
from functools import wraps
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

def verify_session(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('verified', False):
            return jsonify({"error": "먼저 정답을 검증해야 합니다."}), 403
        return f(*args, **kwargs)
    return decorated_function

try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/1')
def page1():
    return render_template('p1.html')

@app.route('/2')
def page2():
    return render_template('p2.html')

@app.route('/3')
def page3():
    return render_template('p3.html')

@app.route('/exit')
def exit():
    return render_template('exit.html')


@app.route('/verify/<answer>')
def verify(answer):
    if answer == config.P1_SECRET_CLUE:
        session['verified'] = True
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/get-p1-clue', methods=['GET', 'POST'])
@verify_session
def get_p1_clue():    
    try:
        clue1 = config.P1_SECRET_KEY
        return jsonify({"clue1": "[1] " + clue1})
    except Exception as e:
        return jsonify({"clue1": "단서를 불러올 수 없습니다."}), 404
    

@app.route('/2/submit', methods=['POST'])
def submit_message():
    header1 = request.headers.get('X-P2-Header1')
    header2 = request.headers.get('X-P2-Header2')
    header3 = request.headers.get('X-P2-Header3')

    secret_header = request.headers.get('X-Secret-Header')
    if secret_header == config.P2_SECRET_CLUE:
        try:
            clue2 = config.P2_SECRET_KEY
            return jsonify({
                "success": True,
                "message": "[2] " + clue2
            })
        except Exception as e:
            return jsonify({
                "success": False,
                "message": "단서를 불러올 수 없습니다."
            })
    
    return jsonify({
        "success": False,
        "message": "메시지가 전송되었습니다!"
    })
    
    
@app.route('/3/submit', methods=['POST'])
def submit_answer():
    try:
        data = request.get_json()
        answer = data.get('answer')

        if answer == config.P3_SECRET_CLUE:
            try:
                clue3 = config.P3_SECRET_KEY
                return jsonify({
                    "success": True,
                    "message": "[3] " + clue3
                })
            except Exception as e:
                return jsonify({
                    "success": False,
                    "message": "단서를 불러올 수 없습니다."
                })
        
        return jsonify({
            "success": False,
            "message": "내가 아는 것과 다른데?"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "오류가 발생했습니다."
        })
    
    
@app.route('/check-flags', methods=['POST'])
def check_flags():
    try:
        data = request.get_json()
        clue1 = data.get('clue1')
        clue2 = data.get('clue2')
        clue3 = data.get('clue3')

        if (clue1 == config.P1_SECRET_KEY and 
            clue2 == config.P2_SECRET_KEY and 
            clue3 == config.P3_SECRET_KEY):
            return jsonify({
                "success": True,
                "flag": FLAG
            })
        return jsonify({
            "success": False
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "오류가 발생했습니다."
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
