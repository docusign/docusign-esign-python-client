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


class BulksendingCopyDocGenFormField(object):
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
        'name': 'str',
        'row_values': 'list[BulkSendingCopyDocGenFormFieldRowValue]',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'row_values': 'rowValues',
        'value': 'value'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulksendingCopyDocGenFormField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._row_values = None
        self._value = None
        self.discriminator = None

        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('row_values'), kwargs.get('row_values', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))

    @property
    def name(self):
        """Gets the name of this BulksendingCopyDocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The name of this BulksendingCopyDocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BulksendingCopyDocGenFormField.

          # noqa: E501

        :param name: The name of this BulksendingCopyDocGenFormField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def row_values(self):
        """Gets the row_values of this BulksendingCopyDocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The row_values of this BulksendingCopyDocGenFormField.  # noqa: E501
        :rtype: list[BulkSendingCopyDocGenFormFieldRowValue]
        """
        return self._row_values

    @row_values.setter
    def row_values(self, row_values):
        """Sets the row_values of this BulksendingCopyDocGenFormField.

          # noqa: E501

        :param row_values: The row_values of this BulksendingCopyDocGenFormField.  # noqa: E501
        :type: list[BulkSendingCopyDocGenFormFieldRowValue]
        """

        self._row_values = row_values

    @property
    def value(self):
        """Gets the value of this BulksendingCopyDocGenFormField.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this BulksendingCopyDocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BulksendingCopyDocGenFormField.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this BulksendingCopyDocGenFormField.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(BulksendingCopyDocGenFormField, dict):
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
        if not isinstance(other, BulksendingCopyDocGenFormField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulksendingCopyDocGenFormField):
            return True

        return self.to_dict() != other.to_dict()
