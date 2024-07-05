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


class MobileNotifierConfiguration(object):
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
        'device_id': 'str',
        'error_details': 'ErrorDetails',
        'platform': 'str'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'error_details': 'errorDetails',
        'platform': 'platform'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """MobileNotifierConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_id = None
        self._error_details = None
        self._platform = None
        self.discriminator = None

        setattr(self, "_{}".format('device_id'), kwargs.get('device_id', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('platform'), kwargs.get('platform', None))

    @property
    def device_id(self):
        """Gets the device_id of this MobileNotifierConfiguration.  # noqa: E501

          # noqa: E501

        :return: The device_id of this MobileNotifierConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this MobileNotifierConfiguration.

          # noqa: E501

        :param device_id: The device_id of this MobileNotifierConfiguration.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def error_details(self):
        """Gets the error_details of this MobileNotifierConfiguration.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this MobileNotifierConfiguration.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this MobileNotifierConfiguration.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this MobileNotifierConfiguration.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def platform(self):
        """Gets the platform of this MobileNotifierConfiguration.  # noqa: E501

          # noqa: E501

        :return: The platform of this MobileNotifierConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this MobileNotifierConfiguration.

          # noqa: E501

        :param platform: The platform of this MobileNotifierConfiguration.  # noqa: E501
        :type: str
        """

        self._platform = platform

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
        if issubclass(MobileNotifierConfiguration, dict):
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
        if not isinstance(other, MobileNotifierConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MobileNotifierConfiguration):
            return True

        return self.to_dict() != other.to_dict()
