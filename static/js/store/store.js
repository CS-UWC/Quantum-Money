$(document).ready(function () {
    let user = fetchUserFromCache();
    let balance = GetBalance(user.email);
    $('#total').append(balance);

    wallet = GetWallet(user.email);
    GenerateWalletView(wallet);

    var edivs = $('#electricity-amounts>div');
    edivs.each(function () {
        var div = $(this);

        // Set the click event listener
        div.click(function () {
            // Get the value of the div
            var value = div.text();

            // we want to highlight the div that was clicked
            // and remove the highlight from the other divs
            div.addClass('border-success');
            edivs.not(this).removeClass('border-success');
        });
    });

    var divs = $('#airtime-amounts>div');
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

    $('#airtime-purchase-button').click(purchaseAirtime);
    $('#electricity-purchase-button').click(purchaseElectricity);


});


function purchaseElectricity() {
    let meter = $('#meter-number').val();
    let amount = $('#electricity-amounts>div.border-success').text();
    if (!meter) {
        alert('Please enter a meter number');
        return;
    }

    if (!amount) {
        alert('Please select an amount');
        return
    }

    // R100 | 1000 kWh => 100
    amount = amount.split('|')[0].trim().split('R')[1];


    var loggedInUser = JSON.parse(sessionStorage.getItem('loggedInUser'));

    wallet = GetWallet(loggedInUser.email);
    note = GetNote(amount, wallet);
    if (note == null) {
        alert('You do not have enough qnotes to make this purchase');
        return;
    }

    payload = {
        'email': loggedInUser.email,
        'receiver': 'admin@quantumbank.com',
        'serial': note,
    }
    $.ajax({
        url: '/cgi-bin/send.py',
        type: 'POST',
        async: false,
        data: JSON.stringify(payload),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            console.log(data)
            if (data['error']) {
                alert(data['error'])
                return;
            }
            alert(data['msg']);
        }
    });

    // remove note from wallet
    UpdateWallet(loggedInUser.email);
    window.location.href = '/store.html';
}

function purchaseAirtime() {
    let phone = $('#phone-number').val();
    let amount = $('#airtime-amounts>div.border-success').text();
    if (!phone) {
        alert('Please enter a meter number');
        return;
    }

    if (!amount) {
        alert('Please select an amount');
        return
    }

    // R100 => 100
    amount = amount.split('R')[1].trim();

    var loggedInUser = JSON.parse(sessionStorage.getItem('loggedInUser'));

    wallet = GetWallet(loggedInUser.email);
    note = GetNote(amount, wallet);
    if (note == null) {
        alert('You do not have enough qnotes to make this purchase');
        return;
    }

    payload = {
        'email': loggedInUser.email,
        'receiver': 'admin@quantumbank.com',
        'serial': note,
    }
    $.ajax({
        url: '/cgi-bin/send.py',
        type: 'POST',
        async: false,
        data: JSON.stringify(payload),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            console.log(data)
            if (data['error']) {
                alert(data['error'])
                return;
            }
            alert(data['msg']);
        }
    });

    // remove note from wallet
    UpdateWallet(loggedInUser.email);
    window.location.href = '/store.html';
}