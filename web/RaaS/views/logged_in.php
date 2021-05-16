<!-- if you need user information, just put them into the $_SESSION variable and output them here -->
<?php require_once("config/db.php"); ?>. 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iofrm</title>
    <link rel="stylesheet" type="text/css" href="css/bank.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
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
              <button class="my-action-button" onclick="location.href='transaction.php'">
                <img class="my-action-button__icon" src="./images/money.png">
                Send money
              </button>
            </div>
          </div>
        </div>
      </section>
      <!-- End content header -->

      <!-- Begin content body -->
      <section class="my-app__body">
        <div class="container">
          <div class="row">
            <div class="col-4">
              <!-- Begin Payment Balance card -->
              <div class="my-card card">
                <div class="my-card__body card-body">
                  <div class="my-text-overline">Bank accounts and cards</div>
                  <?php
                  if (isset($_GET['errorcode']) && $_GET['errorcode'] == "toomuchcards") : 
                  ?>
                  <span class="errorMsg" id="validation">You can't have more than 2 cards</span>
                  <?php endif; ?>
                  <ul class="my-list my-list--simple list-inline mb-0">
                   <?php
                   $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
                   $sql = "SELECT * FROM users A INNER JOIN cards B ON A.user_id = B.user_id WHERE A.user_name ='" . $_SESSION['user_name'] . "'";
                   $result = $conn->query($sql);
                   if ($result!== false && $result->num_rows > 0) {
                    while($row = $result->fetch_assoc()) {
                        echo "<li class='my-list-item'>";   
                        echo "<span class='list__icon'>"; 
                        echo "<img src='./images/visa.png' alt> "; 
                        echo "</span>"; 
                        echo "<span style='padding-left:10px;'> Card: " . $row["cardNumber"]. "<br /> Amount: ". $row["amount"].  " EUR </span>";
                        echo "</li>";
                    }
                      }
                    $conn->close();
                    ?>
                  </ul>
                  <hr class="my-divider">
                  <ul class="my-list-inline list-inline mb-0">
                    <li>
                        <form method="post" action="cards.php" name="cards">
                    <button class="my-action-button" id="submit" type="submit" name="name" value="Personal Card" disabled>Add a Bank Account or Card</button>
                  </form>
                </li>
                  </ul>
                </div>
              </div>
            </div>

            <div class="col-8">
              <div class="my-alert alert alert-info">
                <img class="my-alert__icon" src="./images/icon-alert.svg" alt>
                <span class="my-alert__text">
                  Your latest transaction may take a few minutes to show up in your activity.
                </span>
              </div>

              <!-- Begin Completed card -->
              <div class="my-card card">
                <div class="my-card__header card-header">
                  <h3 class="my-card__header-title card-title">Completed</h3>
                </div>
                <ul class="my-list list-group list-group-flush">
                  <?php
                   $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
                   $sql = "SELECT * FROM users A INNER JOIN transactions B ON A.user_id = B.user_id WHERE A.user_name ='" . $_SESSION['user_name'] . "' ORDER BY B.TransactionID DESC";
                   $result = $conn->query($sql);

                   
                   if ($result!== false && $result->num_rows > 0) {
                    while($row = $result->fetch_assoc()) {
                        $date =(date_parse_from_format("Y.n.j",$row["date"]));
                        $dateObj = DateTime::createFromFormat('!m', $date["month"]);
                        $monthName = $dateObj->format('F');
                        echo "<li class='my-list-item list-group-item'>";   
                        echo "<div class='my-list-item__date'><span class='my-list-item__date-day'>" . $date["day"] . "</span>";
                        echo "<span class='my-list-item__date-month'>". $monthName ."</span></div>";
                        echo "<div class='my-list-item__text'><h4 class='my-list-item__text-title'>Transfert to " . $row["cardTo"] . "</h4>";
                        echo "<p class='my-list-item__text-description'>From " . $row["cardFrom"] ."</p><div>";
                        echo "<div class='my-list-item__fee'><span class='my-list-item__fee-delta'>+" . $row["amount"] ."</span>";
                        echo "<span class='my-list-item__fee-currency'>EUR</span></div>"; 
                        echo "</li>";
                    }
                      }
                    $conn->close();
                    ?>
                </ul>
              </div>
              <!-- End Completed card -->
            </div>
          </div>
        </div>
      </section>
      <!-- End content body -->
    </main>
</div>
