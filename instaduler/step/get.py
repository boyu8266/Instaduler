import glob
import os
from typing import Any, Callable

from tpdp import Step

from instaduler.state import InstaState


class GetFiles(Step):
    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        state.files = glob.glob(os.path.join(state.folder, "*.jpg"))
        return state
