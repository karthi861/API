import flask_sqlalchemy
from flask import Flask, request, jsonify, make_response
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


@app.route('/user', methods=['POST'])
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


@app.route('/user/feed', methods=['GET'])
def get_all():
    pt = User.query.all()
    results = [
        {
            "id": user.id,
            "name": user.name,
            "title": user.title,
            "content": user.content
        } for user in pt]

    return {"count": len(results), "pt": results}


@app.route('/user/<user_id>', methods=['GET', 'PUT'])
def handle_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'GET':
        response = {
            "name": user.name,
            "title": user.title,
            "content": user.content
        }
        return {"message": "success", "user": response}
    else:
        data = request.get_json()
        user.name = data['name']
        user.title = data['title']
        user.content = data['content']
        db.session.add(user)
        db.session.commit()

    db.session.commit()
    return jsonify({
        'Message': 'User {name} {title} {content} altered.'
    })


@app.route('/user/<user_id>', methods=['DELETE'])
def del_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"message": f"User {user.name} successfully deleted."}


if __name__ == '__main__':
    app.run(debug=True)


