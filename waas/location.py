import requests

IPIFY = 'http://api.ipify.org?format=json'
CARDINAL_MAPPING = [
    'N','NE','NNE','ENE',
    'E','ESE','SE', 'SSE',
    'S','SSW','SW','WSW',
    'W','WNW','NW','NNW'
]


from geoip import geolite2

def get_coords_from_ip(ip=None):
    if ip is None:
        ip = _get_local_ip()
    match = geolite2.lookup(ip)
    return match.location


def degrees_to_cardinal(degrees):
    return CARDINAL_MAPPING[
        int(degrees / (360.0 / len(CARDINAL_MAPPING)))
    ]


def _get_local_ip():
    response = requests.get(IPIFY)
    if not response.ok:
        return ''
    return response.json()['ip']
