<!DOCTYPE html>
<html>
<head>
  <title>Form Submit</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
  <form enctype="multipart/form-data" name="user_details" class="user_details" action="form-submit.php" method="post">
    <input type="text" name="username" class="username" id="input-username">
    <input type="text" name="email" class="email">
    <input type="radio" name="radio" value="yes" class="radio" <?php if (isset($_POST['radio']) && $_POST['radio'] == 'yes'): ?>checked='checked'<?php endif; ?> /> Yes
    <input type="radio" name="radio" value="no"  class="radio" <?php if (isset($_POST['radio']) && $_POST['radio'] ==  'no'): ?>checked='checked'<?php endif; ?> /> No
    <input type="submit" value="Submit" class="submit">
  </form>
  <script src="form.js"></script>
</body>
</html>