from instagrapi import Client
from tpdp import State


class IState(State):
    session_file: str = None
    client: Client = None

    class Config:
        arbitrary_types_allowed = True
