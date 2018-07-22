import unittest

import requests

from secure import SecureData
from Qc import Qc


class QcTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(QcTestCase, self).__init__(methodName)
        self.username = SecureData.username
        self.password = SecureData.password
        self.project = SecureData.project
        self.domain = SecureData.domain

    def test_isAuthenticatedWhenNotAuthenticated(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        self.assertNotEqual(True, client.isAuthenticated())

    def test_isAuthenticatedWhenAuthenticated(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        self.assertTrue(client.isAuthenticated())

    def test_logout(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        client.logout()
        self.assertNotEqual(True, client.isAuthenticated())

    def test_loginWithCorrectData(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        self.assertTrue(client.login())

    def test_loginWithIncorrectData(self):
        client = Qc('test', 'test', self.domain, self.project)
        self.assertFalse(client.login())

    def test_loginAfterLogin(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        self.assertTrue(client.login())

    def test_containsCookieAfterLogin(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        self.assertIn('LWSSO_COOKIE_KEY', client.session.cookies.get_dict().keys())

    def test_createSessionWithoutLogin(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        self.assertFalse(client.createSession())

    def test_containsCookiesAfterCreateSession(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        client.createSession()

        self.assertIn('X-XSRF-TOKEN', client.session.cookies.get_dict().keys())
        self.assertIn('QCSession', client.session.cookies.get_dict().keys())

    def test_getEntityWithCorrectData(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        client.createSession()
        self.assertIsInstance(client.getEntity('tests'), list)

    def test_getEntityWithIncorrectData(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        client.login()
        client.createSession()
        with self.assertRaises(ValueError):
            client.getEntity('entity')

    def test_getEntityWithoutLoginAndSession(self):
        client = Qc(self.username, self.password, self.domain, self.project)
        with self.assertRaises(requests.HTTPError):
            self.assertRaises(client.getEntity('tests'))

    def test_classAsContextManagerWithCorrectData(self):
        with Qc(self.username, self.password, self.domain, self.project) as client:
            client.createSession()
            self.assertIsInstance(client.getEntity('tests'), list)

    def test_classAsContexManagerExitCorrect(self):
        with self.assertRaises(requests.exceptions.RequestException):
            with Qc(self.username, self.password, self.domain, self.project) as client:
                pass

            client.getEntity('tests')


if __name__ == '__main__':
    unittest.main()

