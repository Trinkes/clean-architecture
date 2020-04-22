# clean-architecture
Excercise:
With The Clean Architecture in mind, make the following code cleaner:


    def find_related_topic(word: str) -> str:
        q = word
        url = 'http://api.duckduckgo.com/?'
        url += urlencode({'q': q, 'format': 'json'})
        response = requests.get(url)
        data = response.json()
        related_topics = data['RelatedTopics']
        if not related_topics:
            raise ValueError('That\'s not a word')
        for topic in related_topics:
            if topic['Text'] is not None:
                return topic['Text']
        raise ValueError('That\'s not a word')
    
    
    print(find_related_topic('ball'))

