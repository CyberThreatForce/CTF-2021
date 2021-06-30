<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title> APT403 Forum</title>
    <meta name="author" content="Codeconvey" />
    <!-- favicon --> 
    <!-- Font Awesome -->
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    
    <!-- Stylish Login Page CSS -->
    <link rel="stylesheet" href="css/login-page.css">
    
    <!--Only for demo purpose - no need to add.-->
    <link rel="stylesheet" href="css/demo.css" />
</head>
<body>
<header class="ScriptHeader">
    <div class="rt-container">
        <div class="col-rt-12">
                <div class="rt-heading">
                <h1>APT403 Forum</h1>
                <p>For our country we will deploy evil measure</p>
            </div>
        </div>
    </div>
</header>

<section>
    <div class="rt-container">
          <div class="col-rt-12">
              <div class="Scriptcontent">

              <!-- Stylish Login Page Start -->
    <form class="codehim-form" method=post action="inscription.php">
        <div class="form-title">
            <div class="user-icon gr-bg">
            </div>
     <h2>Authentication</h2>
	    </div>
	<div id="imageback">
    		<label for="username"><i class="fa fa-user"></i> Username:</label>
        	<input type="username" id="username" name="username" class="cm-input" placeholder="Enter your username">

        	<label for="pass"><i class="fa fa-lock"></i> Password:</label>
        	<input id="pass" type="password" name="password" class="cm-input" placeholder="Enter your password">
	</div>
	<div id="follow">
		<?php
			session_start();
			include("simple-php-captcha.php");
			$_SESSION['captcha'] = simple_php_captcha();
		?>
		<img src=<?php echo $_SESSION['captcha']['image_src']?> >
		<input id="username" class="cm-input" type="username" name="captcha" placeholder="Enter the captcha value">
		<?php 
			if(isset($_GET['errorcode']) && $_GET['errorcode']=="wrongcaptcha") : 
		?>
		<br>
		<span class="errorMsg">Wrong captcha</span>
		<?php endif; ?>
		<button type="submit" class="btn-login  gr-bg">Login</button>
	</div>
    </form>
	


                	</div>
                </div>
    	</div>
	</section>
</form>
</body>
</html>
