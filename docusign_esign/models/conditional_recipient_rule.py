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


class ConditionalRecipientRule(object):
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
        'conditions': 'list[ConditionalRecipientRuleCondition]',
        'order': 'str',
        'recipient_group': 'RecipientGroup',
        'recipient_id': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'order': 'order',
        'recipient_group': 'recipientGroup',
        'recipient_id': 'recipientId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConditionalRecipientRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._conditions = None
        self._order = None
        self._recipient_group = None
        self._recipient_id = None
        self.discriminator = None

        setattr(self, "_{}".format('conditions'), kwargs.get('conditions', None))
        setattr(self, "_{}".format('order'), kwargs.get('order', None))
        setattr(self, "_{}".format('recipient_group'), kwargs.get('recipient_group', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))

    @property
    def conditions(self):
        """Gets the conditions of this ConditionalRecipientRule.  # noqa: E501

          # noqa: E501

        :return: The conditions of this ConditionalRecipientRule.  # noqa: E501
        :rtype: list[ConditionalRecipientRuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ConditionalRecipientRule.

          # noqa: E501

        :param conditions: The conditions of this ConditionalRecipientRule.  # noqa: E501
        :type: list[ConditionalRecipientRuleCondition]
        """

        self._conditions = conditions

    @property
    def order(self):
        """Gets the order of this ConditionalRecipientRule.  # noqa: E501

          # noqa: E501

        :return: The order of this ConditionalRecipientRule.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ConditionalRecipientRule.

          # noqa: E501

        :param order: The order of this ConditionalRecipientRule.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def recipient_group(self):
        """Gets the recipient_group of this ConditionalRecipientRule.  # noqa: E501

        A set of recipients that may be used for the envelope, depending on the `conditions` defined.  # noqa: E501

        :return: The recipient_group of this ConditionalRecipientRule.  # noqa: E501
        :rtype: RecipientGroup
        """
        return self._recipient_group

    @recipient_group.setter
    def recipient_group(self, recipient_group):
        """Sets the recipient_group of this ConditionalRecipientRule.

        A set of recipients that may be used for the envelope, depending on the `conditions` defined.  # noqa: E501

        :param recipient_group: The recipient_group of this ConditionalRecipientRule.  # noqa: E501
        :type: RecipientGroup
        """

        self._recipient_group = recipient_group

    @property
    def recipient_id(self):
        """Gets the recipient_id of this ConditionalRecipientRule.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this ConditionalRecipientRule.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this ConditionalRecipientRule.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this ConditionalRecipientRule.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

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
        if issubclass(ConditionalRecipientRule, dict):
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
        if not isinstance(other, ConditionalRecipientRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionalRecipientRule):
            return True

        return self.to_dict() != other.to_dict()
