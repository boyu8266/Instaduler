from typing import Any, Callable

from instagrapi import Client
from tpdp import Step

from instaduler.state import InstaState


class PostAlbum(Step):
    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        state.client.album_upload(
            state.post.files,
            state.post.caption
        )
        return state
