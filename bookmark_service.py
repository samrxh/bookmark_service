import zmq
from zmq.utils import jsonapi
import json


class BookmarkService:
    def __init__(self):
        self.bookmarks = {}

    def add_bookmark(self, bookmark_id, data):
        self.bookmarks[bookmark_id] = data

    def remove_bookmark(self, bookmark_id):
        del self.bookmarks[bookmark_id]

    def list_bookmarks(self):
        return self.bookmarks

    def get_bookmark_data(self, bookmark_id):
        return self.bookmarks[bookmark_id]

    def run(self):
        # Set up context and socket
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://localhost:7000")

        while True:
            message = socket.recv()
            request = json.loads(jsonapi.loads(message))

            if request['method'] == 'add':
                self.add_bookmark(request['id'], request['data'])
                response = {'status': 'OK'}

            elif request['method'] == 'remove':
                self.remove_bookmark(request['id'])
                response = {'status': 'OK'}

            elif request['method'] == 'list':
                response = self.list_bookmarks()

            elif request['method'] == 'get':
                response = self.get_bookmark_data(request['id'])

            else:
                response = {'status': 'error', 'message': 'Invalid request'}
            socket.send(jsonapi.dumps(response))


if __name__ == '__main__':
    BookmarkService().run()
