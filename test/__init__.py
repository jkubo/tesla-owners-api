# can import
from api import Tesla

t = Tesla()

# t
assert t.__class__ == Tesla

# t.oauth() ~ t.api.refresh_token()
assert t.oauth() is not None

# t.list ~ t.api.vehicles.keys()
assert t.list() is not None

VID = t.list()[-1]
# VID = '12345678901234567'

# t.set ~ t.api.set_vehicle
assert not hasattr(t.api, 'id_s')
t.set(VID)
assert hasattr(t.api, 'id_s')

# t.api.wake_up
assert t.set(VID).wake_up() == 'online'
assert t.get(VID).get('state') == 'online'

# t.get ~ t.api.get_vehicle
assert t.get(VID).get('data') is None
t.api.get_vehicle_data()
assert t.get(VID).get('data') is not None

# t.api.door ~ lock/unlock
assert t.api.door.unlock()['result']
assert t.api.door.lock()['result']

# t.api.climate ~ start/stop
assert t.api.climate.start_hvac()['result']
assert t.api.climate.stop_hvac()['result']

# t.api.media ~ user not present in car
# assert t.api.media.toggle_playback()['result']
# assert t.api.media.next_track()['result']
# assert t.api.media.toggle_playback()['result']
