from models.feed import Feed


class FeedService:

    @staticmethod
    def add_feed(feed):
        name = feed.get('name')
        title = feed.get('title')
        content = feed.get('content')

        Feed.create_feed(
            name=name,
            title=title,
            content=content
        )

    @staticmethod
    def get_all_feed():
        feed = Feed.get_all_feed()
        data = []
        for feeds in feed:
            _feeds = dict(
                id=feeds.id,
                name=feeds.name,
                title=feeds.title,
                content=feeds.content
            )
            data.append(_feeds)
        return data

    @staticmethod
     def update_feed(feed):
        Feed.update_feed(
            _id=feed.get('id'),
            name=feed.get('name'),
            title=feed.get('title'),
            content=feed.get('content')
        )
 

    @staticmethod
    def delete_feed(_id):
        Feed.del_feed(_id)
