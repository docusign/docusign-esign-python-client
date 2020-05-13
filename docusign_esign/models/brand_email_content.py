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


class BrandEmailContent(object):
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
        'content': 'str',
        'email_content_type': 'str',
        'email_to_link': 'str',
        'link_text': 'str'
    }

    attribute_map = {
        'content': 'content',
        'email_content_type': 'emailContentType',
        'email_to_link': 'emailToLink',
        'link_text': 'linkText'
    }

    def __init__(self, content=None, email_content_type=None, email_to_link=None, link_text=None):  # noqa: E501
        """BrandEmailContent - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._email_content_type = None
        self._email_to_link = None
        self._link_text = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if email_content_type is not None:
            self.email_content_type = email_content_type
        if email_to_link is not None:
            self.email_to_link = email_to_link
        if link_text is not None:
            self.link_text = link_text

    @property
    def content(self):
        """Gets the content of this BrandEmailContent.  # noqa: E501

          # noqa: E501

        :return: The content of this BrandEmailContent.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this BrandEmailContent.

          # noqa: E501

        :param content: The content of this BrandEmailContent.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def email_content_type(self):
        """Gets the email_content_type of this BrandEmailContent.  # noqa: E501

          # noqa: E501

        :return: The email_content_type of this BrandEmailContent.  # noqa: E501
        :rtype: str
        """
        return self._email_content_type

    @email_content_type.setter
    def email_content_type(self, email_content_type):
        """Sets the email_content_type of this BrandEmailContent.

          # noqa: E501

        :param email_content_type: The email_content_type of this BrandEmailContent.  # noqa: E501
        :type: str
        """

        self._email_content_type = email_content_type

    @property
    def email_to_link(self):
        """Gets the email_to_link of this BrandEmailContent.  # noqa: E501

          # noqa: E501

        :return: The email_to_link of this BrandEmailContent.  # noqa: E501
        :rtype: str
        """
        return self._email_to_link

    @email_to_link.setter
    def email_to_link(self, email_to_link):
        """Sets the email_to_link of this BrandEmailContent.

          # noqa: E501

        :param email_to_link: The email_to_link of this BrandEmailContent.  # noqa: E501
        :type: str
        """

        self._email_to_link = email_to_link

    @property
    def link_text(self):
        """Gets the link_text of this BrandEmailContent.  # noqa: E501

          # noqa: E501

        :return: The link_text of this BrandEmailContent.  # noqa: E501
        :rtype: str
        """
        return self._link_text

    @link_text.setter
    def link_text(self, link_text):
        """Sets the link_text of this BrandEmailContent.

          # noqa: E501

        :param link_text: The link_text of this BrandEmailContent.  # noqa: E501
        :type: str
        """

        self._link_text = link_text

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
        if issubclass(BrandEmailContent, dict):
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
        if not isinstance(other, BrandEmailContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
