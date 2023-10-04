from typing import Any, Callable

from instagrapi import Client
from tpdp import Step

from instaduler.state import IState


class GetSession(Step):
    def run(self, state: IState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IState:
        client = Client()
        client.load_settings(state.session_file)
        state.client = client
        return state
