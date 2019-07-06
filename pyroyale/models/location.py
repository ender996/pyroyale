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


class Location(object):
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
        'id': 'int',
        'name': 'str',
        'is_country': 'bool',
        'country_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_country': 'isCountry',
        'country_code': 'countryCode'
    }

    def __init__(self, id=None, name=None, is_country=None, country_code=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_country = None
        self._country_code = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_country is not None:
            self.is_country = is_country
        if country_code is not None:
            self.country_code = country_code

    @property
    def id(self):
        """Gets the id of this Location.  # noqa: E501


        :return: The id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.


        :param id: The id of this Location.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Location.  # noqa: E501


        :return: The name of this Location.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Location.


        :param name: The name of this Location.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_country(self):
        """Gets the is_country of this Location.  # noqa: E501


        :return: The is_country of this Location.  # noqa: E501
        :rtype: bool
        """
        return self._is_country

    @is_country.setter
    def is_country(self, is_country):
        """Sets the is_country of this Location.


        :param is_country: The is_country of this Location.  # noqa: E501
        :type: bool
        """

        self._is_country = is_country

    @property
    def country_code(self):
        """Gets the country_code of this Location.  # noqa: E501


        :return: The country_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Location.


        :param country_code: The country_code of this Location.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

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
        if issubclass(Location, dict):
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
