import app
import flask_testing
import requests
import unittest

class ServerIntegrationTest(flask_testing.LiveServerTestCase):
    def create_app(self):
        return app.app

    def test_root_url(self):
        response = requests.get(self.get_server_url())
        self.assertEquals(response.text, "Hello, world!")

if __name__ == '__main__':
    unittest.main()