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


class ExternalDocServiceErrorDetails(object):
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
        'authentication_url': 'str',
        'error_code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'authentication_url': 'authenticationUrl',
        'error_code': 'errorCode',
        'message': 'message'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ExternalDocServiceErrorDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authentication_url = None
        self._error_code = None
        self._message = None
        self.discriminator = None

        setattr(self, "_{}".format('authentication_url'), kwargs.get('authentication_url', None))
        setattr(self, "_{}".format('error_code'), kwargs.get('error_code', None))
        setattr(self, "_{}".format('message'), kwargs.get('message', None))

    @property
    def authentication_url(self):
        """Gets the authentication_url of this ExternalDocServiceErrorDetails.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The authentication_url of this ExternalDocServiceErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._authentication_url

    @authentication_url.setter
    def authentication_url(self, authentication_url):
        """Sets the authentication_url of this ExternalDocServiceErrorDetails.

        Reserved: TBD  # noqa: E501

        :param authentication_url: The authentication_url of this ExternalDocServiceErrorDetails.  # noqa: E501
        :type: str
        """

        self._authentication_url = authentication_url

    @property
    def error_code(self):
        """Gets the error_code of this ExternalDocServiceErrorDetails.  # noqa: E501

          # noqa: E501

        :return: The error_code of this ExternalDocServiceErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ExternalDocServiceErrorDetails.

          # noqa: E501

        :param error_code: The error_code of this ExternalDocServiceErrorDetails.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this ExternalDocServiceErrorDetails.  # noqa: E501

          # noqa: E501

        :return: The message of this ExternalDocServiceErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ExternalDocServiceErrorDetails.

          # noqa: E501

        :param message: The message of this ExternalDocServiceErrorDetails.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(ExternalDocServiceErrorDetails, dict):
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
        if not isinstance(other, ExternalDocServiceErrorDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalDocServiceErrorDetails):
            return True

        return self.to_dict() != other.to_dict()
