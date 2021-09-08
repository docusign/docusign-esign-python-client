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


class TemplateDocumentsResult(object):
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
        'template_documents': 'list[EnvelopeDocument]',
        'template_id': 'str'
    }

    attribute_map = {
        'template_documents': 'templateDocuments',
        'template_id': 'templateId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """TemplateDocumentsResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._template_documents = None
        self._template_id = None
        self.discriminator = None

        setattr(self, "_{}".format('template_documents'), kwargs.get('template_documents', None))
        setattr(self, "_{}".format('template_id'), kwargs.get('template_id', None))

    @property
    def template_documents(self):
        """Gets the template_documents of this TemplateDocumentsResult.  # noqa: E501

          # noqa: E501

        :return: The template_documents of this TemplateDocumentsResult.  # noqa: E501
        :rtype: list[EnvelopeDocument]
        """
        return self._template_documents

    @template_documents.setter
    def template_documents(self, template_documents):
        """Sets the template_documents of this TemplateDocumentsResult.

          # noqa: E501

        :param template_documents: The template_documents of this TemplateDocumentsResult.  # noqa: E501
        :type: list[EnvelopeDocument]
        """

        self._template_documents = template_documents

    @property
    def template_id(self):
        """Gets the template_id of this TemplateDocumentsResult.  # noqa: E501

        The unique identifier of the template. If this is not provided, DocuSign will generate a value.   # noqa: E501

        :return: The template_id of this TemplateDocumentsResult.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateDocumentsResult.

        The unique identifier of the template. If this is not provided, DocuSign will generate a value.   # noqa: E501

        :param template_id: The template_id of this TemplateDocumentsResult.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

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
        if issubclass(TemplateDocumentsResult, dict):
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
        if not isinstance(other, TemplateDocumentsResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateDocumentsResult):
            return True

        return self.to_dict() != other.to_dict()
