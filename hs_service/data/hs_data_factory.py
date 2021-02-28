from copy import deepcopy
from dataclasses import dataclass

from common_functions import load_json_schema


@dataclass
class HSDataFactory:
    """Data factory class for serving payloads"""
    __EXP_RESP_DATA_PAYLOAD = load_json_schema('./hs_service/data/exp_resp_data.json')
    _EXP_CANDIDATES_EMAIL_ADDRESSES = ['captainamerica@yahoo.com', 'bruce-wayne-batman@verizon.net',
                                       'Peter.Parker@Spidermantech.com', 'Heisenberg@hotmail.com']

    def exp_resp_data_payload(self):
        payload = deepcopy(self.__EXP_RESP_DATA_PAYLOAD)
        return payload
