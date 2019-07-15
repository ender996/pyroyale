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
from pyroyale.models.battle_log_entry import BattleLogEntry  # noqa: E501
from pyroyale.rest import ApiException


class TestBattleLogEntry(unittest.TestCase):
    """BattleLogEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = pyroyale.models.battle_log_entry.BattleLogEntry()
        pass

    def testConstructorInitializers(self):
        model = pyroyale.models.battle_log_entry.BattleLogEntry(
            type='type',
            battle_time='battle_time',
            is_ladder_tournament='is_ladder_tournament',
            arena='arena',
            game_mode='game_mode',
            deck_selection='deck_selection',
            team='team',
            opponent='opponent'
        )

        assert model.type=='type'
        assert model.battle_time=='battle_time'
        assert model.is_ladder_tournament=='is_ladder_tournament'
        assert model.arena=='arena'
        assert model.game_mode=='game_mode'
        assert model.deck_selection=='deck_selection'
        assert model.team=='team'
        assert model.opponent=='opponent'

    def testToDict(self):
        model = pyroyale.models.battle_log_entry.BattleLogEntry(
            type=123,
            battle_time='battle_time',
        )

        modelDict = model.to_dict()

        assert modelDict['type']==123
        assert modelDict['battle_time']=='battle_time'

    def testToString(self):
        model = pyroyale.models.battle_log_entry.BattleLogEntry('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = pyroyale.models.battle_log_entry.BattleLogEntry('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = pyroyale.models.battle_log_entry.BattleLogEntry('A')
        model_a2 = pyroyale.models.battle_log_entry.BattleLogEntry('A')
        model_b  = pyroyale.models.battle_log_entry.BattleLogEntry('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()