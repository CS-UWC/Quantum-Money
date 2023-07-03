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

function storeWalletInCache(wallet) {
    sessionStorage.setItem("wallet", JSON.stringify(wallet));
}

function fetchWalletFromCache() {
    let wallet = sessionStorage.getItem("wallet");
    if (wallet) {
        return JSON.parse(wallet);
    }
    return null;
}
