<?php
require_once("config/db.php");
require_once("classes/Login.php");

session_start();

if (empty($_POST['from'])) {
    header("Location: /transaction.php?errorcode=emptyto");//echo "Bad email!!!";
} elseif (empty($_POST['to'])) {
    header("Location: /transaction.php?errorcode=emptyfrom");//echo "Bad email!!!";
    exit;
} elseif (empty($_POST['amount']) OR $_POST['amount'] < 0) {
    header("Location: /transaction.php?errorcode=emptyamount");//echo "Bad email!!!";
    exit;
} elseif (strlen($_POST['to']) > 64) {
    header("Location: /transaction.php?errorcode=tomax");//echo "Bad email!!!";
    exit;
} elseif (strlen($_POST['amount']) > 64) {
    header("Location: /transaction.php?errorcode=frommax");//echo "Bad email!!!";
    exit;
} elseif (strlen($_POST['from']) > 64) {
    header("Location: /transaction.php?errorcode=amountmax");//echo "Bad email!!!";
    exit;
} elseif (is_numeric($_POST['amount']) == false) {
    header("Location: /transaction.php?errorcode=tonotnumeric");//echo "Bad email!!!";
    exit;
} elseif (is_numeric($_POST['from']) == false) {
    header("Location: /transaction.php?errorcode=fromnotnumeric");//echo "Bad email!!!";
    exit;
} elseif (is_numeric($_POST['to']) == false) {
    header("Location: /transaction.php?errorcode=amountnotnumeric");//echo "Bad email!!!";
    exit;
} elseif ($_POST['to'] == $_POST['from']) {
    header("Location: /lol.html");//echo "Bad email!!!";
    exit;    
} elseif (!empty($_POST['from'])
    && strlen($_POST['from']) <= 64
    && is_numeric($_POST['from']) == true
    && !empty($_POST['amount'])
    && strlen($_POST['amount']) <= 64
    && is_numeric($_POST['amount']) == true
    && !empty($_POST['to'])
    && strlen($_POST['to']) <= 64
    && is_numeric($_POST['to']) == true
) {

$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

$sql = "SELECT `amount` FROM cards WHERE cardNumber ='" . $_POST['from'] . "'";
$result = $conn->query($sql);
$row = $result->fetch_assoc();
if ($row != true){
  header("Location: /transaction.php?errorcode=carderror");
} elseif ($_POST['amount'] > $row["amount"]){
    header("Location: /transaction.php?errorcode=notrich");//echo "Bad email!!!";
} else {

$sql = "SELECT `transaction` FROM cards WHERE cardNumber ='" . $_POST['to'] . "'";
$result = $conn->query($sql);
$row = $result->fetch_assoc();
if ($row != true) {
  header("Location: /transaction.php?errorcode=carderror");
}else{

$ciphering = "AES-128-CTR";
$iv_length = openssl_cipher_iv_length($ciphering);
$options = 0;
$encryption_iv = '1234567891011121';
$encryption_key = "`D+B4E#aQuM;'}9{";
$encryption = openssl_encrypt($_POST['from'] + $_POST['to'] + $_POST['amount'] . "EUR" . $row["transaction"], $ciphering,$encryption_key, $options, $encryption_iv);
}
}
} else {
    echo"error";
}

?>
                   <!DOCTYPE html>
                   <html lang="en">
                   <head>
                       <meta charset="UTF-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1.0">
                       <title>iofrm</title>
                       <link rel="stylesheet" type="text/css" href="css/bank.css">
                       <link rel="stylesheet" type="text/css" href="css/transfert.css">
                       <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
                       <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
                         <link rel="stylesheet" type="text/css" href="css/fontawesome-all.min.css">
                        <link rel="stylesheet" type="text/css" href="css/iofrm-style1.css">
                        <link rel="stylesheet" type="text/css" href="css/iofrm-theme141.css">
                        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600,700&display=swap" rel="stylesheet">
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
                        
                   </head>
                   <div class="my-app">
                       <header class="my-header">
                         <nav class="my-navbar navbar navbar-expand-lg navbar-light bg-white">
                           <a class="my-navbar__logo navbar-brand" href="#">
                             <img class="my-navbar__logo-icon" src="./images/icon-money.svg" alt>
                             <span class="my-navbar__logo-text">Dashboard</span>
                           </a>
                           <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                             <span class="navbar-toggler-icon"></span>
                           </button>
                   
                           <div class="collapse navbar-collapse" id="navbarSupportedContent">
                             <ul class="navbar-nav mr-auto">
                             <li class="nav-item active">
                                   <a class="nav-link" href="index.php">Home</a>
                               </li>
                               <li class="nav-item ">
                                   <a class="nav-link" href="#">Shop</a>
                               </li>
                               <li class="nav-item">
                                   <a class="nav-link" href="#">Flag</a>
                               </li>
                               <li class="nav-item">
                                   <a class="nav-link" href="index.php?logout">Logout</a>  
                               </li>
                             </ul>
                             <div class="my-navbar-buttons">
                               <button class="my-navbar-button">
                                 <img class="my-navbar-button__icon" src="./images/icon-settings.svg" alt>
                               </button>
                               <button class="my-navbar-button">
                                 <img class="my-navbar-button__icon" src="./images/icon-notifications.svg" alt>
                               </button>
                             </div>
                           </div>
                         </nav>
                       </header>
                       <main>
                         <!-- Begin content header -->
                         <section class="my-app__header">
                           <div class="container">
                             <div class="my-app__header-inner">
                               <div class="my-app__header-text media">
                                 <div class="media-body">
                                   <h1 class="my-app__header-title">Hi there, <?php echo $_SESSION['user_name']; ?>!</h1>
                                 </div>
                               </div>
                               <div class="my-action-buttons my-app__header__buttons">
                                <button class="my-action-button" onclick="location.href='index.php'">Cancel</button>
                              </div>
                             </div>
                           </div>
                         </section>
                         <body>
      <div class="form-wrapper">
         <h1>Confirmation</h1>
         <div class="card">
         <form class="form" action="/pay.php" method="post">
            <div class="card">
               <pre><b>From:</b></pre> 
               <?php echo"<span>" . $_POST['from'] ."</span></br>"; ?>
               <pre><b>To:</b></pre>
               <?php echo"<span>" . $_POST['to'] ."</span></br>"; ?>
               <pre><b>Amount:</b></pre>
               <?php echo"<span>" . $_POST['amount'] . " " . $_POST['Currency'] ."</span></br>"; ?>
            </div>
            <?php echo"<input type='hidden' name='from' value='". $_POST['from'] ."'><input type='hidden' name='to' value='" . $_POST['to'] . "'><input type='hidden' name='amount' value='" . $_POST['amount'] ."'><input type='hidden' name='validation' value='" . $encryption  . "'><button class='primary transfer' type='submit'>Confirm</button>"; ?>
         </form>
         </div>
      </div>
   </body>
</html>