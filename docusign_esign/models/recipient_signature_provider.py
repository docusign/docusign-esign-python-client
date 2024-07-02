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


class RecipientSignatureProvider(object):
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
        'seal_documents_with_tabs_only': 'str',
        'seal_name': 'str',
        'signature_provider_name': 'str',
        'signature_provider_name_metadata': 'PropertyMetadata',
        'signature_provider_options': 'RecipientSignatureProviderOptions'
    }

    attribute_map = {
        'seal_documents_with_tabs_only': 'sealDocumentsWithTabsOnly',
        'seal_name': 'sealName',
        'signature_provider_name': 'signatureProviderName',
        'signature_provider_name_metadata': 'signatureProviderNameMetadata',
        'signature_provider_options': 'signatureProviderOptions'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientSignatureProvider - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._seal_documents_with_tabs_only = None
        self._seal_name = None
        self._signature_provider_name = None
        self._signature_provider_name_metadata = None
        self._signature_provider_options = None
        self.discriminator = None

        setattr(self, "_{}".format('seal_documents_with_tabs_only'), kwargs.get('seal_documents_with_tabs_only', None))
        setattr(self, "_{}".format('seal_name'), kwargs.get('seal_name', None))
        setattr(self, "_{}".format('signature_provider_name'), kwargs.get('signature_provider_name', None))
        setattr(self, "_{}".format('signature_provider_name_metadata'), kwargs.get('signature_provider_name_metadata', None))
        setattr(self, "_{}".format('signature_provider_options'), kwargs.get('signature_provider_options', None))

    @property
    def seal_documents_with_tabs_only(self):
        """Gets the seal_documents_with_tabs_only of this RecipientSignatureProvider.  # noqa: E501

          # noqa: E501

        :return: The seal_documents_with_tabs_only of this RecipientSignatureProvider.  # noqa: E501
        :rtype: str
        """
        return self._seal_documents_with_tabs_only

    @seal_documents_with_tabs_only.setter
    def seal_documents_with_tabs_only(self, seal_documents_with_tabs_only):
        """Sets the seal_documents_with_tabs_only of this RecipientSignatureProvider.

          # noqa: E501

        :param seal_documents_with_tabs_only: The seal_documents_with_tabs_only of this RecipientSignatureProvider.  # noqa: E501
        :type: str
        """

        self._seal_documents_with_tabs_only = seal_documents_with_tabs_only

    @property
    def seal_name(self):
        """Gets the seal_name of this RecipientSignatureProvider.  # noqa: E501

          # noqa: E501

        :return: The seal_name of this RecipientSignatureProvider.  # noqa: E501
        :rtype: str
        """
        return self._seal_name

    @seal_name.setter
    def seal_name(self, seal_name):
        """Sets the seal_name of this RecipientSignatureProvider.

          # noqa: E501

        :param seal_name: The seal_name of this RecipientSignatureProvider.  # noqa: E501
        :type: str
        """

        self._seal_name = seal_name

    @property
    def signature_provider_name(self):
        """Gets the signature_provider_name of this RecipientSignatureProvider.  # noqa: E501

          # noqa: E501

        :return: The signature_provider_name of this RecipientSignatureProvider.  # noqa: E501
        :rtype: str
        """
        return self._signature_provider_name

    @signature_provider_name.setter
    def signature_provider_name(self, signature_provider_name):
        """Sets the signature_provider_name of this RecipientSignatureProvider.

          # noqa: E501

        :param signature_provider_name: The signature_provider_name of this RecipientSignatureProvider.  # noqa: E501
        :type: str
        """

        self._signature_provider_name = signature_provider_name

    @property
    def signature_provider_name_metadata(self):
        """Gets the signature_provider_name_metadata of this RecipientSignatureProvider.  # noqa: E501

        Metadata that indicates whether the `signatureProviderName` property is editable.   # noqa: E501

        :return: The signature_provider_name_metadata of this RecipientSignatureProvider.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._signature_provider_name_metadata

    @signature_provider_name_metadata.setter
    def signature_provider_name_metadata(self, signature_provider_name_metadata):
        """Sets the signature_provider_name_metadata of this RecipientSignatureProvider.

        Metadata that indicates whether the `signatureProviderName` property is editable.   # noqa: E501

        :param signature_provider_name_metadata: The signature_provider_name_metadata of this RecipientSignatureProvider.  # noqa: E501
        :type: PropertyMetadata
        """

        self._signature_provider_name_metadata = signature_provider_name_metadata

    @property
    def signature_provider_options(self):
        """Gets the signature_provider_options of this RecipientSignatureProvider.  # noqa: E501

        Not applicable for this object.  # noqa: E501

        :return: The signature_provider_options of this RecipientSignatureProvider.  # noqa: E501
        :rtype: RecipientSignatureProviderOptions
        """
        return self._signature_provider_options

    @signature_provider_options.setter
    def signature_provider_options(self, signature_provider_options):
        """Sets the signature_provider_options of this RecipientSignatureProvider.

        Not applicable for this object.  # noqa: E501

        :param signature_provider_options: The signature_provider_options of this RecipientSignatureProvider.  # noqa: E501
        :type: RecipientSignatureProviderOptions
        """

        self._signature_provider_options = signature_provider_options

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
        if issubclass(RecipientSignatureProvider, dict):
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
        if not isinstance(other, RecipientSignatureProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientSignatureProvider):
            return True

        return self.to_dict() != other.to_dict()
