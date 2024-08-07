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


class ConsentDetails(object):
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
        'consent_key': 'str',
        'delivery_method': 'str',
        'signer_consent_status': 'str'
    }

    attribute_map = {
        'consent_key': 'consentKey',
        'delivery_method': 'deliveryMethod',
        'signer_consent_status': 'signerConsentStatus'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConsentDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consent_key = None
        self._delivery_method = None
        self._signer_consent_status = None
        self.discriminator = None

        setattr(self, "_{}".format('consent_key'), kwargs.get('consent_key', None))
        setattr(self, "_{}".format('delivery_method'), kwargs.get('delivery_method', None))
        setattr(self, "_{}".format('signer_consent_status'), kwargs.get('signer_consent_status', None))

    @property
    def consent_key(self):
        """Gets the consent_key of this ConsentDetails.  # noqa: E501

          # noqa: E501

        :return: The consent_key of this ConsentDetails.  # noqa: E501
        :rtype: str
        """
        return self._consent_key

    @consent_key.setter
    def consent_key(self, consent_key):
        """Sets the consent_key of this ConsentDetails.

          # noqa: E501

        :param consent_key: The consent_key of this ConsentDetails.  # noqa: E501
        :type: str
        """

        self._consent_key = consent_key

    @property
    def delivery_method(self):
        """Gets the delivery_method of this ConsentDetails.  # noqa: E501

        Reserved: For DocuSign use only.  # noqa: E501

        :return: The delivery_method of this ConsentDetails.  # noqa: E501
        :rtype: str
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this ConsentDetails.

        Reserved: For DocuSign use only.  # noqa: E501

        :param delivery_method: The delivery_method of this ConsentDetails.  # noqa: E501
        :type: str
        """

        self._delivery_method = delivery_method

    @property
    def signer_consent_status(self):
        """Gets the signer_consent_status of this ConsentDetails.  # noqa: E501

          # noqa: E501

        :return: The signer_consent_status of this ConsentDetails.  # noqa: E501
        :rtype: str
        """
        return self._signer_consent_status

    @signer_consent_status.setter
    def signer_consent_status(self, signer_consent_status):
        """Sets the signer_consent_status of this ConsentDetails.

          # noqa: E501

        :param signer_consent_status: The signer_consent_status of this ConsentDetails.  # noqa: E501
        :type: str
        """

        self._signer_consent_status = signer_consent_status

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
        if issubclass(ConsentDetails, dict):
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
        if not isinstance(other, ConsentDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsentDetails):
            return True

        return self.to_dict() != other.to_dict()
