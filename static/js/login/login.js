$(document).ready(function () {
    $('#loginForm').submit(function (event) {
        event.preventDefault();
        var username = $('#username').val();
        console.log(username)

        $.ajax({
            url: '/cgi-bin/user.py',
            type: 'post',
            data: JSON.stringify({'email': username}),
            error: function(xhr, status, error) {
                // Handle the error if the AJAX request fails
                alert('Error: ' + error);
                },
            success: function(data) {
                console.log(data)
                if (data['error']) {
                    alert(data['error']);
                    return;
                }
                var loggedInUser = data['user'];
        
                sessionStorage.setItem('loggedInUser', JSON.stringify(loggedInUser));
                window.location.href = 'wallet.html';
            }
        });


        
    });
});