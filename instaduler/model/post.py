from typing import List

from pydantic import BaseModel

from instaduler.const import ALBUM


class Post(BaseModel):
    classification: str = ALBUM
    files: List[str]
    caption: str


class PostList(BaseModel):
    posts: List[Post] = None
