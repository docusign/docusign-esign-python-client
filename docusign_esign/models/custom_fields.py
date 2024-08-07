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


class CustomFields(object):
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
        'list_custom_fields': 'list[ListCustomField]',
        'text_custom_fields': 'list[TextCustomField]'
    }

    attribute_map = {
        'list_custom_fields': 'listCustomFields',
        'text_custom_fields': 'textCustomFields'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CustomFields - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._list_custom_fields = None
        self._text_custom_fields = None
        self.discriminator = None

        setattr(self, "_{}".format('list_custom_fields'), kwargs.get('list_custom_fields', None))
        setattr(self, "_{}".format('text_custom_fields'), kwargs.get('text_custom_fields', None))

    @property
    def list_custom_fields(self):
        """Gets the list_custom_fields of this CustomFields.  # noqa: E501

        An array of list custom fields.  # noqa: E501

        :return: The list_custom_fields of this CustomFields.  # noqa: E501
        :rtype: list[ListCustomField]
        """
        return self._list_custom_fields

    @list_custom_fields.setter
    def list_custom_fields(self, list_custom_fields):
        """Sets the list_custom_fields of this CustomFields.

        An array of list custom fields.  # noqa: E501

        :param list_custom_fields: The list_custom_fields of this CustomFields.  # noqa: E501
        :type: list[ListCustomField]
        """

        self._list_custom_fields = list_custom_fields

    @property
    def text_custom_fields(self):
        """Gets the text_custom_fields of this CustomFields.  # noqa: E501

        An array of text custom fields.  # noqa: E501

        :return: The text_custom_fields of this CustomFields.  # noqa: E501
        :rtype: list[TextCustomField]
        """
        return self._text_custom_fields

    @text_custom_fields.setter
    def text_custom_fields(self, text_custom_fields):
        """Sets the text_custom_fields of this CustomFields.

        An array of text custom fields.  # noqa: E501

        :param text_custom_fields: The text_custom_fields of this CustomFields.  # noqa: E501
        :type: list[TextCustomField]
        """

        self._text_custom_fields = text_custom_fields

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
        if issubclass(CustomFields, dict):
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
        if not isinstance(other, CustomFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomFields):
            return True

        return self.to_dict() != other.to_dict()
