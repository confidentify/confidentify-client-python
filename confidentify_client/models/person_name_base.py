# coding: utf-8

"""
    Confidentify API

    Services that let you build confidence and identify matches in customer data. ## Features overview * Contact data processing services (tagged with `process`) which offer   validation and enrichment backed by inference and knowledge on complex   data types such as names, email addresses, phone numbers.  * Data matching and searching services (tagged with `matching`) that    allow you to identify duplicated data or matches against third party   contact data list.  * Dataset management services (tagged with `dataset`) that allow record storage and retrieval. ## Integrator notes: * Use the `/auth` endpoint to get an access token. Access tokens are temporary, so design the client the be capable of renewing it. * The APIs are rate-limited, so design the client to be capable of retrying with some delay upon HTTP 429 responses.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from confidentify_client.configuration import Configuration


class PersonNameBase(object):
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
        'given': 'str',
        'middle': 'str',
        'family': 'str',
        'suffix': 'str'
    }

    attribute_map = {
        'given': 'given',
        'middle': 'middle',
        'family': 'family',
        'suffix': 'suffix'
    }

    def __init__(self, given=None, middle=None, family=None, suffix=None, local_vars_configuration=None):  # noqa: E501
        """PersonNameBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._given = None
        self._middle = None
        self._family = None
        self._suffix = None
        self.discriminator = None

        if given is not None:
            self.given = given
        if middle is not None:
            self.middle = middle
        if family is not None:
            self.family = family
        if suffix is not None:
            self.suffix = suffix

    @property
    def given(self):
        """Gets the given of this PersonNameBase.  # noqa: E501


        :return: The given of this PersonNameBase.  # noqa: E501
        :rtype: str
        """
        return self._given

    @given.setter
    def given(self, given):
        """Sets the given of this PersonNameBase.


        :param given: The given of this PersonNameBase.  # noqa: E501
        :type: str
        """

        self._given = given

    @property
    def middle(self):
        """Gets the middle of this PersonNameBase.  # noqa: E501


        :return: The middle of this PersonNameBase.  # noqa: E501
        :rtype: str
        """
        return self._middle

    @middle.setter
    def middle(self, middle):
        """Sets the middle of this PersonNameBase.


        :param middle: The middle of this PersonNameBase.  # noqa: E501
        :type: str
        """

        self._middle = middle

    @property
    def family(self):
        """Gets the family of this PersonNameBase.  # noqa: E501


        :return: The family of this PersonNameBase.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this PersonNameBase.


        :param family: The family of this PersonNameBase.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def suffix(self):
        """Gets the suffix of this PersonNameBase.  # noqa: E501


        :return: The suffix of this PersonNameBase.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this PersonNameBase.


        :param suffix: The suffix of this PersonNameBase.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

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
        if not isinstance(other, PersonNameBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonNameBase):
            return True

        return self.to_dict() != other.to_dict()
