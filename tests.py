"""Tests for Balloonicorn's Flask app."""

import unittest
import server


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get('/')
        self.assertIn(b'having a party', result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        result = self.client.get('/')

         #check that we are prompted to RSVP and don't see party details without it.
        self.assertIn(b'Please RSVP', result.data)
        self.assertNotIn(b'Party Details', result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': 'Jane', 'email': 'jane@jane.com'}

        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)

        #check that once we log in we see party details--but not the form!
        self.assertIn(b'Party Details', result.data)
        self.assertNotIn(b'Please RVSP', result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        pass
        print('FIXME')


if __name__ == '__main__':
    unittest.main()
