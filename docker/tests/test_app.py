import unittest
from unittest.mock import patch, MagicMock
import os


# Simular las variables de entorno antes de importar `app`
@patch.dict(
    os.environ,
    {
        #"SENTRY_DSN": "https://examplePublicKey@o0.ingest.sentry.io/0",
        "GITHUB_TOKEN": "fake_github_token",
        "DEBUG": "True",
    },
)
def setUpModule():
    global app
    from app import app


class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Flask API is running", response.data)

    @patch("app.client.complete")
    def test_chat(self, mock_complete):
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_complete.return_value = mock_response

        response = self.app.get("/chat?message=Hello")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test response", response.data)


if __name__ == "__main__":
    unittest.main()
