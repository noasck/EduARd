from typing_extensions import TypedDict


class IFile(TypedDict, total=False):
    id: int
    filename: str
