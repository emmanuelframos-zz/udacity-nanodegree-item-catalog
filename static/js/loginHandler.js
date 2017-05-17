/* Facebook OAuth2 SignIn */
function checkLoginState() {
FB.getLoginStatus(function(authResponse) {
   if (authResponse.status === 'connected') {
      $.ajax({
          url: 'http://localhost:5000/login',
          type: 'post',
          headers: {
            "auth-token": authResponse.authResponse.accessToken,
            "auth-provider": "facebook"
          },
          success: function (data) {
          }
      });
   }
}, true);
}

var facebookSignOut = function(){
    FB.logout(function(response) {});
}

/* Google OAuth 2 SignIn */
var start = function(){
    googleOAuth2Start();
};

googleSignIn = function(){
var promise = gapi.auth2.getAuthInstance().signIn({ scope: 'email' });

promise.then(function(response){
  $.ajax({
      url: 'http://localhost:5000/login',
      type: 'post',
      headers: {
        "auth-token": response.getAuthResponse().access_token,
        "auth-provider": "google"
      },
      success: function (data) {
      }
  });
});
}

var googleSignOut = function(){
    gapi.auth2.getAuthInstance().signOut();
}