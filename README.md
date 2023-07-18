
<p align="center">
    <br>
    <a href="#"><img width="50%" src="./assets/img/usgs_logo_full.png"></a>
</p>

<br>

# USGS Earthquake GeoJSON API Parser

> A simple USGS Earthquake GeoJSON API parser and an integration with Discord Webhooks.

<a href="#"><img alt="USGS API" src="https://custom-icon-badges.demolab.com/badge/USGS API-009973.svg?logo=server&logoColor=white&style=for-the-badge"></a>
<a href="#"><img alt="discord.py" src="https://img.shields.io/badge/discord-5865f2.svg?logo=discord&logoColor=ffffff&style=for-the-badge"></a>
<a href="#"><img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-8d3f8d.svg?logo=github%20actions&logoColor=white&style=for-the-badge"></a>
<a href="#"><img alt="Cron" src="https://img.shields.io/badge/Cron-372923.svg?logo=ubuntu&logoColor=white&style=for-the-badge"></a>

## Overview
[![GitHub Actions](https://github.com/LordBramster/USGS-GeoJSON-API-Discord/actions/workflows/actions.yml/badge.svg)](https://github.com/LordBramster/USGS-GeoJSON-API-Discord/actions/workflows/actions.yml)

## Discord Webhook

- 

## Custom collection of USGS-API-Feeds in JSON:
```
{
  "feed": {
    "hour": {
      "M1.0": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson",
      "M2.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson",
      "M4.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson",
      "all": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",
      "significant": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"
    },
    "day": {
      "M1.0": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson",
      "M2.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson",
      "M4.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson",
      "all": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
      "significant": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson"
    },
    "week": {
      "M1.0": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson",
      "M2.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson",
      "M4.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson",
      "all": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
      "significant": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson"
    },
    "month": {
      "M1.0": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson",
      "M2.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson",
      "M4.5": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson",
      "all": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
      "significant": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"
    }
  }
}
```