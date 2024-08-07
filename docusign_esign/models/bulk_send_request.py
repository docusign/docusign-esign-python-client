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


class BulkSendRequest(object):
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
        'batch_name': 'str',
        'envelope_or_template_id': 'str'
    }

    attribute_map = {
        'batch_name': 'batchName',
        'envelope_or_template_id': 'envelopeOrTemplateId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batch_name = None
        self._envelope_or_template_id = None
        self.discriminator = None

        setattr(self, "_{}".format('batch_name'), kwargs.get('batch_name', None))
        setattr(self, "_{}".format('envelope_or_template_id'), kwargs.get('envelope_or_template_id', None))

    @property
    def batch_name(self):
        """Gets the batch_name of this BulkSendRequest.  # noqa: E501

          # noqa: E501

        :return: The batch_name of this BulkSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        """Sets the batch_name of this BulkSendRequest.

          # noqa: E501

        :param batch_name: The batch_name of this BulkSendRequest.  # noqa: E501
        :type: str
        """

        self._batch_name = batch_name

    @property
    def envelope_or_template_id(self):
        """Gets the envelope_or_template_id of this BulkSendRequest.  # noqa: E501

          # noqa: E501

        :return: The envelope_or_template_id of this BulkSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_or_template_id

    @envelope_or_template_id.setter
    def envelope_or_template_id(self, envelope_or_template_id):
        """Sets the envelope_or_template_id of this BulkSendRequest.

          # noqa: E501

        :param envelope_or_template_id: The envelope_or_template_id of this BulkSendRequest.  # noqa: E501
        :type: str
        """

        self._envelope_or_template_id = envelope_or_template_id

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
        if issubclass(BulkSendRequest, dict):
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
        if not isinstance(other, BulkSendRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendRequest):
            return True

        return self.to_dict() != other.to_dict()
