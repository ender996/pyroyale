# coding: utf-8

# flake8: noqa

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from pyroyale.api.cards_api import CardsApi
from pyroyale.api.clans_api import ClansApi
from pyroyale.api.locations_api import LocationsApi
from pyroyale.api.players_api import PlayersApi
from pyroyale.api.tournaments_api import TournamentsApi
# import ApiClient
from pyroyale.api_client import ApiClient
from pyroyale.configuration import Configuration
# import models into sdk package
from pyroyale.models.arena import Arena
from pyroyale.models.battle_log_entry import BattleLogEntry
from pyroyale.models.battle_log_team import BattleLogTeam
from pyroyale.models.card import Card
from pyroyale.models.card_icon_urls import CardIconUrls
from pyroyale.models.card_list import CardList
from pyroyale.models.chest import Chest
from pyroyale.models.chest_list import ChestList
from pyroyale.models.clan import Clan
from pyroyale.models.clan_base import ClanBase
from pyroyale.models.clan_member import ClanMember
from pyroyale.models.clan_member_list import ClanMemberList
from pyroyale.models.clan_ranked import ClanRanked
from pyroyale.models.clan_ranking_list import ClanRankingList
from pyroyale.models.clan_search_result import ClanSearchResult
from pyroyale.models.clan_search_result_clan import ClanSearchResultClan
from pyroyale.models.clan_war_ranked import ClanWarRanked
from pyroyale.models.clan_wars_ranking_list import ClanWarsRankingList
from pyroyale.models.error import Error
from pyroyale.models.game_mode import GameMode
from pyroyale.models.location import Location
from pyroyale.models.location_list import LocationList
from pyroyale.models.player_achievement import PlayerAchievement
from pyroyale.models.player_badge import PlayerBadge
from pyroyale.models.player_base import PlayerBase
from pyroyale.models.player_detail import PlayerDetail
from pyroyale.models.player_league_statistics import PlayerLeagueStatistics
from pyroyale.models.player_ranked import PlayerRanked
from pyroyale.models.player_ranking_list import PlayerRankingList
from pyroyale.models.search_paging import SearchPaging
from pyroyale.models.search_paging_cursors import SearchPagingCursors
from pyroyale.models.season_statistics import SeasonStatistics
from pyroyale.models.tournament import Tournament
from pyroyale.models.tournament_detail import TournamentDetail
from pyroyale.models.tournament_player import TournamentPlayer
from pyroyale.models.tournament_search_result import TournamentSearchResult
from pyroyale.models.war import War
from pyroyale.models.war_clan import WarClan
from pyroyale.models.war_current import WarCurrent
from pyroyale.models.war_log import WarLog
from pyroyale.models.war_participant import WarParticipant
from pyroyale.models.war_standing import WarStanding
from pyroyale.models.war_standing_clan import WarStandingClan
