$(document).ready(function () {

    $('#purchase-button').click(function () {
        var loggedInUser = JSON.parse(sessionStorage.getItem('loggedInUser'));
        
        var amount = prompt('How much would you like to purchase?');
        if (!amount) {
            return;
        }
        if (amount <= 0) {
            alert('Please enter a positive amount');
            return;
        }

        for (let i = 0; i < amount; i++) {
            $.ajax({
                url: '/cgi-bin/issue.py',
                type: 'POST',
                data: JSON.stringify({ 'email': loggedInUser.email }),
                error: function (xhr, status, error) {
                    // Handle the error if the AJAX request fails
                    alert('Error: ' + error);
                },
                success: function (data) {
                    console.log({ data });

                }
            });
        }
        window.location.href = 'wallet.html';
    });
});