import unittest
import app

class SocketIOTests(unittest.TestCase):
    def test_on_connect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        print r

if __name__ == '__main__':
    unittest.main()