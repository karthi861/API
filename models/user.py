from models import db


class Feed(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    title = db.Column(db.String(128))
    content = db.Column(db.String(98))

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content

    @staticmethod
    def get_user(user_id):
        users = Feed.query.get(user_id)
        return users

    @staticmethod
    def get_all_users():
        users = Feed.query.all()
        return users

    @staticmethod
    def create_user(
            name,
            title,
            content
    ):
        users = Feed(
            name=name,
            title=title,
            content=content
        )
        db.session.add(users)
        db.session.commit()

    @staticmethod
     def update_users(_id, name, title, content):
        users = Feed.query.get(_id)
        users.name = name
        users.title = title
        users.content = content
        db.session.add(users)
        db.session.commit()

    @staticmethod
    def del_user(_id):
        users = Feed.query.get(_id)
        db.session.delete(users)
        db.session.commit()

