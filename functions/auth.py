import os
import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

def is_signed_in(request: httpx.Request):
    sdk = Clerk(bearer_auth=os.getenv(os.getenv('CLERK_SECRET'))) #FIXME
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=['https://example.com']
        )
    )
    return request_state.is_signed_in