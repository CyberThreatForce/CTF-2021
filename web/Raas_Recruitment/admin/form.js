$(function() {
  $('.submit').click(function(e) {
    
    e.preventDefault();

    let formdata = new FormData();
    formdata.append( 'username', $.trim($('.username').val()) );
    formdata.append( 'password', $.trim($('.password').val()) );
    formdata.append( 'password2', $.trim($('.password2').val()) );
    formdata.append( 'file', $('.file').prop('files') );

    $.ajax({
      type: 'POST',
      url: 'form-submit.php',
      data: formdata,
      cache: false,
      contentType: false,
      processData: false,
      context: this,

      before: function() {},

      error: function(xhr) {
        console.log('Error Message: ' + xhr.status);
      },

      success: function(response) {
        console.log(response);
        $('.user_details')[0].reset();
      }
    });
  });
});