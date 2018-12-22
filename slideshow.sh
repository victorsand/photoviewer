#!/bin/sh
sudo killall feh
/usr/bin/python /home/pi/apps/photoviewer/fetch.py
feh -ZFz -D 600 --hide-pointer /home/pi/apps/photoviewer/images
