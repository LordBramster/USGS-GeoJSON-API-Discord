import usgs_geojson_api as usgs_api
import usgs_geojson_webhook as usgs_webhook

if __name__ == "__main__":
    # https://earthquake.usgs.gov/fdsnws/event/1/
    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    # for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object

    # FEED QUERY
    # TODO replace input arguments with default variables for server use.
    feed_interval = str(input('\n Select an interval (hour/day/week/month) > '))
    feed_magnitude = str(input('\n Select a magnitude (M1.0/M2.5/M4.5/all/significant) > '))

    # USGS API FEED
    usgs_api_url = usgs_api.api_get_url_feed(feed_interval, feed_magnitude)
    api_raw = usgs_api.api_retrieve_feed(usgs_api_url)
    quake_list, quake_str = usgs_api.geojson_get_quakes(api_raw)

    # USGS WEBHOOK
    webhook_msg = ''
    webhook_url = usgs_webhook.get_webhook_url()
    webhook_username = usgs_webhook.get_webhook_username()
    webhook_embeds_color = usgs_webhook.get_webhook_embeds_color('violet')
    webhook_embeds = [
        {
            "title": f"Earthquakes :: <{feed_magnitude}><{feed_interval}>",
            "description": quake_str,
            "color": webhook_embeds_color
        }
    ]
    usgs_webhook.send_webhook(webhook_username, webhook_msg, webhook_embeds, webhook_url)
