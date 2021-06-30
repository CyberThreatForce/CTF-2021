<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <title>Template</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">

    <!-- External Css -->
    <link rel="stylesheet" href="assets/css/line-awesome.min.css">
    <link rel="stylesheet" href="assets/css/owl.carousel.min.css" />

    <!-- Custom Css --> 
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <link rel="stylesheet" type="text/css" href="css/job-1.css">

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

    <!-- Favicon -->
    <link rel="icon" href="../images/favicon.png">
    <link rel="apple-touch-icon" href="../images/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="72x72" href="../images/icon-72x72.png">
    <link rel="apple-touch-icon" sizes="114x114" href="../images/icon-114x114.png">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>


  </head>
  <body>

    <div class="ugf-wrapper">
      <div class="logo">
        <img src="images/logo.png" class="img-fluid logo-white" alt="">
        <img src="images/logo-dark.png" class="img-fluid logo-black" alt="">
      </div>
      <div class="ugf-content-block">
        <div class="content-block">
          <h1>We are creative agency <br> Let’s Join with us !</h1>
          <p>Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain but because.</p>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-lg-5 offset-lg-7">
            <div class="ufg-job-application-wrapper pt150">
              <div class="progress">
                <div class="progress-bar" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"><span class="step-text"><span class="current-step"></span> of <span class="total-step"></span> completed</span></div>
              </div>
              <div class="form-steps active">
                <h3>Personal information</h3>
                <form enctype="multipart/form-data" name="user_details" class="user_details job-application-form" action="form-submit.php" method="post">
                  <div class="form-group">
                    <input type="text" name="username" class="username form-control" id="input-username" required>
                    <label for="input-username">UserName</label>
                  </div>
                  <div class="form-group">
                  <input type="text" name="email" class="email form-control" id="input-mail" required>
                    <label for="input-mail">Email Addresss</label>
                  </div>
                  <div class="form-group check-gender" required>
                    <span class="lebel-text">Are you Russian?</span>
                    <div class="custom-radio">
                    <input type="radio" name="radio" class="radio custom-control-input" id="yes" value="yes" <?php if (isset($_POST['radio']) && $_POST['radio'] == 'yes'): ?>checked='checked'<?php endif; ?> />
                    <label class="custom-control-label" for="yes">Yes</label>
                    </div>
                    <div class="custom-radio">
                      <input type="radio" name="radio" class="radio custom-control-input" id="no" value="no" <?php if (isset($_POST['radio']) && $_POST['radio'] == 'no'): ?>checked='checked'<?php endif; ?> />
                      <label class="custom-control-label" for="no">No</label>
                    </div>
                  </div>
                      <input type="submit" value="Submit" class="btn submit">
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer">
        <div class="social-links">
          <a href="#"><i class="lab la-facebook-f"></i></a>
          <a href="#"><i class="lab la-twitter"></i></a>
          <a href="#"><i class="lab la-linkedin-in"></i></a>
          <a href="#"><i class="lab la-instagram"></i></a>
        </div>
        <div class="copyright">
          <p>Copyright © 2021 Anfra. All Rights Reserved</p>
        </div>
      </div>
    </div>




    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="form.js"></script>
    <script src="assets/js/popper.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="js/custom.js"></script>
  </body>
</html>
