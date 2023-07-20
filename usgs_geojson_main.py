import os
from datetime import datetime
import json
import usgs_geojson_api as usgs_api
import usgs_geojson_webhook as usgs_webhook

if __name__ == "__main__":

    # API FEED QUERY
    # Change query parameters (e.g, week => day, M4.5 => all) in: usgs_geojson_api_query.json
    feed_interval = usgs_api.api_get_feed_interval()
    feed_magnitude = usgs_api.api_get_feed_magnitude()

    # USGS API FEED
    usgs_api_url = usgs_api.api_get_url_feed(feed_interval, feed_magnitude)
    api_raw = usgs_api.api_retrieve_feed(usgs_api_url)
    quake_list, quake_str = usgs_api.geojson_get_quakes(api_raw)

    # NO QUAKES AND DEFAULT PARAMETERS
    if usgs_api.geojson_exists_quakes(quake_list):
        embeds_title = 'Earthquakes'
        embeds_color = 'violet'
        embeds_desc = quake_str
    else:
        embeds_title = 'No New Earthquake Data'
        embeds_color = 'blue'
        embeds_desc = ''

    # USGS WEBHOOK
    webhook_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    webhook_msg = f'`{webhook_datetime} | <{feed_magnitude}><{feed_interval}>`'

    # TODO replace webhook_urls with os.environ[...] variable for server/job use.
    # webhook_urls = usgs_webhook.get_webhook_urls()
    webhook_urls = json.loads(os.environ['ENV_URLS'])

    # NOTE
    # Formatting using json.loads(os.environ[...]) below:
    # ["URL1", "URL2", "URL3", "URL+"] => '["URL1", "URL2", "URL3", "URL+"]'
    # usgs_webhook.get_webhook_urls() => json.loads(os.environ['ENV_URLS'])

    webhook_username = usgs_webhook.get_webhook_username()
    webhook_embeds_color = usgs_webhook.get_webhook_embeds_color(embeds_color)
    webhook_embeds = [
        {
            "title": embeds_title,
            "description": embeds_desc,
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
        # PRINT
        print()
        print(f"DATA: {webhook_sent}")
        print(f"RESPONSE: {webhook_status}")
