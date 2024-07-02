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


class CommentPublish(object):
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
        'id': 'str',
        'mentions': 'list[str]',
        'text': 'str',
        'thread_anchor_keys': 'dict(str, str)',
        'thread_id': 'str',
        'visible_to': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'mentions': 'mentions',
        'text': 'text',
        'thread_anchor_keys': 'threadAnchorKeys',
        'thread_id': 'threadId',
        'visible_to': 'visibleTo'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CommentPublish - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._mentions = None
        self._text = None
        self._thread_anchor_keys = None
        self._thread_id = None
        self._visible_to = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('mentions'), kwargs.get('mentions', None))
        setattr(self, "_{}".format('text'), kwargs.get('text', None))
        setattr(self, "_{}".format('thread_anchor_keys'), kwargs.get('thread_anchor_keys', None))
        setattr(self, "_{}".format('thread_id'), kwargs.get('thread_id', None))
        setattr(self, "_{}".format('visible_to'), kwargs.get('visible_to', None))

    @property
    def id(self):
        """Gets the id of this CommentPublish.  # noqa: E501

          # noqa: E501

        :return: The id of this CommentPublish.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommentPublish.

          # noqa: E501

        :param id: The id of this CommentPublish.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mentions(self):
        """Gets the mentions of this CommentPublish.  # noqa: E501

          # noqa: E501

        :return: The mentions of this CommentPublish.  # noqa: E501
        :rtype: list[str]
        """
        return self._mentions

    @mentions.setter
    def mentions(self, mentions):
        """Sets the mentions of this CommentPublish.

          # noqa: E501

        :param mentions: The mentions of this CommentPublish.  # noqa: E501
        :type: list[str]
        """

        self._mentions = mentions

    @property
    def text(self):
        """Gets the text of this CommentPublish.  # noqa: E501

          # noqa: E501

        :return: The text of this CommentPublish.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CommentPublish.

          # noqa: E501

        :param text: The text of this CommentPublish.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def thread_anchor_keys(self):
        """Gets the thread_anchor_keys of this CommentPublish.  # noqa: E501

          # noqa: E501

        :return: The thread_anchor_keys of this CommentPublish.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._thread_anchor_keys

    @thread_anchor_keys.setter
    def thread_anchor_keys(self, thread_anchor_keys):
        """Sets the thread_anchor_keys of this CommentPublish.

          # noqa: E501

        :param thread_anchor_keys: The thread_anchor_keys of this CommentPublish.  # noqa: E501
        :type: dict(str, str)
        """

        self._thread_anchor_keys = thread_anchor_keys

    @property
    def thread_id(self):
        """Gets the thread_id of this CommentPublish.  # noqa: E501

          # noqa: E501

        :return: The thread_id of this CommentPublish.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this CommentPublish.

          # noqa: E501

        :param thread_id: The thread_id of this CommentPublish.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

    @property
    def visible_to(self):
        """Gets the visible_to of this CommentPublish.  # noqa: E501

          # noqa: E501

        :return: The visible_to of this CommentPublish.  # noqa: E501
        :rtype: list[str]
        """
        return self._visible_to

    @visible_to.setter
    def visible_to(self, visible_to):
        """Sets the visible_to of this CommentPublish.

          # noqa: E501

        :param visible_to: The visible_to of this CommentPublish.  # noqa: E501
        :type: list[str]
        """

        self._visible_to = visible_to

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
        if issubclass(CommentPublish, dict):
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
        if not isinstance(other, CommentPublish):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommentPublish):
            return True

        return self.to_dict() != other.to_dict()
