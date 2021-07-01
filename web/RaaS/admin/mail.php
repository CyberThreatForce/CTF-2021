<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';
$mail = new PHPMailer;
#$mail->SMTPDebug = SMTP::DEBUG_SERVER;
#$mail->SMTPDebug = SMTP::DEBUG_SERVER;
$mail->SMTPDebug = 4;
$mail->CharSet    = 'UTF-8';
$mail->SMTPAuth   = true;
$mail->Encoding   = 'base64';
$mail->isSMTP();
$mail->SMTPSecure = "tls"; 
$mail->Host       = "pro2.mail.ovh.net";
$mail->Port       = 587;
$mail->AuthType   = 'LOGIN';
$mail->Username   = "no-reply@cyberthreatforce-ctf.com";
$mail->Password   = "YPqa3@DQ";

$mail->From = 'no-reply@cyberthreatforce-ctf.com';
$mail->FromName = 'Mailer';
$mail->setFrom('no-reply@cyberthreatforce-ctf.com', 'test');
$mail->addAddress('admin@cyberthreatforce-ctf.com', 'Toto');     // Add a recipient
#$mail->addAddress('ellen@example.com');               // Name is optional
#$mail->addReplyTo('info@example.com', 'Information');
#$mail->addCC('cc@example.com');
#$mail->addBCC('bcc@example.com');

#$mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
#$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
$mail->isHTML(true);                                  // Set email format to HTML

$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

echo "C'est beau!!";

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
?>