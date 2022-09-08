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
        'action': 'str',
        'action_status': 'str',
        'batch_id': 'str',
        'batch_name': 'str',
        'batch_size': 'str',
        'bulk_errors': 'list[BulkSendErrorStatus]',
        'envelope_id_or_template_id': 'str',
        'envelopes_info': 'BulkSendEnvelopesInfo',
        'envelopes_uri': 'str',
        'failed': 'str',
        'mailing_list_id': 'str',
        'mailing_list_name': 'str',
        'owner_user_id': 'str',
        'queued': 'str',
        'resends_remaining': 'str',
        'sender_user_id': 'str',
        'sent': 'str',
        'submitted_date': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_status': 'actionStatus',
        'batch_id': 'batchId',
        'batch_name': 'batchName',
        'batch_size': 'batchSize',
        'bulk_errors': 'bulkErrors',
        'envelope_id_or_template_id': 'envelopeIdOrTemplateId',
        'envelopes_info': 'envelopesInfo',
        'envelopes_uri': 'envelopesUri',
        'failed': 'failed',
        'mailing_list_id': 'mailingListId',
        'mailing_list_name': 'mailingListName',
        'owner_user_id': 'ownerUserId',
        'queued': 'queued',
        'resends_remaining': 'resendsRemaining',
        'sender_user_id': 'senderUserId',
        'sent': 'sent',
        'submitted_date': 'submittedDate'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendBatchStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._action_status = None
        self._batch_id = None
        self._batch_name = None
        self._batch_size = None
        self._bulk_errors = None
        self._envelope_id_or_template_id = None
        self._envelopes_info = None
        self._envelopes_uri = None
        self._failed = None
        self._mailing_list_id = None
        self._mailing_list_name = None
        self._owner_user_id = None
        self._queued = None
        self._resends_remaining = None
        self._sender_user_id = None
        self._sent = None
        self._submitted_date = None
        self.discriminator = None

        setattr(self, "_{}".format('action'), kwargs.get('action', None))
        setattr(self, "_{}".format('action_status'), kwargs.get('action_status', None))
        setattr(self, "_{}".format('batch_id'), kwargs.get('batch_id', None))
        setattr(self, "_{}".format('batch_name'), kwargs.get('batch_name', None))
        setattr(self, "_{}".format('batch_size'), kwargs.get('batch_size', None))
        setattr(self, "_{}".format('bulk_errors'), kwargs.get('bulk_errors', None))
        setattr(self, "_{}".format('envelope_id_or_template_id'), kwargs.get('envelope_id_or_template_id', None))
        setattr(self, "_{}".format('envelopes_info'), kwargs.get('envelopes_info', None))
        setattr(self, "_{}".format('envelopes_uri'), kwargs.get('envelopes_uri', None))
        setattr(self, "_{}".format('failed'), kwargs.get('failed', None))
        setattr(self, "_{}".format('mailing_list_id'), kwargs.get('mailing_list_id', None))
        setattr(self, "_{}".format('mailing_list_name'), kwargs.get('mailing_list_name', None))
        setattr(self, "_{}".format('owner_user_id'), kwargs.get('owner_user_id', None))
        setattr(self, "_{}".format('queued'), kwargs.get('queued', None))
        setattr(self, "_{}".format('resends_remaining'), kwargs.get('resends_remaining', None))
        setattr(self, "_{}".format('sender_user_id'), kwargs.get('sender_user_id', None))
        setattr(self, "_{}".format('sent'), kwargs.get('sent', None))
        setattr(self, "_{}".format('submitted_date'), kwargs.get('submitted_date', None))

    @property
    def action(self):
        """Gets the action of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The action of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BulkSendBatchStatus.

          # noqa: E501

        :param action: The action of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def action_status(self):
        """Gets the action_status of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The action_status of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this BulkSendBatchStatus.

          # noqa: E501

        :param action_status: The action_status of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

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
    def envelopes_info(self):
        """Gets the envelopes_info of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The envelopes_info of this BulkSendBatchStatus.  # noqa: E501
        :rtype: BulkSendEnvelopesInfo
        """
        return self._envelopes_info

    @envelopes_info.setter
    def envelopes_info(self, envelopes_info):
        """Sets the envelopes_info of this BulkSendBatchStatus.

          # noqa: E501

        :param envelopes_info: The envelopes_info of this BulkSendBatchStatus.  # noqa: E501
        :type: BulkSendEnvelopesInfo
        """

        self._envelopes_info = envelopes_info

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
    def resends_remaining(self):
        """Gets the resends_remaining of this BulkSendBatchStatus.  # noqa: E501

          # noqa: E501

        :return: The resends_remaining of this BulkSendBatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._resends_remaining

    @resends_remaining.setter
    def resends_remaining(self, resends_remaining):
        """Sets the resends_remaining of this BulkSendBatchStatus.

          # noqa: E501

        :param resends_remaining: The resends_remaining of this BulkSendBatchStatus.  # noqa: E501
        :type: str
        """

        self._resends_remaining = resends_remaining

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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendBatchStatus):
            return True

        return self.to_dict() != other.to_dict()
