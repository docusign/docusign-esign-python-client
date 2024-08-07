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


class ConnectSalesforceField(object):
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
        'ds_attribute': 'str',
        'ds_link': 'str',
        'ds_node': 'str',
        'id': 'str',
        'sf_field': 'str',
        'sf_field_name': 'str',
        'sf_folder': 'str',
        'sf_locked_value': 'str'
    }

    attribute_map = {
        'ds_attribute': 'dsAttribute',
        'ds_link': 'dsLink',
        'ds_node': 'dsNode',
        'id': 'id',
        'sf_field': 'sfField',
        'sf_field_name': 'sfFieldName',
        'sf_folder': 'sfFolder',
        'sf_locked_value': 'sfLockedValue'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConnectSalesforceField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ds_attribute = None
        self._ds_link = None
        self._ds_node = None
        self._id = None
        self._sf_field = None
        self._sf_field_name = None
        self._sf_folder = None
        self._sf_locked_value = None
        self.discriminator = None

        setattr(self, "_{}".format('ds_attribute'), kwargs.get('ds_attribute', None))
        setattr(self, "_{}".format('ds_link'), kwargs.get('ds_link', None))
        setattr(self, "_{}".format('ds_node'), kwargs.get('ds_node', None))
        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('sf_field'), kwargs.get('sf_field', None))
        setattr(self, "_{}".format('sf_field_name'), kwargs.get('sf_field_name', None))
        setattr(self, "_{}".format('sf_folder'), kwargs.get('sf_folder', None))
        setattr(self, "_{}".format('sf_locked_value'), kwargs.get('sf_locked_value', None))

    @property
    def ds_attribute(self):
        """Gets the ds_attribute of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The ds_attribute of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._ds_attribute

    @ds_attribute.setter
    def ds_attribute(self, ds_attribute):
        """Sets the ds_attribute of this ConnectSalesforceField.

          # noqa: E501

        :param ds_attribute: The ds_attribute of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._ds_attribute = ds_attribute

    @property
    def ds_link(self):
        """Gets the ds_link of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The ds_link of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._ds_link

    @ds_link.setter
    def ds_link(self, ds_link):
        """Sets the ds_link of this ConnectSalesforceField.

          # noqa: E501

        :param ds_link: The ds_link of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._ds_link = ds_link

    @property
    def ds_node(self):
        """Gets the ds_node of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The ds_node of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._ds_node

    @ds_node.setter
    def ds_node(self, ds_node):
        """Sets the ds_node of this ConnectSalesforceField.

          # noqa: E501

        :param ds_node: The ds_node of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._ds_node = ds_node

    @property
    def id(self):
        """Gets the id of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The id of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectSalesforceField.

          # noqa: E501

        :param id: The id of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sf_field(self):
        """Gets the sf_field of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The sf_field of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._sf_field

    @sf_field.setter
    def sf_field(self, sf_field):
        """Sets the sf_field of this ConnectSalesforceField.

          # noqa: E501

        :param sf_field: The sf_field of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._sf_field = sf_field

    @property
    def sf_field_name(self):
        """Gets the sf_field_name of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The sf_field_name of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._sf_field_name

    @sf_field_name.setter
    def sf_field_name(self, sf_field_name):
        """Sets the sf_field_name of this ConnectSalesforceField.

          # noqa: E501

        :param sf_field_name: The sf_field_name of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._sf_field_name = sf_field_name

    @property
    def sf_folder(self):
        """Gets the sf_folder of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The sf_folder of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._sf_folder

    @sf_folder.setter
    def sf_folder(self, sf_folder):
        """Sets the sf_folder of this ConnectSalesforceField.

          # noqa: E501

        :param sf_folder: The sf_folder of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._sf_folder = sf_folder

    @property
    def sf_locked_value(self):
        """Gets the sf_locked_value of this ConnectSalesforceField.  # noqa: E501

          # noqa: E501

        :return: The sf_locked_value of this ConnectSalesforceField.  # noqa: E501
        :rtype: str
        """
        return self._sf_locked_value

    @sf_locked_value.setter
    def sf_locked_value(self, sf_locked_value):
        """Sets the sf_locked_value of this ConnectSalesforceField.

          # noqa: E501

        :param sf_locked_value: The sf_locked_value of this ConnectSalesforceField.  # noqa: E501
        :type: str
        """

        self._sf_locked_value = sf_locked_value

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
        if issubclass(ConnectSalesforceField, dict):
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
        if not isinstance(other, ConnectSalesforceField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectSalesforceField):
            return True

        return self.to_dict() != other.to_dict()
