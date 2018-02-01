"""
@File: config
@Author: Ray
@Date: 2018-01-29 15:33:53
@Version: 1.0
"""
import json
import os
from ..lib.LogHandler import LogHandler
from ..lib import GetDictParam, CasesManager, CasesContainer


__all__ = [
    "CasesContainer",
    "CasesManager",
    "CASE_PATH",
    "TESTCASES_PATH",
    "REPORT_PATH",
    "HEADERS_TEMPLATE_PATH",
    "CONTENT_TEMPLATE_PATH"
]
# PATH


CASE_PATH = 'cases/'
TESTCASES_PATH = 'src/testcases/'
REPORT_PATH = 'src/report/'
HEADERS_TEMPLATE_PATH = 'src/template/header.txt'
CONTENT_TEMPLATE_PATH = 'src/template/content.txt'
DEBUG_INFO = 1


# Messages

# load testcases


class TestCaseLoader(GetDictParam, CasesManager):
    """ TestCase Loader"""
    __slots__ = "tags"

    if DEBUG_INFO is 1:
        logger = LogHandler(__name__)
    else:
        logger = LogHandler(__name__, level=30)

    def __init__(self):
        """ init class"""
        super(TestCaseLoader, self).__init__()
        self.files = os.listdir(CASE_PATH)
        self.data = {}
        self.tags = self.make_cases_info()

    def __repr__(self) -> str:
        """
            return repr obj
        :return:
        """
        return json.dumps(self.tags)
