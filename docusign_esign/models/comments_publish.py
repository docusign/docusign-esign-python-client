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


class CommentsPublish(object):
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
        'comments_to_publish': 'list[CommentPublish]'
    }

    attribute_map = {
        'comments_to_publish': 'commentsToPublish'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CommentsPublish - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._comments_to_publish = None
        self.discriminator = None

        setattr(self, "_{}".format('comments_to_publish'), kwargs.get('comments_to_publish', None))

    @property
    def comments_to_publish(self):
        """Gets the comments_to_publish of this CommentsPublish.  # noqa: E501

          # noqa: E501

        :return: The comments_to_publish of this CommentsPublish.  # noqa: E501
        :rtype: list[CommentPublish]
        """
        return self._comments_to_publish

    @comments_to_publish.setter
    def comments_to_publish(self, comments_to_publish):
        """Sets the comments_to_publish of this CommentsPublish.

          # noqa: E501

        :param comments_to_publish: The comments_to_publish of this CommentsPublish.  # noqa: E501
        :type: list[CommentPublish]
        """

        self._comments_to_publish = comments_to_publish

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
        if issubclass(CommentsPublish, dict):
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
        if not isinstance(other, CommentsPublish):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommentsPublish):
            return True

        return self.to_dict() != other.to_dict()
