# -*-coding:UTF-8 -*-

import smtplib

# Email sending function from the exchange server mail  with a config. SMTP

#Request alert 80%

def envoi_onereq():
	fromaddr = 'yourMail@mail.com'
	toaddrs = ['xxxx@mail.com', 'zzzz@mail.com']
	sujet = "Alerte GLPI"
	message = u"""\
	My message
	"""
	param = """\
	From: %s\r\n\
	To: %s\r\n\
	Subject: %s\r\n\
	\r\n\
	%s
	"""
	msg = param % (fromaddr, ", ".join(toaddrs), sujet, message)
	server = smtplib.SMTP()
	#server.set_debuglevel(1)		#Uncomment this line to activate debug
	server.connect('SMTP Server Adress', Port)		#Connect to SMTP Server
	server.helo()
	server.sendmail(fromaddr, toaddrs, msg)		#Send email
	server.quit()		#Logout server
