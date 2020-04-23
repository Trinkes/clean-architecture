from typing import List, Tuple

from entities.response_status import ResponseStatus
from entities.topic import Topic


class ApiResponseMapper(object):
    def map_topics(self, data: dict) -> List[Topic]:
        related_topics = data['RelatedTopics']
        if not related_topics:
            raise ValueError('No related topics found')
        topics = []
        for topic in related_topics:
            if 'Text' in topic.keys() and topic['Text'] is not None:
                topics.append(Topic(topic['Text']))
        return topics

    def map(self, response_code, data) -> Tuple[ResponseStatus, List[Topic]]:
        if response_code == 200:
            return ResponseStatus.SUCCESS, self.map_topics(data)
        else:
            return ResponseStatus.ERROR, []
