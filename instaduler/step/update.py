import json
from typing import Any, Callable

from tpdp import Step

from instaduler.const import *
from instaduler.model import PostList
from instaduler.state import InstaState


class UpdateSchedule(Step):
    def run(self, state: InstaState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> InstaState:
        try:
            postlist = PostList.parse_file(SCHEDULE_FILE)
        except:
            print('ex')
            return state

        if not isinstance(postlist.posts, list):
            print('isinstance')
            return state

        postlist.posts.pop(0)

        try:
            with open(SCHEDULE_FILE, 'w', encoding='utf-8') as file:
                json.dump(postlist.dict(), file, ensure_ascii=False, indent=4)
        except:
            print(f"An exception occurred while saving the JSON file.")
        return state
