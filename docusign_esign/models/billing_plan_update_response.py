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


class BillingPlanUpdateResponse(object):
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
        'account_payment_method': 'str',
        'billing_plan_preview': 'BillingPlanPreview',
        'currency_code': 'str',
        'included_seats': 'str',
        'payment_cycle': 'str',
        'payment_method': 'str',
        'plan_id': 'str',
        'plan_name': 'str'
    }

    attribute_map = {
        'account_payment_method': 'accountPaymentMethod',
        'billing_plan_preview': 'billingPlanPreview',
        'currency_code': 'currencyCode',
        'included_seats': 'includedSeats',
        'payment_cycle': 'paymentCycle',
        'payment_method': 'paymentMethod',
        'plan_id': 'planId',
        'plan_name': 'planName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BillingPlanUpdateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_payment_method = None
        self._billing_plan_preview = None
        self._currency_code = None
        self._included_seats = None
        self._payment_cycle = None
        self._payment_method = None
        self._plan_id = None
        self._plan_name = None
        self.discriminator = None

        setattr(self, "_{}".format('account_payment_method'), kwargs.get('account_payment_method', None))
        setattr(self, "_{}".format('billing_plan_preview'), kwargs.get('billing_plan_preview', None))
        setattr(self, "_{}".format('currency_code'), kwargs.get('currency_code', None))
        setattr(self, "_{}".format('included_seats'), kwargs.get('included_seats', None))
        setattr(self, "_{}".format('payment_cycle'), kwargs.get('payment_cycle', None))
        setattr(self, "_{}".format('payment_method'), kwargs.get('payment_method', None))
        setattr(self, "_{}".format('plan_id'), kwargs.get('plan_id', None))
        setattr(self, "_{}".format('plan_name'), kwargs.get('plan_name', None))

    @property
    def account_payment_method(self):
        """Gets the account_payment_method of this BillingPlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The account_payment_method of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_payment_method

    @account_payment_method.setter
    def account_payment_method(self, account_payment_method):
        """Sets the account_payment_method of this BillingPlanUpdateResponse.

          # noqa: E501

        :param account_payment_method: The account_payment_method of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._account_payment_method = account_payment_method

    @property
    def billing_plan_preview(self):
        """Gets the billing_plan_preview of this BillingPlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The billing_plan_preview of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: BillingPlanPreview
        """
        return self._billing_plan_preview

    @billing_plan_preview.setter
    def billing_plan_preview(self, billing_plan_preview):
        """Sets the billing_plan_preview of this BillingPlanUpdateResponse.

          # noqa: E501

        :param billing_plan_preview: The billing_plan_preview of this BillingPlanUpdateResponse.  # noqa: E501
        :type: BillingPlanPreview
        """

        self._billing_plan_preview = billing_plan_preview

    @property
    def currency_code(self):
        """Gets the currency_code of this BillingPlanUpdateResponse.  # noqa: E501

        Specifies the ISO currency code for the account.  # noqa: E501

        :return: The currency_code of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this BillingPlanUpdateResponse.

        Specifies the ISO currency code for the account.  # noqa: E501

        :param currency_code: The currency_code of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def included_seats(self):
        """Gets the included_seats of this BillingPlanUpdateResponse.  # noqa: E501

        The number of seats (users) included.  # noqa: E501

        :return: The included_seats of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._included_seats

    @included_seats.setter
    def included_seats(self, included_seats):
        """Sets the included_seats of this BillingPlanUpdateResponse.

        The number of seats (users) included.  # noqa: E501

        :param included_seats: The included_seats of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._included_seats = included_seats

    @property
    def payment_cycle(self):
        """Gets the payment_cycle of this BillingPlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The payment_cycle of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_cycle

    @payment_cycle.setter
    def payment_cycle(self, payment_cycle):
        """Sets the payment_cycle of this BillingPlanUpdateResponse.

          # noqa: E501

        :param payment_cycle: The payment_cycle of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._payment_cycle = payment_cycle

    @property
    def payment_method(self):
        """Gets the payment_method of this BillingPlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The payment_method of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this BillingPlanUpdateResponse.

          # noqa: E501

        :param payment_method: The payment_method of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def plan_id(self):
        """Gets the plan_id of this BillingPlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The plan_id of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this BillingPlanUpdateResponse.

          # noqa: E501

        :param plan_id: The plan_id of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this BillingPlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The plan_name of this BillingPlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this BillingPlanUpdateResponse.

          # noqa: E501

        :param plan_name: The plan_name of this BillingPlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

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
        if issubclass(BillingPlanUpdateResponse, dict):
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
        if not isinstance(other, BillingPlanUpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingPlanUpdateResponse):
            return True

        return self.to_dict() != other.to_dict()
