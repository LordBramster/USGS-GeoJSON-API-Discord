import os
from datetime import datetime
import json
import usgs_geojson_api as usgs_api
import usgs_geojson_webhook as usgs_webhook

if __name__ == "__main__":
    # https://earthquake.usgs.gov/fdsnws/event/1/
    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    # for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object

    # FEED QUERY
    # TODO replace input arguments with default variables for server/job use.
    feed_interval = "day"
    feed_magnitude = "significant"

    # USGS API FEED
    usgs_api_url = usgs_api.api_get_url_feed(feed_interval, feed_magnitude)
    api_raw = usgs_api.api_retrieve_feed(usgs_api_url)
    quake_list, quake_str = usgs_api.geojson_get_quakes(api_raw)

    # USGS WEBHOOK
    webhook_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    webhook_msg = f'`{webhook_datetime} | <{feed_magnitude}><{feed_interval}>`'
    # webhook_url = os.environ['ENV_URL'] or use config.json's -> usgs_webhook.get_webhook_url()
    webhook_urls = json.loads(os.environ['ENV_URLS'])  # '["URL1", "URL2", "URL3", "URL+"]'
    webhook_username = usgs_webhook.get_webhook_username()
    webhook_embeds_color = usgs_webhook.get_webhook_embeds_color('violet')
    webhook_embeds = [
        {
            "title": f"Earthquakes",
            "description": quake_str,
            "color": webhook_embeds_color
        }
    ]

    # FOR ALL URLs, SEND SAME WEBHOOK MESSAGE
    for url in webhook_urls:
        # SEND WEBHOOK
        webhook_status, webhook_sent = usgs_webhook.send_webhook(
            webhook_username,
            webhook_msg,
            webhook_embeds,
            url
        )
        # Print
        print(f"\nWEBHOOK: {webhook_sent}")
        print(f"RESPONSE: {webhook_status}")

    # TODO send multiple webhooks at once, and update webhook_config to have multiple keys.
    # SEND WEBHOOK
    # webhook_status, webhook_sent = usgs_webhook.send_webhook(webhook_username, webhook_msg, webhook_embeds, webhook_url)

    # Print
    # print(f"\nWEBHOOK: {webhook_sent}")
    # print(f"RESPONSE: {webhook_status}")
