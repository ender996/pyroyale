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
from pyroyale.models.player_base import PlayerBase  # noqa: E501
from pyroyale.rest import ApiException


class TestPlayerBase(unittest.TestCase):
    """PlayerBase unit test stubs"""

    def testDefaults(self):
        model = PlayerBase()

    def testConstructorInitializers(self):
        model = PlayerBase(
            tag='tag',
            name='name',
            exp_level='exp_level',
            trophies='trophies',
            arena='arena',
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.exp_level=='exp_level'
        assert model.trophies=='trophies'
        assert model.arena=='arena'

    def testToDict(self):
        model = PlayerBase(
            tag={'foo':'bar'},
            name=PlayerBase(tag=123),
            exp_level=[PlayerBase(name='name')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']['foo']=='bar'
        assert modelDict['name']['tag']==123
        assert modelDict['exp_level'][0]['name']=='name'

    def testToString(self):
        model = PlayerBase('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = PlayerBase('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = PlayerBase('A')
        model_a2 = PlayerBase('A')
        model_b  = PlayerBase('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
