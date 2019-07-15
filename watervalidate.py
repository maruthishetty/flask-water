#!C:\Anaconda3\python.exe

import cgi
import cgitb
import pymysql

print("Content-type:text/html\r\n\r\n")

conn = pymysql.connect(host='127.0.0.1',database='waterconsumption',user='root',password='')
cursor = conn.cursor()


form = cgi.FieldStorage()

global a,b,c,p,k
global email

a = form.getvalue('username')
b = form.getvalue('password')

#a = 'rajath.ask@gmail.com'

cursor.execute("SELECT id from logdata where emailid='%s'AND passwordgenerated='%s'"%(a,b))
data = cursor.fetchall()


def upddbwithpassw():
	cursor.execute("UPDATE logdata SET passwordgenerated=%s where otpgenerated=%s",(b,a))

def printgood():
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

				<h1>Water is Precious..!</h1>

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
	
def printbad():
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

				<h1>Check Your UserName and Password</h1>

				<form class="form-mini" action="watervalidate.py" method="post">
					<div class="form-row">
						<input type="text" name="username" placeholder="Registered E-Mail" required>
					</div>
					
					<div class="form-row">
						<input type="password" name="password" placeholder="Password" required>
					</div>
					<div class="form-row form-last-row">
						<button type="submit">Sign In</button>
					</div>
				</form>
				<form class="form-mini" action="waterregform.py">
					<h2>Register Here</h2>
					<div class="form-row form-last-row">
						<button type="submit">Sign Up</button>
					</div>

				</form>
			</div>

		</div>


	</body>
	</html>""") 
	
if(data):
    printgood()
else:
    printbad()

