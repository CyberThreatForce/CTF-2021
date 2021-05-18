function validateForm(){
    var correctPassphrase = "54081510540548410485145";
    var passphrase = document.myForm.passphrase;
    if (passphrase.value == ""){
        alert("Enter password");
    }

    else if (passphrase.value == correctPassphrase){
        alert("Correct password -");
        window.location.href='Login.php';
        return false;
            
    }

    else {
        alert("Hack detected");
    }
}
