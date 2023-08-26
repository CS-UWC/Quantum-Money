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
    // We have banknotes of R1, R5, R10, R20, R50, R100, R200
    // We dont want to display each individual, but rather tally them up into the groups
    // Each group will have a value and a count

    colours = {
        1: 'border-black',
        5: 'border-black',
        10: 'border-success',
        20: 'border-warning-subtle',
        50: 'border-danger',
        100: 'border-primary',
        200: 'border-warning'

    }

    let banknoteGroups = {
        1: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0,
        200: 0
    }

    for (let i = 0; i < wallet.length; i++) {
        let amount = wallet[i][1];
        banknoteGroups[amount] += 1;
    }

    for (let i = 0; i < Object.keys(banknoteGroups).length; i++) {
        let amount = Object.keys(banknoteGroups)[i];
        let count = banknoteGroups[amount];
        let colour = colours[amount];
        if (count == 0) {
            continue;
        }

        const banknote = `
            <div class="card mb-2 border ${colour}" style="width: 18rem;" id="banknote-${amount}" data-amount="${amount}">
                <div class="card-body">
                    <div class="d-flex justify-content-center">
                        <div class="rounded-circle p-4 border ${colour} mx-auto d-flex justify-content-center align-center">
                        <h3 class="card-title"><img src="static/images/svg/ket.svg" style="width: 2rem;"class="img-fluid"></img> ${amount}</h3>
                        </div>
                    </div>
                    <p class="card-text">${count} x R${amount}</p>
                </div>
            </div>
        `;

        $('#wallet').append(banknote);
        $(`#banknote-${amount}`).click(function () {
            // check if noteModal exists

            window.scrollTo({
                top: 0,
                left: 0,
                behavior: 'smooth'
            });
            if ($("#noteModal").length == 0) {
                return;
            }
            $("#noteModal").modal('show');
            $("#noteModalLabel").text(`R${amount} Banknotes`);
            $('#qnote-serial-list').empty();
            for (let i = 0; i < wallet.length; i++) {
                let serial = wallet[i][0];
                let noteAmount = wallet[i][1];
                if (noteAmount == amount) {
                    $('#qnote-serial-list').append(`<li class="list-group-item" id="note-${serial}">${serial}</li>`);
                    $(`#note-${serial}`).click(function () {
                        if (getSerial(serial) != null) {
                            return;
                        }
                        addSerial({
                            'serial': serial,
                            'amount': amount
                        });
                        updateView();
                    });
                }
            }
        });
    }
}

function GenerateWalletViewOld(wallet) {
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