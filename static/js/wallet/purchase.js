$(document).ready(function () {
    var divs = $('#qnote-amounts>div');
    divs.each(function () {
        var div = $(this);

        // Set the click event listener
        div.click(function () {
            // Get the value of the div
            
            // we want to highlight the div that was clicked
            // and remove the highlight from the other divs
            div.addClass('border-success');
            divs.not(this).removeClass('border-success');
            console.log("passage")
            var value = div.text();
            qnote_value = value;
            UpdateView();
        });
    });

    $("#qnote-quantity").on("input", function() {
        let amount = $(this).val();
        if (!amount || isNaN(amount) || (amount <= 0)) {
            return;
        }
        // convert to number
        amount = parseInt(amount);
        qnote_amount = amount;
        UpdateView();
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

        if (calcFinalLimit() > 50000) {
            alert('You have exceeded your limit');
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
        // The wallet view only fetches from db if it doesn't exist in cache
        // so we need to clear it from cache to force a fetch from db
        clearWalletFromCache();
        window.location.href = 'wallet.html';
    });
   
});

let limit = 0
let limitView = 0
let qnote_amount = 0
let qnote_value = 0

function GetLimit(email) {
    $.ajax({
        url: '/cgi-bin/user/get_limit.py',
        type: 'POST',
        async: false,
        data: JSON.stringify({ 'email': email }),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            if (data['error']) {
                console.log({ data });
                return
            }
            console.log(data);
            limit = data['limit'];
            UpdateView();
        }
    });
}


function calcFinalLimit() {
    let balance = qnote_amount * qnote_value;
    limitView = 50000 - limit + balance;
    return limitView;
}

function UpdateView() {
    let balance = qnote_amount * qnote_value;
    limitView = 50000 - limit + balance;
    $('#qnote-limit').text('R' + limitView);
}