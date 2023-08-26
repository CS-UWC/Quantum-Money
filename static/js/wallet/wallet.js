$(document).ready(function () {

    let user = fetchUserFromCache();

    wallet = GetWallet(user.email);
    GenerateWalletView(wallet);

    GetBalance(user.email);

    GetLimit(user.email);

    $('#sendbutton').click(function () {
        window.location.href = 'send.html';
    });
});


function GetWalletOld(email) {

    $.ajax({
        url: '/cgi-bin/wallet.py',
        type: 'POST',
        data: JSON.stringify({ 'email': email }),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            if (data['error']) {
                console.log({ data });
            }
            let banknotes = data['serials'];
            for (let i = 0; i < banknotes.length; i++) {
                console.log(banknotes[i])
                let serial = banknotes[i][0];
                let amount = banknotes[i][1];
                const banknote = `
                    <div class="card mb-2 border border-warning" style="width: 18rem;" id="banknote">
                        <div class="card-body">
                            <div class="d-flex justify-content-center">
                                <div class="rounded-circle p-4 border border-warning mx-auto d-flex justify-content-center align-center">
                                    <h3 class="card-title"><img src="static/images/svg/ket.svg" style="width: 2rem;"class="img-fluid"></img> ${amount}</h3>
                                </div>
                            </div>    
                            <p class="card-text" >${serial}</p>
                        </div>
                    </div>
                `;
                $('#wallet').append(banknote);
            }
            $('#banknote').click(function () {
                $(this).toggleClass('selected');
            });
        }
    })
}

function GetBalance(email) {
    $.ajax({
        url: '/cgi-bin/wallet/get_balance.py',
        type: 'POST',
        data: JSON.stringify({ 'email': email }),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            let amount = 0;
            if (data['error']) {
                console.log({ data });
                $('#total').text(amount);
                return
            }
            let balance = data['balance'];
            $('#total').text(balance);
        }
    });
}

