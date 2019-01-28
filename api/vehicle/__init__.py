import time
import requests
from .command import command

class vehicle(command):
    def __init__(self, cfg_files):
        super().__init__(cfg_files)
        self.api_url = self.url + '/api/1/vehicles'

    def get_vehicles(self, path=''):
        """
        Retrieve a list of your owned vehicles (includes vehicles not yet shipped!)
        
        :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
        :param path: (optional) string of API endpoint
        """
        headers = self.get_headers()
        try:
            res = requests.get(url='%s%s' % (self.api_url, path), headers=headers)
            self.vehicles = dict({v['id_s']:v for v in res.json()['response']})
        except:
            raise 'could not retrieve vehicles - is your token set?'
        return self.vehicles

    def get_vehicle(self, id_s=None, path='/{id_s}'):
        """
        These resources are read-only and determine the state of the vehicle's various sub-systems.
        
        :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
        :param path: (optional) string of API endpoint
        """
        if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
        headers = self.get_headers()
        try:
            res = requests.get(url='%s%s' % (self.api_url, path.format(id_s=id_s)), headers=headers)
            data = self.vehicles.get(id_s).get('data')
            self.vehicles[id_s] = res.json()['response']
            self.vehicles[id_s]['data'] = data
        except:
            raise 'could not retrieve vehicles - is your token set?'
        return self.vehicles.get(id_s)

    def get_vehicle_data(self, id_s=None, path='/{id_s}/vehicle_data'):
        """
        A rollup of all the `data_request` endpoints plus vehicle configuration.
        
        :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
        :param path: (optional) string of API endpoint
        """
        if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
        headers = self.get_headers()
        try:
            res = requests.get(url='%s%s' % (self.api_url, path.format(id_s=id_s)), headers=headers)
            self.vehicles[id_s]['data'] = res.json()['response']
        except:
            raise 'could not retrieve vehicle - is your list up-to-date'
        return self.vehicles.get(id_s).get('data')

    def wake_up(self, id_s=None, path='/{id_s}/wake_up'):
        """
        Wakes up the car from a sleeping state.

        :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
        :param path: (optional) string of API endpoint
        """
        if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
        headers = self.get_headers()
        try:
            # 60 second timeout
            t = 0
            while t <= 12:
                res = requests.post(url='%s%s' % (self.api_url, path.format(id_s=id_s)), headers=headers)
                self.vehicles[id_s] = res.json()['response']
                try:
                    # print(t, self.vehicles.get(id_s).get('state'))
                    if self.vehicles.get(id_s).get('state') == 'online':
                        break
                except:
                    pass
                t += 1
                time.sleep(5)
        except:
            raise 'could not wake up vehicle'
        return self.vehicles.get(id_s).get('state')