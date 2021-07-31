from rest_framework_simplejwt.tokens import RefreshToken

def get_token(user_object):
    refresh = RefreshToken.for_user(user_object)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token