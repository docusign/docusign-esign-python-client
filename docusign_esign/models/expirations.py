# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Expirations(object):
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
        'expire_after': 'str',
        'expire_enabled': 'str',
        'expire_warn': 'str'
    }

    attribute_map = {
        'expire_after': 'expireAfter',
        'expire_enabled': 'expireEnabled',
        'expire_warn': 'expireWarn'
    }

    def __init__(self, expire_after=None, expire_enabled=None, expire_warn=None):  # noqa: E501
        """Expirations - a model defined in Swagger"""  # noqa: E501

        self._expire_after = None
        self._expire_enabled = None
        self._expire_warn = None
        self.discriminator = None

        if expire_after is not None:
            self.expire_after = expire_after
        if expire_enabled is not None:
            self.expire_enabled = expire_enabled
        if expire_warn is not None:
            self.expire_warn = expire_warn

    @property
    def expire_after(self):
        """Gets the expire_after of this Expirations.  # noqa: E501

        An integer that sets the number of days the envelope is active.  # noqa: E501

        :return: The expire_after of this Expirations.  # noqa: E501
        :rtype: str
        """
        return self._expire_after

    @expire_after.setter
    def expire_after(self, expire_after):
        """Sets the expire_after of this Expirations.

        An integer that sets the number of days the envelope is active.  # noqa: E501

        :param expire_after: The expire_after of this Expirations.  # noqa: E501
        :type: str
        """

        self._expire_after = expire_after

    @property
    def expire_enabled(self):
        """Gets the expire_enabled of this Expirations.  # noqa: E501

        When set to **true**, the envelope expires (is no longer available for signing) in the set number of days. If false, the account default setting is used. If the account does not have an expiration setting, the DocuSign default value of 120 days is used.  # noqa: E501

        :return: The expire_enabled of this Expirations.  # noqa: E501
        :rtype: str
        """
        return self._expire_enabled

    @expire_enabled.setter
    def expire_enabled(self, expire_enabled):
        """Sets the expire_enabled of this Expirations.

        When set to **true**, the envelope expires (is no longer available for signing) in the set number of days. If false, the account default setting is used. If the account does not have an expiration setting, the DocuSign default value of 120 days is used.  # noqa: E501

        :param expire_enabled: The expire_enabled of this Expirations.  # noqa: E501
        :type: str
        """

        self._expire_enabled = expire_enabled

    @property
    def expire_warn(self):
        """Gets the expire_warn of this Expirations.  # noqa: E501

        An integer that sets the number of days before envelope expiration that an expiration warning email is sent to the recipient. If set to 0 (zero), no warning email is sent.  # noqa: E501

        :return: The expire_warn of this Expirations.  # noqa: E501
        :rtype: str
        """
        return self._expire_warn

    @expire_warn.setter
    def expire_warn(self, expire_warn):
        """Sets the expire_warn of this Expirations.

        An integer that sets the number of days before envelope expiration that an expiration warning email is sent to the recipient. If set to 0 (zero), no warning email is sent.  # noqa: E501

        :param expire_warn: The expire_warn of this Expirations.  # noqa: E501
        :type: str
        """

        self._expire_warn = expire_warn

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
        if issubclass(Expirations, dict):
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
        if not isinstance(other, Expirations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
