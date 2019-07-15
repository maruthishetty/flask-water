#!C:\Anaconda3\python.exe

# Import modules for CGI handling 
import cgi, cgitb
import os
import cgi
import cgitb
import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import pymysql

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

global tnd
global firstname
global lastname
global mobileno
global email
global otp
global data

# Get data from fields
firstname = form.getvalue('firstname')
lastname  = form.getvalue('lastname')
mobileno = form.getvalue('mobileno')
email = form.getvalue('email')



conn = pymysql.connect(host='127.0.0.1',database='waterconsumption',user='root',password='')
cursor = conn.cursor()

tnd = datetime.datetime.now()
tnd = tnd.strftime('%Y-%m-%d %H:%M:%S')

cursor.execute("SELECT id from logdata where emailid='%s'"%email)
data = cursor.fetchall()

def gen_otp():
        global otp
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
        otp = str(otp)
	#print otp

# E-Mail Section
def sen_email():
	fromaddr = "dumfun01@gmail.com"
	toaddr = email
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Water Management Tool Registration OTP"

	body = "Your OTP for Water Management tool Registration is "+otp+" ."
	msg.attach(MIMEText(body,'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "dumb_1234")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

#print "E-Mail Sent with OTP"

# FORM for Taking EMAIL OTP Input

def uppdb():
	add_user = ("INSERT INTO logdata(firstname,lastname,mobileno,emailid,otpgenerated,logtime)VALUES (%s, %s, %s, %s, %s, %s)")
	user_data = (firstname,lastname,mobileno,email,otp,tnd)
	cursor.execute(add_user,user_data)
	conn.commit()
	
def printruu():
	print("Content-type:text/html\r\n\r\n")
	print("""
	<html>
	<body>
	<title>REVA University</title>

		<link rel="stylesheet" href="assets/demo.css">
		<link rel="stylesheet" href="assets/form-mini.css">

	</head>

		<header>
			<h1>Water Management Tool using IoT</h1>
			<a href="http://www.reva.edu.in/">REVA University</a>
		</header>

		<div class="main-content">

			<!-- You only need this form and the form-mini.css -->
			
			<div class="form-mini-container">

				<h1>Enter the OTP Recieved in Registered E-Mail</h1>

				<form class="form-mini" action="waterregformprocessnext.py">

					<div class="form-row">
						<input type="text" name="otpentered" placeholder="Enter OTP">
					</div>
					
					<div class="form-row form-last-row">
						<button type="submit">Submit OTP</button>
					</div>

				</form>
			</div>


		</div>


	</body>
	</html>""" )
	
def prinfall():
	print("Content-type:text/html\r\n\r\n")
	print("""
	<html>
	<body>
	<title>REVA University</title>

		<link rel="stylesheet" href="assets/demo.css">
		<link rel="stylesheet" href="assets/form-mini.css">

	</head>

		<header>
			<h1>Water Management Tool using IoT</h1>
			<a href="http://www.reva.edu.in/">REVA University</a>
		</header>

		<div class="main-content">

			<!-- You only need this form and the form-mini.css -->
			
			<div class="form-mini-container">

				<h1>E-Mail Already Existed Try Different</h1>

				<form class="form-mini" action="waterregformprocess.py">

					<div class="form-row">
						<input type="text" name="firstname" placeholder="First Name" required>
					</div>
					
					<div class="form-row">
						<input type="text" name="lastname" placeholder="Last Name" required>
					</div>
					
					<div class="form-row">
						<input type="text" name="mobileno" placeholder="Mobile No." required>
					</div>

					<div class="form-row">
						<input type="email" name="email" placeholder="Your Email" required>
					</div>
					
					<div class="form-row form-last-row">
						<button type="submit">Submit Form</button>
					</div>

				</form>
			</div>


		</div>


	</body>
	</html>""" )

if (data):
    prinfall()
else:
    gen_otp()
    uppdb()
    sen_email()
    printruu()