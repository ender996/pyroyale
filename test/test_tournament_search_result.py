# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.tournament_search_result import TournamentSearchResult  # noqa: E501
from pyroyale.rest import ApiException


class TestTournamentSearchResult(unittest.TestCase):
    """TournamentSearchResult unit test stubs"""

    def testDefaults(self):
        model = TournamentSearchResult()

    def testConstructorInitializers(self):
        model = TournamentSearchResult(
            items='items',
            paging='paging'
        )

        assert model.items=='items'
        assert model.paging=='paging'

    def testToDict(self):
        model = TournamentSearchResult(
            items=TournamentSearchResult(items='items', paging=123),
            paging=[TournamentSearchResult(items={'foo': 'bar'})]
        )
        modelDict = model.to_dict()

        assert modelDict['items']['items']=='items'
        assert modelDict['items']['paging']==123
        assert modelDict['paging'][0]['items']['foo']=='bar'

    def testToString(self):
        model = TournamentSearchResult('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = TournamentSearchResult('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = TournamentSearchResult('A')
        model_a2 = TournamentSearchResult('A')
        model_b  = TournamentSearchResult('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
