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


class AuthRequest(object):
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
        'username': 'str',
        'password': 'str',
        'refresh_token': 'str',
        'google_access_token': 'str',
        'expire_after_seconds': 'int',
        'service_grants': 'list[str]'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'refresh_token': 'refresh_token',
        'google_access_token': 'google_access_token',
        'expire_after_seconds': 'expire_after_seconds',
        'service_grants': 'service_grants'
    }

    def __init__(self, username=None, password=None, refresh_token=None, google_access_token=None, expire_after_seconds=300, service_grants=None, local_vars_configuration=None):  # noqa: E501
        """AuthRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._password = None
        self._refresh_token = None
        self._google_access_token = None
        self._expire_after_seconds = None
        self._service_grants = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if google_access_token is not None:
            self.google_access_token = google_access_token
        if expire_after_seconds is not None:
            self.expire_after_seconds = expire_after_seconds
        if service_grants is not None:
            self.service_grants = service_grants

    @property
    def username(self):
        """Gets the username of this AuthRequest.  # noqa: E501

        The username of the user, usually an email address.  # noqa: E501

        :return: The username of this AuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthRequest.

        The username of the user, usually an email address.  # noqa: E501

        :param username: The username of this AuthRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this AuthRequest.  # noqa: E501

        Password to use for authentication.  # noqa: E501

        :return: The password of this AuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AuthRequest.

        Password to use for authentication.  # noqa: E501

        :param password: The password of this AuthRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AuthRequest.  # noqa: E501

        A previously issued `refresh_token` value to provide for authentication.  # noqa: E501

        :return: The refresh_token of this AuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AuthRequest.

        A previously issued `refresh_token` value to provide for authentication.  # noqa: E501

        :param refresh_token: The refresh_token of this AuthRequest.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def google_access_token(self):
        """Gets the google_access_token of this AuthRequest.  # noqa: E501

        Access token issued by Google to use for authentication.  # noqa: E501

        :return: The google_access_token of this AuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._google_access_token

    @google_access_token.setter
    def google_access_token(self, google_access_token):
        """Sets the google_access_token of this AuthRequest.

        Access token issued by Google to use for authentication.  # noqa: E501

        :param google_access_token: The google_access_token of this AuthRequest.  # noqa: E501
        :type: str
        """

        self._google_access_token = google_access_token

    @property
    def expire_after_seconds(self):
        """Gets the expire_after_seconds of this AuthRequest.  # noqa: E501

        Optional property specifying the number of seconds that the returned token should be valid for.   # noqa: E501

        :return: The expire_after_seconds of this AuthRequest.  # noqa: E501
        :rtype: int
        """
        return self._expire_after_seconds

    @expire_after_seconds.setter
    def expire_after_seconds(self, expire_after_seconds):
        """Sets the expire_after_seconds of this AuthRequest.

        Optional property specifying the number of seconds that the returned token should be valid for.   # noqa: E501

        :param expire_after_seconds: The expire_after_seconds of this AuthRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                expire_after_seconds is not None and expire_after_seconds > 1200):  # noqa: E501
            raise ValueError("Invalid value for `expire_after_seconds`, must be a value less than or equal to `1200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                expire_after_seconds is not None and expire_after_seconds < 60):  # noqa: E501
            raise ValueError("Invalid value for `expire_after_seconds`, must be a value greater than or equal to `60`")  # noqa: E501

        self._expire_after_seconds = expire_after_seconds

    @property
    def service_grants(self):
        """Gets the service_grants of this AuthRequest.  # noqa: E501

        An optional array of service names to grant access to. Use this to generate access tokens with limited capabilities.   # noqa: E501

        :return: The service_grants of this AuthRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_grants

    @service_grants.setter
    def service_grants(self, service_grants):
        """Sets the service_grants of this AuthRequest.

        An optional array of service names to grant access to. Use this to generate access tokens with limited capabilities.   # noqa: E501

        :param service_grants: The service_grants of this AuthRequest.  # noqa: E501
        :type: list[str]
        """

        self._service_grants = service_grants

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
        if not isinstance(other, AuthRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthRequest):
            return True

        return self.to_dict() != other.to_dict()
