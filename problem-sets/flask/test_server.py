import unitttest
import server

class KittehServerTest(unittest.TestCase):
  """Tests for Kitteh site"""

  def setUp(self):
    """Sets up test client per route"""
    self.client = server.app.test_client()
    server.app.config['TESTING'] = True

  def test_homepage(self):
    """Test the homepage"""
    result = client.get('/')
    self.assertEqual(result.status_code, 200)
    self.assertIn('We\'re hiring!', result.data)

if __name__ == '__main__':
  unittest.main()
