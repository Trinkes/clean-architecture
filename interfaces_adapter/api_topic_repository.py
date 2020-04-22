from typing import Tuple, List

from business_rules.topic_repository import TopicRepository
from entity.response_status import ResponseStatus
from entity.topic import Topic
from interfaces_adapter.api_response_mapper import ApiResponseMapper
from interfaces_adapter.topic_api import TopicApi


class ApiTopicRepository(TopicRepository):
    def __init__(self, api: TopicApi, mapper: ApiResponseMapper):
        self.mapper = mapper
        self.api = api

    def find_related_topic(self, word) -> Tuple[ResponseStatus, List[Topic]]:
        response_code, data = self.api.get(word)
        return self.mapper.map(response_code, data)
