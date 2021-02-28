import requests


class RequestsAPI:
    """Implementing requests API as Interface for services under test"""

    @staticmethod
    def get(endpoint):
        r = requests.get(endpoint)
        return r
