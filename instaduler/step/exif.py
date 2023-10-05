import contextlib
from typing import Any, Callable

from PIL import Image
from state import InstaState
from tpdp import Step


class ExifOrientation(Step):
    def read_image_with_exif_rotation(self, image_path):
        image = Image.open(image_path)

        exif = image._getexif()
        if exif:
            exif_orientation = exif.get(274)
            if exif_orientation == 3:
                image = image.rotate(180, expand=True)
            elif exif_orientation == 6:
                image = image.rotate(270, expand=True)
            elif exif_orientation == 8:
                image = image.rotate(90, expand=True)

        return image

    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        for file in state.post.files:
            with contextlib.suppress(Exception):
                image = self.read_image_with_exif_rotation(file)
                image.save(file)

        return state
