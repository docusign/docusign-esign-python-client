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


class EnvelopeSummary(object):
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
        'bulk_envelope_status': 'BulkEnvelopeStatus',
        'envelope_id': 'str',
        'error_details': 'ErrorDetails',
        'recipient_signing_uri': 'str',
        'recipient_signing_uri_error': 'str',
        'status': 'str',
        'status_date_time': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'bulk_envelope_status': 'bulkEnvelopeStatus',
        'envelope_id': 'envelopeId',
        'error_details': 'errorDetails',
        'recipient_signing_uri': 'recipientSigningUri',
        'recipient_signing_uri_error': 'recipientSigningUriError',
        'status': 'status',
        'status_date_time': 'statusDateTime',
        'uri': 'uri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopeSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bulk_envelope_status = None
        self._envelope_id = None
        self._error_details = None
        self._recipient_signing_uri = None
        self._recipient_signing_uri_error = None
        self._status = None
        self._status_date_time = None
        self._uri = None
        self.discriminator = None

        setattr(self, "_{}".format('bulk_envelope_status'), kwargs.get('bulk_envelope_status', None))
        setattr(self, "_{}".format('envelope_id'), kwargs.get('envelope_id', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('recipient_signing_uri'), kwargs.get('recipient_signing_uri', None))
        setattr(self, "_{}".format('recipient_signing_uri_error'), kwargs.get('recipient_signing_uri_error', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('status_date_time'), kwargs.get('status_date_time', None))
        setattr(self, "_{}".format('uri'), kwargs.get('uri', None))

    @property
    def bulk_envelope_status(self):
        """Gets the bulk_envelope_status of this EnvelopeSummary.  # noqa: E501


        :return: The bulk_envelope_status of this EnvelopeSummary.  # noqa: E501
        :rtype: BulkEnvelopeStatus
        """
        return self._bulk_envelope_status

    @bulk_envelope_status.setter
    def bulk_envelope_status(self, bulk_envelope_status):
        """Sets the bulk_envelope_status of this EnvelopeSummary.


        :param bulk_envelope_status: The bulk_envelope_status of this EnvelopeSummary.  # noqa: E501
        :type: BulkEnvelopeStatus
        """

        self._bulk_envelope_status = bulk_envelope_status

    @property
    def envelope_id(self):
        """Gets the envelope_id of this EnvelopeSummary.  # noqa: E501

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :return: The envelope_id of this EnvelopeSummary.  # noqa: E501
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """Sets the envelope_id of this EnvelopeSummary.

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :param envelope_id: The envelope_id of this EnvelopeSummary.  # noqa: E501
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def error_details(self):
        """Gets the error_details of this EnvelopeSummary.  # noqa: E501


        :return: The error_details of this EnvelopeSummary.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this EnvelopeSummary.


        :param error_details: The error_details of this EnvelopeSummary.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def recipient_signing_uri(self):
        """Gets the recipient_signing_uri of this EnvelopeSummary.  # noqa: E501

          # noqa: E501

        :return: The recipient_signing_uri of this EnvelopeSummary.  # noqa: E501
        :rtype: str
        """
        return self._recipient_signing_uri

    @recipient_signing_uri.setter
    def recipient_signing_uri(self, recipient_signing_uri):
        """Sets the recipient_signing_uri of this EnvelopeSummary.

          # noqa: E501

        :param recipient_signing_uri: The recipient_signing_uri of this EnvelopeSummary.  # noqa: E501
        :type: str
        """

        self._recipient_signing_uri = recipient_signing_uri

    @property
    def recipient_signing_uri_error(self):
        """Gets the recipient_signing_uri_error of this EnvelopeSummary.  # noqa: E501

          # noqa: E501

        :return: The recipient_signing_uri_error of this EnvelopeSummary.  # noqa: E501
        :rtype: str
        """
        return self._recipient_signing_uri_error

    @recipient_signing_uri_error.setter
    def recipient_signing_uri_error(self, recipient_signing_uri_error):
        """Sets the recipient_signing_uri_error of this EnvelopeSummary.

          # noqa: E501

        :param recipient_signing_uri_error: The recipient_signing_uri_error of this EnvelopeSummary.  # noqa: E501
        :type: str
        """

        self._recipient_signing_uri_error = recipient_signing_uri_error

    @property
    def status(self):
        """Gets the status of this EnvelopeSummary.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this EnvelopeSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnvelopeSummary.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this EnvelopeSummary.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_date_time(self):
        """Gets the status_date_time of this EnvelopeSummary.  # noqa: E501

        The DateTime that the envelope changed status (i.e. was created or sent.)  # noqa: E501

        :return: The status_date_time of this EnvelopeSummary.  # noqa: E501
        :rtype: str
        """
        return self._status_date_time

    @status_date_time.setter
    def status_date_time(self, status_date_time):
        """Sets the status_date_time of this EnvelopeSummary.

        The DateTime that the envelope changed status (i.e. was created or sent.)  # noqa: E501

        :param status_date_time: The status_date_time of this EnvelopeSummary.  # noqa: E501
        :type: str
        """

        self._status_date_time = status_date_time

    @property
    def uri(self):
        """Gets the uri of this EnvelopeSummary.  # noqa: E501

          # noqa: E501

        :return: The uri of this EnvelopeSummary.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EnvelopeSummary.

          # noqa: E501

        :param uri: The uri of this EnvelopeSummary.  # noqa: E501
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
        if issubclass(EnvelopeSummary, dict):
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
        if not isinstance(other, EnvelopeSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopeSummary):
            return True

        return self.to_dict() != other.to_dict()
