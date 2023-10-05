from typing import List

from pydantic import BaseModel


class Post(BaseModel):
    paths: List[str]
    caption: str


class PostList(BaseModel):
    posts: List[Post]
