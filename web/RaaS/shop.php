<?php
require_once("config/db.php");
require_once("classes/Login.php");

session_start();

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
                        <link rel="stylesheet" href="css/shop.css">

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
                                   <a class="nav-link" href="shop.php">Shop</a>
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
                                <button class="my-action-button" onclick="location.href='index.php'">Home</button>
                              </div>
                             </div>
                           </div>
                         </section>
                         <body>
<div class="shop-card">
  <div class="title">
    Mattcon 2 Trojan
  </div>
  <div class="desc">
    The best trojon from APT403
  </div>
  <div class="slider">
    <figure data-color="#E24938, #A30F22">
      <img src="./images/trojan.png" />
    </figure>
  </div>

  <div class="cta">
    <div class="price">100'000'000 EUR</div>
    <button class="btn">Buy Now<span class="bg"></span></button>
  </div>
</div>
<div class="bg"></div>



<a class="the-most" target="_blank" href="https://codepen.io/2016/popular/pens/">
</a>
