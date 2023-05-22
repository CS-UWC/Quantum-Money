function sendBanknote(serial, email) {
    console.log({serial,email})
    let receiver = prompt("Please enter receiver's email", "");
    if (receiver == null || receiver == "") {
        alert("You must enter a receiver's email");
        return;
    }

    $.ajax({
        url: '/cgi-bin/send.py',
        type: 'POST',
        data: JSON.stringify({'serial': serial, 'email': email, 'receiver': receiver}),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            console.log(data)
            if (data['error']) {
                alert(data['error'])
            }
            alert(data['msg']);
        }
    });
    
}