*** Instructions for setting up Raspberry Pi ***



1. Connect the Pi to the internet either through an ethernet cable (required for first time) or (for later sessions) by running the following command while SSHed in:

   nmcli device wifi connect SSID-Name password wireless-password



2. SSH into the Pi using the following command:

   ssh root@ipaddress

   The password will be "capstone"



3. Configure your AWS Command Line Interface by running the following command:

   aws configure



4. Run the configuration script to generate the environment variables (env.sh) by running the following command:

   /root/scripts/config.sh



5. Open up your cron jobs with the following command:

   crontab -e



6. Uncomment the cron jobs at the bottom you wish to use, then save and quit. For example, one will look like this:

   # Scan MAC addresses nearby and upload the log file every 30 minutes
   # @reboot sleep 120 ; /root/scripts/setup-mon ; sleep 5 ; /root/scripts/scan-log; sleep 5 ; /root/scripts/upload-log

   and end up looking like this:

   # Scan MAC addresses nearby and upload the log file every 30 minutes
   @reboot sleep 120 ; /root/scripts/setup-mon ; sleep 5 ; /root/scripts/scan-log; sleep 5 ; /root/scripts/upload-log



7. Refresh your cron jobs by running the following command:

   /etc/init.d/cron start



8. Reboot the Raspberry Pi by typing the following command:

   reboot



9. It should now be set to scan and upload logs on boot if you uncommented the proper cron jobs!
