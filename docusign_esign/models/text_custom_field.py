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


class TextCustomField(object):
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
        'configuration_type': 'str',
        'error_details': 'ErrorDetails',
        'field_id': 'str',
        'name': 'str',
        'required': 'str',
        'show': 'str',
        'value': 'str'
    }

    attribute_map = {
        'configuration_type': 'configurationType',
        'error_details': 'errorDetails',
        'field_id': 'fieldId',
        'name': 'name',
        'required': 'required',
        'show': 'show',
        'value': 'value'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """TextCustomField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._configuration_type = None
        self._error_details = None
        self._field_id = None
        self._name = None
        self._required = None
        self._show = None
        self._value = None
        self.discriminator = None

        setattr(self, "_{}".format('configuration_type'), kwargs.get('configuration_type', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('field_id'), kwargs.get('field_id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('required'), kwargs.get('required', None))
        setattr(self, "_{}".format('show'), kwargs.get('show', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))

    @property
    def configuration_type(self):
        """Gets the configuration_type of this TextCustomField.  # noqa: E501

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :return: The configuration_type of this TextCustomField.  # noqa: E501
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this TextCustomField.

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :param configuration_type: The configuration_type of this TextCustomField.  # noqa: E501
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def error_details(self):
        """Gets the error_details of this TextCustomField.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this TextCustomField.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this TextCustomField.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this TextCustomField.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def field_id(self):
        """Gets the field_id of this TextCustomField.  # noqa: E501

        An ID used to specify a custom field.  # noqa: E501

        :return: The field_id of this TextCustomField.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this TextCustomField.

        An ID used to specify a custom field.  # noqa: E501

        :param field_id: The field_id of this TextCustomField.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def name(self):
        """Gets the name of this TextCustomField.  # noqa: E501

        The name of the custom field.  # noqa: E501

        :return: The name of this TextCustomField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TextCustomField.

        The name of the custom field.  # noqa: E501

        :param name: The name of this TextCustomField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this TextCustomField.  # noqa: E501

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :return: The required of this TextCustomField.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this TextCustomField.

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :param required: The required of this TextCustomField.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def show(self):
        """Gets the show of this TextCustomField.  # noqa: E501

        A boolean indicating if the value should be displayed.  # noqa: E501

        :return: The show of this TextCustomField.  # noqa: E501
        :rtype: str
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this TextCustomField.

        A boolean indicating if the value should be displayed.  # noqa: E501

        :param show: The show of this TextCustomField.  # noqa: E501
        :type: str
        """

        self._show = show

    @property
    def value(self):
        """Gets the value of this TextCustomField.  # noqa: E501

        The value of the custom field.  # noqa: E501

        :return: The value of this TextCustomField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TextCustomField.

        The value of the custom field.  # noqa: E501

        :param value: The value of this TextCustomField.  # noqa: E501
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
        if issubclass(TextCustomField, dict):
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
        if not isinstance(other, TextCustomField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextCustomField):
            return True

        return self.to_dict() != other.to_dict()
