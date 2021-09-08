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


class BulkSendBatchSummary(object):
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
        'batch_id': 'str',
        'batch_name': 'str',
        'batch_size': 'str',
        'batch_uri': 'str',
        'failed': 'str',
        'queued': 'str',
        'sent': 'str',
        'submitted_date': 'str'
    }

    attribute_map = {
        'batch_id': 'batchId',
        'batch_name': 'batchName',
        'batch_size': 'batchSize',
        'batch_uri': 'batchUri',
        'failed': 'failed',
        'queued': 'queued',
        'sent': 'sent',
        'submitted_date': 'submittedDate'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendBatchSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batch_id = None
        self._batch_name = None
        self._batch_size = None
        self._batch_uri = None
        self._failed = None
        self._queued = None
        self._sent = None
        self._submitted_date = None
        self.discriminator = None

        setattr(self, "_{}".format('batch_id'), kwargs.get('batch_id', None))
        setattr(self, "_{}".format('batch_name'), kwargs.get('batch_name', None))
        setattr(self, "_{}".format('batch_size'), kwargs.get('batch_size', None))
        setattr(self, "_{}".format('batch_uri'), kwargs.get('batch_uri', None))
        setattr(self, "_{}".format('failed'), kwargs.get('failed', None))
        setattr(self, "_{}".format('queued'), kwargs.get('queued', None))
        setattr(self, "_{}".format('sent'), kwargs.get('sent', None))
        setattr(self, "_{}".format('submitted_date'), kwargs.get('submitted_date', None))

    @property
    def batch_id(self):
        """Gets the batch_id of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The batch_id of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this BulkSendBatchSummary.

          # noqa: E501

        :param batch_id: The batch_id of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def batch_name(self):
        """Gets the batch_name of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The batch_name of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        """Sets the batch_name of this BulkSendBatchSummary.

          # noqa: E501

        :param batch_name: The batch_name of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._batch_name = batch_name

    @property
    def batch_size(self):
        """Gets the batch_size of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The batch_size of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this BulkSendBatchSummary.

          # noqa: E501

        :param batch_size: The batch_size of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._batch_size = batch_size

    @property
    def batch_uri(self):
        """Gets the batch_uri of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The batch_uri of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._batch_uri

    @batch_uri.setter
    def batch_uri(self, batch_uri):
        """Sets the batch_uri of this BulkSendBatchSummary.

          # noqa: E501

        :param batch_uri: The batch_uri of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._batch_uri = batch_uri

    @property
    def failed(self):
        """Gets the failed of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The failed of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this BulkSendBatchSummary.

          # noqa: E501

        :param failed: The failed of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._failed = failed

    @property
    def queued(self):
        """Gets the queued of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The queued of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._queued

    @queued.setter
    def queued(self, queued):
        """Sets the queued of this BulkSendBatchSummary.

          # noqa: E501

        :param queued: The queued of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._queued = queued

    @property
    def sent(self):
        """Gets the sent of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The sent of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this BulkSendBatchSummary.

          # noqa: E501

        :param sent: The sent of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._sent = sent

    @property
    def submitted_date(self):
        """Gets the submitted_date of this BulkSendBatchSummary.  # noqa: E501

          # noqa: E501

        :return: The submitted_date of this BulkSendBatchSummary.  # noqa: E501
        :rtype: str
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """Sets the submitted_date of this BulkSendBatchSummary.

          # noqa: E501

        :param submitted_date: The submitted_date of this BulkSendBatchSummary.  # noqa: E501
        :type: str
        """

        self._submitted_date = submitted_date

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
        if issubclass(BulkSendBatchSummary, dict):
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
        if not isinstance(other, BulkSendBatchSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendBatchSummary):
            return True

        return self.to_dict() != other.to_dict()
