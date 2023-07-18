from urllib.request import urlopen
import json

""" Local Variable for the API config """
config_api_file = 'usgs_geojson_api_config.json'
config_api = json.load(open(config_api_file, 'r'))


def api_get_url_feed(key_interval, key_magnitude):
    """ Get URL of API Feed, based on INTERVAL and MAGNITUDE """
    return config_api['feed'][key_interval][key_magnitude]


def api_retrieve_feed(url):
    """ Request API Feed from URL """
    response = urlopen(url)
    response_raw = json.loads(response.read())
    return response_raw


def api_status_valid(status):
    """ Check API Status is 200 """
    if str(status) == '200':
        return True
    else:
        return False


def geojson_get_quakes(geojson):
    """ Get Quake Properties from GeoJSON """
    quakes = []
    quakes_str = ""
    for quake in geojson['features']:
        quake_title = quake['properties']['title']
        quakes.append(quake_title)
        quakes_str += f'\n{quake_title}'
    return quakes, quakes_str
