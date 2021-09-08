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


class ConsoleViewRequest(object):
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
        'envelope_id': 'str',
        'return_url': 'str'
    }

    attribute_map = {
        'envelope_id': 'envelopeId',
        'return_url': 'returnUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConsoleViewRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._envelope_id = None
        self._return_url = None
        self.discriminator = None

        setattr(self, "_{}".format('envelope_id'), kwargs.get('envelope_id', None))
        setattr(self, "_{}".format('return_url'), kwargs.get('return_url', None))

    @property
    def envelope_id(self):
        """Gets the envelope_id of this ConsoleViewRequest.  # noqa: E501

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :return: The envelope_id of this ConsoleViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """Sets the envelope_id of this ConsoleViewRequest.

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :param envelope_id: The envelope_id of this ConsoleViewRequest.  # noqa: E501
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def return_url(self):
        """Gets the return_url of this ConsoleViewRequest.  # noqa: E501

        The URL to be redirected to after the console view session has ended.  # noqa: E501

        :return: The return_url of this ConsoleViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this ConsoleViewRequest.

        The URL to be redirected to after the console view session has ended.  # noqa: E501

        :param return_url: The return_url of this ConsoleViewRequest.  # noqa: E501
        :type: str
        """

        self._return_url = return_url

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
        if issubclass(ConsoleViewRequest, dict):
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
        if not isinstance(other, ConsoleViewRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsoleViewRequest):
            return True

        return self.to_dict() != other.to_dict()
