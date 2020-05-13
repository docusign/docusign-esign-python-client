# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RecipientEvent(object):
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
        'include_documents': 'str',
        'recipient_event_status_code': 'str'
    }

    attribute_map = {
        'include_documents': 'includeDocuments',
        'recipient_event_status_code': 'recipientEventStatusCode'
    }

    def __init__(self, include_documents=None, recipient_event_status_code=None):  # noqa: E501
        """RecipientEvent - a model defined in Swagger"""  # noqa: E501

        self._include_documents = None
        self._recipient_event_status_code = None
        self.discriminator = None

        if include_documents is not None:
            self.include_documents = include_documents
        if recipient_event_status_code is not None:
            self.recipient_event_status_code = recipient_event_status_code

    @property
    def include_documents(self):
        """Gets the include_documents of this RecipientEvent.  # noqa: E501

        When set to **true**, the PDF documents are included in the message along with the updated XML.   # noqa: E501

        :return: The include_documents of this RecipientEvent.  # noqa: E501
        :rtype: str
        """
        return self._include_documents

    @include_documents.setter
    def include_documents(self, include_documents):
        """Sets the include_documents of this RecipientEvent.

        When set to **true**, the PDF documents are included in the message along with the updated XML.   # noqa: E501

        :param include_documents: The include_documents of this RecipientEvent.  # noqa: E501
        :type: str
        """

        self._include_documents = include_documents

    @property
    def recipient_event_status_code(self):
        """Gets the recipient_event_status_code of this RecipientEvent.  # noqa: E501

        The recipient status, this can be Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded.  # noqa: E501

        :return: The recipient_event_status_code of this RecipientEvent.  # noqa: E501
        :rtype: str
        """
        return self._recipient_event_status_code

    @recipient_event_status_code.setter
    def recipient_event_status_code(self, recipient_event_status_code):
        """Sets the recipient_event_status_code of this RecipientEvent.

        The recipient status, this can be Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded.  # noqa: E501

        :param recipient_event_status_code: The recipient_event_status_code of this RecipientEvent.  # noqa: E501
        :type: str
        """

        self._recipient_event_status_code = recipient_event_status_code

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
        if issubclass(RecipientEvent, dict):
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
        if not isinstance(other, RecipientEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
