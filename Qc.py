import re
import requests
import xml.etree.ElementTree as ET


class Qc:
    url = "https://almalmqc1250saastrial.saas.hpe.com/qcbin"

    def __init__(self, username, password, domain, project):
        self.username = username
        self.password = password
        self.domain = domain
        self.project = project

        self.session = requests.Session()

    def __del__(self):
        self.session.close()

    def __enter__(self):
        try:
            if not self.login():
                raise requests.exceptions.HTTPError("There is exception at the beginning of session")

        except requests.exceptions.HTTPError as e:
            if self.logout():
                raise e
            else:
                raise requests.exceptions.HTTPError("Exception in logout")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.logout():
            raise requests.exceptions.HTTPError("Exception in logout")

    def login(self):


        authenticationStatus = self.isAuthenticated()
        if authenticationStatus is True:
            return True

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'login.software.microfocus.com',
        }

        answer = self.session.post('https://login.software.microfocus.com/msg/actions/doLogin.action', headers=headers,
                            data={'username': self.username, 'password': self.password})

        if answer.status_code == requests.codes.ok:
            if 'LWSSO_COOKIE_KEY' in answer.cookies.get_dict():
                self.session.cookies.update({
                    'LWSSO_COOKIE_KEY': answer.cookies.get('LWSSO_COOKIE_KEY'),
                })
                return True
            else:
                return False
        else:
            return False

    def createSession(self):
        requestUrl = self.url + '/rest/site-session'
        answer = self.session.post(requestUrl)

        if answer.status_code == requests.codes.created:
            cookies = answer.cookies.get_dict()
            if ('XSRF-TOKEN' in cookies and 'QCSession' in cookies):
                self.session.cookies.update({
                    'X-XSRF-TOKEN': cookies.get('XSRF-TOKEN'),
                    'QCSession': cookies.get('QCSession'),
                })
                return True
            else:
                return False
        else:
            return False

    def logout(self):
        logoutUrl = self.url + '/authentication-point/logout'
        answer = self.session.get(logoutUrl)

        if answer.status_code == requests.codes.ok:
            self.session.cookies.clear()
            return True
        else:
            return False

    def isAuthenticated(self):
        answer = self.session.get(self.url + '/rest/is-authenticated')
        if answer.status_code == requests.codes.ok:
            return True
        elif answer.status_code == requests.codes.unauthorized:
            authenticationUrl = (re.search('\"(.*)\"', answer.headers.get('WWW-Authenticate'))).group(1)
            return authenticationUrl
        else:
            raise answer.raise_for_status()

    def getEntity(self, entityType, entityId=None, query=None):
        entities = ['tests', 'test-sets', 'test-configs',
                    'test-set-folders', 'test-instances',
                    'runs', 'release-cycles', 'defects']
        if entityType not in entities:
            raise ValueError("There is not in entities")
        entityRequestUrl = '{0}/rest/domains/{1}/projects/{2}/{3}'.format(self.url, self.domain,
                                                                          self.project, entityType)
        if entityId is not None:
            entityRequestUrl = entityRequestUrl + '/{0}'.format(entityId)
        answer = self.session.get(entityRequestUrl, params={'query': query})
        if answer.status_code == requests.codes.ok:
            xml = ET.fromstring(answer.content)
            return xml.findall('Entity')
        else:
            raise answer.raise_for_status()
