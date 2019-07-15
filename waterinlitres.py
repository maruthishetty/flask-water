#!C:\Anaconda3\python.exe

import cgi
import cgitb
import pymysql
import datetime

tnd = datetime.datetime.now()
tnd = tnd.strftime('%Y-%m-%d %H:%M:%S')

print("Content-type:text/html\r\n\r\n")

conn = pymysql.connect(host='127.0.0.1',database='waterconsumption',user='root',password='')
cursor = conn.cursor()


form = cgi.FieldStorage()

global a,b,c,p,k
global email

a = form.getvalue('noinlitres')
b = form.getvalue('watermeterno')

def upddbtowater():
	ta = ("INSERT INTO waterreq(waterinlitres,tnd,watermeterno)VALUES (%s, %s, %s)")
	tb = (a,tnd,b)
	cursor.execute(ta,tb)
	conn.commit()
	
a = int(a)
if a >= 10:
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

				<h1>Can't Supply More Than 10 Litres</h1>

				<form class="form-mini" action="waterinlitres.py">
					<div class="form-row">
						<input type="text" name="watermeterno" placeholder="Enter Water Meter Number" required>
					</div>
					
					<div class="form-row">
						<input type="text" name="noinlitres" placeholder="Number Of Litres You Required" required>
					</div>
					
					<div class="form-row form-last-row">
						<button type="submit">Request for Water</button>
					</div>

				</form>
			</div>


		</div>


	</body>
	</html>""")
else:
	upddbtowater()
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

				<h1>Successfully Submitted</h1>

				<form class="form-mini">

					<h1> Please Turn On Your Tap</h1>

				</form>
			</div>


		</div>


	</body>
	</html>""")

