# ./DECENTRALIZED_IRC-DJANGO/api/utils.py
# Helper functions here.

from django.http import HttpResponseRedirect
from django.utils import timezone
from django.conf import settings
import jwt
import datetime


# generate jwt for authentication or chat
def generate_auth_jwt(payload,type):
    iat = int(datetime.datetime.now(tz=timezone.utc).timestamp())
    exp = int((datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=3600)).timestamp())
    if type == 'auth':
        encoded_jwt = jwt.encode({"user_info":payload,"iat":iat,"exp":exp},settings.AUTH_SECRET_KEY,algorithm='HS256')
    elif type == 'chat':
        encoded_jwt = jwt.encode({"rooms":payload,"iat":iat,"exp":exp},settings.CHAT_SECRET_KEY,algorithm='HS256')
    return encoded_jwt


# decode jwt, returns payload or error
def decode_jwt(jwt_token,type):
    try:
        if type == 'auth':
            decoded = jwt.decode(jwt_token,settings.AUTH_SECRET_KEY,algorithms=['HS256'])
        elif type == 'chat':
            decoded = jwt.decode(jwt_token,settings.CHAT_SECRET_KEY,algorithms=['HS256'])
        print(decoded)
        return decoded
    except:
        print("Generic Error")
        return False


## function to check if the request is authenticated. Need to perform check on every API endpoint.

def is_logged_in(function):
    def wrapper(request, *args, **kw):
        if 'id_token' in request.COOKIES:
            jwt = request.COOKIES['id_token'] 
            decoded = decode_jwt(jwt,'auth')
            print(decoded)
            if decoded != False:
                user = decoded["user_info"]["UID"]
                if user:    #replace with user.in_database():
                    return function(request, *args, **kw)
            else:
                return HttpResponseRedirect('/user/login')
        else:
            return HttpResponseRedirect('/user/login')
    return wrapper