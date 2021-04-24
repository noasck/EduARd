import json
from jose import jwt
from flask import jsonify, request
from ..project.injector import Injector
from .model import User
from .schema import UserSchema
from urllib.request import urlopen

jwt_extended = Injector.jwt
app = Injector.app

AUTH0_DOMAIN = app.config['AUTH0_DOMAIN']
ALGORITHMS = app.config['AUTH0_ALGORITHMS']
API_AUDIENCE = app.config['AUTH0_API_AUDIENCE']


@jwt_extended.user_claims_loader
def user_based_token(user: User):
    """
    Serialize single User entity data to JWT.

    :param user: User instance
    :return: serialized User Instance
    """
    return UserSchema().dump(user)


#: TEST: Delete
def verify_token(token: str) -> str:
    """
    Mock google and fb auth.

    :param token: email
    :return: email
    """
    return token.strip()


@jwt_extended.user_identity_loader
def user_identity_lookup(user: User) -> str:
    """Define identity user field."""
    return user.email


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def get_payload():
    """Obtains the Access Token from the Authorization Header"""

    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/"
            )
        except jwt.ExpiredSignatureError:
            raise AuthError({"message": "token_expired",
                             "description": "token is expired"}, 401)
        except jwt.JWTClaimsError:
            raise AuthError({"message": "invalid_claims",
                             "description":
                                 "incorrect claims,"
                                 "please check the audience and issuer"}, 401)
        except Exception:
            raise AuthError({"message": "invalid_header",
                             "description":
                                 "Unable to parse authentication"
                                 " token."}, 401)

        return payload
    raise AuthError({"code": "invalid_header", "description": "Unable to find appropriate key"}, 401)
