import unittest
import server

class KittehServerTest(unittest.TestCase):
    """Tests for Kitteh site"""

    def setUp(self):
        """Sets up test client per route."""
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Test that the homepage loads."""
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('We\'re hiring!', result.data)

    def test_application_form(self):
        """Test that the application form shows."""
        result = self.client.get('/application-form')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Please fill out this application form to apply to an open position at Kitteh.', result.data)
        self.assertIn('<input id="salaryrequirement" type="number" name="salaryreq" min="0" required>', result.data)

    def test_application_success(self):
        """Test that the success page upon application submission works."""
        result = self.client.post('/application-success', data={'firstname': 'Joanne', 'lastname': 'Yeung', 'salaryreq': 1000000, 'position': 'kittehmaster'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('We have recorded your minimum salary', result.data)


if __name__ == '__main__':
    unittest.main()
