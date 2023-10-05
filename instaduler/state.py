from instagrapi import Client
from model import Post
from tpdp import State


class InstaState(State):
    session_file: str = 'config/session.json'
    client: Client = None

    post: Post = None

    class Config:
        arbitrary_types_allowed = True
