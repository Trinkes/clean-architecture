from typing import Tuple, List

from entities.response_status import ResponseStatus
from entities.topic import Topic


class TopicRepository:
    def find_related_topic(self, word) -> Tuple[ResponseStatus, List[Topic]]:
        pass
