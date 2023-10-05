from tpdp import Pipeline

from instaduler.model import Post
from instaduler.state import InstaState
from instaduler.step import *


class InstaPipeline:
    def __init__(self) -> None:
        set_session = SetSession('set session')
        exif_orientation = ExifOrientation('exif orientation')

        self.steps = [
            set_session,
            exif_orientation
        ]

        self.pipeline = Pipeline(__name__)
        for step in self.steps:
            self.pipeline.registry_step(step)

    def run(self, post: Post) -> InstaState:
        state = InstaState()
        state.post = post

        r = self.pipeline.run(state)
        return state
