import unittest
import app

class SocketIOTests(unittest.TestCase):
    def test_on_connect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        server_msg = r[0]
        self.assertEquals(server_msg['name'], 'server says hello')
        data = server_msg['args'][0]
        self.assertEquals(data['message'], 'Hello, client!')

    def test_emit(self):
        client = app.socketio.test_client(app.app)
        client.emit('new massage', {
            'massage': 'This is my client massage'
        })
        r = client.get_received()
        result = r[1]
        self.assertEquals(result['name'], 'server sends data back')

if __name__ == '__main__':
    unittest.main()