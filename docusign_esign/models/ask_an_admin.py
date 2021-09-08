# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class AskAnAdmin(object):
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
        'email': 'str',
        'message': 'str',
        'name': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'email',
        'message': 'message',
        'name': 'name',
        'phone': 'phone'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AskAnAdmin - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._message = None
        self._name = None
        self._phone = None
        self.discriminator = None

        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('message'), kwargs.get('message', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('phone'), kwargs.get('phone', None))

    @property
    def email(self):
        """Gets the email of this AskAnAdmin.  # noqa: E501

          # noqa: E501

        :return: The email of this AskAnAdmin.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AskAnAdmin.

          # noqa: E501

        :param email: The email of this AskAnAdmin.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def message(self):
        """Gets the message of this AskAnAdmin.  # noqa: E501

          # noqa: E501

        :return: The message of this AskAnAdmin.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AskAnAdmin.

          # noqa: E501

        :param message: The message of this AskAnAdmin.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this AskAnAdmin.  # noqa: E501

          # noqa: E501

        :return: The name of this AskAnAdmin.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AskAnAdmin.

          # noqa: E501

        :param name: The name of this AskAnAdmin.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this AskAnAdmin.  # noqa: E501

          # noqa: E501

        :return: The phone of this AskAnAdmin.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AskAnAdmin.

          # noqa: E501

        :param phone: The phone of this AskAnAdmin.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(AskAnAdmin, dict):
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
        if not isinstance(other, AskAnAdmin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AskAnAdmin):
            return True

        return self.to_dict() != other.to_dict()
