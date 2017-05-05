from oauth2client.client import AccessTokenCredentials
import httplib2

class OAuth2TokenManager:

    @staticmethod
    def foo(access_token):
        credentials = AccessTokenCredentials(access_token, 'my-user-agent/1.0')
        http = httplib2.Http()
        x = credentials.authorize(http)
        return x