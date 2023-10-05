from typing import List

from pydantic import BaseModel

ALBUM = 'ALBUM'
REELS = 'REELS'


class Post(BaseModel):
    classification: str = ALBUM
    files: List[str]
    caption: str


class PostList(BaseModel):
    posts: List[Post] = None
