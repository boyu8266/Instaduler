from tpdp import Pipeline

from instaduler.model import Post
from instaduler.model.post import ALBUM, REELS
from instaduler.state import InstaState
from instaduler.step import *


class InstaPipeline:
    def __init__(self) -> None:
        set_session = SetSession('set session')
        exif_orientation = ExifOrientation('exif orientation')
        post_album = PostAlbum('post album')
        post_reels = PostReels('post reels')
        update_schedule = UpdateSchedule('update schedule')

        steps_album = [
            set_session,
            exif_orientation,
            post_album,
            update_schedule
        ]
        self.pipeline_album = Pipeline(f'{__name__}: : album')
        for step in steps_album:
            self.pipeline_album.registry_step(step)

        steps_reels = [
            set_session,
            post_reels,
            update_schedule
        ]
        self.pipeline_reels = Pipeline(f'{__name__}: : reels')
        for step in steps_reels:
            self.pipeline_reels.registry_step(step)

    def run(self, post: Post) -> InstaState:
        state = InstaState()
        state.post = post

        if post.classification == ALBUM:
            r = self.pipeline_album.run(state)
        elif post.classification == REELS:
            r = self.pipeline_reels.run(state)
        return state
