from ..project.injector import Injector
from .interface import ITimeline

db = Injector.db


class Timeline(db.Model):
    """Describe timeline table."""

    __tablename__ = 'timelines'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    seconds = db.Column(db.Integer, nullable=False)
    model_filename = db.Column(
        db.String,
        db.ForeignKey('files.filename'),
        nullable=False,
    )
    pup_id = db.Column(
        db.Integer,
        db.ForeignKey('pups.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False
    )

    def update(self, changes: ITimeline):
        """Update certain record."""
        for key, new_value in changes.items():
            if key not in {'id', 'seconds'}:
                setattr(self, key, new_value)
        return self
