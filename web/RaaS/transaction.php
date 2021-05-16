<?php
require_once("config/db.php");
require_once("classes/Login.php");

session_start();

#$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
#                   $sql = "SELECT * FROM users A INNER JOIN cards B ON A.user_id = B.user_id WHERE A.user_name ='" . $_SESSION['user_name'] . "'";
  #                  $result = $conn->query($sql);
   #                 if ($result!== false && $result->num_rows < 2) {
   #                     $row = $result->fetch_assoc();
    #                    $number = mt_rand(1111111111111111, 9999999999999999);
    #                    $sql = "INSERT INTO cards (cardNumber, amount, user_id)
      #                  VALUES($number, '0', (SELECT user_id FROM users WHERE user_name = '" . $row["user_name"] . "'));";
         #               $query_new_user_insert = $conn->query($sql);
            #            header('Location: /index.php');
               #     } else {
             #           header('Location: /index.php?errorcode=toomuchcards');
                #    }
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
                           <a class="my-navbar__logo navbar-brand" href="index.php">
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
                                   <a class="nav-link" href="https://discord.gg/XnSUhSBpVF">Flag</a>
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
<div class="form-wrapper"><?php
if (isset($_GET['errorcode']) && $_GET['errorcode'] == "emptyfrom"){
  echo"<span class='errorMsg' id='validation'>Empty card from</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "emptyto"){
  echo"<span class='errorMsg' id='validation'>Empty card from</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "emptyamount"){
  echo"<span class='errorMsg' id='validation'>You can not pay nothing or less..</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "amount"){
  echo"<span class='errorMsg' id='validation'>Empty Amount</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "tomax"){
  echo"<span class='errorMsg' id='validation'>Card Number to cannot be longer than 64 characters</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "frommax"){
  echo"<span class='errorMsg' id='validation'>Card Number from cannot be longer than 64 characters</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "amountmax"){
  echo"<span class='errorMsg' id='validation'>Amount cannot be longer than 64 characters</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "tonotnumeric"){
  echo"<span class='errorMsg' id='validation'>To card can be only number</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "fromnotnumeric"){
  echo"<span class='errorMsg' id='validation'>From card can be only number</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "amountnotnumeric"){
  echo"<span class='errorMsg' id='validation'>Amount can be only number</span>";
} elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "notrich"){
  echo"<span class='errorMsg' id='validation'>You don't have enough money</span>";
}elseif (isset($_GET['errorcode']) && $_GET['errorcode'] == "carderror"){
  echo"<span class='errorMsg' id='validation'>the card you specified does not exist...</span>";
}else {

}
 ?>
    <h1>Transfer money fast! </h1>
    <div class="card">
        <form class="form" method="post" action="/confirmation.php">
            <div class="form__item"><label>From</label>
            <select class="account-select" id="login_input_account" name="from" aria-invalid="false" required>
              <?php
              $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
              $sql = "SELECT * FROM users A INNER JOIN cards B ON A.user_id = B.user_id WHERE A.user_name ='" . $_SESSION['user_name'] . "'";
              $result = $conn->query($sql);
              while ($row = $result->fetch_assoc()) {
                echo "<option value='" . $row['cardNumber'] . "'>" . $row['cardNumber'] . " | " . $row['amount'] . " EUR</option>";
              }
              ?>     
                </select></div>
            <div class="form__item"><label>To</label>
            <input id="login_input_card_number" type="text" name="to" placeholder="Card Number" required /></div>
            <div class="form__item">
              <label>Amount</label>
            <input id="login_input_amount" type="text" name="amount"value="" maxlength="15" id="c1" required />
            </div>
            <div class="form__item">
            <label>Currency</label>
            <input class="Currency" name="Currency" value="EUR" id="c2" readonly />
            </div>
            <div class="form__item type">
            </div>
            <div class="form__item cta">
              <button class="primary transfer" id="submit" type="submit" name="transfert" >Send Funds </button>
            </div>
        </form>
    </div>
</div>
</body>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script><script  src="./js/script.js"></script>
