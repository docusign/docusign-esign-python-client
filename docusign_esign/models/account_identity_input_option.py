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


class AccountIdentityInputOption(object):
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
        'is_required': 'bool',
        'option_name': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'is_required': 'isRequired',
        'option_name': 'optionName',
        'value_type': 'valueType'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AccountIdentityInputOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_required = None
        self._option_name = None
        self._value_type = None
        self.discriminator = None

        setattr(self, "_{}".format('is_required'), kwargs.get('is_required', None))
        setattr(self, "_{}".format('option_name'), kwargs.get('option_name', None))
        setattr(self, "_{}".format('value_type'), kwargs.get('value_type', None))

    @property
    def is_required(self):
        """Gets the is_required of this AccountIdentityInputOption.  # noqa: E501

          # noqa: E501

        :return: The is_required of this AccountIdentityInputOption.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this AccountIdentityInputOption.

          # noqa: E501

        :param is_required: The is_required of this AccountIdentityInputOption.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

    @property
    def option_name(self):
        """Gets the option_name of this AccountIdentityInputOption.  # noqa: E501

          # noqa: E501

        :return: The option_name of this AccountIdentityInputOption.  # noqa: E501
        :rtype: str
        """
        return self._option_name

    @option_name.setter
    def option_name(self, option_name):
        """Sets the option_name of this AccountIdentityInputOption.

          # noqa: E501

        :param option_name: The option_name of this AccountIdentityInputOption.  # noqa: E501
        :type: str
        """

        self._option_name = option_name

    @property
    def value_type(self):
        """Gets the value_type of this AccountIdentityInputOption.  # noqa: E501

          # noqa: E501

        :return: The value_type of this AccountIdentityInputOption.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this AccountIdentityInputOption.

          # noqa: E501

        :param value_type: The value_type of this AccountIdentityInputOption.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

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
        if issubclass(AccountIdentityInputOption, dict):
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
        if not isinstance(other, AccountIdentityInputOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountIdentityInputOption):
            return True

        return self.to_dict() != other.to_dict()
