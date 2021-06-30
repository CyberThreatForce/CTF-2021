<html>
<head>
	<title>Inscription</title>
</head>
<body>
<?php
session_start();
if(preg_match("/sqlmap/", $_SERVER['HTTP_USER_AGENT']) == 1)
{
	header("APT_403: Don't be a skid bro, we will hunt you!");
	header("Location: https://www.youtube.com/watch?v=dQw4w9WgXcQ");
	exit;
}
else
{
	if(isset($_POST['username']) && isset($_POST['password']) && isset($_POST['captcha']))
	{
		if($_POST['captcha'] == $_SESSION['captcha']['code'])
		{
			$bdd = new PDO('mysql:host=localhost;dbname=ch4ll3ng3;charset=utf8', 'root', 'lnmyFqyPo3ZNw13PApZq');
			$sql = "select us3rn4me,p455w0rd from u53r where us3rn4me='" . $_POST['username'] . "' and p455w0rd= '".$_POST['password']. "';";
			try
			{
				$response = $bdd->query($sql);
				$result = $response->fetch();
				$username = $result[0];
				$password = $result[1];
				if( $_POST['username']==$username && $_POST['password']==$password )
				{
					echo "<html><body><pre>Well done!!</pre></body></html>";
					exit;
				}
				else
				{
					echo "<html><body><pre><img src=\"trollface.png\"></pre></body></html>";
					exit;
				}
			}
			catch(Exception $e)
			{
				echo "<html><body><pre><img src=\"trollface.png\"></pre></body></html>";
				exit;
			}
		}
		else
		{
			header("Location: /index.php?errorcode=wrongcaptcha");
			exit;
		}
	}
	else 
	{
		echo "<html><body><pre><img src=\"trollface.png\"></pre></body></html>";
		exit;
	}
}
?>
</body>
</html>
