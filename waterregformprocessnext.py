#!C:\Anaconda3\python.exe

import cgi
import cgitb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from grampg import PasswordGenerator
import pymysql


print("Content-type:text/html\r\n\r\n")

passwords = (PasswordGenerator().of().between(5, 10, 'letters')
                                     .at_least(4, 'numbers')
                                     .length(10)
                                     .beginning_with('letters')
                                     .done())

conn = pymysql.connect(host='127.0.0.1',database='waterconsumption',user='root',password='')
cursor = conn.cursor()


form = cgi.FieldStorage()

global a,b,c,p,k
global email

a = form.getvalue('otpentered')

cursor.execute("SELECT id,emailid from logdata where otpgenerated='%s'"%a)
data = cursor.fetchall()

def upddbwithpassw():
	cursor.execute("UPDATE logdata SET passwordgenerated=%s where otpgenerated=%s",(b,a))
	conn.commit()
	
def sen_email():
	k = data[0]
	p = str(k[1])
	fromaddr = "dumfun01@gmail.com"
	toaddr = p
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Water management Registration Password"

	body = "Your Password for Water management tool is "+b+" ."
	msg.attach(MIMEText(body,'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "dumb_1234")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

	
def printtrr():
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

				<h1>Registration Successful</h1>
				
				<form class="form-mini" >

					<h1>Password Sent to your Registered E-Mail ID</h1>

				</form>

			</div>


		</div>


	</body>
	</html>""") 
	
def prinffll():
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

				<h1>Entered OTP is Wrong Please Try Again</h1>

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
	</html>""")
	
if (data):
	b = passwords.generate()
	upddbwithpassw()
	sen_email()
	printtrr()
else:
	b = 'Entered OTP is Not Right'
	prinffll()



