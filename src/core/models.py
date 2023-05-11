import sqlalchemy as sqla
from sqlalchemy.types import DateTime


class TimeBaseModel(object):
    """The base class of the model, the time of creation of the extension and the time of updating the model"""

    create_time = sqla.Column(
        DateTime,
        nullable=False,
        default=sqla.func.now(),
    )

    update_time = sqla.Column(
        DateTime,
        nullable=False,
        default=sqla.func.now(),
        onupdate=sqla.func.now(),
    )
