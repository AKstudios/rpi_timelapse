# RPi_timelapse
This is a Python script that takes images (as timelapse at a specified interval) using Raspberry Pi 3 + camera module (v2.1) and uploads the images to Dropbox using an access token. This will allow you to make API calls to Dropbox without going through the usual authorization flow. This is works even if the account has two-factor authentication.

Place the file in `/home/pi/` and run it using the following command:

    python dbx.py


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





