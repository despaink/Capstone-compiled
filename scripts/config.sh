#!/bin/bash
# Configures the Raspberry Pi beacon by storing environment variables in env.sh
# BUCKET_NAME - name of S3 bucket
# STORE_NAME - name of directory in bucket


rm /root/scripts/env.sh
touch /root/scripts/env.sh
chmod 755 /root/scripts/env.sh
echo "*** CONFIGURING RASPBERRY PI BEACON ***"

read -p "Set bucket name: BUCKET_NAME = " bucket_name
echo "export BUCKET_NAME=\"$bucket_name\"" >> env.sh

read -p "Set store name: STORE_NAME = " store_name
echo "export STORE_NAME=\"$store_name\"" >> env.sh

echo "*** CONFIGURATION COMPLETE ***"
