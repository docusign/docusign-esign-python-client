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


class SignatureUser(object):
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
        'is_default': 'str',
        'rights': 'str',
        'user_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'is_default': 'isDefault',
        'rights': 'rights',
        'user_id': 'userId',
        'user_name': 'userName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SignatureUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_default = None
        self._rights = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        setattr(self, "_{}".format('is_default'), kwargs.get('is_default', None))
        setattr(self, "_{}".format('rights'), kwargs.get('rights', None))
        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))
        setattr(self, "_{}".format('user_name'), kwargs.get('user_name', None))

    @property
    def is_default(self):
        """Gets the is_default of this SignatureUser.  # noqa: E501

          # noqa: E501

        :return: The is_default of this SignatureUser.  # noqa: E501
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SignatureUser.

          # noqa: E501

        :param is_default: The is_default of this SignatureUser.  # noqa: E501
        :type: str
        """

        self._is_default = is_default

    @property
    def rights(self):
        """Gets the rights of this SignatureUser.  # noqa: E501

          # noqa: E501

        :return: The rights of this SignatureUser.  # noqa: E501
        :rtype: str
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """Sets the rights of this SignatureUser.

          # noqa: E501

        :param rights: The rights of this SignatureUser.  # noqa: E501
        :type: str
        """

        self._rights = rights

    @property
    def user_id(self):
        """Gets the user_id of this SignatureUser.  # noqa: E501

          # noqa: E501

        :return: The user_id of this SignatureUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SignatureUser.

          # noqa: E501

        :param user_id: The user_id of this SignatureUser.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this SignatureUser.  # noqa: E501

          # noqa: E501

        :return: The user_name of this SignatureUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SignatureUser.

          # noqa: E501

        :param user_name: The user_name of this SignatureUser.  # noqa: E501
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
        if issubclass(SignatureUser, dict):
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
        if not isinstance(other, SignatureUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignatureUser):
            return True

        return self.to_dict() != other.to_dict()
