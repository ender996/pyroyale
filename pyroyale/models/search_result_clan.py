# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from pyroyale.models.clan_base import ClanBase  # noqa: F401,E501
from pyroyale.models.location import Location  # noqa: F401,E501


class SearchResultClan(ClanBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'clan_score': 'int',
        'required_trophies': 'int',
        'donations_per_week': 'int',
        'clan_chest_level': 'int',
        'clan_chest_max_level': 'int',
        'members': 'int',
        'location': 'Location'
    }

    attribute_map = {
        'type': 'type',
        'clan_score': 'clanScore',
        'required_trophies': 'requiredTrophies',
        'donations_per_week': 'donationsPerWeek',
        'clan_chest_level': 'clanChestLevel',
        'clan_chest_max_level': 'clanChestMaxLevel',
        'members': 'members',
        'location': 'location'
    }

    def __init__(self, type=None, clan_score=None, required_trophies=None, donations_per_week=None, clan_chest_level=None, clan_chest_max_level=None, members=None, location=None):  # noqa: E501
        """SearchResultClan - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._clan_score = None
        self._required_trophies = None
        self._donations_per_week = None
        self._clan_chest_level = None
        self._clan_chest_max_level = None
        self._members = None
        self._location = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if clan_score is not None:
            self.clan_score = clan_score
        if required_trophies is not None:
            self.required_trophies = required_trophies
        if donations_per_week is not None:
            self.donations_per_week = donations_per_week
        if clan_chest_level is not None:
            self.clan_chest_level = clan_chest_level
        if clan_chest_max_level is not None:
            self.clan_chest_max_level = clan_chest_max_level
        if members is not None:
            self.members = members
        if location is not None:
            self.location = location

    @property
    def type(self):
        """Gets the type of this SearchResultClan.  # noqa: E501


        :return: The type of this SearchResultClan.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchResultClan.


        :param type: The type of this SearchResultClan.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def clan_score(self):
        """Gets the clan_score of this SearchResultClan.  # noqa: E501


        :return: The clan_score of this SearchResultClan.  # noqa: E501
        :rtype: int
        """
        return self._clan_score

    @clan_score.setter
    def clan_score(self, clan_score):
        """Sets the clan_score of this SearchResultClan.


        :param clan_score: The clan_score of this SearchResultClan.  # noqa: E501
        :type: int
        """

        self._clan_score = clan_score

    @property
    def required_trophies(self):
        """Gets the required_trophies of this SearchResultClan.  # noqa: E501


        :return: The required_trophies of this SearchResultClan.  # noqa: E501
        :rtype: int
        """
        return self._required_trophies

    @required_trophies.setter
    def required_trophies(self, required_trophies):
        """Sets the required_trophies of this SearchResultClan.


        :param required_trophies: The required_trophies of this SearchResultClan.  # noqa: E501
        :type: int
        """

        self._required_trophies = required_trophies

    @property
    def donations_per_week(self):
        """Gets the donations_per_week of this SearchResultClan.  # noqa: E501


        :return: The donations_per_week of this SearchResultClan.  # noqa: E501
        :rtype: int
        """
        return self._donations_per_week

    @donations_per_week.setter
    def donations_per_week(self, donations_per_week):
        """Sets the donations_per_week of this SearchResultClan.


        :param donations_per_week: The donations_per_week of this SearchResultClan.  # noqa: E501
        :type: int
        """

        self._donations_per_week = donations_per_week

    @property
    def clan_chest_level(self):
        """Gets the clan_chest_level of this SearchResultClan.  # noqa: E501


        :return: The clan_chest_level of this SearchResultClan.  # noqa: E501
        :rtype: int
        """
        return self._clan_chest_level

    @clan_chest_level.setter
    def clan_chest_level(self, clan_chest_level):
        """Sets the clan_chest_level of this SearchResultClan.


        :param clan_chest_level: The clan_chest_level of this SearchResultClan.  # noqa: E501
        :type: int
        """

        self._clan_chest_level = clan_chest_level

    @property
    def clan_chest_max_level(self):
        """Gets the clan_chest_max_level of this SearchResultClan.  # noqa: E501


        :return: The clan_chest_max_level of this SearchResultClan.  # noqa: E501
        :rtype: int
        """
        return self._clan_chest_max_level

    @clan_chest_max_level.setter
    def clan_chest_max_level(self, clan_chest_max_level):
        """Sets the clan_chest_max_level of this SearchResultClan.


        :param clan_chest_max_level: The clan_chest_max_level of this SearchResultClan.  # noqa: E501
        :type: int
        """

        self._clan_chest_max_level = clan_chest_max_level

    @property
    def members(self):
        """Gets the members of this SearchResultClan.  # noqa: E501


        :return: The members of this SearchResultClan.  # noqa: E501
        :rtype: int
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this SearchResultClan.


        :param members: The members of this SearchResultClan.  # noqa: E501
        :type: int
        """

        self._members = members

    @property
    def location(self):
        """Gets the location of this SearchResultClan.  # noqa: E501


        :return: The location of this SearchResultClan.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SearchResultClan.


        :param location: The location of this SearchResultClan.  # noqa: E501
        :type: Location
        """

        self._location = location

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SearchResultClan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchResultClan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
