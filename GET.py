from flask import Flask, redirect, url_for
from flask import request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

Feed = [
    {'id': 0,
     'title': 'karachi',
     'date': '20/05/2000',
     'content': 'hi'},
    {'id': '1',
     'title': 'Sample',
     'date': '19/07/1999',
     'content': 'good morning'
      }
]


@app.route('/', methods=['GET'])
def page():
    return 'Create a feed'


@app.route('/Feed/all', methods=['GET'])
def todo():
    return jsonify(Feed)


@app.route('/Feed', methods=['GET'])
def feed_id():
    if'id' in request.args:
        id = int(request.args['id'])
    else:
        return "error"
    results = []
    for feed in Feed:
        if feed['id'] == id:
            results.append(feed)
    return jsonify(results)


app.run()


