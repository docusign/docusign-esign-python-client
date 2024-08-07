# coding: utf-8

"""
    Docusign eSignature REST API

    The Docusign eSignature REST API provides you with a powerful, convenient, and simple Web services API for interacting with Docusign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class AuthenticationMethod(object):
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
        'authentication_type': 'str',
        'last_provider': 'str',
        'last_timestamp': 'str',
        'total_count': 'str'
    }

    attribute_map = {
        'authentication_type': 'authenticationType',
        'last_provider': 'lastProvider',
        'last_timestamp': 'lastTimestamp',
        'total_count': 'totalCount'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AuthenticationMethod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authentication_type = None
        self._last_provider = None
        self._last_timestamp = None
        self._total_count = None
        self.discriminator = None

        setattr(self, "_{}".format('authentication_type'), kwargs.get('authentication_type', None))
        setattr(self, "_{}".format('last_provider'), kwargs.get('last_provider', None))
        setattr(self, "_{}".format('last_timestamp'), kwargs.get('last_timestamp', None))
        setattr(self, "_{}".format('total_count'), kwargs.get('total_count', None))

    @property
    def authentication_type(self):
        """Gets the authentication_type of this AuthenticationMethod.  # noqa: E501

        Indicates the type of authentication. Valid values are: PhoneAuth, STAN, ISCheck, OFAC, AccessCode, AgeVerify, or SSOAuth.   # noqa: E501

        :return: The authentication_type of this AuthenticationMethod.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this AuthenticationMethod.

        Indicates the type of authentication. Valid values are: PhoneAuth, STAN, ISCheck, OFAC, AccessCode, AgeVerify, or SSOAuth.   # noqa: E501

        :param authentication_type: The authentication_type of this AuthenticationMethod.  # noqa: E501
        :type: str
        """

        self._authentication_type = authentication_type

    @property
    def last_provider(self):
        """Gets the last_provider of this AuthenticationMethod.  # noqa: E501

        The last provider that authenticated the user.   # noqa: E501

        :return: The last_provider of this AuthenticationMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_provider

    @last_provider.setter
    def last_provider(self, last_provider):
        """Sets the last_provider of this AuthenticationMethod.

        The last provider that authenticated the user.   # noqa: E501

        :param last_provider: The last_provider of this AuthenticationMethod.  # noqa: E501
        :type: str
        """

        self._last_provider = last_provider

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this AuthenticationMethod.  # noqa: E501

         The data and time the user last used the authentication method.   # noqa: E501

        :return: The last_timestamp of this AuthenticationMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this AuthenticationMethod.

         The data and time the user last used the authentication method.   # noqa: E501

        :param last_timestamp: The last_timestamp of this AuthenticationMethod.  # noqa: E501
        :type: str
        """

        self._last_timestamp = last_timestamp

    @property
    def total_count(self):
        """Gets the total_count of this AuthenticationMethod.  # noqa: E501

        The number of times the authentication method was used.   # noqa: E501

        :return: The total_count of this AuthenticationMethod.  # noqa: E501
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this AuthenticationMethod.

        The number of times the authentication method was used.   # noqa: E501

        :param total_count: The total_count of this AuthenticationMethod.  # noqa: E501
        :type: str
        """

        self._total_count = total_count

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
        if issubclass(AuthenticationMethod, dict):
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
        if not isinstance(other, AuthenticationMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticationMethod):
            return True

        return self.to_dict() != other.to_dict()
