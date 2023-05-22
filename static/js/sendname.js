$(document).ready(function() {
    $('#submit').click(function() {
        var name = $('#name').val();
        console.log(name)
        $.ajax({
            url: '/cgi-bin/hello.py',
            type: 'post',
            data: JSON.stringify({'name': name}),
            error: function(xhr, status, error) {
                // Handle the error if the AJAX request fails
                alert('Error: ' + error);
              },
            success: function(data) {
                console.log(data)
                $('#response').html(data['name']);
            }
        });
    });
});