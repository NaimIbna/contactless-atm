from flask import Flask, render_template, send_from_directory, jsonify
from flask_cors import CORS
import MoveCursor
import Data

app = Flask(__name__, static_url_path='/dashboard/dist/')
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

runCursorCamera = True


@app.route('/api/user/<password>')
def sendUser(password):
    for i in Data.allUser:
        if(i.password==password):
            x = {
                "name": i.name,
                "password": i.password,
                "balance": i.balance,
                "uname": i.uname
            }
            return jsonify(x)
    return "UserNotFound"

@app.route('/api/face-rec')
def faceRecognition():
    return "Okay"


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('dashboard/dist/', path)


@app.route('/api/change-cursor-camera')
def changeCursorCamera():
    global runCursorCamera
    runCursorCamera = not runCursorCamera
    if(runCursorCamera):
        MoveCursor.run_hand_recognition()
    return 'Okay'


@app.route('/status')
def status():
    return 'Okay'


@app.route('/')
def index():
    return send_from_directory('dashboard/dist/', 'index.html')
    # return render_template('index.html')


def run_server():
    app.run(host='0.0.0.0', port=5009)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5009, debug=True, threaded=True)

