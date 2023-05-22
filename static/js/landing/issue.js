$(document).ready(function() {
    $('#issue').click(function() {
        console.log(name)
        $.ajax({
            url: '/cgi-bin/issue.py',
            type: 'post',
            data: JSON.stringify({'user_id': 1}),
            error: function(xhr, status, error) {
                // Handle the error if the AJAX request fails
                alert('Error: ' + error);
              },
            success: function(data) {
                console.log(data)
            }
        });
    });
});