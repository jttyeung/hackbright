"""Tests for the shopping site wannabe"""

import server
import shipping
import unittest


class ShippingTestCase(unittest.TestCase):

    def test_cali(self):
        """Test shipping for California."""

        cali_shipping = shipping.calculate_shipping('CA')
        self.assertEqual(cali_shipping, 0)


    def test_alaska(self):
        """Test shipping for Alaska."""

        ak_shipping = shipping.calculate_shipping('AK')
        self.assertEqual(ak_shipping, 20)


    def test_indiana(self):
        """Test shipping for Indiana."""

        in_shipping = shipping.calculate_shipping('IN')
        self.assertEqual(in_shipping, 5)



class MelonSiteIntegrationTestCase(unittest.TestCase):
    """Flask tests for the site"""

    def setUp(self):
        """Set up a test client before every test."""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True


    def test_index(self):
        """Test the homepage."""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1>Welcome to Ubermelon!</h1>', result.data)


    def test_melon_order_form(self):
        """Test the display of the order form."""

        result = self.client.get('/order_melons')
        self.assertEqual(result.status_code, 200)

        melon_option = '<option value="alib">Ali Baba Watermelon</option>'
        self.assertIn(melon_option, result.data)


    def test_melon_order(self):
        """Test submitting an order."""

        result = self.client.post('/process_order', 
                                  data={'melon_id': 'alib',
                                        'qty': '4',
                                        'state': 'CA'}, 
                                  follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)

        # make sure the order total is in the resulting page
        self.assertIn('Your order total comes to $', result.data)

        # make sure we were redirected to the listing page
        page_title = '<h1>Ubermelon\'s Artisinal, Bespoke Melon Selection</h1>'
        self.assertIn(page_title, result.data)


    def test_melon_detail(self):
        """Test a melon detail page."""
        
        result = self.client.get('/melon/alib')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Ali Baba Watermelon', result.data)


if __name__ == '__main__':
    unittest.main()