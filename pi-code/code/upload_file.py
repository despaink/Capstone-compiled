import boto3
import sys
from datetime import datetime
import csv
import os

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
				if blank_lines == 2 and r is not None and len(r) > 0:
					wtr.writerow((r[0], r[1], r[2], r[3]))
				elif len(r) == 0:
					blank_lines += 1


def main():
	args = sys.argv

	if len(args) < 2:
        	print("Usage: upload_file.py <path To File From Root>")
        	return

	# Create an S3 client
	S3 = boto3.client('s3')

	if "BUCKET_NAME" not in os.environ:
		print("Error: BUCKET_NAME not defined")
		return
	BUCKET_NAME = os.environ.get("BUCKET_NAME") 

	# Clean the log csv file
	time = datetime.now()
	write_time = time.strftime("%Y-%m-%d_%H%M")
	write_prefix = r"/root/logs/log_"
	READ_FILENAME = args[1]
	WRITE_FILENAME = write_prefix + write_time + ".csv"
	print(write_time)
	clean_csv(READ_FILENAME, WRITE_FILENAME)

	# Where to upload from
	SOURCE_FILENAME = WRITE_FILENAME

	# Directory in S3 bucket
	if "STORE_NAME" not in os.environ:
		print("Error: STORE_NAME not defined")
		return
	DEST_FILENAME = os.environ.get("STORE_NAME") + "/log_" + write_time + ".csv" 

	# Uploads the file
	S3.upload_file(SOURCE_FILENAME, BUCKET_NAME, DEST_FILENAME, ExtraArgs={'ACL': 'public-read'})


if __name__ == '__main__':
	main()
