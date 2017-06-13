from httplib2 import Http
from flask import request, abort
from functools import wraps


def is_google_token_valid(access_token):
    """
    Checks if token is valid on Google API
    :param access_token: 
    :return: Boolean 
    """
    response = Http().request(
        "https://www.googleapis.com/userinfo/v2/me",
        headers={'Host': 'www.googleapis.com',
                 'Authorization': 'Bearer ' + access_token})
    return True if response[0]['status'] == '200' else False


def is_facebook_token_valid(access_token):
    """
    Checks if token is valid on Facebook API
    :param access_token: 
    :return: Boolean 
    """
    response = Http().request(
        "https://graph.facebook.com/me?access_token=%s" % access_token)
    return True if response[0]['status'] == '200' else False


def authorized(func):
    @wraps(func)
    def validate_token(*args, **kwargs):
        """
        Checks token validation using provider header
        :param args: 
        :param kwargs: 
        :return: func
        """
        auth_token = request.headers.get('auth-token')
        auth_provider = request.headers.get('auth-provider')

        if auth_token and auth_provider:
            is_token_valid = False

            if auth_provider == 'google':
                is_token_valid = is_google_token_valid(auth_token)
            elif auth_provider == 'facebook':
                is_token_valid = is_facebook_token_valid(auth_token)

            if is_token_valid:
                return func(*args, **kwargs)

        return abort(401)

    return validate_token
