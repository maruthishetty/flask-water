import cgi
import os
import time
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

            <h1>Login / SignUp</h1>

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
</html>
