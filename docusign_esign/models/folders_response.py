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


class FoldersResponse(object):
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
        'end_position': 'str',
        'envelopes': 'list[EnvelopeSummary]',
        'folders': 'list[Folder]',
        'next_uri': 'str',
        'previous_uri': 'str',
        'result_set_size': 'str',
        'start_position': 'str',
        'total_set_size': 'str'
    }

    attribute_map = {
        'end_position': 'endPosition',
        'envelopes': 'envelopes',
        'folders': 'folders',
        'next_uri': 'nextUri',
        'previous_uri': 'previousUri',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'total_set_size': 'totalSetSize'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """FoldersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_position = None
        self._envelopes = None
        self._folders = None
        self._next_uri = None
        self._previous_uri = None
        self._result_set_size = None
        self._start_position = None
        self._total_set_size = None
        self.discriminator = None

        setattr(self, "_{}".format('end_position'), kwargs.get('end_position', None))
        setattr(self, "_{}".format('envelopes'), kwargs.get('envelopes', None))
        setattr(self, "_{}".format('folders'), kwargs.get('folders', None))
        setattr(self, "_{}".format('next_uri'), kwargs.get('next_uri', None))
        setattr(self, "_{}".format('previous_uri'), kwargs.get('previous_uri', None))
        setattr(self, "_{}".format('result_set_size'), kwargs.get('result_set_size', None))
        setattr(self, "_{}".format('start_position'), kwargs.get('start_position', None))
        setattr(self, "_{}".format('total_set_size'), kwargs.get('total_set_size', None))

    @property
    def end_position(self):
        """Gets the end_position of this FoldersResponse.  # noqa: E501

        The last position in the result set.   # noqa: E501

        :return: The end_position of this FoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this FoldersResponse.

        The last position in the result set.   # noqa: E501

        :param end_position: The end_position of this FoldersResponse.  # noqa: E501
        :type: str
        """

        self._end_position = end_position

    @property
    def envelopes(self):
        """Gets the envelopes of this FoldersResponse.  # noqa: E501

          # noqa: E501

        :return: The envelopes of this FoldersResponse.  # noqa: E501
        :rtype: list[EnvelopeSummary]
        """
        return self._envelopes

    @envelopes.setter
    def envelopes(self, envelopes):
        """Sets the envelopes of this FoldersResponse.

          # noqa: E501

        :param envelopes: The envelopes of this FoldersResponse.  # noqa: E501
        :type: list[EnvelopeSummary]
        """

        self._envelopes = envelopes

    @property
    def folders(self):
        """Gets the folders of this FoldersResponse.  # noqa: E501

          # noqa: E501

        :return: The folders of this FoldersResponse.  # noqa: E501
        :rtype: list[Folder]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this FoldersResponse.

          # noqa: E501

        :param folders: The folders of this FoldersResponse.  # noqa: E501
        :type: list[Folder]
        """

        self._folders = folders

    @property
    def next_uri(self):
        """Gets the next_uri of this FoldersResponse.  # noqa: E501

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :return: The next_uri of this FoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this FoldersResponse.

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :param next_uri: The next_uri of this FoldersResponse.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """Gets the previous_uri of this FoldersResponse.  # noqa: E501

        The postal code for the billing address.  # noqa: E501

        :return: The previous_uri of this FoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """Sets the previous_uri of this FoldersResponse.

        The postal code for the billing address.  # noqa: E501

        :param previous_uri: The previous_uri of this FoldersResponse.  # noqa: E501
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """Gets the result_set_size of this FoldersResponse.  # noqa: E501

        The number of results returned in this response.   # noqa: E501

        :return: The result_set_size of this FoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this FoldersResponse.

        The number of results returned in this response.   # noqa: E501

        :param result_set_size: The result_set_size of this FoldersResponse.  # noqa: E501
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this FoldersResponse.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this FoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this FoldersResponse.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this FoldersResponse.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this FoldersResponse.  # noqa: E501

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :return: The total_set_size of this FoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this FoldersResponse.

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :param total_set_size: The total_set_size of this FoldersResponse.  # noqa: E501
        :type: str
        """

        self._total_set_size = total_set_size

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
        if issubclass(FoldersResponse, dict):
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
        if not isinstance(other, FoldersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FoldersResponse):
            return True

        return self.to_dict() != other.to_dict()
