from typing import List

from pydantic import BaseModel


class Post(BaseModel):
    files: List[str]
    caption: str


class PostList(BaseModel):
    posts: List[Post] = None
