import requests
from time import time
from requests_futures.sessions import FuturesSession
from concurrent.futures import ThreadPoolExecutor
from torrequest import TorRequest

class ElapsedFuturesSession(FuturesSession):
    """
    Extends FutureSession to add a response time metric to each request.

    This is taken (almost) directly from here: https://github.com/ross/requests-futures#working-in-the-background
    """

    def __init__(self, tor=False, max_threads=1, **kwargs):

        # Allow 1 thread for each external service.
        executor = ThreadPoolExecutor(max_workers=max_threads)

        # Create session based on request methodology
        if tor:
            self._underlying_request = TorRequest()
            self._underlying_session = self._underlying_request.session
        else:
            self._underlying_session = requests.session()
            self._underlying_request = requests.Request()

        super(ElapsedFuturesSession, self).__init__(executor=executor, session=self._underlying_session, **kwargs)

    def request(self, method, url, hooks={}, *args, **kwargs):
        start = time()

        def timing(r, *args, **kwargs):
            elapsed_sec = time() - start
            r.elapsed = round(elapsed_sec * 1000)

        try:
            if isinstance(hooks["response"], (list, tuple)):
                # needs to be first so we don't time other hooks execution
                hooks["response"].insert(0, timing)
            else:
                hooks["response"] = [timing, hooks["response"]]
        except KeyError:
            hooks["response"] = timing

        return super(ElapsedFuturesSession, self).request(
            method, url, hooks=hooks, *args, **kwargs
        )
