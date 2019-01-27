from unittest import TestCase
from sherlock.core import Log
from colorama import Fore, Style

class TestLog(TestCase):
    def test_getLogger(self):
        log = Log.getLogger(name="testgetlogger", verbose=False, replaced=True, warninglevel=0)
        log.log("Hello Sherlock!")

    def test_lock(self):
        log = Log.getLogger(name="locktest",
                            verbose=False,
                            replaced=True,
                            warninglevel=0)
        log.lock()


    def test_unlock(self):
        log = Log.getLogger(name="unlocktest",
                            verbose=False,
                            replaced=True,
                            warninglevel=0)
        log.unlock()

    def test_eprint(self):
        log = Log.getLogger(name="eprinttest",
                            verbose=False,
                            replaced=True,
                            warninglevel=0)
        log.eprint("+",
                   "This is an eprint",
                   store=False,
                   status_color=Fore.WHITE,
                   status_frame=Fore.WHITE,
                   message_color=Fore.WHITE,
                   style=Style.BRIGHT
                )


    def test_log(self):
        log = Log.getLogger(name="testerror",
                            verbose=False,
                            replaced=True,
                            warninglevel=0)

        log.log("Just log")

    def test_error(self):
        log = Log.getLogger(name="testerror",
                            verbose=False,
                            replaced=True,
                            warninglevel=0)

        log.error("Erroring")

    def test_info(self):
        log = Log.getLogger(name="testerror",
                            verbose=False,
                            replaced=True,
                            warninglevel=0)

        log.info("Info")
