
$(document).ready(function () {
    let user = fetchUserFromCache();
    
    GetWallet(user.email);

    $('#sendbutton').click(function () {
        window.location.href = 'send.html';
    });
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
            if (data['error']) {
                console.log({ data });
            }
            let banknotes = data['serials'];
            $('#total').append(banknotes.length);
            for (let i = 0; i < banknotes.length; i++) {
                let serial = banknotes[i];
                const banknote = `
                    <div class="card mb-2" style="width: 18rem;" id="banknote">
                        <div class="card-body">
                            <h3 class="card-title">R 1</h3>
                            <p class="card-text" >Serial Number: ${serial}</p>
                        </div>
                    </div>
                `;
                $('#wallet').append(banknote);
            }
            $('#banknote').click(function () {
                console.log("clicked");
                $(this).toggleClass('selected');
            });
        }
    })
}