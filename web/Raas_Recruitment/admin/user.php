<?php require_once("config/db.php"); 
session_start();
if($_SESSION['user_login_status'] != 1){
    header("Location: index.php");
}
$iduser = $_GET["id"];

$conn = new mysqli('localhost', 'root', '', 'chall2');
$sql = "SELECT * FROM user_details WHERE id = $iduser";
$result = $conn->query($sql);
$row = $result->fetch_assoc();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="assets2/img/basic/favicon.ico" type="image/x-icon">
    <title>Admin</title>
    <!-- CSS -->
    <link rel="stylesheet" href="assets2/css/panel.css">
    <style>
        .loader {
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: #F5F8FA;
            z-index: 9998;
            text-align: center;
        }

        .plane-container {
            position: absolute;
            top: 50%;
            left: 50%;
        }
    </style>
</head>
<body>
<!-- Pre loader -->
<div id="loader" class="loader">
    <div class="plane-container">
        <div class="preloader-wrapper small active">
            <div class="spinner-layer spinner-blue">
                <div class="circle-clipper left">
                    <div class="circle"></div>
                </div><div class="gap-patch">
                <div class="circle"></div>
            </div><div class="circle-clipper right">
                <div class="circle"></div>
            </div>
            </div>

            <div class="spinner-layer spinner-red">
                <div class="circle-clipper left">
                    <div class="circle"></div>
                </div><div class="gap-patch">
                <div class="circle"></div>
            </div><div class="circle-clipper right">
                <div class="circle"></div>
            </div>
            </div>

            <div class="spinner-layer spinner-yellow">
                <div class="circle-clipper left">
                    <div class="circle"></div>
                </div><div class="gap-patch">
                <div class="circle"></div>
            </div><div class="circle-clipper right">
                <div class="circle"></div>
            </div>
            </div>

            <div class="spinner-layer spinner-green">
                <div class="circle-clipper left">
                    <div class="circle"></div>
                </div><div class="gap-patch">
                <div class="circle"></div>
            </div><div class="circle-clipper right">
                <div class="circle"></div>
            </div>
            </div>
        </div>
    </div>
</div>
<div id="app" class="paper-loading">
<aside class="main-sidebar fixed offcanvas shadow">

        <div class="relative">

  
            <div class="user-panel p-3 light mb-2">
                <div class="clearfix">
                    <div class="float-left info">
                        <h6 class="font-weight-light mt-2 mb-1"><?php echo $_SESSION['user_name']; ?></h5>
                            <a ><i class="icon-circle text-primary blink"></i> Online</a>
                    </div>
                </div>
                <div class="collapse multi-collapse" id="multiCollapseExample1">
                    <div class=" p-3">

                    </div>
                </div>
            </div>
        </div>

        <ul class="sidebar-menu">
            <li class="header"><strong>MAIN NAVIGATION</strong></li>
            <li class="treeview"><a href="index.php">
                <i class="icon icon-sailing-boat-water purple-text s-18"></i> <span>Dashboard</span>
            </a>
            <li class="treeview active"><a href="#"><i class="icon icon-user-circle-o light-green-text s-18 active"></i>Users</a>
            </li> 
        </ul>
    </section>
</aside>
<!--Sidebar End-->
<div class="offcanvas-page">
    <div class="pos-f-t">
    <div class="collapse" id="navbarToggleExternalContent">
        <div class="bg-dark pt-2 pb-2 pl-4 pr-2">
            <div class="search-bar">
                <input class="transparent s-24 text-white b-0 font-weight-lighter w-128 height-50" type="text"
                       placeholder="start typing...">
            </div>
            <a href="#" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-expanded="false"
               aria-label="Toggle navigation" class="paper-nav-toggle paper-nav-white active "><i></i></a>
        </div>
    </div>
</div>
    <div class="sticky">
        <div class="navbar navbar-expand navbar-dark d-flex justify-content-between bd-navbar blue accent-3">
            <div class="relative">
                <a href="#" data-toggle="offcanvas" class="paper-nav-toggle pp-nav-toggle">
                    <i></i>
                </a>
            </div>
            <!--Top Menu Start -->
<ul class="navbar-nav p-t-10">
    <!-- Messages Dropdown-->
    <!-- Notification Dropdown-->
    <li class="nav-item ml-2 dropdown">
        <a class="nav-item ml-2 nav-link  ml-2" href="#" id="bd-versions" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="icon-more_vert s-18"></i>
        </a>
        <div class="dropdown-menu dropdown-menu-right b-0 shadow1">

            <a class="dropdown-item"  href="index.php?logout">
                <i class="icon-money"></i> Logout </a>
        </div>
</ul>
<!--Top Menu End -->
        </div>
    </div>
</div>

<div class="page light offcanvas-page  height-full">
    <header class="blue accent-3 relative">
        <div class="container-fluid text-white">
            <div class="row p-t-b-10 ">
                <div class="col">
                    <h4>
                        <i class="icon-database"></i>
                        Users
                    </h4>
                </div>
            </div>
            <div class="row justify-content-between">
                <ul class="nav nav-material nav-material-white responsive-tab" id="v-pills-tab" role="tablist">
                    <li>
                        <a class="nav-link active" id="v-pills-all-tab" data-toggle="pill" href="#v-pills-all"
                           role="tab" aria-controls="v-pills-all"><i class="icon icon-home2"></i>User info</a>
                    </li>

                    <li>

                    </li>
                </ul>
            </div>
        </div>
    </header>
    <div class="container-fluid">
        <div class="tab-content pt-3 pb-3" id="v-pills-tabContent">
            <div class="tab-pane fade show active" id="v-pills-all" role="tabpanel" aria-labelledby="v-pills-all-tab">
                <div class="row">
                    <div class="col-md-8">
                        <form action="#">
                           <div class="card no-b shadow no-r">
                               <div class="card-body">
                                   <h5 class="card-title">About User</h5>
                                   <div class="form-row">
                                       <div class="col-8">
                                            <div class="form-group m-0">
                                                <label for="name" class="col-form-label s-12">User Name</label>
                                                <input id="name" placeholder="<?php 
                                                echo $row["username"];
                                                ?>" class="form-control r-0 light s-12 " type="text" readonly>
                                            </div>
                                           <div class="form-group m-0">
                                               <label for="russian" class="col-form-label s-12">Russian ?</label>
                                                <input id="russian" placeholder="<?php 
                                                echo $row["radio"];
                                                ?>" class="form-control r-0 light s-12 " type="text" readonly>
                                           </div>
                                       </div>

                                    </div>

                                   <div class="form-row mt-1">
                                       <div class="form-group col-4 m-0">
                                           <label for="email" class="col-form-label s-12"><i class="icon-envelope-o mr-2"></i>Email for contact</label>
                                           <input id="email" placeholder="<?php 
                                                echo $row["email"];
                                                ?>" class="form-control r-0 light s-12 " type="text" readonly>
                                       </div>

                                   </div>
                               </div>
                               <hr>
                           </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

          <!-- Control Sidebar -->
          <aside class="control-sidebar fixed white">
                <ul class="nav nav-tabs  nav-material" id="myTab2" role="tablist">
                    <li class="nav-item">
                        <a class="nav-link active" id="home-tab2" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-expanded="true"><i class="icon-cogs"></i></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="profile-tab2" data-toggle="tab" href="#profile" role="tab" aria-controls="profile"><i class="icon-cogs"></i></a>
                    </li>
                </ul>
                <div class="tab-content" id="myTabContent2">
                    <div role="tabpanel" class="tab-pane fade show active" id="home" aria-labelledby="home-tab">
                      <!-- Big Heading -->
                      <div class="text-center">
                            <h3 class="my-3">$25,000</h3>
                            <i class="icon-angle-double-up yellow icon-box-md cirlce"></i>
                        </div>

                        <div class="d-flex justify-content-between">
                            <div>
                                <p>
                                    <i class="icon-circle-o text-red mr-2"></i>Sales</p>

                                <p>
                                    <i class="icon-circle-o text-green mr-2"></i>Last Month</p>

                            </div>
                            <div>
                                <p>
                                    <i class="icon-angle-double-down text-red mr-2"></i>1,4,348</p>


                                <p>
                                    <i class="icon-angle-double-up text-green mr-2"></i>1,11,5</p>
                            </div>
                        </div>
                                    <div >
                                        <div class="my-3">
                                            <small>25% Complete</small>
                                                <div class="progress" style="height: 3px;">
                                                    <div class="progress-bar bg-success" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                                                </div>
                                        </div>
                                        <div class="my-3">
                                            <small>45% Complete</small>
                                            <div class="progress" style="height: 3px;">
                                                <div class="progress-bar bg-info" role="progressbar" style="width: 45%;" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </div>
                                        <div class="my-3">
                                            <small>60% Complete</small>
                                            <div class="progress" style="height: 3px;">
                                                <div class="progress-bar bg-warning" role="progressbar" style="width: 60%;" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </div>
                                        <div class="my-3">
                                            <small>75% Complete</small>
                                            <div class="progress" style="height: 3px;">
                                                <div class="progress-bar bg-danger" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </div>
                                        <div class="my-3">
                                                <small>100% Complete</small>
                                                <div class="progress" style="height: 3px;">
                                                    <div class="progress-bar" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                                </div>
                                            </div>
                
                                    </div>
                                
                    </div>
                    <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                            <ul class="list-group no-b">
                                    <li class="my-3 d-flex justify-content-between align-items-center">
                                           <div> <i class="icon-wifi text-blue"></i>Wifi</div>
                                           <div class="material-switch">
                                                <input id="someSwitchOptionDefault1" name="someSwitchOption001" checked="true" type="checkbox"/>
                                                <label for="someSwitchOptionDefault1" class="bg-primary"></label>
                                            </div>
                                    </li>
                                    <li class="my-3 d-flex justify-content-between align-items-center">
                                            <div><i class="icon-cogs text-blue"></i>Email</div>
                                            <div class="material-switch">
                                                    <input id="someSwitchOptionDefault2" name="someSwitchOption001" checked="true" type="checkbox"/>
                                                    <label for="someSwitchOptionDefault2" class="bg-secondary"></label>
                                                </div>
                                    </li>
                                    <li class="my-3 d-flex justify-content-between align-items-center">
                                          <div>  <i class="icon-wifi text-blue"></i> Password</div>
                                          <div class="material-switch">
                                                <input id="someSwitchOptionDefault3" name="someSwitchOption001"  checked="true" type="checkbox"/>
                                                <label for="someSwitchOptionDefault3" class="bg-danger"></label>
                                            </div>
                                    </li>
                                    <li class="my-3 d-flex justify-content-between align-items-center">
                                            <div>  <i class="icon-wifi text-blue"></i> Password</div>
                                            <div class="material-switch">
                                                    <input id="someSwitchOptionDefault4" name="someSwitchOption001" checked="true" type="checkbox"/>
                                                    <label for="someSwitchOptionDefault4" class="bg-warning"></label>
                                                </div>
                                      </li>
                                      <li class="my-3 d-flex justify-content-between align-items-center">
                                            <div>  <i class="icon-wifi text-blue"></i> Password</div>
                                            <div class="material-switch">
                                                    <input id="someSwitchOptionDefault5" name="someSwitchOption001"  checked="true" type="checkbox"/>
                                                    <label for="someSwitchOptionDefault5" class="bg-default"></label>
                                                </div>
                                      </li>
                                  </ul>
                    </div>
                    <div class="tab-pane fade" id="dropdown12" role="tabpanel" aria-labelledby="dropdown1-tab">
                    
                    </div>
                
                </div>
         </aside>
        <!-- /.control-sidebar -->
        <!-- Add the sidebar's background. This div must be placed
                 immediately after the control sidebar -->
        <div class="control-sidebar-bg shadow white fixed"></div>
</div>
<!--End Page paper-loading -->
<script src="assets2/js/panel.js"></script>
</body>
</html>