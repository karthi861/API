from models.user import Feed


class FeedService:

    @staticmethod
    def add_user(users):
        name = users.get('name')
        title = users.get('title')
        content = users.get('content')

        Feed.create_user(
            name=name,
            title=title,
            content=content
        )

    @staticmethod
    def get_all_users():
        users = Feed.get_all_users()
        data = []
        for user in users:
            _user = dict(
                id=user.id,
                name=user.name,
                title=user.title,
                content=user.content
            )
            data.append(_user)
        return data

    @staticmethod
    def update_user(users):
        Feed.update_users(users)

    @staticmethod
    def delete_user(user_id):
        Feed.del_user(user_id)
