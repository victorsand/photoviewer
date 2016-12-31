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
Placed at `/home/pi/apps/photoviewer/config/aws`, with the following contents:**

	eu-central-1
	myBucketName
	MYAWSACCESSKEYID
	MYAWSSECRETACCESSKEY

Containing your own region, bucket name, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY values.

**4. Run the script**
Execute `/home/pi/apps/photoviewer/slideshow.sh` which will launch the Python program that sync with the S3 bucket, and then fires up the slideshow.