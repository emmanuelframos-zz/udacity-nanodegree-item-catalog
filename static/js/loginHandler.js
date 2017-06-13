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

var facebookSignOut = function(){
    console.log("Facebook - Signing out.");
    FB.logout(function(response) {
        window.localStorage.clear();

        console.log("Facebook - Signed out.");

        window.location.href = '/#/signIn';       
    });
}

/* Google OAuth 2 SignIn */
var start = function(){
    googleOAuth2Start();
};

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

var googleSignOut = function(){
    console.log("Google - Signing out.");

    gapi.auth2.getAuthInstance().signOut();
    window.localStorage.clear();

    console.log("Google - Signed out.");

    window.location.href = '/#/signIn';        
}