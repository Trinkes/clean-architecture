from business_rules.topic_repository import TopicRepository
from entity.response_status import ResponseStatus
from entity.topic import Topic


class TopicService:
    def __init__(self, api: TopicRepository):
        self.api = api

    def find_related_topic(self, word: str) -> Topic:
        response_status, topics = self.api.find_related_topic(word)
        if response_status == ResponseStatus.ERROR:
            raise ValueError('Error accessing external data')

        for topic in topics:
            if topic.title:
                return topic
        raise ValueError('No related topics found')
