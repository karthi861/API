from models import db


class Feed(db.Model):
    __tablename__ = 'feed'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    title = db.Column(db.String(128))
    content = db.Column(db.String(98))

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content

    @staticmethod
    def get_feed(_id):
        feed = Feed.query.get(_id)
        return feed

    @staticmethod
    def get_all_feed():
        users = Feed.query.all()
        return feed

    @staticmethod
    def create_feed(
            name,
            title,
            content
    ):
        feed = Feed(
            name=name,
            title=title,
            content=content
        )
        db.session.add(feed)
        db.session.commit()

    @staticmethod
     def update_feed(_id, name, title, content):
        feed = Feed.query.get(_id)
        feed.name = name
        feed.title = title
        users.content = content
        db.session.add(feed)
        db.session.commit()

    @staticmethod
    def del_feed(_id):
        feed = Feed.query.get(_id)
        db.session.delete(feed)
        db.session.commit()

