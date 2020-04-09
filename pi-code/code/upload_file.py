import boto3
from boto3.s3.transfer import S3Transfer
import sys
from datetime import datetime
import csv
import os
import time

# Keeps MAC address, first time seen, last time seen, and power (rough distance metric)
# Reads from read_file, writes a new csv to write_file
def clean_csv(read_file, write_file):
	# Open file for reading
	with open(read_file, "rb") as source:
		rdr = csv.reader(source)

		# Open file for writing
		with open(write_file, "wb") as result:
			wtr = csv.writer(result)
			blank_lines = 0
			for r in rdr:
				# Only contain rows for bottom table in scan csv
				if blank_lines == 2 and r is not None and '\x00' not in r and len(r) > 0:
					try:
						wtr.writerow((r[0], r[1], r[2], r[3]))
					except Exception, err:
						f = open("error_log.txt", "a")
						f.write("ERROR: %s\n" % str(err))
						f.close()
				elif len(r) == 0:
					blank_lines += 1


def main():
	# Command line arguments
	args = sys.argv

	if len(args) < 2:
        	print("Usage: upload_file.py <path To File From Root>")
        	return

	# Create an S3 client
	S3 = boto3.client('s3', 'us-east-2')
	transfer = S3Transfer(S3)

	if "BUCKET_NAME" not in os.environ:
		print("Error: BUCKET_NAME not defined. Try running configuration script (/root/scripts/config.sh)")
		return
	BUCKET_NAME = os.environ.get("BUCKET_NAME")

	# Clean the log csv file
	time = datetime.now()
	write_time = time.strftime("%Y-%m-%d_%H%M")
	write_prefix = r"/root/logs/log_"
	READ_FILENAME = args[1]
	WRITE_FILENAME = write_prefix + write_time + ".csv"
	clean_csv(READ_FILENAME, WRITE_FILENAME)

	# Where to upload from
	SOURCE_FILENAME = WRITE_FILENAME

	# Directory in S3 bucket
	if "STORE_NAME" not in os.environ:
		print("Error: STORE_NAME not defined. Try running configuration script (/root/scripts/config.sh)")
		return
	DEST_FILENAME = "store-logs/" + os.environ.get("STORE_NAME") + "/log_" + write_time + ".csv"

	# Uploads the given file and sets it to public so other services can read it
	# boto3.s3.transfer handles retries automatically
	transfer.upload_file(SOURCE_FILENAME, BUCKET_NAME, DEST_FILENAME, extra_args={'ACL': 'public-read'})

if __name__ == '__main__':
	main()
