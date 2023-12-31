from urllib.request import urlopen
import json
from datetime import datetime

# for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
# for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object

""" Local Variable for the API config """
config_api_file = 'usgs_geojson_api_config.json'
config_api = json.load(open(config_api_file, 'r'))
config_query_file = 'usgs_geojson_api_query.json'
config_query = json.load(open(config_query_file, 'r'))


def api_get_feed_interval():
    """ Get API INTERVAL """
    return config_query['params']['interval']


def api_get_feed_magnitude():
    """ Get API MAGNITUDE """
    return config_query['params']['magnitude']


def api_get_query_url():
    """ Get API Query URL """
    return config_api['query']['url']


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


def geojson_get_quakes_titles(geojson):
    """ Get Quake Properties from GeoJSON """
    quakes = []
    quakes_str = ""
    for quake in geojson['features']:
        quake_title = quake['properties']['title']
        quake_message = f'{quake_title}'
        quakes.append(quake_message)
        quakes_str += f'\n{quake_message}'
    return quakes, quakes_str


def geojson_get_quakes(geojson):
    """ Get Quake Unixtime+Magnitude+Place from GeoJSON """
    quakes = []
    quakes_str = ""
    for quake in geojson['features']:
        # TODO /1000 is required for Win10 OS
        quake_unixtime = quake['properties']['time']
        quake_utc = datetime.fromtimestamp(quake_unixtime / 1000)
        quake_mag = quake['properties']['mag']
        quake_place = quake['properties']['place']
        quake_message = f'{quake_utc:%Y-%m-%d} | M{quake_mag} => {quake_place}'
        quakes.append(quake_message)
        quakes_str += f'\n{quake_message}'
    return quakes, quakes_str


def geojson_exists_quakes(quakes):
    """ Return True/False if no Earthquakes from GeoJSON """
    if len(quakes) <= 0:
        return False
    else:
        return True
