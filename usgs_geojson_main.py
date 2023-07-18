import usgs_geojson_api as usgs_api
import usgs_geojson_webhook as usgs_webhook

if __name__ == "__main__":
    # https://earthquake.usgs.gov/fdsnws/event/1/
    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    # for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object

    # FEED QUERY
    feed_interval = "day"
    feed_magnitude = "M4.5"

    # USGS API FEED
    usgs_api_url = usgs_api.api_get_url_feed(feed_interval, feed_magnitude)
    api_raw = usgs_api.api_retrieve_feed(usgs_api_url)
    quake_list, quake_str = usgs_api.geojson_get_quakes(api_raw)

    # USGS WEBHOOK
    webhook_msg = ''
    webhook_url = usgs_webhook.get_webhook_url()
    webhook_username = usgs_webhook.get_webhook_username()
    webhook_embeds_color = usgs_webhook.get_webhook_embeds_color('purple')
    webhook_embeds = [
        {
            "title": f"<{feed_magnitude}><{feed_interval}> :: Quakes",
            "description": quake_str,
            "color": webhook_embeds_color
        }
    ]
    usgs_webhook.send_webhook(webhook_username, webhook_msg, webhook_embeds, webhook_url)
