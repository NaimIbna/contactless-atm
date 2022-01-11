from flask import Flask, send_from_directory
from flask_cors import CORS
import threading
import FaceRecognition

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})


@app.route('/api/name')
def detectedName():
    if(len(FaceRecognition.currentFaceName)>0):
        print(FaceRecognition.currentFaceName)
        return FaceRecognition.currentFaceName[0]
    else:
        return '404'


@app.route('/status')
def status():
    return 'Okay'


@app.route('/')
def index():
    return 'Okay'
    # return render_template('index.html')


def run_server():
    app.run(host='0.0.0.0', port=5055)



p1 = threading.Thread(target=run_server)
p2 = threading.Thread(target=FaceRecognition.runFaceRecognition)
p1.start()
p2.start()
