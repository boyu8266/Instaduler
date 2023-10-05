from instagrapi import Client
from tpdp import State

from instaduler.model import Post


class InstaState(State):
    session_file: str = 'config/session.json'
    client: Client = None

    post: Post = None

    class Config:
        arbitrary_types_allowed = True
