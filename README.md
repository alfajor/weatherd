# Weatherd

Get automatic, localized desktop weather notifications.

# Requirements
Python3 should be installed. Notifications can only be run on OSX and Linux currently.

# Install
Download or clone and move `setup.sh` outside of the main `/notifer/` directory. 

# Setup 
Get API keys for [Open Weather Map](https://openweathermap.org/api) and [IP Info](https://ipinfo.io) and create a `.env` file in the project root. 
Add `OPEN_WEATHER_TOKEN=<YOURAPIKEYHERE>` and `IP_INFO_TOKEN=<YOURTOKENHERE>` to the file.
These are required for fetching the local weather.

Run `chmod +x setup.sh && ./setup.sh`

The script will create a new `/bin` in the user's home directory, find for the notifier directory, move it into the new `bin` directory, and create and run a new cron to trigger desktop weather notifications. 

This is done in order to allow cron execution from an accessible location in the filesystem.

The cron defaults to run a weather notification at 10AM, but can be configured inside of the `setup.sh` script.

Run `crontab -l` to view all scheduled jobs and `crontab -r` to delete.