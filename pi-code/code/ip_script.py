import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import os

def main():

	# Change to your own account information
	if ('RECEIVER_EMAIL_ADDRESS' not in os.environ
		or 'SENDER_EMAIL_ADDRESS' not in os.environ
		or 'SENDER_EMAIL_PASSWORD' not in os.environ):
		print('Error: Configuration script has not been run yet. (/root/scripts/config.sh)')
		return

	to = os.environ.get('RECEIVER_EMAIL_ADDRESS')				# Receiver's email address
	gmail_user = os.environ.get('SENDER_EMAIL_ADDRESS')			# Sender's email address (requires permissions for third-party programs to use it)
	gmail_password = os.environ.get('SENDER_EMAIL_PASSWORD')	# Sender's email password
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(gmail_user, gmail_password)
	today = datetime.date.today()
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)

	# Sends email to "to" from "gmail_user" indicating this Raspberry Pi's IP address
	arg='ip route list'
	p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
	data = p.communicate()
	split_data = data[0].split()
	ipaddr = split_data[split_data.index('src')+1]
	my_ip = 'Your ip is %s' %  ipaddr
	msg = MIMEText(my_ip)
	msg['Subject'] = 'IP for RaspberryPi on %s' % today.strftime('%b %d %Y')
	msg['From'] = gmail_user
	msg['To'] = to
	smtpserver.sendmail(gmail_user, [to], msg.as_string())
	smtpserver.quit()

if __name__ == '__main__':
	main()
