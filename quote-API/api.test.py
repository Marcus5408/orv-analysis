# BEGIN: 8f7c1d3a6b2c
import json
from api import app
from unittest import TestCase
from unittest.mock import patch

class TestQuote(TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch("api.open")
    def test_get_quotes(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = json.dumps([{"id": 1, "quote": "test quote"}])
        response = self.app.get("/quotes")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{"id": 1, "quote": "test quote"}])

    @patch("api.open")
    def test_get_quote_by_id(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = json.dumps([{"id": 1, "quote": "test quote"}])
        response = self.app.get("/quotes/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"id": 1, "quote": "test quote"})

    @patch("api.open")
    def test_get_quote_by_id_not_found(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = json.dumps([{"id": 1, "quote": "test quote"}])
        response = self.app.get("/quotes/2")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, "Quote not found")