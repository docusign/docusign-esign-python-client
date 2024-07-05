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


class BulkSendingCopy(object):
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
        'custom_fields': 'list[BulkSendingCopyCustomField]',
        'doc_gen_form_fields': 'list[BulksendingCopyDocGenFormField]',
        'email_blurb': 'str',
        'email_subject': 'str',
        'recipients': 'list[BulkSendingCopyRecipient]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'doc_gen_form_fields': 'docGenFormFields',
        'email_blurb': 'emailBlurb',
        'email_subject': 'emailSubject',
        'recipients': 'recipients'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendingCopy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_fields = None
        self._doc_gen_form_fields = None
        self._email_blurb = None
        self._email_subject = None
        self._recipients = None
        self.discriminator = None

        setattr(self, "_{}".format('custom_fields'), kwargs.get('custom_fields', None))
        setattr(self, "_{}".format('doc_gen_form_fields'), kwargs.get('doc_gen_form_fields', None))
        setattr(self, "_{}".format('email_blurb'), kwargs.get('email_blurb', None))
        setattr(self, "_{}".format('email_subject'), kwargs.get('email_subject', None))
        setattr(self, "_{}".format('recipients'), kwargs.get('recipients', None))

    @property
    def custom_fields(self):
        """Gets the custom_fields of this BulkSendingCopy.  # noqa: E501

        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.  # noqa: E501

        :return: The custom_fields of this BulkSendingCopy.  # noqa: E501
        :rtype: list[BulkSendingCopyCustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this BulkSendingCopy.

        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.  # noqa: E501

        :param custom_fields: The custom_fields of this BulkSendingCopy.  # noqa: E501
        :type: list[BulkSendingCopyCustomField]
        """

        self._custom_fields = custom_fields

    @property
    def doc_gen_form_fields(self):
        """Gets the doc_gen_form_fields of this BulkSendingCopy.  # noqa: E501

          # noqa: E501

        :return: The doc_gen_form_fields of this BulkSendingCopy.  # noqa: E501
        :rtype: list[BulksendingCopyDocGenFormField]
        """
        return self._doc_gen_form_fields

    @doc_gen_form_fields.setter
    def doc_gen_form_fields(self, doc_gen_form_fields):
        """Sets the doc_gen_form_fields of this BulkSendingCopy.

          # noqa: E501

        :param doc_gen_form_fields: The doc_gen_form_fields of this BulkSendingCopy.  # noqa: E501
        :type: list[BulksendingCopyDocGenFormField]
        """

        self._doc_gen_form_fields = doc_gen_form_fields

    @property
    def email_blurb(self):
        """Gets the email_blurb of this BulkSendingCopy.  # noqa: E501

          # noqa: E501

        :return: The email_blurb of this BulkSendingCopy.  # noqa: E501
        :rtype: str
        """
        return self._email_blurb

    @email_blurb.setter
    def email_blurb(self, email_blurb):
        """Sets the email_blurb of this BulkSendingCopy.

          # noqa: E501

        :param email_blurb: The email_blurb of this BulkSendingCopy.  # noqa: E501
        :type: str
        """

        self._email_blurb = email_blurb

    @property
    def email_subject(self):
        """Gets the email_subject of this BulkSendingCopy.  # noqa: E501

        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.  # noqa: E501

        :return: The email_subject of this BulkSendingCopy.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this BulkSendingCopy.

        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.  # noqa: E501

        :param email_subject: The email_subject of this BulkSendingCopy.  # noqa: E501
        :type: str
        """

        self._email_subject = email_subject

    @property
    def recipients(self):
        """Gets the recipients of this BulkSendingCopy.  # noqa: E501

        An array of powerform recipients.  # noqa: E501

        :return: The recipients of this BulkSendingCopy.  # noqa: E501
        :rtype: list[BulkSendingCopyRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this BulkSendingCopy.

        An array of powerform recipients.  # noqa: E501

        :param recipients: The recipients of this BulkSendingCopy.  # noqa: E501
        :type: list[BulkSendingCopyRecipient]
        """

        self._recipients = recipients

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
        if issubclass(BulkSendingCopy, dict):
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
        if not isinstance(other, BulkSendingCopy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendingCopy):
            return True

        return self.to_dict() != other.to_dict()
