#!/bin/sh
sudo killall feh
/usr/bin/python /home/pi/apps/photoview/fetch.py
feh -ZF -D 30 --hide-pointer /home/pi/apps/photoview/images
