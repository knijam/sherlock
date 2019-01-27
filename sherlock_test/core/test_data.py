import json
import yaml

from sherlock_test import framework
from unittest import TestCase
from sherlock.core import Data


def setup_module():
    framework.clean()
    _fromFile_json = framework.create("test_fromFile.json")
    _fromFile_yaml = framework.create("test_fromFile.yaml")

    fromFileDict = {
        "Instagram": {
            "url": "https://www.instagram.com/{}",
            "urlMain": "https://www.instagram.com/",
            "errorType": "message",
            "errorMsg": "The link you followed may be broken",
        },
        "Twitter": {
            "url": "https://www.twitter.com/{}",
            "urlMain": "https://www.twitter.com/",
            "errorType": "message",
            "errorMsg": "page doesn’t exist",
        },
        "Facebook": {
            "url": "https://www.facebook.com/{}",
            "urlMain": "https://www.facebook.com/",
            "errorType": "status_code",
            "regexCheck": "^[a-zA-Z0-9]{4,49}(?<!.com|.org|.net)$",
        },
    }

    with open(_fromFile_json, "w") as f:
        f.write(json.dumps(fromFileDict))

    with open(_fromFile_yaml, "w") as f:
        f.write(yaml.dump(fromFileDict))


def teardown_module():
    framework.clean()


class TestData(TestCase):

    # Tests the read from file
    def test_fromFile(self):
        try:
            Data.fromFile(framework.temploc("test_fromFile.json"), t="json")
            Data.fromFile(framework.temploc("test_fromFile.yaml"), t="yaml")
        except Exception as err:
            self.fail(msg="Exception Occurred: " + str(err))

    # Check all keys
    def test_keys(self):
        data = Data.fromFile(framework.temploc("test_fromFile.json"), t="json")
        assert (
            "Instagram" in data.keys()
            and "Twitter" in data.keys()
            and "Facebook" in data.keys()
        )

    # Check all indices byindex
    def test_byindex(self):
        finding = ["Instagram", "Twitter", "Facebook"]
        found = []
        data = Data.fromFile(framework.temploc("test_fromFile.json"), t="json")
        for i in range(0, len(data)):
            k, v = data.byindex(i)
            for f in finding:
                if f == k:
                    found.append(f)
                    break

        # Let us check this error.
        assert len(found) == len(finding)
        for find in finding:
            if not find in found:
                self.fail(msg="Has not found %s" % find)
