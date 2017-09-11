import os
import os.path
import boto3
import logging

def sync_image_folder():

	app_path = os.path.join(os.path.sep, 'home', 'pi', 'apps', 'photoviewer')
	logging.info('App path: %s' % app_path)

	config_file_path = os.path.join(app_path, 'config', 'aws')
	logging.info('Config file: %s' % config_file_path)	

	with open(config_file_path) as config:
		config_lines = config.readlines()

	region      	  = config_lines[0].rstrip()
	bucket_name 	  = config_lines[1].rstrip()
	access_key_id 	  = config_lines[2].rstrip()
	secret_access_key = config_lines[3].rstrip()

	image_path = os.path.join(app_path, 'images')
	if not os.path.exists(image_path):
		os.makedirs(image_path)

	files_in_dir = os.listdir(image_path)
	logging.info('Files in dir: %s ' % files_in_dir)

	client = boto3.client(
		's3',
		region_name=region,
		aws_access_key_id=access_key_id,
		aws_secret_access_key=secret_access_key
	)

	logging.info('Connecting to bucket: %s' % bucket_name)

	bucket_objects = client.list_objects(Bucket=bucket_name)['Contents']
	files_in_bucket = [key['Key'] for key in bucket_objects]
	logging.info('Files in bucket: %s' % files_in_bucket)

	for bucket_file in files_in_bucket:
		if not bucket_file in files_in_dir:
			logging.info('Downloading %s ' % bucket_file)
			file_path = os.path.join(image_path, bucket_file)
			client.download_file(bucket_name, bucket_file, file_path)
		else:
			logging.info('%s already downloaded' % bucket_file)

	for downloaded_file in files_in_dir:
		if not downloaded_file in files_in_bucket:
			logging.info('Removing % s ' % downloaded_file)
			os.remove(os.path.join(image_path, downloaded_file))
	
	return



logging.basicConfig(filename='/home/pi/apps/photoviewer/debug.log',
		    level=logging.INFO,
		    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
		    datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Running fetch script')
try:
	sync_image_folder()
except Exception as e:
	logging.exception(e)
