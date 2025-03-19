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


class DocGenFormField(object):
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
        'connected_object_details': 'ConnectedObjectDetails',
        'description': 'str',
        'fully_qualified_path': 'str',
        'label': 'str',
        'name': 'str',
        'options': 'list[DocGenFormFieldOption]',
        'order': 'str',
        'predefined_validation': 'str',
        'required': 'str',
        'row_values': 'list[DocGenFormFieldRowValue]',
        'type': 'str',
        'validation': 'DocGenFormFieldValidation',
        'value': 'str'
    }

    attribute_map = {
        'connected_object_details': 'connectedObjectDetails',
        'description': 'description',
        'fully_qualified_path': 'fullyQualifiedPath',
        'label': 'label',
        'name': 'name',
        'options': 'options',
        'order': 'order',
        'predefined_validation': 'predefinedValidation',
        'required': 'required',
        'row_values': 'rowValues',
        'type': 'type',
        'validation': 'validation',
        'value': 'value'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DocGenFormField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connected_object_details = None
        self._description = None
        self._fully_qualified_path = None
        self._label = None
        self._name = None
        self._options = None
        self._order = None
        self._predefined_validation = None
        self._required = None
        self._row_values = None
        self._type = None
        self._validation = None
        self._value = None
        self.discriminator = None

        setattr(self, "_{}".format('connected_object_details'), kwargs.get('connected_object_details', None))
        setattr(self, "_{}".format('description'), kwargs.get('description', None))
        setattr(self, "_{}".format('fully_qualified_path'), kwargs.get('fully_qualified_path', None))
        setattr(self, "_{}".format('label'), kwargs.get('label', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('options'), kwargs.get('options', None))
        setattr(self, "_{}".format('order'), kwargs.get('order', None))
        setattr(self, "_{}".format('predefined_validation'), kwargs.get('predefined_validation', None))
        setattr(self, "_{}".format('required'), kwargs.get('required', None))
        setattr(self, "_{}".format('row_values'), kwargs.get('row_values', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))
        setattr(self, "_{}".format('validation'), kwargs.get('validation', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))

    @property
    def connected_object_details(self):
        """Gets the connected_object_details of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The connected_object_details of this DocGenFormField.  # noqa: E501
        :rtype: ConnectedObjectDetails
        """
        return self._connected_object_details

    @connected_object_details.setter
    def connected_object_details(self, connected_object_details):
        """Sets the connected_object_details of this DocGenFormField.

          # noqa: E501

        :param connected_object_details: The connected_object_details of this DocGenFormField.  # noqa: E501
        :type: ConnectedObjectDetails
        """

        self._connected_object_details = connected_object_details

    @property
    def description(self):
        """Gets the description of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The description of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocGenFormField.

          # noqa: E501

        :param description: The description of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fully_qualified_path(self):
        """Gets the fully_qualified_path of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The fully_qualified_path of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._fully_qualified_path

    @fully_qualified_path.setter
    def fully_qualified_path(self, fully_qualified_path):
        """Sets the fully_qualified_path of this DocGenFormField.

          # noqa: E501

        :param fully_qualified_path: The fully_qualified_path of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._fully_qualified_path = fully_qualified_path

    @property
    def label(self):
        """Gets the label of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The label of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DocGenFormField.

          # noqa: E501

        :param label: The label of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The name of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocGenFormField.

          # noqa: E501

        :param name: The name of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The options of this DocGenFormField.  # noqa: E501
        :rtype: list[DocGenFormFieldOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DocGenFormField.

          # noqa: E501

        :param options: The options of this DocGenFormField.  # noqa: E501
        :type: list[DocGenFormFieldOption]
        """

        self._options = options

    @property
    def order(self):
        """Gets the order of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The order of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DocGenFormField.

          # noqa: E501

        :param order: The order of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def predefined_validation(self):
        """Gets the predefined_validation of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The predefined_validation of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._predefined_validation

    @predefined_validation.setter
    def predefined_validation(self, predefined_validation):
        """Sets the predefined_validation of this DocGenFormField.

          # noqa: E501

        :param predefined_validation: The predefined_validation of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._predefined_validation = predefined_validation

    @property
    def required(self):
        """Gets the required of this DocGenFormField.  # noqa: E501

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :return: The required of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DocGenFormField.

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :param required: The required of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def row_values(self):
        """Gets the row_values of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The row_values of this DocGenFormField.  # noqa: E501
        :rtype: list[DocGenFormFieldRowValue]
        """
        return self._row_values

    @row_values.setter
    def row_values(self, row_values):
        """Sets the row_values of this DocGenFormField.

          # noqa: E501

        :param row_values: The row_values of this DocGenFormField.  # noqa: E501
        :type: list[DocGenFormFieldRowValue]
        """

        self._row_values = row_values

    @property
    def type(self):
        """Gets the type of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The type of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocGenFormField.

          # noqa: E501

        :param type: The type of this DocGenFormField.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def validation(self):
        """Gets the validation of this DocGenFormField.  # noqa: E501

          # noqa: E501

        :return: The validation of this DocGenFormField.  # noqa: E501
        :rtype: DocGenFormFieldValidation
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this DocGenFormField.

          # noqa: E501

        :param validation: The validation of this DocGenFormField.  # noqa: E501
        :type: DocGenFormFieldValidation
        """

        self._validation = validation

    @property
    def value(self):
        """Gets the value of this DocGenFormField.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this DocGenFormField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DocGenFormField.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this DocGenFormField.  # noqa: E501
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
        if issubclass(DocGenFormField, dict):
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
        if not isinstance(other, DocGenFormField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocGenFormField):
            return True

        return self.to_dict() != other.to_dict()
