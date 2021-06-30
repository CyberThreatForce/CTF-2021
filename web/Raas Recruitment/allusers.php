<?php require 'user_deatils.php'; ?>

<?php if(isset($user_details)){ ?>
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Filename</th>
      <th>Username</th>
      <th>email</th>
      <th>radio</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach($user_details as $key => $user){ ?>
    <tr>
      <td><?= $user['id']; ?></td>
      <td><?= $user['name']; ?></td>
      <td><?= $user['filename']; ?></td>
      <td><?= $user['username']; ?></td>
      <td><?= $user['email']; ?></td>
      <td><?= $user['radio']; ?></td>
    </tr>
    <?php } ?>
  </tbody>
</table>
<?php } ?>