import requests
from os import environ
from configparser import SafeConfigParser
from getpass import getpass

class oauth:
    """
    The Password grant type is used by first-party clients to exchange a user's credentials for an access token.
    """
    def __init__(self, cfg_files):
        """
        :param cfg_files: list of string(s) containing paths to configuration files
        """
        self.env = environ
        self.cfg = SafeConfigParser()
        self.cfg.read(cfg_files)
        self.token = {}
        self.url = 'https://%s' % self.cfg.get('owner_api', 'base_url')
        self.data = {
            'client_id': self.cfg.get('owner_api', 'client_id'),
            'client_secret': self.cfg.get('owner_api', 'client_secret')
        }

    def get_access_token(self, path='/oauth/token', data={}):
        """
        The initial authentication process is via an OAuth 2.0 Password Grant.
        This is the same credentials used for tesla.com and the mobile apps.

        :param path: (optional) string of API endpoint
        :param data: (optional) dictionary of request parameters

        Note: The access token has a 45 day expiration.
        """
        if data.keys():
            data.update(self.data)
        else:
            data = self.data.copy()
            data.update({
                'grant_type': 'password',
                'email': self.env.get('TESLA_EMAIL'),
                'password': self.env.get('TESLA_PASSWORD')
            })
        try:
            req = requests.post(url='%s%s' % (self.url, path), data=data)
            # print(req.status_code)
            # print(req.content)
            self.token.update(req.json())
        except:
            raise 'invalid credentials'
        return self.token

    def refresh_token(self, path='/oauth/token', data={}):
        """
        You can use the refresh_token from the Password Grant to obtain a new access token.
        
        :param path: (optional) string of API endpoint
        :param data: (optional) dictionary of request parameters

        Note: This will invalidate the previous access token.
        """
        if data.keys():
            data.update(self.data)
        else:
            data = self.data.copy()
            data.update({
                'grant_type': 'refresh_token',
                'refresh_token': self.token.get('refresh_token')
            })
        try:
            self.token.update(requests.post(url='%s%s' % (self.url, path), data=data).json())
        except:
            raise 'unknown issue'
        return self.token