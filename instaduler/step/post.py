import traceback
from typing import Any, Callable

from instagrapi import Client
from instagrapi.extractors import extract_track
from logging_service import LoggingService
from tpdp import Step

from instaduler.model.post import ALBUM, REELS
from instaduler.state import InstaState


class PostAlbum(Step):
    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        if state.post.classification != ALBUM:
            return state

        state.client.album_upload(
            state.post.files,
            state.post.caption
        )
        return state


class PostReels(Step):
    def custom_search_music(self, client: Client, query: str):
        params = {
            "query": query,
            "browse_session_id": client.generate_uuid(),
        }
        result = client.private_request("music/audio_global_search/", params=params)
        items = result['items']
        for item in items:
            item['track']['territory_validity_periods'] = {}
        return [extract_track(item["track"]) for item in result["items"]]

    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        if state.post.classification != REELS:
            return state

        try:
            track_to_post = None

            if state.post.track_query == None or len(state.post.track_query) == 0:
                state.client.clip_upload(
                    state.post.files[0],
                    state.post.caption,
                )
            else:
                tracks = self.custom_search_music(state.client, state.post.track_query)
                for track in tracks:
                    if track.audio_asset_id != state.post.track_id:
                        continue

                    track.highlight_start_times_in_ms = state.post.track_highlight_start_times_in_ms
                    track_to_post = track
                    break

                state.client.clip_upload_as_reel_with_music(
                    state.post.files[0],
                    state.post.caption,
                    track_to_post
                )
        except:
            LoggingService().err(traceback.format_exc())
            pipeline_abort = True
        return state
