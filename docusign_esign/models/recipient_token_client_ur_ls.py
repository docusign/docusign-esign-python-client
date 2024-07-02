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


class RecipientTokenClientURLs(object):
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
        'on_access_code_failed': 'str',
        'on_cancel': 'str',
        'on_decline': 'str',
        'on_exception': 'str',
        'on_fax_pending': 'str',
        'on_id_check_failed': 'str',
        'on_session_timeout': 'str',
        'on_signing_complete': 'str',
        'on_ttl_expired': 'str',
        'on_viewing_complete': 'str'
    }

    attribute_map = {
        'on_access_code_failed': 'onAccessCodeFailed',
        'on_cancel': 'onCancel',
        'on_decline': 'onDecline',
        'on_exception': 'onException',
        'on_fax_pending': 'onFaxPending',
        'on_id_check_failed': 'onIdCheckFailed',
        'on_session_timeout': 'onSessionTimeout',
        'on_signing_complete': 'onSigningComplete',
        'on_ttl_expired': 'onTTLExpired',
        'on_viewing_complete': 'onViewingComplete'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientTokenClientURLs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._on_access_code_failed = None
        self._on_cancel = None
        self._on_decline = None
        self._on_exception = None
        self._on_fax_pending = None
        self._on_id_check_failed = None
        self._on_session_timeout = None
        self._on_signing_complete = None
        self._on_ttl_expired = None
        self._on_viewing_complete = None
        self.discriminator = None

        setattr(self, "_{}".format('on_access_code_failed'), kwargs.get('on_access_code_failed', None))
        setattr(self, "_{}".format('on_cancel'), kwargs.get('on_cancel', None))
        setattr(self, "_{}".format('on_decline'), kwargs.get('on_decline', None))
        setattr(self, "_{}".format('on_exception'), kwargs.get('on_exception', None))
        setattr(self, "_{}".format('on_fax_pending'), kwargs.get('on_fax_pending', None))
        setattr(self, "_{}".format('on_id_check_failed'), kwargs.get('on_id_check_failed', None))
        setattr(self, "_{}".format('on_session_timeout'), kwargs.get('on_session_timeout', None))
        setattr(self, "_{}".format('on_signing_complete'), kwargs.get('on_signing_complete', None))
        setattr(self, "_{}".format('on_ttl_expired'), kwargs.get('on_ttl_expired', None))
        setattr(self, "_{}".format('on_viewing_complete'), kwargs.get('on_viewing_complete', None))

    @property
    def on_access_code_failed(self):
        """Gets the on_access_code_failed of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_access_code_failed of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_access_code_failed

    @on_access_code_failed.setter
    def on_access_code_failed(self, on_access_code_failed):
        """Sets the on_access_code_failed of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_access_code_failed: The on_access_code_failed of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_access_code_failed = on_access_code_failed

    @property
    def on_cancel(self):
        """Gets the on_cancel of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_cancel of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_cancel

    @on_cancel.setter
    def on_cancel(self, on_cancel):
        """Sets the on_cancel of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_cancel: The on_cancel of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_cancel = on_cancel

    @property
    def on_decline(self):
        """Gets the on_decline of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_decline of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_decline

    @on_decline.setter
    def on_decline(self, on_decline):
        """Sets the on_decline of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_decline: The on_decline of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_decline = on_decline

    @property
    def on_exception(self):
        """Gets the on_exception of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_exception of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_exception

    @on_exception.setter
    def on_exception(self, on_exception):
        """Sets the on_exception of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_exception: The on_exception of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_exception = on_exception

    @property
    def on_fax_pending(self):
        """Gets the on_fax_pending of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_fax_pending of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_fax_pending

    @on_fax_pending.setter
    def on_fax_pending(self, on_fax_pending):
        """Sets the on_fax_pending of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_fax_pending: The on_fax_pending of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_fax_pending = on_fax_pending

    @property
    def on_id_check_failed(self):
        """Gets the on_id_check_failed of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_id_check_failed of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_id_check_failed

    @on_id_check_failed.setter
    def on_id_check_failed(self, on_id_check_failed):
        """Sets the on_id_check_failed of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_id_check_failed: The on_id_check_failed of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_id_check_failed = on_id_check_failed

    @property
    def on_session_timeout(self):
        """Gets the on_session_timeout of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_session_timeout of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_session_timeout

    @on_session_timeout.setter
    def on_session_timeout(self, on_session_timeout):
        """Sets the on_session_timeout of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_session_timeout: The on_session_timeout of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_session_timeout = on_session_timeout

    @property
    def on_signing_complete(self):
        """Gets the on_signing_complete of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_signing_complete of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_signing_complete

    @on_signing_complete.setter
    def on_signing_complete(self, on_signing_complete):
        """Sets the on_signing_complete of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_signing_complete: The on_signing_complete of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_signing_complete = on_signing_complete

    @property
    def on_ttl_expired(self):
        """Gets the on_ttl_expired of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_ttl_expired of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_ttl_expired

    @on_ttl_expired.setter
    def on_ttl_expired(self, on_ttl_expired):
        """Sets the on_ttl_expired of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_ttl_expired: The on_ttl_expired of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_ttl_expired = on_ttl_expired

    @property
    def on_viewing_complete(self):
        """Gets the on_viewing_complete of this RecipientTokenClientURLs.  # noqa: E501

          # noqa: E501

        :return: The on_viewing_complete of this RecipientTokenClientURLs.  # noqa: E501
        :rtype: str
        """
        return self._on_viewing_complete

    @on_viewing_complete.setter
    def on_viewing_complete(self, on_viewing_complete):
        """Sets the on_viewing_complete of this RecipientTokenClientURLs.

          # noqa: E501

        :param on_viewing_complete: The on_viewing_complete of this RecipientTokenClientURLs.  # noqa: E501
        :type: str
        """

        self._on_viewing_complete = on_viewing_complete

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
        if issubclass(RecipientTokenClientURLs, dict):
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
        if not isinstance(other, RecipientTokenClientURLs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientTokenClientURLs):
            return True

        return self.to_dict() != other.to_dict()
