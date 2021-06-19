import json
from flask import Blueprint, request
from services.feed_service import FeedService


FEED = Blueprint(
    'feed',
    __name__,
    url_prefix='/api/v1'

)


@FEED.route('/users', methods=['POST'])
def create_user():
    params = request.get_json()
    FeedService.add_user(params)
    return json.dumps({
        'Message': 'User {name} {title} {content} inserted.'
    })


@FEED.route('/users', methods=['GET'])
def get_all_user():
    users = FeedService.get_all_users()
    return json.dumps({'users': users})


@FEED.route('/user', methods=['PUT'])
def update_user():
    params = request.get_json()
    FeedService.update_user(params)
    return json.dumps(({'message': 'user updated successfully'}))


@FEED.route('/user/<_id>', methods=['DELETE'])
def delete_user(_id):
    FeedService.delete_user(_id)
    return {"message": f"User successfully deleted."}
