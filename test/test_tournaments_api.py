# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest
from unittest.mock import patch

import pyroyale
from pyroyale.api.tournaments_api import TournamentsApi  # noqa: E501
from pyroyale.rest import ApiException
from pyroyale.exceptions import ApiTypeError, ApiValueError

class TestTournamentsApi(unittest.TestCase):
    """TournamentsApi unit test stubs"""

    def setUp(self):
        self.api = TournamentsApi()  # noqa: E501

    @patch('urllib3.PoolManager.request')
    def test_get_tournament(self, mock_get):
        mock_get.return_value.status=200
        mock_get.return_value.data = """
            {
              "tag": "#AAAAAA",
              "type": "open",
              "status": "inProgress",
              "creatorTag": "#BBBBBB",
              "name": "fake tournament",
              "description": "fake tournament",
              "levelCap": 9,
              "firstPlaceCardPrize": 0,
              "capacity": 608,
              "maxCapacity": 1000,
              "preparationDuration": 3600,
              "duration": 86400,
              "createdTime": "20190718T093058.000Z",
              "startedTime": "20190718T103058.000Z",
              "membersList": [
                {
                  "tag": "#BBBBBB",
                  "name": "fakeplayer_B",
                  "score": 26,
                  "rank": 1,
                  "clan": {
                    "tag": "#CCCCCC",
                    "name": "fakeclan_C",
                    "badgeId": 16000168
                  }
                },
                {
                  "tag": "#DDDDDD",
                  "name": "fakeplayer_D",
                  "score": 25,
                  "rank": 2,
                  "clan": {
                    "tag": "#EEEEEE",
                    "name": "fakeclan_#",
                    "badgeId": 16000166
                  }
                }
              ],
              "gameMode": {
                "id": 72000027
              }
            }
        """.encode('utf-8')

        tournament = self.api.get_tournament('#AAAAAA')
        assert type(tournament.members_list) == list
        assert len(tournament.members_list) == 2
        assert tournament.tag=="#AAAAAA"
        assert tournament.type=="open"
        assert tournament.status=="inProgress"
        assert tournament.name=="fake tournament"
        assert tournament.description=="fake tournament"
        assert tournament.level_cap==9
        assert tournament.first_place_card_prize==0
        assert tournament.capacity==608
        assert tournament.max_capacity==1000
        assert tournament.preparation_duration==3600
        assert tournament.duration==86400
        assert tournament.created_time=="20190718T093058.000Z"
        assert tournament.game_mode.id==72000027


    @patch('urllib3.PoolManager.request')
    def test_get_tournament_fail(self, mock_get):

        mock_get.return_value.status=500

        try:
            cardList = self.api.get_tournament('fail')
            assert False

        except ApiException as e:
            assert True

    def test_get_tournament_param(self):
        try:
            cardList = self.api.get_tournament('fail', garbage='garbage')
            assert False

        except ApiTypeError as e:
            assert True

    @patch('urllib3.PoolManager.request')
    def test_search_tournaments(self, mock_get):
        mock_get.return_value.status=200
        mock_get.return_value.data = """
            {
              "items": [
                {
                  "tag": "#AAAAAA",
                  "type": "open",
                  "status": "inProgress",
                  "creatorTag": "#BBBBBB",
                  "name": "fake tournament",
                  "description": "fake tournament",
                  "levelCap": 9,
                  "firstPlaceCardPrize": 0,
                  "capacity": 608,
                  "maxCapacity": 1000,
                  "preparationDuration": 3600,
                  "duration": 86400,
                  "createdTime": "20190718T093058.000Z",
                  "gameMode": {
                    "id": 72000027
                  }
                }
              ],
              "paging": {
                "cursors": {
                  "after": "after"
                }
              }
            }
        """.encode('utf-8')

        tournaments = self.api.search_tournaments(name='a', limit='a', after='a', before='a')

        assert type(tournaments.items) == list
        assert tournaments.paging.cursors.after=='after'

        tournament = tournaments.items[0]

        assert tournament.tag=="#AAAAAA"
        assert tournament.type=="open"
        assert tournament.status=="inProgress"
        assert tournament.name=="fake tournament"
        assert tournament.description=="fake tournament"
        assert tournament.level_cap==9
        assert tournament.first_place_card_prize==0
        assert tournament.capacity==608
        assert tournament.max_capacity==1000
        assert tournament.preparation_duration==3600
        assert tournament.duration==86400
        assert tournament.created_time=="20190718T093058.000Z"
        assert tournament.game_mode.id==72000027


    @patch('urllib3.PoolManager.request')
    def test_search_tournaments_fail(self, mock_get):

        mock_get.return_value.status=500

        try:
            cardList = self.api.search_tournaments(name='aaa')
            assert False

        except ApiException as e:
            assert True

    def test_get_global_tournaments_bad_param(self):
        try:
            cardList = self.api.search_tournaments(garbage='garbage')
            assert False

        except ApiTypeError as e:
            assert True

    @patch('urllib3.PoolManager.request')
    def test_get_global_tournaments(self, mock_get):

        mock_get.return_value.status=200
        mock_get.return_value.data = """
            {
              "items": []
            }
        """.encode('utf-8')

        try:
            tournaments = self.api.get_global_tournaments()
            assert type(tournaments.items) == list
        except ApiException as e:
            assert False

    @patch('urllib3.PoolManager.request')
    def test_get_global_tournaments_fail(self, mock_get):

        mock_get.return_value.status=500

        try:
            cardList = self.api.get_global_tournaments()
            assert False

        except ApiException as e:
            print("Exception when calling TournamentsApi->get_global_tournaments(): %s\n" % e)
            assert True

    def test_get_global_tournament_param(self):
        try:
            cardList = self.api.get_global_tournaments(garbage='garbage')
            assert False

        except ApiTypeError as e:
            assert True

if __name__ == '__main__':
    unittest.main()
