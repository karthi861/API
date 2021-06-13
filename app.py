from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'pt'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    title = db.Column(db.String(128))
    content = db.Column(db.String(98))

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content


db.create_all()


@app.route('/user', methods=['GET', 'POST'])
def post():
    name = request.json['name']
    title = request.json['title']
    content = request.json['content']

    user = User(name, title, content)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'Message': 'User {name} {title} {content} inserted.'
    })


@app.route('/user/feed', methods=['PUT'])
def put():
    try:
        id = request.args['id']
    except Exception as _:
        id = None
    if not id:
        return jsonify({'Message': 'provide the user ID'})
    user = User.query.get(id)

    name = request.json['name']
    title = request.json['title']
    content = request.json['content']

    user.name = name
    user.title = title
    user.content = content

    db.session.commit()
    return jsonify({
        'Message': 'User {name} {title} {content} altered.'
    })


@app.route('/user/feed/<int:id>', methods=['DELETE'])
def delete():
    try:
        id = request.args['id']
    except Exception as _:
        id = None
    if not id:
        return jsonify({'Message': 'provide the user ID'})
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        'Message': 'User {str(id)} deleted.'
    })


if __name__ == '__main__':
    app.run(debug=True)
