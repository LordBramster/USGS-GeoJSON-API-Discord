import requests
import json

""" Local Variable for the Webhook config """
config_webhook_file = 'usgs_geojson_webhook_config.json'
config_webhook = json.load(open(config_webhook_file, 'r'))


def get_webhook_urls():
    """ Return URLS from config """
    return config_webhook['webhook']['urls']


def get_webhook_username():
    """ Return USERNAME from config """
    return config_webhook['webhook']['username']


def get_webhook_embeds_color(color):
    """ Return integer color DECIMAL from available in config """
    return int(config_webhook['colors'][color]['dec'])


def get_response_code(result):
    """ Return STATUS code of the Webhook result """
    result_code = str(result.status_code)
    return result_code


def send_webhook(username, message, embeds, url):
    """ Send Webhook to URL """

    # Combine content and username into data dict
    webhook_data = dict(content=message, username=username)

    # Add Embedded Message
    if embeds is not None:
        """
        [
            {
                "title": "",
                "description": "",
                "color": 1234
            }
        ]
        """
        webhook_data["embeds"] = embeds

    # Send Request
    result_webhook = requests.post(url, json=webhook_data)

    # Get Response Code
    result_response = get_response_code(result_webhook)

    return result_response, webhook_data
