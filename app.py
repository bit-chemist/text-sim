from flask import Flask, jsonify, request

app = Flask(__name__)

test = [
    {'text': u'you POSTed something'}
]


@app.route('/')
def index():
    return 'Hey, we have a Flask application inside a docker container!'


@app.route('/text-sim/api/v1.0/compare', methods=['POST'])
def parse_request():
    request.get_data()
    data = request.data
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')