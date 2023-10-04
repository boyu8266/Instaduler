from tpdp import Pipeline

from instaduler.state import InstaState
from instaduler.step import *


class InstaPipeline:
    def __init__(self) -> None:
        set_session = SetSession('set session')
        get_files = GetFiles('get files')
        exif_orientation = ExifOrientation('exif orientation')

        self.steps = [
            set_session,
            get_files, exif_orientation
        ]

        self.pipeline = Pipeline(__name__)
        for step in self.steps:
            self.pipeline.registry_step(step)

    def run(self, folder: str) -> InstaState:
        state = InstaState()
        state.folder = folder

        r = self.pipeline.run(state)
        return state
