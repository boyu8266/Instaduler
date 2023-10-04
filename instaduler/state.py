from instagrapi import Client
from tpdp import State


class InstaState(State):
    session_file: str = 'config/session.json'
    client: Client = None

    class Config:
        arbitrary_types_allowed = True
