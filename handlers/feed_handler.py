import json
from flask import Blueprint, request
from services.feed_service import FeedService


FEED = Blueprint(
    'feed',
    __name__,
    url_prefix='/api/v1'

)


@FEED.route('/feed', methods=['POST'])
def create_feed():
    params = request.get_json()
    FeedService.add_feed(params)
    return json.dumps({
        'Message': 'Feed {name} {title} {content} inserted.'
    })


@FEED.route('/feed', methods=['GET'])
def get_all_feed():
    feed = FeedService.get_all_feed()
    return json.dumps({'feed': feed})


@FEED.route('/feed', methods=['PUT'])
def update_feed():
    params = request.get_json()
    FeedService.update_feed(params)
    return json.dumps(({'message': 'feed updated successfully'}))


@FEED.route('/feed/<_id>', methods=['DELETE'])
def delete_feed(_id):
    FeedService.delete_feed(_id)
    return {"message": f"Feed successfully deleted."}
