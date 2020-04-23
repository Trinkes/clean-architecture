from frameworks.requests_topic_api import RequestsTopicApi
from interface_adapter.api_response_mapper import ApiResponseMapper
from interface_adapter.api_topic_repository import ApiTopicRepository
from use_cases.topic_service import TopicService

service = TopicService(
    ApiTopicRepository(RequestsTopicApi('http://api.duckduckgo.com/'),
                       ApiResponseMapper()))
print(service.find_related_topic('java').title)
