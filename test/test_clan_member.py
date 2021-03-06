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
from pyroyale.models.clan_member import ClanMember  # noqa: E501
from pyroyale.rest import ApiException


class TestClanMember(unittest.TestCase):
    """ClanMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = ClanMember()
        pass

    def testConstructorInitializers(self):
        model = ClanMember(
            tag='tag',
            name='name',
            exp_level='exp_level',
            trophies='trophies',
            arena='arena',
            role='role',
            clan_rank='clan_rank',
            previous_clan_rank='previous_clan_rank',
            donations='donations',
            donations_received='donations_received',
            clan_chest_points='clan_chest_points',
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.exp_level=='exp_level'
        assert model.trophies=='trophies'
        assert model.arena=='arena'
        assert model.role=='role'
        assert model.clan_rank=='clan_rank'
        assert model.donations=='donations'
        assert model.donations_received=='donations_received'
        assert model.clan_chest_points=='clan_chest_points'

    def testToDict(self):
        model = ClanMember(
            tag={'foo':'bar'},
            name=ClanMember(tag=123),
            clan_chest_points=[ClanMember(name='name')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']['foo']=='bar'
        assert modelDict['name']['tag']==123
        assert modelDict['clan_chest_points'][0]['name']=='name'

    def testToString(self):
        model = ClanMember('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = ClanMember('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = ClanMember('A')
        model_a2 = ClanMember('A')
        model_b  = ClanMember('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
