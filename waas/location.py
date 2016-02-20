import requests

IPIFY = 'https://api.ipify.org?format=json'

from geoip import geolite2

def get_coords_from_ip(ip=None):
    if ip is None:
        ip = _get_local_ip()
    match = geolite2.lookup(ip)
    return match.location


def _get_local_ip():
    response = requests.get(IPIFY)
    if not response.ok:
        return ''
    return response.json()['ip']
