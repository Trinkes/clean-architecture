from typing import Tuple, List

from entities.response_status import ResponseStatus
from entities.topic import Topic
from interface_adapter.api_response_mapper import ApiResponseMapper
from interface_adapter.topic_api import TopicApi
from use_cases.topic_repository import TopicRepository


class ApiTopicRepository(TopicRepository):
    def __init__(self, api: TopicApi, mapper: ApiResponseMapper):
        self.mapper = mapper
        self.api = api

    def find_related_topic(self, word) -> Tuple[ResponseStatus, List[Topic]]:
        response_code, data = self.api.get(word)
        return self.mapper.map(response_code, data)
