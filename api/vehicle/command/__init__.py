from os import environ
from requests import post
from time import time
from ..oauth import oauth

class base(object):
    """
    Sets the url root path to reduce repetitive coding.
    Inherited by most of the command subclasses.
    """
    def __init__(self, url):
        """
        :param url: string of base of API's endpoint(s)
        """
        self.url = url

class command(oauth):
    def __init__(self, cfg_files):
        """
        :param cfg_files: list of string(s) containing paths to configuration files
        """
        super().__init__(cfg_files)
        self.headers = {"User-Agent": "i<3tesla by Jay Kubo; LinkedIn: jaykubo; GitHub: jkubo;"}
        self.cmd_url = self.url + '/api/1/vehicles/{id_s}/command'
        self.alert = self.alert(self.cmd_url)
        self.remote = self.remote(self.cmd_url)
        self.speed = self.speed(self.cmd_url)
        self.valet = self.valet(self.cmd_url)
        self.door = self.door(self.cmd_url)
        self.trunk = self.trunk(self.cmd_url)
        self.sunroof = self.sunroof(self.cmd_url)
        self.charge = self.charge(self.cmd_url)
        self.climate = self.climate(self.cmd_url)
        self.media = self.media(self.cmd_url)
        self.navigation = self.navigation(self.cmd_url)

    def set_vehicle(self, id_s):
        """
        Sets the vehicle id to be used in subsequent API requests

        :param id_s: string of vehicle id
        """
        self.id_s = id_s
        self.alert.id_s = self.remote.id_s = self.speed.id_s = self.valet.id_s = self.door.id_s = self.trunk.id_s = self.id_s
        self.sunroof.id_s = self.charge.id_s = self.climate.id_s = self.media.id_s = self.navigation.id_s = self.id_s
        return self

    def get_headers(self):
        """
        Obtains the latest valid access token and sets up the authorization header bearer token
        """
        headers = self.headers.copy()
        headers.update({"Authorization": "Bearer {access_token}".format(access_token=self.token.get('access_token'))})
        self.alert.headers = self.remote.headers = self.speed.headers = self.valet.headers = headers
        self.door.headers = self.trunk.headers = self.sunroof.headers = self.charge.headers = headers
        self.climate.headers = self.media.headers = self.navigation.headers = headers
        return headers

    ########################################
    ################ ALERT ################
    ########################################
    class alert(base):
        def __init__(self, url):
            super().__init__(url)

        def honk_horn(self, id_s=None, path='/honk_horn'):
            """
            Honks the horn twice.
            
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not honk horn'
            return data

        def flash_lights(self, id_s=None, path='/flash_lights'):
            """
            Flashes the headlights once.
            
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not flash headlights'
            return data

    ########################################
    ############# REMOTE START #############
    ########################################
    class remote(base):
        def __init__(self, url):
            super().__init__(url)

        def start_drive(self, password, id_s=None, path='/remote_start_drive'):
            """
            Enables keyless driving. There is a two minute window after issuing the command to start driving the car.

            :param password: The password for the authenticated tesla.com account.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'password': password}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not remote start drive'
            return data

    ########################################
    ############# SPEED LIMIT #############
    ########################################
    class speed(base):
        def __init__(self, url):
            super().__init__(url)

        def set_limit(self, limit_mph, id_s=None, path='/speed_limit_set_limit'):
            """
            Sets the maximum speed allowed when Speed Limit Mode is active.

            :param limit_mph: The speed limit in MPH. Must be between 50-90.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'limit_mph': limit_mph}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not set speed limit'
            return data

        def activate_limit(self, pin, id_s=None, path='/speed_limit_activate'):
            """
            Activates Speed Limit Mode at the currently set speed.

            :param pin: The existing PIN, if previously set, or a new 4 digit PIN.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'pin': pin}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not activate speed limit'
            return data
    
        def deactivate_limit(self, pin, id_s=None, path='/speed_limit_deactivate'):
            """
            Deactivates Speed Limit Mode if it is currently active.

            :param pin: The existing PIN, if previously set, or a new 4 digit PIN.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'pin': pin}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not deactivate speed limit'
            return data

        def clear_pin(self, pin, id_s=None, path='/speed_limit_deactivate'):
            """
            Clears the currently set PIN for Speed Limit Mode.

            :param pin: The existing PIN, if previously set, or a new 4 digit PIN.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'pin': pin}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not clear speed limit pin'
            return data

    ########################################
    ############## VALET MODE ##############
    ########################################
    class valet(base):
        def __init__(self, url):
            super().__init__(url)

        def set_valet(self, on, password, id_s=None, path='/set_valet_mode'):
            """
            Activates or deactivates Valet Mode.

            :param on: `True` to activate, `False` to deactivate. Must include previous PIN if deactivating.
            :param password: A PIN to deactivate Valet Mode. Can be blank if activating with a previous PIN.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'on': on, 'password': password}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not set valet mode'
            return data

        def reset_pin(self, id_s=None, path='/reset_valet_pin'):
            """
            Clears the currently set PIN for Valet Mode when deactivated. A new PIN will be required when activating again.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not reset valet pin'
            return data

    ########################################
    ################# DOOR #################
    ########################################
    class door(base):
        def __init__(self, url):
            super().__init__(url)

        def unlock(self, id_s=None, path='/door_unlock'):
            """
            Unlocks the doors to the car. Extends the handles on the S and X.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not unlock door'
            return data

        def lock(self, id_s=None, path='/door_lock'):
            """
            Locks the doors to the car. Retracts the handles on the S and X, if they are extended.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not lock door'
            return data
    
    ########################################
    ################ TRUNK ################
    ########################################
    class trunk(base):
        def __init__(self, url):
            super().__init__(url)

        def actuate(self, which_trunk, id_s=None, path='/actuate_trunk'):
            """
            Opens either the front or rear trunk. On the Model S and X, it will also close the rear trunk.

            :param which_trunk: Which trunk to open/close. `rear` and `front` are the only options.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'which_trunk': which_trunk}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not actuate %s trunk' % which_trunk
            return data

    ########################################
    ############### SUNROOF ###############
    ########################################
    class sunroof(base):
        def __init__(self, url):
            super().__init__(url)

        def control(self, state, id_s=None, path='/sun_roof_control'):
            """
            Controls the panoramic sunroof on the Model S.

            :param state: The amount to open the sunroof. Currently this only allows the values `vent` and `close`.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'state': state}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not %s sunroof' % state
            return data

    ########################################
    ################ CHARGE ################
    ########################################
    class charge(base):        
        def __init__(self, url):
            super().__init__(url)
        
        def open_port_door(self, id_s=None, path='/charge_port_door_open'):
            """
            Opens the charge port.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not open charge port'
            return data

        def close_port_door(self, id_s=None, path='/charge_port_door_close'):
            """
            For vehicles with a motorized charge port, this closes it.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not close charge port'
            return data

        def start(self, id_s=None, path='/charge_start'):
            """
            If the car is plugged in but not currently charging, this will start it charging.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not start charge'
            return data

        def stop(self, id_s=None, path='/charge_stop'):
            """
            If the car is currently charging, this will stop it.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not stop charge'
            return data

        def standard(self, id_s=None, path='/charge_stop'):
            """
            Sets the charge limit to "standard" or ~90%.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not set standard range'
            return data

        def max_range(self, id_s=None, path='/charge_max_range'):
            """
            Sets the charge limit to "max range" or 100%.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not set max range'
            return data

        def set_limit(self, percent, id_s=None, path='/set_charge_limit'):
            """
            Sets the charge limit to a custom value.

            :param percent: The percentage the battery will charge until.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'percent': percent}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not set charge limit'
            return data

    ########################################
    ############### CLIMATE ###############
    ########################################
    class climate(base):        
        def __init__(self, url):
            super().__init__(url)

        def start_hvac(self, id_s=None, path='/auto_conditioning_start'):
            """
            Stop the climate control (HVAC) system.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not start hvac'
            return data

        def stop_hvac(self, id_s=None, path='/auto_conditioning_stop'):
            """
            Stop the climate control (HVAC) system.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not stop hvac'
            return data

        def set_temps(self, driver_temp, passenger_temp, id_s=None, path='/set_temps'):
            """
            Sets the target temperature for the climate control (HVAC) system.
            
            :param driver_temp: The desired temperature on the driver's side in celsius.
            :param passenger_temp: The desired temperature on the passenger's side in celsius.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint

            Note: The parameters are always in celsius, regardless of the region the car is in or the display settings of the car.
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'driver_temp': driver_temp, 'passenger_temp': passenger_temp}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not set tempurature'
            return data
        
        def heat_seat(self, seat, level, path='/remote_seat_heater_request', id_s=None):
            """
            Sets the specified seat's heater level.

            :param seat: 0 - driver, 1 - passenger, 2 - left, 4 - center, 5 - right
            :param level: 0-3
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {'seat': seat, 'level': level}
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not heat seat'
            return data

    ########################################
    ################ MEDIA ################
    ########################################
    class media(base):        
        def __init__(self, url):
            super().__init__(url)

        def toggle_playback(self, id_s=None, path='/media_toggle_playback'):
            """
            Toggles the media between playing and paused. For the radio, this mutes or unmutes the audio.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not stop toggle playback'
            return data

        def next_track(self, id_s=None, path='/media_next_track'):
            """
            Skips to the next track in the current playlist.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not skip to next track'
            return data

        def prev_track(self, id_s=None, path='/media_prev_track'):
            """
            Skips to the previous track in the current playlist. Does nothing for streaming from Stitcher.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not skip to previous track'
            return data

        def next_fav(self, id_s=None, path='/media_next_fav'):
            """
            Skips to the next saved favorite in the media system.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not skip to next favorite track'
            return data

        def prev_fav(self, id_s=None, path='/media_prev_fav'):
            """
            Skips to the previous saved favorite in the media system.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not skip to previous favorite track'
            return data
    
        def volume_up(self, id_s=None, path='/media_volume_up'):
            """
            Turns up the volume of the media system.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not turn up volume'
            return data

        def volume_down(self, id_s=None, path='/media_volume_down'):
            """
            Turns down the volume of the media system.

            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers)
                data = res.json()['response']
            except:
                raise 'could not turn down volume'
            return data

    ########################################
    ############## NAVIGATION ##############
    ########################################
    class navigation(base):        
        def __init__(self, url):
            super().__init__(url)

        def request(self, value, locale='en-US', id_s=None, path='/request'):
            """
            Sends a location for the car to start navigation.

            :param value: The address to set as the navigation destination.
            :param locale: (optional) The locale for the navigation request.
            :param id_s: (optional) string of vehicle id, overwritten by object `id_s` attribute
            :param path: (optional) string of API endpoint
            """
            if id_s is None and hasattr(self, 'id_s'): id_s = self.id_s
            headers = self.headers
            try:
                payload = {
                    'type': 'share_ext_content_raw',
                    'timestamp_ms': int(time()),
                    'value': {'android.intent.extra.TEXT': value},
                    'locale': locale
                }
                res = post(url='%s%s' % (self.url.format(id_s=id_s), path), headers=headers, data=payload)
                data = res.json()['response']
            except:
                raise 'could not request navigation'
            return data