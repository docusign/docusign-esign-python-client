# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CurrencyPlanPrice(object):
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
        'currency_code': 'str',
        'currency_symbol': 'str',
        'per_seat_price': 'str',
        'supported_card_types': 'CreditCardTypes',
        'support_incident_fee': 'str',
        'support_plan_fee': 'str'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'currency_symbol': 'currencySymbol',
        'per_seat_price': 'perSeatPrice',
        'supported_card_types': 'supportedCardTypes',
        'support_incident_fee': 'supportIncidentFee',
        'support_plan_fee': 'supportPlanFee'
    }

    def __init__(self, currency_code=None, currency_symbol=None, per_seat_price=None, supported_card_types=None, support_incident_fee=None, support_plan_fee=None):  # noqa: E501
        """CurrencyPlanPrice - a model defined in Swagger"""  # noqa: E501

        self._currency_code = None
        self._currency_symbol = None
        self._per_seat_price = None
        self._supported_card_types = None
        self._support_incident_fee = None
        self._support_plan_fee = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if per_seat_price is not None:
            self.per_seat_price = per_seat_price
        if supported_card_types is not None:
            self.supported_card_types = supported_card_types
        if support_incident_fee is not None:
            self.support_incident_fee = support_incident_fee
        if support_plan_fee is not None:
            self.support_plan_fee = support_plan_fee

    @property
    def currency_code(self):
        """Gets the currency_code of this CurrencyPlanPrice.  # noqa: E501

        Specifies the ISO currency code for the account.  # noqa: E501

        :return: The currency_code of this CurrencyPlanPrice.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CurrencyPlanPrice.

        Specifies the ISO currency code for the account.  # noqa: E501

        :param currency_code: The currency_code of this CurrencyPlanPrice.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this CurrencyPlanPrice.  # noqa: E501

        Specifies the currency symbol for the account.  # noqa: E501

        :return: The currency_symbol of this CurrencyPlanPrice.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CurrencyPlanPrice.

        Specifies the currency symbol for the account.  # noqa: E501

        :param currency_symbol: The currency_symbol of this CurrencyPlanPrice.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def per_seat_price(self):
        """Gets the per_seat_price of this CurrencyPlanPrice.  # noqa: E501

          # noqa: E501

        :return: The per_seat_price of this CurrencyPlanPrice.  # noqa: E501
        :rtype: str
        """
        return self._per_seat_price

    @per_seat_price.setter
    def per_seat_price(self, per_seat_price):
        """Sets the per_seat_price of this CurrencyPlanPrice.

          # noqa: E501

        :param per_seat_price: The per_seat_price of this CurrencyPlanPrice.  # noqa: E501
        :type: str
        """

        self._per_seat_price = per_seat_price

    @property
    def supported_card_types(self):
        """Gets the supported_card_types of this CurrencyPlanPrice.  # noqa: E501


        :return: The supported_card_types of this CurrencyPlanPrice.  # noqa: E501
        :rtype: CreditCardTypes
        """
        return self._supported_card_types

    @supported_card_types.setter
    def supported_card_types(self, supported_card_types):
        """Sets the supported_card_types of this CurrencyPlanPrice.


        :param supported_card_types: The supported_card_types of this CurrencyPlanPrice.  # noqa: E501
        :type: CreditCardTypes
        """

        self._supported_card_types = supported_card_types

    @property
    def support_incident_fee(self):
        """Gets the support_incident_fee of this CurrencyPlanPrice.  # noqa: E501

        The support incident fee charged for each support incident.  # noqa: E501

        :return: The support_incident_fee of this CurrencyPlanPrice.  # noqa: E501
        :rtype: str
        """
        return self._support_incident_fee

    @support_incident_fee.setter
    def support_incident_fee(self, support_incident_fee):
        """Sets the support_incident_fee of this CurrencyPlanPrice.

        The support incident fee charged for each support incident.  # noqa: E501

        :param support_incident_fee: The support_incident_fee of this CurrencyPlanPrice.  # noqa: E501
        :type: str
        """

        self._support_incident_fee = support_incident_fee

    @property
    def support_plan_fee(self):
        """Gets the support_plan_fee of this CurrencyPlanPrice.  # noqa: E501

        The support plan fee charged for this plan.  # noqa: E501

        :return: The support_plan_fee of this CurrencyPlanPrice.  # noqa: E501
        :rtype: str
        """
        return self._support_plan_fee

    @support_plan_fee.setter
    def support_plan_fee(self, support_plan_fee):
        """Sets the support_plan_fee of this CurrencyPlanPrice.

        The support plan fee charged for this plan.  # noqa: E501

        :param support_plan_fee: The support_plan_fee of this CurrencyPlanPrice.  # noqa: E501
        :type: str
        """

        self._support_plan_fee = support_plan_fee

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
        if issubclass(CurrencyPlanPrice, dict):
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
        if not isinstance(other, CurrencyPlanPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
