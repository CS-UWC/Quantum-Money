$(document).ready(function () {
    // Get logged in user from session storage
    // if user is not logged in, redirect to login page
    var loggedInUser = JSON.parse(sessionStorage.getItem('loggedInUser'));
    if (!loggedInUser) {
        window.location.href = 'index.html';
    }

    // console.log(loggedInUser)
    
    // modify welcome message to include username
    $('#welcome').html('Welcome ' + loggedInUser.firstname + '!');
});