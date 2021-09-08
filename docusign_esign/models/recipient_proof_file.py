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


class RecipientProofFile(object):
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
        'has_identity_attempts': 'str',
        'is_in_proof_file': 'str'
    }

    attribute_map = {
        'has_identity_attempts': 'hasIdentityAttempts',
        'is_in_proof_file': 'isInProofFile'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientProofFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._has_identity_attempts = None
        self._is_in_proof_file = None
        self.discriminator = None

        setattr(self, "_{}".format('has_identity_attempts'), kwargs.get('has_identity_attempts', None))
        setattr(self, "_{}".format('is_in_proof_file'), kwargs.get('is_in_proof_file', None))

    @property
    def has_identity_attempts(self):
        """Gets the has_identity_attempts of this RecipientProofFile.  # noqa: E501

          # noqa: E501

        :return: The has_identity_attempts of this RecipientProofFile.  # noqa: E501
        :rtype: str
        """
        return self._has_identity_attempts

    @has_identity_attempts.setter
    def has_identity_attempts(self, has_identity_attempts):
        """Sets the has_identity_attempts of this RecipientProofFile.

          # noqa: E501

        :param has_identity_attempts: The has_identity_attempts of this RecipientProofFile.  # noqa: E501
        :type: str
        """

        self._has_identity_attempts = has_identity_attempts

    @property
    def is_in_proof_file(self):
        """Gets the is_in_proof_file of this RecipientProofFile.  # noqa: E501

          # noqa: E501

        :return: The is_in_proof_file of this RecipientProofFile.  # noqa: E501
        :rtype: str
        """
        return self._is_in_proof_file

    @is_in_proof_file.setter
    def is_in_proof_file(self, is_in_proof_file):
        """Sets the is_in_proof_file of this RecipientProofFile.

          # noqa: E501

        :param is_in_proof_file: The is_in_proof_file of this RecipientProofFile.  # noqa: E501
        :type: str
        """

        self._is_in_proof_file = is_in_proof_file

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
        if issubclass(RecipientProofFile, dict):
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
        if not isinstance(other, RecipientProofFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientProofFile):
            return True

        return self.to_dict() != other.to_dict()
