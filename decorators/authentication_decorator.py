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


def authenticated(func):
    @wraps(func)
    def validate_token(*args, **kwargs):
        """
        Checks token validation using header
        :param args: 
        :param kwargs: 
        :return: func
        """
        auth_token = request.headers.get('auth_token')

        if auth_token and is_google_token_valid(auth_token):
            return func(*args, **kwargs)

        return abort(403)

    return validate_token
