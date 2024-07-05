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


class LockRequest(object):
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
        'lock_duration_in_seconds': 'str',
        'locked_by_app': 'str',
        'lock_type': 'str',
        'template_password': 'str',
        'use_scratch_pad': 'str'
    }

    attribute_map = {
        'lock_duration_in_seconds': 'lockDurationInSeconds',
        'locked_by_app': 'lockedByApp',
        'lock_type': 'lockType',
        'template_password': 'templatePassword',
        'use_scratch_pad': 'useScratchPad'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """LockRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lock_duration_in_seconds = None
        self._locked_by_app = None
        self._lock_type = None
        self._template_password = None
        self._use_scratch_pad = None
        self.discriminator = None

        setattr(self, "_{}".format('lock_duration_in_seconds'), kwargs.get('lock_duration_in_seconds', None))
        setattr(self, "_{}".format('locked_by_app'), kwargs.get('locked_by_app', None))
        setattr(self, "_{}".format('lock_type'), kwargs.get('lock_type', None))
        setattr(self, "_{}".format('template_password'), kwargs.get('template_password', None))
        setattr(self, "_{}".format('use_scratch_pad'), kwargs.get('use_scratch_pad', None))

    @property
    def lock_duration_in_seconds(self):
        """Gets the lock_duration_in_seconds of this LockRequest.  # noqa: E501

        The number of seconds to lock the envelope for editing.  Must be greater than 0 seconds.  # noqa: E501

        :return: The lock_duration_in_seconds of this LockRequest.  # noqa: E501
        :rtype: str
        """
        return self._lock_duration_in_seconds

    @lock_duration_in_seconds.setter
    def lock_duration_in_seconds(self, lock_duration_in_seconds):
        """Sets the lock_duration_in_seconds of this LockRequest.

        The number of seconds to lock the envelope for editing.  Must be greater than 0 seconds.  # noqa: E501

        :param lock_duration_in_seconds: The lock_duration_in_seconds of this LockRequest.  # noqa: E501
        :type: str
        """

        self._lock_duration_in_seconds = lock_duration_in_seconds

    @property
    def locked_by_app(self):
        """Gets the locked_by_app of this LockRequest.  # noqa: E501

        A friendly name of the application used to lock the envelope.  Will be used in error messages to the user when lock conflicts occur.  # noqa: E501

        :return: The locked_by_app of this LockRequest.  # noqa: E501
        :rtype: str
        """
        return self._locked_by_app

    @locked_by_app.setter
    def locked_by_app(self, locked_by_app):
        """Sets the locked_by_app of this LockRequest.

        A friendly name of the application used to lock the envelope.  Will be used in error messages to the user when lock conflicts occur.  # noqa: E501

        :param locked_by_app: The locked_by_app of this LockRequest.  # noqa: E501
        :type: str
        """

        self._locked_by_app = locked_by_app

    @property
    def lock_type(self):
        """Gets the lock_type of this LockRequest.  # noqa: E501

        The type of envelope lock.  Currently \"edit\" is the only supported type.  # noqa: E501

        :return: The lock_type of this LockRequest.  # noqa: E501
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """Sets the lock_type of this LockRequest.

        The type of envelope lock.  Currently \"edit\" is the only supported type.  # noqa: E501

        :param lock_type: The lock_type of this LockRequest.  # noqa: E501
        :type: str
        """

        self._lock_type = lock_type

    @property
    def template_password(self):
        """Gets the template_password of this LockRequest.  # noqa: E501

          # noqa: E501

        :return: The template_password of this LockRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_password

    @template_password.setter
    def template_password(self, template_password):
        """Sets the template_password of this LockRequest.

          # noqa: E501

        :param template_password: The template_password of this LockRequest.  # noqa: E501
        :type: str
        """

        self._template_password = template_password

    @property
    def use_scratch_pad(self):
        """Gets the use_scratch_pad of this LockRequest.  # noqa: E501

        Reserved for future use.  Indicates whether a scratchpad is used for editing information.    # noqa: E501

        :return: The use_scratch_pad of this LockRequest.  # noqa: E501
        :rtype: str
        """
        return self._use_scratch_pad

    @use_scratch_pad.setter
    def use_scratch_pad(self, use_scratch_pad):
        """Sets the use_scratch_pad of this LockRequest.

        Reserved for future use.  Indicates whether a scratchpad is used for editing information.    # noqa: E501

        :param use_scratch_pad: The use_scratch_pad of this LockRequest.  # noqa: E501
        :type: str
        """

        self._use_scratch_pad = use_scratch_pad

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
        if issubclass(LockRequest, dict):
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
        if not isinstance(other, LockRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LockRequest):
            return True

        return self.to_dict() != other.to_dict()
