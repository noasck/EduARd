from ..project.injector import Injector
from .interface import IPup
from time import time

db = Injector.db


class Pup(db.Model):
    """Describe pup table."""

    __tablename__ = 'pups'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    video_filename = db.Column(
        db.String,
        db.ForeignKey('files.filename', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=True,
    )
    creator_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
    )
    join_code = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.Integer, onupdate=int(time()))
    preview_filename = db.Column(
        db.String,
        db.ForeignKey('files.filename', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=True
    )

    def update(self, changes: IPup):
        """Update certain record."""
        for key, new_value in changes.items():
            if key not in {'id', 'creator_id', 'join_code', 'created_at'}:
                setattr(self, key, new_value)
        return self


class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    pup_id = db.Column(db.Integer, db.ForeignKey('pups.id'), primary_key=True)
