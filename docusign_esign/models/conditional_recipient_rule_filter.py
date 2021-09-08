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


class ConditionalRecipientRuleFilter(object):
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
        'operator': 'str',
        'recipient_id': 'str',
        'scope': 'str',
        'tab_id': 'str',
        'tab_label': 'str',
        'tab_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'recipient_id': 'recipientId',
        'scope': 'scope',
        'tab_id': 'tabId',
        'tab_label': 'tabLabel',
        'tab_type': 'tabType',
        'value': 'value'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConditionalRecipientRuleFilter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operator = None
        self._recipient_id = None
        self._scope = None
        self._tab_id = None
        self._tab_label = None
        self._tab_type = None
        self._value = None
        self.discriminator = None

        setattr(self, "_{}".format('operator'), kwargs.get('operator', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('scope'), kwargs.get('scope', None))
        setattr(self, "_{}".format('tab_id'), kwargs.get('tab_id', None))
        setattr(self, "_{}".format('tab_label'), kwargs.get('tab_label', None))
        setattr(self, "_{}".format('tab_type'), kwargs.get('tab_type', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))

    @property
    def operator(self):
        """Gets the operator of this ConditionalRecipientRuleFilter.  # noqa: E501

          # noqa: E501

        :return: The operator of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ConditionalRecipientRuleFilter.

          # noqa: E501

        :param operator: The operator of this ConditionalRecipientRuleFilter.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def recipient_id(self):
        """Gets the recipient_id of this ConditionalRecipientRuleFilter.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this ConditionalRecipientRuleFilter.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this ConditionalRecipientRuleFilter.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def scope(self):
        """Gets the scope of this ConditionalRecipientRuleFilter.  # noqa: E501

          # noqa: E501

        :return: The scope of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ConditionalRecipientRuleFilter.

          # noqa: E501

        :param scope: The scope of this ConditionalRecipientRuleFilter.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def tab_id(self):
        """Gets the tab_id of this ConditionalRecipientRuleFilter.  # noqa: E501

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :return: The tab_id of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        """Sets the tab_id of this ConditionalRecipientRuleFilter.

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :param tab_id: The tab_id of this ConditionalRecipientRuleFilter.  # noqa: E501
        :type: str
        """

        self._tab_id = tab_id

    @property
    def tab_label(self):
        """Gets the tab_label of this ConditionalRecipientRuleFilter.  # noqa: E501

        The label string associated with the tab.  # noqa: E501

        :return: The tab_label of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """Sets the tab_label of this ConditionalRecipientRuleFilter.

        The label string associated with the tab.  # noqa: E501

        :param tab_label: The tab_label of this ConditionalRecipientRuleFilter.  # noqa: E501
        :type: str
        """

        self._tab_label = tab_label

    @property
    def tab_type(self):
        """Gets the tab_type of this ConditionalRecipientRuleFilter.  # noqa: E501

          # noqa: E501

        :return: The tab_type of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._tab_type

    @tab_type.setter
    def tab_type(self, tab_type):
        """Sets the tab_type of this ConditionalRecipientRuleFilter.

          # noqa: E501

        :param tab_type: The tab_type of this ConditionalRecipientRuleFilter.  # noqa: E501
        :type: str
        """

        self._tab_type = tab_type

    @property
    def value(self):
        """Gets the value of this ConditionalRecipientRuleFilter.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this ConditionalRecipientRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConditionalRecipientRuleFilter.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this ConditionalRecipientRuleFilter.  # noqa: E501
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
        if issubclass(ConditionalRecipientRuleFilter, dict):
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
        if not isinstance(other, ConditionalRecipientRuleFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionalRecipientRuleFilter):
            return True

        return self.to_dict() != other.to_dict()
