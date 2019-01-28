import os
from .vehicle import vehicle

cfg_file = os.path.normpath(os.sep.join([os.sep.join([os.path.dirname(__file__), '..', 'default.cfg'])]))

class Tesla(object):
    def __init__(self):
        self.selected = None
        self.api = vehicle(cfg_file)
        try:
            self.api.get_access_token()
            self.api.get_vehicles()
        except:
            raise
    
    def oauth(self):
        """
        Refreshes the OAuth tokens

        Note: Needs to be authenticated via `Tesla.vehicle.get_access_token` first
        """
        return self.api.refresh_token()

    def list(self):
        """
        Lists all the vehicle ids available
        """
        self.oauth()
        return list(self.api.vehicles.keys())

    def set(self, id_s=None):
        """
        Sets the vehicle id to be used in subsequent API requests

        :param id_s: string of vehicle id

        Note: Alias function for `Tesla.vehicle.set_vehicle`
        """
        if id_s is None:
            return self.selected
        self.selected = id_s
        self.oauth()
        return self.api.set_vehicle(self.selected)
    
    def get(self, id_s=None):
        """
        Gets the vehicle id data

        :param id_s: string of vehicle id
        """
        if id_s is None:
            id_s = self.selected
        if id_s is None:
            raise 'vehicle id not provided nor set'
        self.oauth()
        return self.api.get_vehicle(id_s)