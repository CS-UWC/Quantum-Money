function fetchWalletFromDB(email) {
    var wallet = []
    $.ajax({
        url: '/cgi-bin/wallet.py',
        type: 'POST',
        data: JSON.stringify({ 'email': email }),
        async: false,
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            if (data['error']) {
                console.log({ data });
                return
            }
            let banknotes = data['serials'];
            for (let i = 0; i < banknotes.length; i++) {
                let serial = banknotes[i][0];
                let amount = banknotes[i][1];
                wallet.push([serial, amount]);
            }
        }
    })
    return wallet;
}

function GenerateWalletView(wallet) {
    for (let i = 0; i < wallet.length; i++) {
        let serial = wallet[i][0];
        let amount = wallet[i][1];
        const banknote = `
            <div class="card mb-2 border border-warning" style="width: 18rem;" id="banknote">
                <div class="card-body">
                    <div class="d-flex justify-content-center">
                        <div class="rounded-circle p-4 border border-warning mx-auto d-flex justify-content-center align-center">
                            <h3 class="card-title"><img src="static/images/svg/ket.svg" style="width: 2rem;"class="img-fluid"></img> ${amount}</h3>
                        </div>
                    </div>    
                    <p class="card-text">${serial}</p>
                </div>
            </div>
        `;
        $('#wallet').append(banknote);
    }
}

function GetWallet(email) {
    wallet = fetchWalletFromCache(email);
    if (!wallet) {
        wallet = fetchWalletFromDB(email);
        storeWalletInCache(wallet);
    }
    return wallet;
}

function GetBalance(email) {
    let balance = 0;
    $.ajax({
        url: '/cgi-bin/wallet/get_balance.py',
        type: 'POST',
        data: JSON.stringify({ 'email': email }),
        async: false,
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            if (data['error']) {
                return
            }
            balance = data['balance'];
        }
    })
    return balance;
}

function GetNote(value, wallet) {
    // go through wallet and find note with value
    for (let i = 0; i < wallet.length; i++) {
        if (wallet[i][1] == value) {
            return wallet[i][0];
        }
    }
    return null;
}


function UpdateWallet(email) {
    var wallet = fetchWalletFromDB(email);
    storeWalletInCache(wallet);
    return wallet;
}

function RemoveNoteFromWallet(serial, wallet) {
    for (var i = 0; i < wallet.length; i++) {
        if (wallet[i] == serial) {
            wallet.splice(i, 1);
            break;
        }
    }
    storeWalletInCache(wallet);
    return wallet;
}