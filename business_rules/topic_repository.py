from typing import Tuple, List

from entity.response_status import ResponseStatus
from entity.topic import Topic


class TopicRepository:
    def find_related_topic(self, word) -> Tuple[ResponseStatus, List[Topic]]:
        pass
