function fetchUserFromCache() {
    let user = sessionStorage.getItem("loggedInUser");
    if (user) {
        return JSON.parse(user);
    }
    return null;
}

function storeUserInCache(user) {
    sessionStorage.setItem("loggedInUser", JSON.stringify(user));
}