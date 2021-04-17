from typing_extensions import TypedDict


class IPup(TypedDict, total=False):
    id: int
    name: str
    video_filename: str
    creator_id: int
    join_code: str
    created_at: int
