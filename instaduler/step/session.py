from typing import Any, Callable

from instagrapi import Client
from state import InstaState
from tpdp import Step


class SetSession(Step):
    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        client = Client()
        client.load_settings(state.session_file)
        state.client = client
        return state
