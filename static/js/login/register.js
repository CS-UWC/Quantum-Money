$(document).ready(function () {
    $('#cancel').click(function (event) {
        event.preventDefault();
        window.location.href = '/';
    });
    $('#registerForm').submit(function (event) {
        event.preventDefault();
        

        var pass = $('#password').val();
        var passCheck = checkPassword(pass);
        if (passCheck['error']) {
            alert(passCheck['error']);
            return;
        }

        var passConfirm = $('#passconfirm').val();
        if (pass != passConfirm) {
            alert('Passwords do not match.');
            return;
        }

        var username = $('#email').val();
        var firstName = $('#firstname').val();
        var lastName = $('#lastname').val();
        console.log(username)

        $.ajax({
            url: '/cgi-bin/user/register.py',
            type: 'post',
            data: JSON.stringify({
                'email': username,
                'first_name': firstName,
                'surname': lastName,
                "password": pass
        }),
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
                
                if (data['success']) {
                    alert('Account created successfully. Please log in.');
                    window.location.href = '/';
                    return;
                }

                alert('Unknown error. Please try again.')
            }
        });
    });
});

function checkPassword(pass) {
    if (pass.length < 8) {
        return {'error': 'Password must be at least 8 characters long.'};
    }

    var regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$/;
    if (!regex.test(pass)) {
        return {'error': 'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.'};
    }

    return {'success': 'Password is valid.'};

}