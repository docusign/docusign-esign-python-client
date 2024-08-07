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


class BccEmailArchiveHistoryList(object):
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
        'bcc_email_archive_history': 'list[BccEmailArchiveHistory]',
        'end_position': 'str',
        'next_uri': 'str',
        'previous_uri': 'str',
        'result_set_size': 'str',
        'start_position': 'str',
        'total_set_size': 'str'
    }

    attribute_map = {
        'bcc_email_archive_history': 'bccEmailArchiveHistory',
        'end_position': 'endPosition',
        'next_uri': 'nextUri',
        'previous_uri': 'previousUri',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'total_set_size': 'totalSetSize'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BccEmailArchiveHistoryList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bcc_email_archive_history = None
        self._end_position = None
        self._next_uri = None
        self._previous_uri = None
        self._result_set_size = None
        self._start_position = None
        self._total_set_size = None
        self.discriminator = None

        setattr(self, "_{}".format('bcc_email_archive_history'), kwargs.get('bcc_email_archive_history', None))
        setattr(self, "_{}".format('end_position'), kwargs.get('end_position', None))
        setattr(self, "_{}".format('next_uri'), kwargs.get('next_uri', None))
        setattr(self, "_{}".format('previous_uri'), kwargs.get('previous_uri', None))
        setattr(self, "_{}".format('result_set_size'), kwargs.get('result_set_size', None))
        setattr(self, "_{}".format('start_position'), kwargs.get('start_position', None))
        setattr(self, "_{}".format('total_set_size'), kwargs.get('total_set_size', None))

    @property
    def bcc_email_archive_history(self):
        """Gets the bcc_email_archive_history of this BccEmailArchiveHistoryList.  # noqa: E501

          # noqa: E501

        :return: The bcc_email_archive_history of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: list[BccEmailArchiveHistory]
        """
        return self._bcc_email_archive_history

    @bcc_email_archive_history.setter
    def bcc_email_archive_history(self, bcc_email_archive_history):
        """Sets the bcc_email_archive_history of this BccEmailArchiveHistoryList.

          # noqa: E501

        :param bcc_email_archive_history: The bcc_email_archive_history of this BccEmailArchiveHistoryList.  # noqa: E501
        :type: list[BccEmailArchiveHistory]
        """

        self._bcc_email_archive_history = bcc_email_archive_history

    @property
    def end_position(self):
        """Gets the end_position of this BccEmailArchiveHistoryList.  # noqa: E501

        The last position in the result set.   # noqa: E501

        :return: The end_position of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this BccEmailArchiveHistoryList.

        The last position in the result set.   # noqa: E501

        :param end_position: The end_position of this BccEmailArchiveHistoryList.  # noqa: E501
        :type: str
        """

        self._end_position = end_position

    @property
    def next_uri(self):
        """Gets the next_uri of this BccEmailArchiveHistoryList.  # noqa: E501

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :return: The next_uri of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this BccEmailArchiveHistoryList.

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :param next_uri: The next_uri of this BccEmailArchiveHistoryList.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """Gets the previous_uri of this BccEmailArchiveHistoryList.  # noqa: E501

        The postal code for the billing address.  # noqa: E501

        :return: The previous_uri of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """Sets the previous_uri of this BccEmailArchiveHistoryList.

        The postal code for the billing address.  # noqa: E501

        :param previous_uri: The previous_uri of this BccEmailArchiveHistoryList.  # noqa: E501
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """Gets the result_set_size of this BccEmailArchiveHistoryList.  # noqa: E501

        The number of results returned in this response.   # noqa: E501

        :return: The result_set_size of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this BccEmailArchiveHistoryList.

        The number of results returned in this response.   # noqa: E501

        :param result_set_size: The result_set_size of this BccEmailArchiveHistoryList.  # noqa: E501
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this BccEmailArchiveHistoryList.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this BccEmailArchiveHistoryList.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this BccEmailArchiveHistoryList.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this BccEmailArchiveHistoryList.  # noqa: E501

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :return: The total_set_size of this BccEmailArchiveHistoryList.  # noqa: E501
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this BccEmailArchiveHistoryList.

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :param total_set_size: The total_set_size of this BccEmailArchiveHistoryList.  # noqa: E501
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
        if issubclass(BccEmailArchiveHistoryList, dict):
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
        if not isinstance(other, BccEmailArchiveHistoryList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BccEmailArchiveHistoryList):
            return True

        return self.to_dict() != other.to_dict()
