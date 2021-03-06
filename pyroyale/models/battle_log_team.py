# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BattleLogTeam(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'tag': 'str',
        'name': 'str',
        'starting_trophies': 'int',
        'trophy_change': 'int',
        'crowns': 'int',
        'king_tower_hit_points': 'int',
        'princess_towers_hit_points': 'list[int]',
        'clan': 'ClanBase',
        'cards': 'list[Card]'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'starting_trophies': 'startingTrophies',
        'trophy_change': 'trophyChange',
        'crowns': 'crowns',
        'king_tower_hit_points': 'kingTowerHitPoints',
        'princess_towers_hit_points': 'princessTowersHitPoints',
        'clan': 'clan',
        'cards': 'cards'
    }

    def __init__(self, tag=None, name=None, starting_trophies=None, trophy_change=None, crowns=None, king_tower_hit_points=None, princess_towers_hit_points=None, clan=None, cards=None):  # noqa: E501
        """BattleLogTeam - a model defined in OpenAPI"""  # noqa: E501

        self._tag = None
        self._name = None
        self._starting_trophies = None
        self._trophy_change = None
        self._crowns = None
        self._king_tower_hit_points = None
        self._princess_towers_hit_points = None
        self._clan = None
        self._cards = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if starting_trophies is not None:
            self.starting_trophies = starting_trophies
        if trophy_change is not None:
            self.trophy_change = trophy_change
        if crowns is not None:
            self.crowns = crowns
        if king_tower_hit_points is not None:
            self.king_tower_hit_points = king_tower_hit_points
        if princess_towers_hit_points is not None:
            self.princess_towers_hit_points = princess_towers_hit_points
        if clan is not None:
            self.clan = clan
        if cards is not None:
            self.cards = cards

    @property
    def tag(self):
        """Gets the tag of this BattleLogTeam.  # noqa: E501


        :return: The tag of this BattleLogTeam.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BattleLogTeam.


        :param tag: The tag of this BattleLogTeam.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this BattleLogTeam.  # noqa: E501


        :return: The name of this BattleLogTeam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BattleLogTeam.


        :param name: The name of this BattleLogTeam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def starting_trophies(self):
        """Gets the starting_trophies of this BattleLogTeam.  # noqa: E501


        :return: The starting_trophies of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._starting_trophies

    @starting_trophies.setter
    def starting_trophies(self, starting_trophies):
        """Sets the starting_trophies of this BattleLogTeam.


        :param starting_trophies: The starting_trophies of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._starting_trophies = starting_trophies

    @property
    def trophy_change(self):
        """Gets the trophy_change of this BattleLogTeam.  # noqa: E501


        :return: The trophy_change of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._trophy_change

    @trophy_change.setter
    def trophy_change(self, trophy_change):
        """Sets the trophy_change of this BattleLogTeam.


        :param trophy_change: The trophy_change of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._trophy_change = trophy_change

    @property
    def crowns(self):
        """Gets the crowns of this BattleLogTeam.  # noqa: E501


        :return: The crowns of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._crowns

    @crowns.setter
    def crowns(self, crowns):
        """Sets the crowns of this BattleLogTeam.


        :param crowns: The crowns of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._crowns = crowns

    @property
    def king_tower_hit_points(self):
        """Gets the king_tower_hit_points of this BattleLogTeam.  # noqa: E501


        :return: The king_tower_hit_points of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._king_tower_hit_points

    @king_tower_hit_points.setter
    def king_tower_hit_points(self, king_tower_hit_points):
        """Sets the king_tower_hit_points of this BattleLogTeam.


        :param king_tower_hit_points: The king_tower_hit_points of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._king_tower_hit_points = king_tower_hit_points

    @property
    def princess_towers_hit_points(self):
        """Gets the princess_towers_hit_points of this BattleLogTeam.  # noqa: E501


        :return: The princess_towers_hit_points of this BattleLogTeam.  # noqa: E501
        :rtype: list[int]
        """
        return self._princess_towers_hit_points

    @princess_towers_hit_points.setter
    def princess_towers_hit_points(self, princess_towers_hit_points):
        """Sets the princess_towers_hit_points of this BattleLogTeam.


        :param princess_towers_hit_points: The princess_towers_hit_points of this BattleLogTeam.  # noqa: E501
        :type: list[int]
        """

        self._princess_towers_hit_points = princess_towers_hit_points

    @property
    def clan(self):
        """Gets the clan of this BattleLogTeam.  # noqa: E501


        :return: The clan of this BattleLogTeam.  # noqa: E501
        :rtype: ClanBase
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this BattleLogTeam.


        :param clan: The clan of this BattleLogTeam.  # noqa: E501
        :type: ClanBase
        """

        self._clan = clan

    @property
    def cards(self):
        """Gets the cards of this BattleLogTeam.  # noqa: E501


        :return: The cards of this BattleLogTeam.  # noqa: E501
        :rtype: list[Card]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Sets the cards of this BattleLogTeam.


        :param cards: The cards of this BattleLogTeam.  # noqa: E501
        :type: list[Card]
        """

        self._cards = cards

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BattleLogTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
