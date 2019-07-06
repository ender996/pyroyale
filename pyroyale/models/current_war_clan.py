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


class CurrentWarClan(object):
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
        'tag': 'str',
        'name': 'str',
        'badge_id': 'int',
        'clan_score': 'int',
        'participants': 'int',
        'battles_played': 'int',
        'wins': 'int',
        'crowns': 'int'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'badge_id': 'badgeId',
        'clan_score': 'clanScore',
        'participants': 'participants',
        'battles_played': 'battlesPlayed',
        'wins': 'wins',
        'crowns': 'crowns'
    }

    def __init__(self, tag=None, name=None, badge_id=None, clan_score=None, participants=None, battles_played=None, wins=None, crowns=None):  # noqa: E501
        """CurrentWarClan - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._name = None
        self._badge_id = None
        self._clan_score = None
        self._participants = None
        self._battles_played = None
        self._wins = None
        self._crowns = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if badge_id is not None:
            self.badge_id = badge_id
        if clan_score is not None:
            self.clan_score = clan_score
        if participants is not None:
            self.participants = participants
        if battles_played is not None:
            self.battles_played = battles_played
        if wins is not None:
            self.wins = wins
        if crowns is not None:
            self.crowns = crowns

    @property
    def tag(self):
        """Gets the tag of this CurrentWarClan.  # noqa: E501


        :return: The tag of this CurrentWarClan.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CurrentWarClan.


        :param tag: The tag of this CurrentWarClan.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this CurrentWarClan.  # noqa: E501


        :return: The name of this CurrentWarClan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrentWarClan.


        :param name: The name of this CurrentWarClan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def badge_id(self):
        """Gets the badge_id of this CurrentWarClan.  # noqa: E501


        :return: The badge_id of this CurrentWarClan.  # noqa: E501
        :rtype: int
        """
        return self._badge_id

    @badge_id.setter
    def badge_id(self, badge_id):
        """Sets the badge_id of this CurrentWarClan.


        :param badge_id: The badge_id of this CurrentWarClan.  # noqa: E501
        :type: int
        """

        self._badge_id = badge_id

    @property
    def clan_score(self):
        """Gets the clan_score of this CurrentWarClan.  # noqa: E501


        :return: The clan_score of this CurrentWarClan.  # noqa: E501
        :rtype: int
        """
        return self._clan_score

    @clan_score.setter
    def clan_score(self, clan_score):
        """Sets the clan_score of this CurrentWarClan.


        :param clan_score: The clan_score of this CurrentWarClan.  # noqa: E501
        :type: int
        """

        self._clan_score = clan_score

    @property
    def participants(self):
        """Gets the participants of this CurrentWarClan.  # noqa: E501


        :return: The participants of this CurrentWarClan.  # noqa: E501
        :rtype: int
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this CurrentWarClan.


        :param participants: The participants of this CurrentWarClan.  # noqa: E501
        :type: int
        """

        self._participants = participants

    @property
    def battles_played(self):
        """Gets the battles_played of this CurrentWarClan.  # noqa: E501


        :return: The battles_played of this CurrentWarClan.  # noqa: E501
        :rtype: int
        """
        return self._battles_played

    @battles_played.setter
    def battles_played(self, battles_played):
        """Sets the battles_played of this CurrentWarClan.


        :param battles_played: The battles_played of this CurrentWarClan.  # noqa: E501
        :type: int
        """

        self._battles_played = battles_played

    @property
    def wins(self):
        """Gets the wins of this CurrentWarClan.  # noqa: E501


        :return: The wins of this CurrentWarClan.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this CurrentWarClan.


        :param wins: The wins of this CurrentWarClan.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def crowns(self):
        """Gets the crowns of this CurrentWarClan.  # noqa: E501


        :return: The crowns of this CurrentWarClan.  # noqa: E501
        :rtype: int
        """
        return self._crowns

    @crowns.setter
    def crowns(self, crowns):
        """Sets the crowns of this CurrentWarClan.


        :param crowns: The crowns of this CurrentWarClan.  # noqa: E501
        :type: int
        """

        self._crowns = crowns

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
        if issubclass(CurrentWarClan, dict):
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
        if not isinstance(other, CurrentWarClan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
