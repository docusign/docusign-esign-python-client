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


class EventResult(object):
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
        'event_timestamp': 'str',
        'failure_description': 'str',
        'status': 'str',
        'vendor_failure_status_code': 'str'
    }

    attribute_map = {
        'event_timestamp': 'eventTimestamp',
        'failure_description': 'failureDescription',
        'status': 'status',
        'vendor_failure_status_code': 'vendorFailureStatusCode'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EventResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_timestamp = None
        self._failure_description = None
        self._status = None
        self._vendor_failure_status_code = None
        self.discriminator = None

        setattr(self, "_{}".format('event_timestamp'), kwargs.get('event_timestamp', None))
        setattr(self, "_{}".format('failure_description'), kwargs.get('failure_description', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('vendor_failure_status_code'), kwargs.get('vendor_failure_status_code', None))

    @property
    def event_timestamp(self):
        """Gets the event_timestamp of this EventResult.  # noqa: E501

          # noqa: E501

        :return: The event_timestamp of this EventResult.  # noqa: E501
        :rtype: str
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """Sets the event_timestamp of this EventResult.

          # noqa: E501

        :param event_timestamp: The event_timestamp of this EventResult.  # noqa: E501
        :type: str
        """

        self._event_timestamp = event_timestamp

    @property
    def failure_description(self):
        """Gets the failure_description of this EventResult.  # noqa: E501

          # noqa: E501

        :return: The failure_description of this EventResult.  # noqa: E501
        :rtype: str
        """
        return self._failure_description

    @failure_description.setter
    def failure_description(self, failure_description):
        """Sets the failure_description of this EventResult.

          # noqa: E501

        :param failure_description: The failure_description of this EventResult.  # noqa: E501
        :type: str
        """

        self._failure_description = failure_description

    @property
    def status(self):
        """Gets the status of this EventResult.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this EventResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventResult.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this EventResult.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def vendor_failure_status_code(self):
        """Gets the vendor_failure_status_code of this EventResult.  # noqa: E501

          # noqa: E501

        :return: The vendor_failure_status_code of this EventResult.  # noqa: E501
        :rtype: str
        """
        return self._vendor_failure_status_code

    @vendor_failure_status_code.setter
    def vendor_failure_status_code(self, vendor_failure_status_code):
        """Sets the vendor_failure_status_code of this EventResult.

          # noqa: E501

        :param vendor_failure_status_code: The vendor_failure_status_code of this EventResult.  # noqa: E501
        :type: str
        """

        self._vendor_failure_status_code = vendor_failure_status_code

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
        if issubclass(EventResult, dict):
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
        if not isinstance(other, EventResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventResult):
            return True

        return self.to_dict() != other.to_dict()
