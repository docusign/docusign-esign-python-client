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


class SenderEmailNotifications(object):
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
        'changed_signer': 'str',
        'clickwrap_responses_limit_notification_email': 'str',
        'comments_only_private_and_mention': 'str',
        'comments_receive_all': 'str',
        'delivery_failed': 'str',
        'envelope_complete': 'str',
        'offline_signing_failed': 'str',
        'powerform_responses_limit_notification_email': 'str',
        'purge_documents': 'str',
        'recipient_viewed': 'str',
        'sender_envelope_declined': 'str',
        'withdrawn_consent': 'str'
    }

    attribute_map = {
        'changed_signer': 'changedSigner',
        'clickwrap_responses_limit_notification_email': 'clickwrapResponsesLimitNotificationEmail',
        'comments_only_private_and_mention': 'commentsOnlyPrivateAndMention',
        'comments_receive_all': 'commentsReceiveAll',
        'delivery_failed': 'deliveryFailed',
        'envelope_complete': 'envelopeComplete',
        'offline_signing_failed': 'offlineSigningFailed',
        'powerform_responses_limit_notification_email': 'powerformResponsesLimitNotificationEmail',
        'purge_documents': 'purgeDocuments',
        'recipient_viewed': 'recipientViewed',
        'sender_envelope_declined': 'senderEnvelopeDeclined',
        'withdrawn_consent': 'withdrawnConsent'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SenderEmailNotifications - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._changed_signer = None
        self._clickwrap_responses_limit_notification_email = None
        self._comments_only_private_and_mention = None
        self._comments_receive_all = None
        self._delivery_failed = None
        self._envelope_complete = None
        self._offline_signing_failed = None
        self._powerform_responses_limit_notification_email = None
        self._purge_documents = None
        self._recipient_viewed = None
        self._sender_envelope_declined = None
        self._withdrawn_consent = None
        self.discriminator = None

        setattr(self, "_{}".format('changed_signer'), kwargs.get('changed_signer', None))
        setattr(self, "_{}".format('clickwrap_responses_limit_notification_email'), kwargs.get('clickwrap_responses_limit_notification_email', None))
        setattr(self, "_{}".format('comments_only_private_and_mention'), kwargs.get('comments_only_private_and_mention', None))
        setattr(self, "_{}".format('comments_receive_all'), kwargs.get('comments_receive_all', None))
        setattr(self, "_{}".format('delivery_failed'), kwargs.get('delivery_failed', None))
        setattr(self, "_{}".format('envelope_complete'), kwargs.get('envelope_complete', None))
        setattr(self, "_{}".format('offline_signing_failed'), kwargs.get('offline_signing_failed', None))
        setattr(self, "_{}".format('powerform_responses_limit_notification_email'), kwargs.get('powerform_responses_limit_notification_email', None))
        setattr(self, "_{}".format('purge_documents'), kwargs.get('purge_documents', None))
        setattr(self, "_{}".format('recipient_viewed'), kwargs.get('recipient_viewed', None))
        setattr(self, "_{}".format('sender_envelope_declined'), kwargs.get('sender_envelope_declined', None))
        setattr(self, "_{}".format('withdrawn_consent'), kwargs.get('withdrawn_consent', None))

    @property
    def changed_signer(self):
        """Gets the changed_signer of this SenderEmailNotifications.  # noqa: E501

        When set to **true**, the sender receives notification if the signer changes.  # noqa: E501

        :return: The changed_signer of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._changed_signer

    @changed_signer.setter
    def changed_signer(self, changed_signer):
        """Sets the changed_signer of this SenderEmailNotifications.

        When set to **true**, the sender receives notification if the signer changes.  # noqa: E501

        :param changed_signer: The changed_signer of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._changed_signer = changed_signer

    @property
    def clickwrap_responses_limit_notification_email(self):
        """Gets the clickwrap_responses_limit_notification_email of this SenderEmailNotifications.  # noqa: E501

          # noqa: E501

        :return: The clickwrap_responses_limit_notification_email of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._clickwrap_responses_limit_notification_email

    @clickwrap_responses_limit_notification_email.setter
    def clickwrap_responses_limit_notification_email(self, clickwrap_responses_limit_notification_email):
        """Sets the clickwrap_responses_limit_notification_email of this SenderEmailNotifications.

          # noqa: E501

        :param clickwrap_responses_limit_notification_email: The clickwrap_responses_limit_notification_email of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._clickwrap_responses_limit_notification_email = clickwrap_responses_limit_notification_email

    @property
    def comments_only_private_and_mention(self):
        """Gets the comments_only_private_and_mention of this SenderEmailNotifications.  # noqa: E501

          # noqa: E501

        :return: The comments_only_private_and_mention of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._comments_only_private_and_mention

    @comments_only_private_and_mention.setter
    def comments_only_private_and_mention(self, comments_only_private_and_mention):
        """Sets the comments_only_private_and_mention of this SenderEmailNotifications.

          # noqa: E501

        :param comments_only_private_and_mention: The comments_only_private_and_mention of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._comments_only_private_and_mention = comments_only_private_and_mention

    @property
    def comments_receive_all(self):
        """Gets the comments_receive_all of this SenderEmailNotifications.  # noqa: E501

          # noqa: E501

        :return: The comments_receive_all of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._comments_receive_all

    @comments_receive_all.setter
    def comments_receive_all(self, comments_receive_all):
        """Sets the comments_receive_all of this SenderEmailNotifications.

          # noqa: E501

        :param comments_receive_all: The comments_receive_all of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._comments_receive_all = comments_receive_all

    @property
    def delivery_failed(self):
        """Gets the delivery_failed of this SenderEmailNotifications.  # noqa: E501

        When set to **true**, the sender receives notification if the delivery of the envelope fails.  # noqa: E501

        :return: The delivery_failed of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._delivery_failed

    @delivery_failed.setter
    def delivery_failed(self, delivery_failed):
        """Sets the delivery_failed of this SenderEmailNotifications.

        When set to **true**, the sender receives notification if the delivery of the envelope fails.  # noqa: E501

        :param delivery_failed: The delivery_failed of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._delivery_failed = delivery_failed

    @property
    def envelope_complete(self):
        """Gets the envelope_complete of this SenderEmailNotifications.  # noqa: E501

        When set to **true**, the user receives notification that the envelope has been completed.  # noqa: E501

        :return: The envelope_complete of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._envelope_complete

    @envelope_complete.setter
    def envelope_complete(self, envelope_complete):
        """Sets the envelope_complete of this SenderEmailNotifications.

        When set to **true**, the user receives notification that the envelope has been completed.  # noqa: E501

        :param envelope_complete: The envelope_complete of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._envelope_complete = envelope_complete

    @property
    def offline_signing_failed(self):
        """Gets the offline_signing_failed of this SenderEmailNotifications.  # noqa: E501

        When set to **true**, the user receives notification if the offline signing failed.  # noqa: E501

        :return: The offline_signing_failed of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._offline_signing_failed

    @offline_signing_failed.setter
    def offline_signing_failed(self, offline_signing_failed):
        """Sets the offline_signing_failed of this SenderEmailNotifications.

        When set to **true**, the user receives notification if the offline signing failed.  # noqa: E501

        :param offline_signing_failed: The offline_signing_failed of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._offline_signing_failed = offline_signing_failed

    @property
    def powerform_responses_limit_notification_email(self):
        """Gets the powerform_responses_limit_notification_email of this SenderEmailNotifications.  # noqa: E501

          # noqa: E501

        :return: The powerform_responses_limit_notification_email of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._powerform_responses_limit_notification_email

    @powerform_responses_limit_notification_email.setter
    def powerform_responses_limit_notification_email(self, powerform_responses_limit_notification_email):
        """Sets the powerform_responses_limit_notification_email of this SenderEmailNotifications.

          # noqa: E501

        :param powerform_responses_limit_notification_email: The powerform_responses_limit_notification_email of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._powerform_responses_limit_notification_email = powerform_responses_limit_notification_email

    @property
    def purge_documents(self):
        """Gets the purge_documents of this SenderEmailNotifications.  # noqa: E501

          # noqa: E501

        :return: The purge_documents of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._purge_documents

    @purge_documents.setter
    def purge_documents(self, purge_documents):
        """Sets the purge_documents of this SenderEmailNotifications.

          # noqa: E501

        :param purge_documents: The purge_documents of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._purge_documents = purge_documents

    @property
    def recipient_viewed(self):
        """Gets the recipient_viewed of this SenderEmailNotifications.  # noqa: E501

        When set to **true**, the sender receives notification that the recipient viewed the enveloper.  # noqa: E501

        :return: The recipient_viewed of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._recipient_viewed

    @recipient_viewed.setter
    def recipient_viewed(self, recipient_viewed):
        """Sets the recipient_viewed of this SenderEmailNotifications.

        When set to **true**, the sender receives notification that the recipient viewed the enveloper.  # noqa: E501

        :param recipient_viewed: The recipient_viewed of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._recipient_viewed = recipient_viewed

    @property
    def sender_envelope_declined(self):
        """Gets the sender_envelope_declined of this SenderEmailNotifications.  # noqa: E501

          # noqa: E501

        :return: The sender_envelope_declined of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._sender_envelope_declined

    @sender_envelope_declined.setter
    def sender_envelope_declined(self, sender_envelope_declined):
        """Sets the sender_envelope_declined of this SenderEmailNotifications.

          # noqa: E501

        :param sender_envelope_declined: The sender_envelope_declined of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._sender_envelope_declined = sender_envelope_declined

    @property
    def withdrawn_consent(self):
        """Gets the withdrawn_consent of this SenderEmailNotifications.  # noqa: E501

        When set to **true**, the user receives notification if consent is withdrawn.  # noqa: E501

        :return: The withdrawn_consent of this SenderEmailNotifications.  # noqa: E501
        :rtype: str
        """
        return self._withdrawn_consent

    @withdrawn_consent.setter
    def withdrawn_consent(self, withdrawn_consent):
        """Sets the withdrawn_consent of this SenderEmailNotifications.

        When set to **true**, the user receives notification if consent is withdrawn.  # noqa: E501

        :param withdrawn_consent: The withdrawn_consent of this SenderEmailNotifications.  # noqa: E501
        :type: str
        """

        self._withdrawn_consent = withdrawn_consent

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
        if issubclass(SenderEmailNotifications, dict):
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
        if not isinstance(other, SenderEmailNotifications):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SenderEmailNotifications):
            return True

        return self.to_dict() != other.to_dict()
