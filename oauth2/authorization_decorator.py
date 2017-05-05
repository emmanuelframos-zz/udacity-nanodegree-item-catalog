from httplib2 import Http
from flask import request, redirect
from functools import wraps


def is_google_token_valid(access_token):
    response = Http().request("https://www.googleapis.com/userinfo/v2/me", headers={'Host': 'www.googleapis.com', 'Authorization': 'Bearer ' + access_token})
    return True if response[0]['status'] == '200' else False


def is_facebook_token_valid(access_token):
    response = Http().request("https://graph.facebook.com/me?access_token=%s" % access_token)
    return True if response[0]['status'] == '200' else False


def authorized(func):
    @wraps(func)
    def validate_token(*args, **kwargs):
        auth_token = request.headers.get('auth-token')
        auth_provider = request.headers.get('auth-provider')

        if auth_token and auth_provider:
            is_token_valid = False

            if auth_provider == 'google':
                is_token_valid = is_google_token_valid(auth_token)
            elif auth_provider == 'facebook':
                is_token_valid = is_facebook_token_valid(auth_token)

            if is_token_valid:
                func(*args, **kwargs)

        redirect("/", code=302)

    return validate_token