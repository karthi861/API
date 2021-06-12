from flask import Flask, redirect, url_for, abort
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
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "error"
    results = []
    for feed in Feed:
        if feed['id'] == id:
            results.append(feed)
    return jsonify(results)


@app.route('/Feed/all/addi', methods=['GET', 'POST'])
def addi():
    ack = {
        "id": Feed[-1]['id'] + str(1),
        "title": request.json['title'],
        "content": request.json.get('content', " ")
    }
    Feed.append(ack)
    return jsonify({'ack': ack}), 201
    
    
    @app.route('//Feed/all/addi/<int:ack_id>', methods=['PUT'])
def update_ack(ack_id):
    ack = [ack for ack in Feed if ack['id'] == ack_id]
    if len(ack) == 0:
        return "error"
    ack[0]['title'] = request.json.get('title', ack[0]['title'])
    ack[0]['id'] = request.json.get('id', ack[0]['id'])
    ack[0]['content'] = request.json.get('content', ack[0]['content'])
    return jsonify({'ack': ack[0]})


@app.route('/Feed/all/addi/<int:ack_id>', methods=['DELETE'])
def delete_ack(ack_id):
    ack = [ack for ack in Feed if ack['id'] == ack_id]
    if len(ack) == 0:
        abort(404)
    Feed.remove(ack[0])
    return jsonify({'result': True})


app.run()
