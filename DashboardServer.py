from flask import Flask, render_template, send_from_directory
app = Flask(__name__, static_url_path='/template')


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('template', path)


@app.route('/status')
def status():
    return 'Okay'


@app.route('/')
def index():
    return send_from_directory('template', 'index.html')
    # return render_template('index.html')


def run_server():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

