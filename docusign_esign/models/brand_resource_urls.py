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


class BrandResourceUrls(object):
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
        'email': 'str',
        'sending': 'str',
        'signing': 'str',
        'signing_captive': 'str'
    }

    attribute_map = {
        'email': 'email',
        'sending': 'sending',
        'signing': 'signing',
        'signing_captive': 'signingCaptive'
    }

    def __init__(self, email=None, sending=None, signing=None, signing_captive=None):  # noqa: E501
        """BrandResourceUrls - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._sending = None
        self._signing = None
        self._signing_captive = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if sending is not None:
            self.sending = sending
        if signing is not None:
            self.signing = signing
        if signing_captive is not None:
            self.signing_captive = signing_captive

    @property
    def email(self):
        """Gets the email of this BrandResourceUrls.  # noqa: E501

          # noqa: E501

        :return: The email of this BrandResourceUrls.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BrandResourceUrls.

          # noqa: E501

        :param email: The email of this BrandResourceUrls.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def sending(self):
        """Gets the sending of this BrandResourceUrls.  # noqa: E501

          # noqa: E501

        :return: The sending of this BrandResourceUrls.  # noqa: E501
        :rtype: str
        """
        return self._sending

    @sending.setter
    def sending(self, sending):
        """Sets the sending of this BrandResourceUrls.

          # noqa: E501

        :param sending: The sending of this BrandResourceUrls.  # noqa: E501
        :type: str
        """

        self._sending = sending

    @property
    def signing(self):
        """Gets the signing of this BrandResourceUrls.  # noqa: E501

          # noqa: E501

        :return: The signing of this BrandResourceUrls.  # noqa: E501
        :rtype: str
        """
        return self._signing

    @signing.setter
    def signing(self, signing):
        """Sets the signing of this BrandResourceUrls.

          # noqa: E501

        :param signing: The signing of this BrandResourceUrls.  # noqa: E501
        :type: str
        """

        self._signing = signing

    @property
    def signing_captive(self):
        """Gets the signing_captive of this BrandResourceUrls.  # noqa: E501

          # noqa: E501

        :return: The signing_captive of this BrandResourceUrls.  # noqa: E501
        :rtype: str
        """
        return self._signing_captive

    @signing_captive.setter
    def signing_captive(self, signing_captive):
        """Sets the signing_captive of this BrandResourceUrls.

          # noqa: E501

        :param signing_captive: The signing_captive of this BrandResourceUrls.  # noqa: E501
        :type: str
        """

        self._signing_captive = signing_captive

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
        if issubclass(BrandResourceUrls, dict):
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
        if not isinstance(other, BrandResourceUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
