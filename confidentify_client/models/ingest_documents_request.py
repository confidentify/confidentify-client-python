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


class IngestDocumentsRequest(object):
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
        'record_source': 'str',
        'records': 'list[IdentifyRequestRecord]'
    }

    attribute_map = {
        'record_source': 'record_source',
        'records': 'records'
    }

    def __init__(self, record_source=None, records=None, local_vars_configuration=None):  # noqa: E501
        """IngestDocumentsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._record_source = None
        self._records = None
        self.discriminator = None

        if record_source is not None:
            self.record_source = record_source
        if records is not None:
            self.records = records

    @property
    def record_source(self):
        """Gets the record_source of this IngestDocumentsRequest.  # noqa: E501

        The value to provide for any `meta_record_source` field in the dataset.  # noqa: E501

        :return: The record_source of this IngestDocumentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._record_source

    @record_source.setter
    def record_source(self, record_source):
        """Sets the record_source of this IngestDocumentsRequest.

        The value to provide for any `meta_record_source` field in the dataset.  # noqa: E501

        :param record_source: The record_source of this IngestDocumentsRequest.  # noqa: E501
        :type: str
        """

        self._record_source = record_source

    @property
    def records(self):
        """Gets the records of this IngestDocumentsRequest.  # noqa: E501


        :return: The records of this IngestDocumentsRequest.  # noqa: E501
        :rtype: list[IdentifyRequestRecord]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this IngestDocumentsRequest.


        :param records: The records of this IngestDocumentsRequest.  # noqa: E501
        :type: list[IdentifyRequestRecord]
        """

        self._records = records

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
        if not isinstance(other, IngestDocumentsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngestDocumentsRequest):
            return True

        return self.to_dict() != other.to_dict()
