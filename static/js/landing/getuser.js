$(document).ready(function() {
    let params = new URLSearchParams(window.location.search);
    let email = "isatippens2@gmail.com";
    if (params.has('email')) {
        email = params.get('email');
    }
    $.ajax({
        url: '/cgi-bin/user.py',
        type: 'POST',
        data: JSON.stringify({'email': email}),
        error: function(xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
          },
        success: function(data) {
            console.log(data)
            if (data['error']) {
                console.log({data});
                $('#welcome').html("Welcome, Guest!");
            }
            let name = data['user']['firstname'];
            let message = "Welcome, " + name + "!";
            $('#welcome').html(message);
        }
    });
});