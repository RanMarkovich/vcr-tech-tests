from dataclasses import dataclass


@dataclass
class HSConfig:
    """Implementing Hired-Score service configuration"""
    _SERVICE_ENDPOINT = 'http://hs-recruiting-test-resume-data.s3.amazonaws.com'
