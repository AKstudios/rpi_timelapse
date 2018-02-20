# RPi_timelapse
This is a Python script that takes images (as timelapse at a specified interval) using Raspberry Pi 3 + camera module (v2.1) and uploads the images to Dropbox using an access token. This will allow you to make API calls to Dropbox without going through the usual authorization flow. This is works even if the account has two-factor authentication.


## Requirements
You may have to install the latest version of pip first:

    sudo python get-pip.py

If you already have pip installed, update it using the following command:

    pip install -U pip


## Install Dropbox

    sudo pip install dropbox

For more information, check [here](https://www.dropbox.com/developers/documentation/python).

## Troubleshooting
If you're getting a timeout while running the script, the Python [requests](https://pypi.python.org/pypi/requests) package may need to be updated. Check your version against the latest one:

    sudo pip2 show requests

Update it using this command:

    sudo pip install requests --upgrade

## Setup
1. [Create an app](https://www.dropbox.com/developers/apps) in your Dropbox account and generate an access token.
2. Clone the repo and edit line 17 and 20 in dbx.py to add your token and path where you want the pics saved

## Run
1. Set the script up as a cron job. Make sure line 76 and line 80 in dbx.py are commented out and run:
```
sudo crontab -e
```
Now add the following to the end:
```
*/15**** python /home/pi/dbx.py >/dev/null 2>&1
@reboot python /home/pi/dbx.py
```
The interval set above is every 15 minutes. That value can be changed to your desired interval. Save the file, close crontab and reboot the Pi. You're set!

2. You can skip this step if you already set it as a cron tab. If you want to run it as a Python script manually on a specified interval instead, uncomment line 76 and line 80 in dbx.py and change the sleep interval in seconds.
3. Place the file in `/home/pi/` and run it using the following command:
```
python dbx.py
```
You will have to manually run the script every time your Pi is rebooted.
