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


class BulkProcessResult(object):
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
        'errors': 'list[BulkSendBatchError]',
        'list_id': 'str',
        'success': 'str'
    }

    attribute_map = {
        'errors': 'errors',
        'list_id': 'listId',
        'success': 'success'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkProcessResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._errors = None
        self._list_id = None
        self._success = None
        self.discriminator = None

        setattr(self, "_{}".format('errors'), kwargs.get('errors', None))
        setattr(self, "_{}".format('list_id'), kwargs.get('list_id', None))
        setattr(self, "_{}".format('success'), kwargs.get('success', None))

    @property
    def errors(self):
        """Gets the errors of this BulkProcessResult.  # noqa: E501

          # noqa: E501

        :return: The errors of this BulkProcessResult.  # noqa: E501
        :rtype: list[BulkSendBatchError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BulkProcessResult.

          # noqa: E501

        :param errors: The errors of this BulkProcessResult.  # noqa: E501
        :type: list[BulkSendBatchError]
        """

        self._errors = errors

    @property
    def list_id(self):
        """Gets the list_id of this BulkProcessResult.  # noqa: E501

          # noqa: E501

        :return: The list_id of this BulkProcessResult.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this BulkProcessResult.

          # noqa: E501

        :param list_id: The list_id of this BulkProcessResult.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def success(self):
        """Gets the success of this BulkProcessResult.  # noqa: E501

          # noqa: E501

        :return: The success of this BulkProcessResult.  # noqa: E501
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this BulkProcessResult.

          # noqa: E501

        :param success: The success of this BulkProcessResult.  # noqa: E501
        :type: str
        """

        self._success = success

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
        if issubclass(BulkProcessResult, dict):
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
        if not isinstance(other, BulkProcessResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkProcessResult):
            return True

        return self.to_dict() != other.to_dict()
