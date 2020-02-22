#!/bin/bash
# Configures the Raspberry Pi beacon
# BUCKET_NAME - name of S3 bucket
# STORE_NAME - name of directory in bucket

# Remove old environment variables if they already exist
if test -f "/root/scripts/env.sh"; then
	rm /root/scripts/env.sh
fi

# Create new environment variables file env.sh
touch /root/scripts/env.sh
chmod 755 /root/scripts/env.sh


printf "\n*** CONFIGURING RASPBERRY PI BEACON ***\n"

printf "\nSet bucket name:\n"
read -p "BUCKET_NAME = " bucket_name
echo "export BUCKET_NAME=\"$bucket_name\"" >> env.sh

printf "\nSet store name:\n"
read -p "STORE_NAME = " store_name
echo "export STORE_NAME=\"$store_name\"" >> env.sh

printf "\n*** IP ADDRESS EMAIL SCRIPT CONFIGURATION ***\n\n"
printf "If you want your Pi to send you an email with its IP address on startup, fill out the information below.\n"
printf "If not, then just press enter to enter blank information.\n"
printf "NOTE: \"Less secure app access\" must be enabled on sender's gmail and the appropriate cron job \n"
printf "      must be uncommented after typing the command \"crontab -e\" for it to work\n"

printf "\nSet sender's email address (needs less secure app access enabled):\n"
read -p "SENDER_EMAIL_ADDRESS = " sender_email_address
echo "export SENDER_EMAIL_ADDRESS=\"$sender_email_address\"" >> env.sh

printf "\nSet sender's email password (not stored securely):\n"
read -p "SENDER_EMAIL_PASSWORD = " sender_email_password
echo "export SENDER_EMAIL_PASSWORD=\"$sender_email_password\"" >> env.sh

printf "\nSet receiver's email address (where you want to receive the IP address email):\n"
read -p "RECEIVER_EMAIL_ADDRESS = " receiver_email_address
echo "export RECEIVER_EMAIL_ADDRESS=\"$receiver_email_address\"" >> env.sh

printf "\n*** CONFIGURATION COMPLETE ***\n"
