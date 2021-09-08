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


class DocumentTemplate(object):
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
        'document_end_page': 'str',
        'document_id': 'str',
        'document_start_page': 'str',
        'error_details': 'ErrorDetails',
        'template_id': 'str'
    }

    attribute_map = {
        'document_end_page': 'documentEndPage',
        'document_id': 'documentId',
        'document_start_page': 'documentStartPage',
        'error_details': 'errorDetails',
        'template_id': 'templateId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DocumentTemplate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._document_end_page = None
        self._document_id = None
        self._document_start_page = None
        self._error_details = None
        self._template_id = None
        self.discriminator = None

        setattr(self, "_{}".format('document_end_page'), kwargs.get('document_end_page', None))
        setattr(self, "_{}".format('document_id'), kwargs.get('document_id', None))
        setattr(self, "_{}".format('document_start_page'), kwargs.get('document_start_page', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('template_id'), kwargs.get('template_id', None))

    @property
    def document_end_page(self):
        """Gets the document_end_page of this DocumentTemplate.  # noqa: E501

          # noqa: E501

        :return: The document_end_page of this DocumentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._document_end_page

    @document_end_page.setter
    def document_end_page(self, document_end_page):
        """Sets the document_end_page of this DocumentTemplate.

          # noqa: E501

        :param document_end_page: The document_end_page of this DocumentTemplate.  # noqa: E501
        :type: str
        """

        self._document_end_page = document_end_page

    @property
    def document_id(self):
        """Gets the document_id of this DocumentTemplate.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this DocumentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentTemplate.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this DocumentTemplate.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_start_page(self):
        """Gets the document_start_page of this DocumentTemplate.  # noqa: E501

          # noqa: E501

        :return: The document_start_page of this DocumentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._document_start_page

    @document_start_page.setter
    def document_start_page(self, document_start_page):
        """Sets the document_start_page of this DocumentTemplate.

          # noqa: E501

        :param document_start_page: The document_start_page of this DocumentTemplate.  # noqa: E501
        :type: str
        """

        self._document_start_page = document_start_page

    @property
    def error_details(self):
        """Gets the error_details of this DocumentTemplate.  # noqa: E501


        :return: The error_details of this DocumentTemplate.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this DocumentTemplate.


        :param error_details: The error_details of this DocumentTemplate.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def template_id(self):
        """Gets the template_id of this DocumentTemplate.  # noqa: E501

        The unique identifier of the template. If this is not provided, DocuSign will generate a value.   # noqa: E501

        :return: The template_id of this DocumentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this DocumentTemplate.

        The unique identifier of the template. If this is not provided, DocuSign will generate a value.   # noqa: E501

        :param template_id: The template_id of this DocumentTemplate.  # noqa: E501
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
        if issubclass(DocumentTemplate, dict):
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
        if not isinstance(other, DocumentTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentTemplate):
            return True

        return self.to_dict() != other.to_dict()
