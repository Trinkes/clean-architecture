from typing import Tuple
from urllib.parse import urlencode

import requests

from interfaces_adapter.topic_api import TopicApi


class RequestsTopicApi(TopicApi):
    def __init__(self, base_host: str):
        self.base_host = base_host

    def get(self, word) -> Tuple[int, str]:
        q = word
        url = "{}?".format(self.base_host)
        url += urlencode({'q': q, 'format': 'json'})
        print(url)
        response = requests.get(url)
        return response.status_code, response.json()
