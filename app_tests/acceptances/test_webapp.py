# coding=utf-8

import unittest
import app.webapp

class WebappTest(unittest.TestCase):
    def setUp(self):
        self.client = app.webapp.app.test_client()

    def test_root_should_display_OK(self):
        # Assign
        # Acts
        rv = self.client.get('/')

        # Assert
        self.assertTrue(b'OK' in rv.data, rv.data)
