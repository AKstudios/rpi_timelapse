#!/usr/bin/python
# coding=utf-8

# Developed by AKstudios
# https://github.com/AKstudios
# Septermber 17, 2017

from picamera import PiCamera
from time import sleep
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# obviously this is a fake token. duh. Use your own.
TOKEN = 'fJHKSv0VXNdsfgadfAALOLDQuA35lkC5zzRUHXsA3S8UsadWDXEWTFzrqq0shV_'
n=0 # set counter for incrementing file name

# Setup Dropbox and upload
def upload():
    global n    # bring global variable into function
    LOCALFILE = '/home/pi/timelapse/image%s.jpg' % n    # set local file path
    BACKUPPATH = '/Apps/AK_rpi3/timelapse/image%s.jpg' % n  # set Dropbox path

    with open(LOCALFILE, 'rb') as f:
        print("\nUploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            # upload file to Dropbox
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
            print("Uploaded! Das wussup, bro.")
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space."
                        "You probably need more money.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

# Capture an image
def capture():
    global n    # bring global variable into function
    n+=1 # increment file name
    camera.start_preview()  # start camera
    sleep(5)    # give some delay after camera starts
    camera.capture('/home/pi/timelapse/image%s.jpg' % n)    # capture image
    camera.stop_preview()   # stop camera

# main program
if __name__ == '__main__':
    camera = PiCamera() # create camera object
    camera.resolution = (1600, 1200)    # set image resolution
                                        # max: 3280 × 2464 (for camera v2)

    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Naw man, Looks like you didn't add your access token.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object using your token...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; What are you even typing fam?"
            "Try re-generating an access token from app console on the web.")

    # Take timelapse forever
    while True:
        capture()   # take image using rpi camera
        upload()    # upload image to dropbox
        sleep(3600)    # take timelapse at the specified interval in seconds
