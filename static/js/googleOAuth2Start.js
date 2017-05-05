var googleOAuth2Start = function(){
     gapi.load('auth2', function () {
        gapi.auth2.init({ client_id: '35461092313-1r1hfo1nmdivevfpks41lap0357k4lrc.apps.googleusercontent.com' });
     });
};