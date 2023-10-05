from model import Post
from state import InstaState
from step import *
from tpdp import Pipeline


class InstaPipeline:
    def __init__(self) -> None:
        set_session = SetSession('set session')
        exif_orientation = ExifOrientation('exif orientation')
        post_album = PostAlbum('post album')
        update_schedule = UpdateSchedule('update schedule')

        self.steps = [
            set_session,
            exif_orientation,
            post_album,
            update_schedule
        ]

        self.pipeline = Pipeline(__name__)
        for step in self.steps:
            self.pipeline.registry_step(step)

    def run(self, post: Post) -> InstaState:
        state = InstaState()
        state.post = post

        r = self.pipeline.run(state)
        return state
