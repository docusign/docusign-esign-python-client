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


class BillingPaymentsResponse(object):
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
        'billing_payments': 'list[BillingPaymentItem]',
        'next_uri': 'str',
        'previous_uri': 'str'
    }

    attribute_map = {
        'billing_payments': 'billingPayments',
        'next_uri': 'nextUri',
        'previous_uri': 'previousUri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BillingPaymentsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_payments = None
        self._next_uri = None
        self._previous_uri = None
        self.discriminator = None

        setattr(self, "_{}".format('billing_payments'), kwargs.get('billing_payments', None))
        setattr(self, "_{}".format('next_uri'), kwargs.get('next_uri', None))
        setattr(self, "_{}".format('previous_uri'), kwargs.get('previous_uri', None))

    @property
    def billing_payments(self):
        """Gets the billing_payments of this BillingPaymentsResponse.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The billing_payments of this BillingPaymentsResponse.  # noqa: E501
        :rtype: list[BillingPaymentItem]
        """
        return self._billing_payments

    @billing_payments.setter
    def billing_payments(self, billing_payments):
        """Sets the billing_payments of this BillingPaymentsResponse.

        Reserved: TBD  # noqa: E501

        :param billing_payments: The billing_payments of this BillingPaymentsResponse.  # noqa: E501
        :type: list[BillingPaymentItem]
        """

        self._billing_payments = billing_payments

    @property
    def next_uri(self):
        """Gets the next_uri of this BillingPaymentsResponse.  # noqa: E501

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :return: The next_uri of this BillingPaymentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this BillingPaymentsResponse.

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :param next_uri: The next_uri of this BillingPaymentsResponse.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """Gets the previous_uri of this BillingPaymentsResponse.  # noqa: E501

        The postal code for the billing address.  # noqa: E501

        :return: The previous_uri of this BillingPaymentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """Sets the previous_uri of this BillingPaymentsResponse.

        The postal code for the billing address.  # noqa: E501

        :param previous_uri: The previous_uri of this BillingPaymentsResponse.  # noqa: E501
        :type: str
        """

        self._previous_uri = previous_uri

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
        if issubclass(BillingPaymentsResponse, dict):
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
        if not isinstance(other, BillingPaymentsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingPaymentsResponse):
            return True

        return self.to_dict() != other.to_dict()
