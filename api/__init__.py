import os
import requests
from configparser import SafeConfigParser

cfg = SafeConfigParser()
cfg.read(os.path.normpath(os.sep.join([os.sep.join([os.path.dirname(__file__), '..', 'default.cfg'])])))
env = {'un': os.environ.get('TESLA_EMAIL'), 'pw': os.environ.get('TESLA_PASSWORD')}
url = 'https://%s' % cfg.get('owner_api', 'base_url')

class Tesla(object):
    def __init__(self, username=env.get('un'), password=env.get('pw'),
                 client_id=cfg.get('owner_api', 'client_id'), client_secret=cfg.get('owner_api', 'client_secret')):
        self._token = {}
        self.get_access_token()
        self.headers = {
            "Authorization": "Bearer {access_token}".format(access_token=self._token.get('access_token')),
            "User-Agent": "iluvelon; GitHub (jkubo); LinkedIn (jaykubo);"
        }
        # self.refresh_token()
        self.get_vehicles()
        # self.vehicle_ids
        self.vehicle_data = {}

    # AUTH
    def get_access_token(self, path='/oauth/token'):
        """
        POST /oauth/token?grant_type=password
        """
        try:
            self._token.update(requests.post(url='%s%s' % (url, path), data={
                'grant_type': 'password',
                'client_id': cfg.get('owner_api', 'client_id'),
                'client_secret': cfg.get('owner_api', 'client_secret'),
                'email': env.get('un'),
                'password': env.get('pw')
            }).json())
        except:
            raise 'invalid credentials'
        return self._token

    def refresh_token(self, path='/oauth/token'):
        """
        POST /oauth/token?grant_type=refresh_token
        """
        try:
            self._token.update(requests.post(url='%s%s' % (url, path), data={
                'grant_type': 'refresh_token',
                'client_id': cfg.get('owner_api', 'client_id'),
                'client_secret': cfg.get('owner_api', 'client_secret'),
                'refresh_token': self._token.get('refresh_token')
            }).json())
        except:
            raise 'unknown issue'
        return self._token

    # VEHICLE/S
    def get_vehicles(self, path='/api/1/vehicles'):
        try:
            self.vehicles = requests.get(url='%s%s' % (url, path), headers=self.headers).json()['response']
            self.vehicle_ids = dict({v['id_s']:v for v in self.vehicles})
        except:
            raise 'could not retrieve vehicles'
        return self.vehicles

    def get_vehicle(self, id_s, path='/api/1/vehicles/{id_s}'):
        try:
            self.vehicle_ids[id_s] = requests.get(url='%s%s' % (url, path.format(id_s=id_s)), headers=self.headers).json()['response']
        except:
            raise 'could not retrieve vehicle %s' % id_s
        return self.vehicle_ids[id_s]

    def get_vehicle_data(self, id_s, path='/api/1/vehicles/{id_s}/vehicle_data'):
        try:
            self.vehicle_data[id_s] = requests.get(url='%s%s' % (url, path.format(id_s=id_s)), headers=self.headers).json()['response']
        except:
            raise 'could not retrieve vehicle data %s' % id_s
        return self.vehicle_data[id_s]