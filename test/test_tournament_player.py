# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.tournament_player import TournamentPlayer  # noqa: E501
from pyroyale.rest import ApiException


class TestTournamentPlayer(unittest.TestCase):
    """TournamentPlayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = TournamentPlayer()
        pass

    def testConstructorInitializers(self):
        model = TournamentPlayer(
            tag='tag',
            name='name',
            score='score',
            rank='rank',
            clan='clan',
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.score=='score'
        assert model.rank=='rank'
        assert model.clan=='clan'

    def testToDict(self):
        model = TournamentPlayer(
            score=TournamentPlayer(name=123),
            rank={'foo':'bar'},
            clan=[TournamentPlayer(name='name')]
        )

        modelDict = model.to_dict()

        assert modelDict['rank']['foo']=='bar'
        assert modelDict['score']['name']==123
        assert modelDict['clan'][0]['name']=='name'

    def testToString(self):
        model = TournamentPlayer('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = TournamentPlayer('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = TournamentPlayer('A')
        model_a2 = TournamentPlayer('A')
        model_b  = TournamentPlayer('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
