import string
from flask import Flask, jsonify, request

app = Flask(__name__)

test = [
    {'text': u'you POSTed something'}
]


def jaccard_similarity(str1, str2):
    string1 = str1.translate(str.maketrans('', '', string.punctuation))
    string2 = str2.translate(str.maketrans('', '', string.punctuation))
    set_a = set(string1.split())
    set_b = set(string2.split())
    intersect = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return float(len(intersect))/float(len(union))


@app.route('/')
def index():
    return 'Hey, we have a Flask application inside a docker container!'


@app.route('/text-sim/api/v1.0/compare', methods=['POST'])
def parse_request():
    data = request.json
    similarity = jaccard_similarity(data['text1'], data['text2'])
    return jsonify(similarity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
