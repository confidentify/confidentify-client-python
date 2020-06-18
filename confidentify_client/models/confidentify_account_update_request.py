# coding: utf-8

"""
    Confidentify API

    Services that let you build confidence and identify matches in customer data. ## Features overview * Contact data processing services (tagged with `process`) which offer   validation and enrichment backed by inference and knowledge on complex   data types such as names, email addresses, phone numbers.  * Data matching and searching services (tagged with `matching`) that    allow you to identify duplicated data or matches against third party   contact data list.  * Dataset management services (tagged with `dataset`) that allow record storage and retrieval. ## Integrator notes: * Use the `/auth` endpoint to get an access token. Access tokens are temporary, so design the client the be capable of renewing it. * The APIs are rate-limited, so design the client to be capable of retrying with some delay upon HTTP 429 responses.   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from confidentify_client.configuration import Configuration


class ConfidentifyAccountUpdateRequest(object):
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
        'name': 'str',
        'image_url': 'str',
        'website_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'image_url': 'image_url',
        'website_url': 'website_url'
    }

    def __init__(self, name=None, image_url=None, website_url=None, local_vars_configuration=None):  # noqa: E501
        """ConfidentifyAccountUpdateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._image_url = None
        self._website_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if image_url is not None:
            self.image_url = image_url
        if website_url is not None:
            self.website_url = website_url

    @property
    def name(self):
        """Gets the name of this ConfidentifyAccountUpdateRequest.  # noqa: E501

        The name of the account, typically a company name.   # noqa: E501

        :return: The name of this ConfidentifyAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfidentifyAccountUpdateRequest.

        The name of the account, typically a company name.   # noqa: E501

        :param name: The name of this ConfidentifyAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image_url(self):
        """Gets the image_url of this ConfidentifyAccountUpdateRequest.  # noqa: E501

        Optional URL to an image representing the account.  # noqa: E501

        :return: The image_url of this ConfidentifyAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ConfidentifyAccountUpdateRequest.

        Optional URL to an image representing the account.  # noqa: E501

        :param image_url: The image_url of this ConfidentifyAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def website_url(self):
        """Gets the website_url of this ConfidentifyAccountUpdateRequest.  # noqa: E501

        Optional URL to the account's website.  # noqa: E501

        :return: The website_url of this ConfidentifyAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this ConfidentifyAccountUpdateRequest.

        Optional URL to the account's website.  # noqa: E501

        :param website_url: The website_url of this ConfidentifyAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

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
        if not isinstance(other, ConfidentifyAccountUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfidentifyAccountUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()
