from justwatch import JustWatch


class JWResponse:
    def __init__(self, search_response):
        response = search_response["items"][0]
        if "offers" not in response:
            self.offers = []
        else:
            self.offers = response["offers"]
        self.title = response["title"]


class JWQuery:
    def __init__(self):
        self.client = JustWatch(country="AR")

    def request(self, query):
        search_response = self.client.search_for_item(query=query)
        return JWResponse(search_response)
