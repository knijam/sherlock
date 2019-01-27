import requests, grequests
from unittest import TestCase
from sherlock.core import Service

# Response alteration
def response_error(req, exception, logger):
    raise exception


class TestService(TestCase):
    def test_grequest(self):

        f = False

        def response(service, found):
            global f
            f = found

        service = Service(
            "USer123",
            response,
            url="https://www.facebook.com/{}",
            regexCheck="^[a-zA-Z0-9]{4,49}(?<!.com|.org|.net)$",
        )

        grequests.map(
            [service.grequest],
            exception_handler=lambda request, exception: response_error(
                request, exception, None
            )
        )


    def test_valid(self):
        service = Service(
            "USer123",
            None,
            url="https://www.facebook.com/{}",
            regexCheck="^[a-zA-Z0-9]{4,49}(?<!.com|.org|.net)$",
        )

        assert(service.valid)

    def test_url(self):
        service = Service(
            "USer123",
            None,
            url="https://www.facebook.com/{}",
            regexCheck="^[a-zA-Z0-9]{4,49}(?<!.com|.org|.net)$",
        )
        assert(service.url == "https://www.facebook.com/USer123")

    def test_host(self):
        service = Service(
            "USer123",
            None,
            url="https://www.facebook.com/{}",
            regexCheck="^[a-zA-Z0-9]{4,49}(?<!.com|.org|.net)$",
        )
        assert(service.host == "https://www.facebook.com")
