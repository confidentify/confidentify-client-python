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


class DatasetListItem(object):
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
        'schema': 'DatasetSchema',
        'id': 'str',
        'href': 'str'
    }

    attribute_map = {
        'name': 'name',
        'schema': 'schema',
        'id': 'id',
        'href': 'href'
    }

    def __init__(self, name=None, schema=None, id=None, href=None, local_vars_configuration=None):  # noqa: E501
        """DatasetListItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._schema = None
        self._id = None
        self._href = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schema is not None:
            self.schema = schema
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href

    @property
    def name(self):
        """Gets the name of this DatasetListItem.  # noqa: E501

        The name of the dataset  # noqa: E501

        :return: The name of this DatasetListItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetListItem.

        The name of the dataset  # noqa: E501

        :param name: The name of this DatasetListItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this DatasetListItem.  # noqa: E501


        :return: The schema of this DatasetListItem.  # noqa: E501
        :rtype: DatasetSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DatasetListItem.


        :param schema: The schema of this DatasetListItem.  # noqa: E501
        :type: DatasetSchema
        """

        self._schema = schema

    @property
    def id(self):
        """Gets the id of this DatasetListItem.  # noqa: E501

        The unique ID of the dataset  # noqa: E501

        :return: The id of this DatasetListItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetListItem.

        The unique ID of the dataset  # noqa: E501

        :param id: The id of this DatasetListItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this DatasetListItem.  # noqa: E501

        The HTTP path to the dataset  # noqa: E501

        :return: The href of this DatasetListItem.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DatasetListItem.

        The HTTP path to the dataset  # noqa: E501

        :param href: The href of this DatasetListItem.  # noqa: E501
        :type: str
        """

        self._href = href

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
        if not isinstance(other, DatasetListItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetListItem):
            return True

        return self.to_dict() != other.to_dict()
