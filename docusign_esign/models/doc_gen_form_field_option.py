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


class DocGenFormFieldOption(object):
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
        'description': 'str',
        'label': 'str',
        'selected': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'label': 'label',
        'selected': 'selected',
        'value': 'value'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DocGenFormFieldOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._label = None
        self._selected = None
        self._value = None
        self.discriminator = None

        setattr(self, "_{}".format('description'), kwargs.get('description', None))
        setattr(self, "_{}".format('label'), kwargs.get('label', None))
        setattr(self, "_{}".format('selected'), kwargs.get('selected', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))

    @property
    def description(self):
        """Gets the description of this DocGenFormFieldOption.  # noqa: E501

          # noqa: E501

        :return: The description of this DocGenFormFieldOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocGenFormFieldOption.

          # noqa: E501

        :param description: The description of this DocGenFormFieldOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this DocGenFormFieldOption.  # noqa: E501

          # noqa: E501

        :return: The label of this DocGenFormFieldOption.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DocGenFormFieldOption.

          # noqa: E501

        :param label: The label of this DocGenFormFieldOption.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def selected(self):
        """Gets the selected of this DocGenFormFieldOption.  # noqa: E501

          # noqa: E501

        :return: The selected of this DocGenFormFieldOption.  # noqa: E501
        :rtype: str
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this DocGenFormFieldOption.

          # noqa: E501

        :param selected: The selected of this DocGenFormFieldOption.  # noqa: E501
        :type: str
        """

        self._selected = selected

    @property
    def value(self):
        """Gets the value of this DocGenFormFieldOption.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this DocGenFormFieldOption.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DocGenFormFieldOption.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this DocGenFormFieldOption.  # noqa: E501
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
        if issubclass(DocGenFormFieldOption, dict):
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
        if not isinstance(other, DocGenFormFieldOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocGenFormFieldOption):
            return True

        return self.to_dict() != other.to_dict()
