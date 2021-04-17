from typing_extensions import TypedDict


class ITimeline(TypedDict, total=False):
    id: int
    seconds: int
    model_filename: str
    pup_id: str
