from unittest import TestCase
from sherlock.core import ElapsedFuturesSession

class TestElapsedFuturesSession(TestCase):
    def test_request(self):
        efs = ElapsedFuturesSession(tor=False, max_threads=1)
        future = efs.get("https://www.bing.com")


