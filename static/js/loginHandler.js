/* Facebook OAuth2 SignIn */
function checkLoginState() {
    FB.getLoginStatus(function(authResponse) {
        if (authResponse.status === 'connected') {
            window.localStorage.auth_token = authResponse.authResponse.accessToken;
            window.localStorage.auth_provider = "facebook";
            window.location.href = '/#/gameList';
        }else{
            window.location.href = '/#/signIn';
        }
    });
}

/* Facebook SignOut */
var facebookSignOut = function(){
    FB.logout(function(response) {
        window.localStorage.clear();

        console.log("Facebook - Signed out.");

        window.location.href = '/#/signIn';       
    });
}

/* Google OAuth 2 Start */
var start = function(){
    googleOAuth2Start();
};

/* Google OAuth 2 SignIn */
googleSignIn = function(){
    var promise = gapi.auth2.getAuthInstance().signIn({ scope: 'email' });

    promise.then(function(response){
       window.localStorage.auth_token = response.getAuthResponse().access_token;
       window.localStorage.auth_provider = "google";
       window.location.href = '/#/gameList';      
    }, function(error){
       window.location.href = '/#/signIn';
    });
}

/* Google SignOut */
var googleSignOut = function(){
    gapi.auth2.getAuthInstance().signOut();

    window.localStorage.clear();

    console.log("Google - Signed out.");

    window.location.href = '/#/signIn';        
}