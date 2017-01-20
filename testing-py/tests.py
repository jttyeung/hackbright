import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        result = self.client.get("/")
        self.assertIn("<h2>Please RSVP</h2>", result.data)
        self.assertNotIn("Treats", result.data)

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        self.assertIn("<h2>Party Details</h2>", result.data)
        self.assertIn("Yay!", result.data)
        self.assertNotIn("<form method='POST' action='/rsvp'>", result.data)

    def test_rsvp_mel(self):
        # FIXME: write a test that mel can't invite himself
        result = self.client.post("/rsvp",
                                  data={'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"},
                                  follow_redirects=True)
        self.assertIn("<h2>Please RSVP</h2>", result.data)
        self.assertNotIn("Treats", result.data)
        self.assertIn("Sorry, Mel. This is kind of awkward.", result.data)



if __name__ == "__main__":
    unittest.main()