# here we are emplementing a subclass of authbase to use it for token auths

from requests.auth import AuthBase
class TokenAuth(AuthBase):
    def __init__(self,token):
        self.token = token
    def __call__(self,request):
        # attaching api token to the authorizations header
        request.headers["Authorization"]= f"Bearer {self.token}"
        return request
        