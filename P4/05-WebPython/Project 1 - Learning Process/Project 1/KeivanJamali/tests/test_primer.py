from django.test import TestCase

class PrimerTestCases(TestCase):
    def test_say_hello(self):
        response = self.client.get('/this_is_the_url/')
        self.assertEqual(200, response.status_code)
        self.assertIn('Hello', str(response.content))