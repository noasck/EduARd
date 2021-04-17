from ..project.injector import Injector
from .model import User
from .schema import UserSchema

jwt = Injector.jwt


@jwt.user_claims_loader
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


@jwt.user_identity_loader
def user_identity_lookup(user: User) -> str:
    """Define identity user field."""
    return user.email
