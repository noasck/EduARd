from ..project.abstract.abstract_service import AbstractService
from .interface import ITimeline
from .model import Timeline


class TimelineService(AbstractService[Timeline, ITimeline]):
    """Class implements Timeline db operations."""

    @classmethod
    def model(cls):
        """
        Resolve Timeline model class.
        :return: Timeline Type.
        :rtype: type
        """
        return Timeline

    @classmethod
    def get_by_pup_id(cls, pup_id: int):
        return Timeline.query.filter_by(pup_id=pup_id).all()