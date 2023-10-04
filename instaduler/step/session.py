from typing import Any, Callable

from instagrapi import Client
from tpdp import Step

from instaduler.state import InstaState


class SetSession(Step):
    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        client = Client()
        client.load_settings(state.session_file)
        state.client = client
        return state
