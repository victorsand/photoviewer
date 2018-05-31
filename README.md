# Photo Viewer
Simple app for showing a slideshow of images fetched from an Amazon S3 bucket. Lots of hardcoded directories, some manual work to do.

## Preparation
1. Get yourself an Amazon S3 account, and create a bucket. Upload some images to it.
2. Set up credentials, allow download/upload and write down the access keys.
## Installation
**1. Install the slideshow software**

`sudo apt-get install feh`

**2. Clone this repository into the directory of your choice**

If you choose `/home/pi/apps/photoviewer`, you won't have to change any hardcoded values.

**3. Create a four-line config file**
Placed at `/home/pi/apps/photoviewer/config/aws`, with the following contents:

	eu-central-1
	myBucketName
	MYAWSACCESSKEYID
	MYAWSSECRETACCESSKEY

Containing your own region, bucket name, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY values.

**4. Install dependencies**

Run `pip install boto3`

**5. Run the script**

Execute `/home/pi/apps/photoviewer/slideshow.sh` which will launch the Python program that syncs with the S3 bucket, and then fires up the slideshow.

## GPIO Buttons

The Raspberry Pi lacks a power button, so I decided to add one. I also added a restart button and an extra button for killing the slideshow app while I was at it! This is not strictly neccessary, but could be useful if running on a non-touch screen for example.

The script is contained in `buttons.py` and runs on startup as described below.

## Automation

Setting up this on a Raspberry Pi and get it to run automatically on boot proved to be a little tricky. The Python library for S3 interaction, boto3, gave me some troubles with credentials when running the scripts as root from crontab, and the Python script for controlling the GPIO buttons demands root access. I ended up with the following setup:

# init.d script for GPIO

TODO

# cronjob for updates on reboot

With `crontab -e` add the line `@reboot export DISPLAY:=0 && /home/pi/apps/photoviewer/slideshow.sh` 

# cronjob for automatic shutdown

I wanted to power the machine off at night. I use crontab and a simple timer for the electrical outlet to turn off the Pi first at 22:00, then the power (say an hour later) and then wake it up again in the morning at 07:00 or so.

With `sudo crontab -e` add the line `0 22 * * * /sbin/shutdown now`



