#!C:\Anaconda3\python.exe

import cgi
import os
import time
print("Content-type: text/html")
print()
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

            <h1>Create an Account</h1>

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
</html>""")