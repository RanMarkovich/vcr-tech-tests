from dataclasses import dataclass

from hs_service.config import HSConfig
from requests_interface.requests_interface import RequestsAPI


@dataclass
class HSTestHelper(HSConfig, RequestsAPI):
    """Implementation of Hired-Score API Calls"""

    def __post_init__(self):
        self.service_endpoint = self._SERVICE_ENDPOINT
        self.all_candidates_endpoint = f"{self.service_endpoint}/allcands-full.json"

    def get_all_candidates(self):
        r = self.get(self.all_candidates_endpoint)
        return r
