from typing import List

from pydantic import BaseModel

ALBUM = 'ALBUM'
REELS = 'REELS'


class Post(BaseModel):
    classification: str = ALBUM
    files: List[str]
    caption: str
    track_query: str = None
    track_id: int = None
    track_highlight_start_times_in_ms: list = None


class PostList(BaseModel):
    posts: List[Post] = None
