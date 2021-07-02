<?php require_once("config/db.php"); ?>
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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
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
            <li class="treeview "><a href="">
                <i class="icon icon-sailing-boat-water purple-text s-18"></i> <span>Dashboard</span> 
                </a>
            </li>
            <li class="treeview"><a href="#"><i class="icon icon-user-circle-o light-green-text s-18"></i>Users
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
                           role="tab" aria-controls="v-pills-all"><i class="icon icon-home2"></i>All Users</a>
                    </li>
                    <li>
                        <a class="nav-link" id="v-pills-add-tab" data-toggle="pill" href="#v-pills-add" role="tab"
                           aria-controls="v-pills-add"><i class="icon icon-plus-circle"></i> Add New User</a>
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
                    <div class="col-md-12">
                        <div class="card">
                            <div class="collapse show" id="salesCard">
                                <div class="card-body p-0">
                                    <form action="">
                                        <div class="table-responsive">
                                            <table class="table table-hover ">
                                                <tbody>
                                                <thead class="shadow">
                                                 <tr>
                                                    <th class="no-b">
                                                        <div class="custom-control custom-checkbox">
                                                            <input type="checkbox" id="checkedAll" class="custom-control-input"><label
                                                                class="custom-control-label" for="checkedAll"></label>
                                                        </div>
                                                    </th>
                                                    <th class="no-b s-12">User</th>
                                                    <th class="no-b s-12">Email</th>
                                                 </tr>
                                            </thead>
                                            <?php
                                            $conn = new mysqli('localhost', 'root', '', 'chall2');
                                            $sql = "SELECT * FROM user_details ORDER BY id DESC";
                                            $result = $conn->query($sql);
                                            if ($result!== false && $result->num_rows > 0) {
                                            while($row = $result->fetch_assoc()) {
                                            echo'
                                                <tr>
                                                    <td>
                                                        <div class="custom-control custom-checkbox">
                                                            <input type="checkbox" class="custom-control-input checkSingle"
                                                                   id="user_id_' . $row["id"] .'" required><label
                                                                class="custom-control-label" for="user_id_' . $row["id"] .'"></label>
                                                        </div>
                                                    </td>

                                                    <td>
                                                        <img class="w-30px mr-3 circle" src="assets2/img/dummy/u1.png" alt="">
                                                        <strong>' . $row["username"] .'</strong>
                                                    </td>
                                                    <td><i class="icon-check_circle text-success mr-2 s-18"></i></td>
                                                    <td><span class="r-3 badge badge-danger ">En Attente</span></td>
                                                    <td>
                                                        <a href="user.php?id='. $row["id"] .'"><i class="icon-eye mr-3"></i></a>
                                                        <a href="panel-page-profile.html"><i class="icon-pencil"></i></a>
                                                    </td>
                                                </tr>';
                                            }
                                        }
                                            ?>
                                                </tbody>
                                            </table>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="tab-pane fade" id="v-pills-add" role="tabpanel" aria-labelledby="v-pills-add-tab">
                <div class="row">
                    <div class="col-md-8">
                        <form enctype="multipart/form-data" name="user_details" class="user_details" action="form-submit.php" method="post"><!--- --->
                           <div class="card no-b shadow no-r">
                               <div class="card-body">
                                   <h5 class="card-title">Dev Account</h5>
                                   <h7 class="card-title">Create Account only for accepted people, they will have access to /bingvxyyaknprxtgwexgldwdcrcqrfacDEV</h7>
                                   <div class="form-row">
                                       <div class="col-8">
                                            <div class="form-group m-0">
                                                <label for="username" class="col-form-label s-12">Username</label>
                                                <input name="username" id="input-username" placeholder="Enter UserName" class="username form-control r-0 light s-12 " type="text">
                                            </div>

                                           <div class="form-row">
                                               <div class="form-group col-6 m-0">
                                                   <label  name="password" for="password" class="col-form-label s-12"></i>Password</label>
                                                   <input id="password" placeholder="Please enter a password" class="password form-control r-0 light s-12 date-picker" type="password">
                                               </div>
                                               <div class="form-group col-6 m-0">
                                                   <label  name="password2" for="password2" class="col-form-label s-12"></i>Confirm Password</label>
                                                   <input id="password2" placeholder="Please confirm your password" class="password2 form-control r-0 light s-12 " type="password">
                                               </div>
                                           </div>
                                       </div>
                                    </div>
                               </div>
                               <hr>
                               <div class="card-body">
                                    <input type="submit" value="Submit" class="submit btn btn-primary btn-lg">
                               </div>
                           </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
        <!-- /.control-sidebar -->
        <!-- Add the sidebar's background. This div must be placed
                 immediately after the control sidebar -->
        <div class="control-sidebar-bg shadow white fixed"></div>
</div>
<!--End Page paper-loading -->

<script src="assets2/js/panel.js"></script>
<script src="form.js"></script>
</body>
</html>