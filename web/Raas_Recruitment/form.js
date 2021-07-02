$(function() {
  $('.submit').click(function(e) {
    
    e.preventDefault();

    let formdata = new FormData();
    formdata.append( 'username', $.trim($('.username').val()) );
    formdata.append( 'email', $.trim($('.email').val()) );
    formdata.append( 'radio', $.trim($('.radio').val()) );

    $.ajax({
      type: 'POST',
      url: 'form-submit.php',
      data: formdata,
      cache: false,
      contentType: false,
      processData: false,
      context: this,

      before: function() {},


    });
  });
});