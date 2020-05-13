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


class ExternalFile(object):
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
        '_date': 'str',
        'id': 'str',
        'img': 'str',
        'name': 'str',
        'size': 'str',
        'supported': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'id': 'id',
        'img': 'img',
        'name': 'name',
        'size': 'size',
        'supported': 'supported',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, _date=None, id=None, img=None, name=None, size=None, supported=None, type=None, uri=None):  # noqa: E501
        """ExternalFile - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._id = None
        self._img = None
        self._name = None
        self._size = None
        self._supported = None
        self._type = None
        self._uri = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if id is not None:
            self.id = id
        if img is not None:
            self.img = img
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if supported is not None:
            self.supported = supported
        if type is not None:
            self.type = type
        if uri is not None:
            self.uri = uri

    @property
    def _date(self):
        """Gets the _date of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The _date of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ExternalFile.

          # noqa: E501

        :param _date: The _date of this ExternalFile.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def id(self):
        """Gets the id of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The id of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalFile.

          # noqa: E501

        :param id: The id of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def img(self):
        """Gets the img of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The img of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._img

    @img.setter
    def img(self, img):
        """Sets the img of this ExternalFile.

          # noqa: E501

        :param img: The img of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._img = img

    @property
    def name(self):
        """Gets the name of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The name of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalFile.

          # noqa: E501

        :param name: The name of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this ExternalFile.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The size of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ExternalFile.

        Reserved: TBD  # noqa: E501

        :param size: The size of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def supported(self):
        """Gets the supported of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The supported of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this ExternalFile.

          # noqa: E501

        :param supported: The supported of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._supported = supported

    @property
    def type(self):
        """Gets the type of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The type of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalFile.

          # noqa: E501

        :param type: The type of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this ExternalFile.  # noqa: E501

          # noqa: E501

        :return: The uri of this ExternalFile.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ExternalFile.

          # noqa: E501

        :param uri: The uri of this ExternalFile.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(ExternalFile, dict):
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
        if not isinstance(other, ExternalFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
