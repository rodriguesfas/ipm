from app import run
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        run.app.testing = True
        self.app = run.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # Make your assertions