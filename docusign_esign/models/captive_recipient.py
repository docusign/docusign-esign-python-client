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


class CaptiveRecipient(object):
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
        'client_user_id': 'str',
        'email': 'str',
        'error_details': 'ErrorDetails',
        'user_name': 'str'
    }

    attribute_map = {
        'client_user_id': 'clientUserId',
        'email': 'email',
        'error_details': 'errorDetails',
        'user_name': 'userName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CaptiveRecipient - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_user_id = None
        self._email = None
        self._error_details = None
        self._user_name = None
        self.discriminator = None

        setattr(self, "_{}".format('client_user_id'), kwargs.get('client_user_id', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('user_name'), kwargs.get('user_name', None))

    @property
    def client_user_id(self):
        """Gets the client_user_id of this CaptiveRecipient.  # noqa: E501

        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters.   # noqa: E501

        :return: The client_user_id of this CaptiveRecipient.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this CaptiveRecipient.

        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters.   # noqa: E501

        :param client_user_id: The client_user_id of this CaptiveRecipient.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def email(self):
        """Gets the email of this CaptiveRecipient.  # noqa: E501

        Specifies the email address associated with the captive recipient.  # noqa: E501

        :return: The email of this CaptiveRecipient.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CaptiveRecipient.

        Specifies the email address associated with the captive recipient.  # noqa: E501

        :param email: The email of this CaptiveRecipient.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error_details(self):
        """Gets the error_details of this CaptiveRecipient.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this CaptiveRecipient.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this CaptiveRecipient.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this CaptiveRecipient.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def user_name(self):
        """Gets the user_name of this CaptiveRecipient.  # noqa: E501

        Specifies the user name associated with the captive recipient.  # noqa: E501

        :return: The user_name of this CaptiveRecipient.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CaptiveRecipient.

        Specifies the user name associated with the captive recipient.  # noqa: E501

        :param user_name: The user_name of this CaptiveRecipient.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(CaptiveRecipient, dict):
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
        if not isinstance(other, CaptiveRecipient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CaptiveRecipient):
            return True

        return self.to_dict() != other.to_dict()
