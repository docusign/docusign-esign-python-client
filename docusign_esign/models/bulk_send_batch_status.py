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


class BulkSendBatchStatus(object):
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
        'bulk_errors': 'list[BulkSendErrorStatus]',
        'envelope_id_or_template_id': 'str',
        'envelopes_uri': 'str',
        'failed': 'str',
        'mailing_list_id': 'str',
        'mailing_list_name': 'str',
        'owner_user_id': 'str',
        'queued': 'str',
        'sender_user_id': 'str',
        'sent': 'str',
        'submitted_date': 'str'
    }

    attribute_map = {
        'batch_id': 'batchId',
        'batch_name': 'batchName',
        'batch_size': 'batchSize',
        'bulk_errors': 'bulkErrors',
        'envelope_id_or_template_id': 'envelopeIdOrTemplateId',
        'envelopes_uri': 'envelopesUri',
        'failed': 'failed',
        'mailing_list_id': 'mailingListId',
        'mailing_list_name': 'mailingListName',
        'owner_user_id': 'ownerUserId',
        'queued': 'queued',
        'sender_user_id': 'senderUserId',
        'sent': 'sent',
        'submitted_date': 'submittedDate'
    }

    def __init__(self, batch_id=None, batch_name=None, batch_size=None, bulk_errors=None, envelope_id_or_template_id=None, envelopes_uri=None, failed=None, mailing_list_id=None, mailing_list_name=None, owner_user_id=None, queued=None, sender_user_id=None, sent=None, submitted_date=None):  # noqa: E501
        """BulkSendBatchStatus - a model defined in Swagger"""  # noqa: E501

        self._batch_id = None
        self._batch_name = None
        self._batch_size = None
        self._bulk_errors = None
        self._envelope_id_or_template_id = None
        self._envelopes_uri = None
        self._failed = None
        self._mailing_list_id = None
        self._mailing_list_name = None
        self._owner_user_id = None
        self._queued = None
        self._sender_user_id = None
        self._sent = None
        self._submitted_date = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if batch_name is not None:
            self.batch_name = batch_name
        if batch_size is not None:
            self.batch_size = batch_size
        if bulk_errors is not None:
            self.bulk_errors = bulk_errors
        if envelope_id_or_template_id is not None:
            self.envelope_id_or_template_id = envelope_id_or_template_id
        if envelopes_uri is not None:
            self.envelopes_uri = envelopes_uri
        if failed is not None:
            self.failed = failed
        if mailing_list_id is not None:
            self.mailing_list_id = mailing_list_id
        if mailing_list_name is not None:
            self.mailing_list_name = mailing_list_name
        if owner_user_id is not None:
            self.owner_user_id = owner_user_id
        if queued is not None:
            self.queued = queued
        if sender_user_id is not None:
            self.sender_user_id = sender_user_id
        if sent is not None:
            self.sent = sent
        if submitted_date is not None:
            self.submitted_date = submitted_date

    @property
    def batch_id(self):
        """Gets the batch_id of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The batch_id of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this BulkSendBatchStatus.

          # noqa: E501

        :param batch_id: The batch_id of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def batch_name(self):
        """Gets the batch_name of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The batch_name of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        """Sets the batch_name of this BulkSendBatchStatus.

          # noqa: E501

        :param batch_name: The batch_name of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._batch_name = batch_name

    @property
    def batch_size(self):
        """Gets the batch_size of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The batch_size of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this BulkSendBatchStatus.

          # noqa: E501

        :param batch_size: The batch_size of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._batch_size = batch_size

    @property
    def bulk_errors(self):
        """Gets the bulk_errors of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The bulk_errors of this BulkSendBatchStatus.  # noqa: E501
        :rtype: list[BulkSendErrorStatus]
        """
        return self._bulk_errors

    @bulk_errors.setter
    def bulk_errors(self, bulk_errors):
        """Sets the bulk_errors of this BulkSendBatchStatus.

          # noqa: E501

        :param bulk_errors: The bulk_errors of this BulkSendBatchStatus.  # noqa: E501
        :type: list[BulkSendErrorStatus]
        """

        self._bulk_errors = bulk_errors

    @property
    def envelope_id_or_template_id(self):
        """Gets the envelope_id_or_template_id of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The envelope_id_or_template_id of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._envelope_id_or_template_id

    @envelope_id_or_template_id.setter
    def envelope_id_or_template_id(self, envelope_id_or_template_id):
        """Sets the envelope_id_or_template_id of this BulkSendBatchStatus.

          # noqa: E501

        :param envelope_id_or_template_id: The envelope_id_or_template_id of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._envelope_id_or_template_id = envelope_id_or_template_id

    @property
    def envelopes_uri(self):
        """Gets the envelopes_uri of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The envelopes_uri of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._envelopes_uri

    @envelopes_uri.setter
    def envelopes_uri(self, envelopes_uri):
        """Sets the envelopes_uri of this BulkSendBatchStatus.

          # noqa: E501

        :param envelopes_uri: The envelopes_uri of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._envelopes_uri = envelopes_uri

    @property
    def failed(self):
        """Gets the failed of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The failed of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this BulkSendBatchStatus.

          # noqa: E501

        :param failed: The failed of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._failed = failed

    @property
    def mailing_list_id(self):
        """Gets the mailing_list_id of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The mailing_list_id of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._mailing_list_id

    @mailing_list_id.setter
    def mailing_list_id(self, mailing_list_id):
        """Sets the mailing_list_id of this BulkSendBatchStatus.

          # noqa: E501

        :param mailing_list_id: The mailing_list_id of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._mailing_list_id = mailing_list_id

    @property
    def mailing_list_name(self):
        """Gets the mailing_list_name of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The mailing_list_name of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._mailing_list_name

    @mailing_list_name.setter
    def mailing_list_name(self, mailing_list_name):
        """Sets the mailing_list_name of this BulkSendBatchStatus.

          # noqa: E501

        :param mailing_list_name: The mailing_list_name of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._mailing_list_name = mailing_list_name

    @property
    def owner_user_id(self):
        """Gets the owner_user_id of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The owner_user_id of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, owner_user_id):
        """Sets the owner_user_id of this BulkSendBatchStatus.

          # noqa: E501

        :param owner_user_id: The owner_user_id of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._owner_user_id = owner_user_id

    @property
    def queued(self):
        """Gets the queued of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The queued of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._queued

    @queued.setter
    def queued(self, queued):
        """Sets the queued of this BulkSendBatchStatus.

          # noqa: E501

        :param queued: The queued of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._queued = queued

    @property
    def sender_user_id(self):
        """Gets the sender_user_id of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The sender_user_id of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, sender_user_id):
        """Sets the sender_user_id of this BulkSendBatchStatus.

          # noqa: E501

        :param sender_user_id: The sender_user_id of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._sender_user_id = sender_user_id

    @property
    def sent(self):
        """Gets the sent of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The sent of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this BulkSendBatchStatus.

          # noqa: E501

        :param sent: The sent of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._sent = sent

    @property
    def submitted_date(self):
        """Gets the submitted_date of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The submitted_date of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """Sets the submitted_date of this BulkSendBatchStatus.

          # noqa: E501

        :param submitted_date: The submitted_date of this BulkSendBatchStatus.  # noqa: E501
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
        if issubclass(BulkSendBatchStatus, dict):
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
        if not isinstance(other, BulkSendBatchStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
