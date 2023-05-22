$(document).ready(function () {
    let params = new URLSearchParams(window.location.search);
    let email = "isatippens2@gmail.com";
    if (params.has('email')) {
        email = params.get('email');
    }
    GetWallet(email);
});

function GetWallet(email) {
    
    $.ajax({
        url: '/cgi-bin/wallet.py',
        type: 'POST',
        data: JSON.stringify({'email': email}),
        error: function (xhr, status, error) {
            // Handle the error if the AJAX request fails
            alert('Error: ' + error);
        },
        success: function (data) {
            console.log(data)
            if (data['error']) {
                console.log({ data });
            }
            let banknotes = data['serials'];
            for (let i = 0; i < banknotes.length; i++) {
                let serial = banknotes[i];
                const banknote = `
                <div class="col-sm">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">R1</h5>
                            <p class="card-text">Serial Number: ${serial}</p>
                            <button type="button" class="btn btn-primary" onclick="sendBanknote('${serial}','${email}')">Send</button>
                        </div>
                    </div>
                </div>
                `;
                $('#wallet').append(banknote);
            }
        }
    })
}