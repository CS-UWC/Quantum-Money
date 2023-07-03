$(document).ready(function () {
    var divs = $('#qnote-amounts>div');
    divs.each(function () {
        var div = $(this);

        // Set the click event listener
        div.click(function () {
            // Get the value of the div
            var value = div.text();

            // we want to highlight the div that was clicked
            // and remove the highlight from the other divs
            div.addClass('border-success');
            divs.not(this).removeClass('border-success');
        });
    });

    $('#purchase-qnote-btn').click(function () {
        let quantity = $('#qnote-quantity').val();
        console.log(quantity)
        if (!quantity) {
            alert('Please enter a quantity');
            return;
        }
        // check if number
        if (isNaN(quantity)) {
            alert('Please enter a number');
            return;
        }
        // check if positive
        if (quantity <= 0) {
            alert('Please enter a positive number');
            return;
        }


        let amount = $('#qnote-amounts>div.border-success').text();
        console.log(amount)
        if (!amount) {
            alert('Please select an amount');
            return;
        }
        var loggedInUser = JSON.parse(sessionStorage.getItem('loggedInUser'));
        payload = {
            'email': loggedInUser.email, 
            'qnotes': {
                [amount]: quantity,
            }
        }
        console.log(payload.qnotes)
        $.ajax({
            url: '/cgi-bin/issuev2.py',
            type: 'POST',
            data: JSON.stringify(payload),
            error: function (xhr, status, error) {
                // Handle the error if the AJAX request fails
                alert('Error: ' + error);
            },
            success: function (data) {
                console.log({ data });

            }
        });

        alert('You have purchased ' + (quantity) + ' QNotes worth ' + amount + ' each. Total: R' + (quantity * amount));
        $('#purchaseQNoteModal').modal('toggle');
        window.location.href = 'wallet.html';
    });
    $('#unused').click(function () {
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