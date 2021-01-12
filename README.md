# Weatherd

Schedule desktop weather notifications using custom cronjobs.

# Requirements
Python 3 is required. Notifications can only be run on OSX and Linux currently.

# Install
Download or clone and move `run.sh` outside of the main `/notifer/` directory. 

# Setup 
Get an API keys for [Open Weather Map](https://openweathermap.org/api) and [IP Info](https://ipinfo.io) and create a `.env` file in the project root. 
Add `OPEN_WEATHER_TOKEN=<YOURAPIKEYHERE>` and `IP_INFO_TOKEN=<YOURTOKENHERE>` to the file.
These are required for fetching the local weather.

Run `chmod +x run.sh && ./run.sh`

The script will create a new `/bin` in the user's home directory, look for the notifier directory, move it into the new `bin` directory, and create and run a new cron to trigger desktop weather notifications. 

This is done in order to allow cron execution from an accessible location in the filesystem.

The cron defaults to run a weather notification at 10AM GMT, but can be configured inside of the `run.sh` script.