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


class RecipientGroup(object):
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
        'group_message': 'str',
        'group_name': 'str',
        'recipients': 'list[RecipientOption]'
    }

    attribute_map = {
        'group_message': 'groupMessage',
        'group_name': 'groupName',
        'recipients': 'recipients'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_message = None
        self._group_name = None
        self._recipients = None
        self.discriminator = None

        setattr(self, "_{}".format('group_message'), kwargs.get('group_message', None))
        setattr(self, "_{}".format('group_name'), kwargs.get('group_name', None))
        setattr(self, "_{}".format('recipients'), kwargs.get('recipients', None))

    @property
    def group_message(self):
        """Gets the group_message of this RecipientGroup.  # noqa: E501

          # noqa: E501

        :return: The group_message of this RecipientGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_message

    @group_message.setter
    def group_message(self, group_message):
        """Sets the group_message of this RecipientGroup.

          # noqa: E501

        :param group_message: The group_message of this RecipientGroup.  # noqa: E501
        :type: str
        """

        self._group_message = group_message

    @property
    def group_name(self):
        """Gets the group_name of this RecipientGroup.  # noqa: E501

        The name of the group.  # noqa: E501

        :return: The group_name of this RecipientGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RecipientGroup.

        The name of the group.  # noqa: E501

        :param group_name: The group_name of this RecipientGroup.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def recipients(self):
        """Gets the recipients of this RecipientGroup.  # noqa: E501

        An array of powerform recipients.  # noqa: E501

        :return: The recipients of this RecipientGroup.  # noqa: E501
        :rtype: list[RecipientOption]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this RecipientGroup.

        An array of powerform recipients.  # noqa: E501

        :param recipients: The recipients of this RecipientGroup.  # noqa: E501
        :type: list[RecipientOption]
        """

        self._recipients = recipients

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
        if issubclass(RecipientGroup, dict):
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
        if not isinstance(other, RecipientGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientGroup):
            return True

        return self.to_dict() != other.to_dict()
