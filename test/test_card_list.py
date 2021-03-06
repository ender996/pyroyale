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
from pyroyale.models.card_list import CardList  # noqa: E501
from pyroyale.rest import ApiException


class TestCardList(unittest.TestCase):
    """CardList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = CardList()
        pass

    def testConstructorInitializers(self):
        model = CardList(
            items='items'
        )

        assert model.items=='items'

    def testToDict(self):
        model = CardList(
            items='items'
        )
        modelDict = model.to_dict()
        assert modelDict['items']=='items'

        model = CardList(
            items=123
        )
        modelDict = model.to_dict()
        assert modelDict['items']==123

        model = CardList(
            items={'foo': 'bar'}
        )
        modelDict = model.to_dict()
        assert modelDict['items']['foo']=='bar'

        model = CardList(
            items=CardList(items='items')
        )
        modelDict = model.to_dict()
        assert modelDict['items']['items']=='items'

        model = CardList(
            items=[CardList(items='items')]
        )
        modelDict = model.to_dict()
        assert modelDict['items'][0]['items']=='items'

    def testToString(self):
        model = CardList('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = CardList('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = CardList('A')
        model_a2 = CardList('A')
        model_b  = CardList('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
