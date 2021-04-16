from typing_extensions import TypedDict


class IUser(TypedDict, total=False):
    id: int
    email: str
