from sqlalchemy import String, Text

from .mixins import UserRelationMixin
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"
    title: Mapped[str] = mapped_column(String(50), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
