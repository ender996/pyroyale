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
from pyroyale.models.chest_list import ChestList  # noqa: E501
from pyroyale.rest import ApiException


class TestChestList(unittest.TestCase):
    """ChestList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = ChestList()
        pass

    def testConstructorInitializers(self):
        model = ChestList(
            items='items'
        )

        assert model.items=='items'

    def testToDict(self):
        model = ChestList(
            items='items'
        )
        modelDict = model.to_dict()
        assert modelDict['items']=='items'

        model = ChestList(
            items=123
        )
        modelDict = model.to_dict()
        assert modelDict['items']==123

        model = ChestList(
            items={'foo': 'bar'}
        )
        modelDict = model.to_dict()
        assert modelDict['items']['foo']=='bar'

        model = ChestList(
            items=ChestList(items='items')
        )
        modelDict = model.to_dict()
        assert modelDict['items']['items']=='items'

        model = ChestList(
            items=[ChestList(items='items')]
        )
        modelDict = model.to_dict()
        assert modelDict['items'][0]['items']=='items'

    def testToString(self):
        model = ChestList('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = ChestList('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = ChestList('A')
        model_a2 = ChestList('A')
        model_b  = ChestList('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
