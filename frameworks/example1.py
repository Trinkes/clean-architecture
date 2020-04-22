from business_rules.topic_service import TopicService
from frameworks.requests_topic_api import RequestsTopicApi
from interfaces_adapter.api_response_mapper import ApiResponseMapper
from interfaces_adapter.api_topic_repository import ApiTopicRepository


def find_related_topic(word: str) -> str:
    service = TopicService(
        ApiTopicRepository(RequestsTopicApi('http://api.duckduckgo.com/'),
                           ApiResponseMapper()))
    return service.find_related_topic(word).title
