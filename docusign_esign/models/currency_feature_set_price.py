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


class CurrencyFeatureSetPrice(object):
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
        'envelope_fee': 'str',
        'fixed_fee': 'str',
        'seat_fee': 'str'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'currency_symbol': 'currencySymbol',
        'envelope_fee': 'envelopeFee',
        'fixed_fee': 'fixedFee',
        'seat_fee': 'seatFee'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CurrencyFeatureSetPrice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._currency_code = None
        self._currency_symbol = None
        self._envelope_fee = None
        self._fixed_fee = None
        self._seat_fee = None
        self.discriminator = None

        setattr(self, "_{}".format('currency_code'), kwargs.get('currency_code', None))
        setattr(self, "_{}".format('currency_symbol'), kwargs.get('currency_symbol', None))
        setattr(self, "_{}".format('envelope_fee'), kwargs.get('envelope_fee', None))
        setattr(self, "_{}".format('fixed_fee'), kwargs.get('fixed_fee', None))
        setattr(self, "_{}".format('seat_fee'), kwargs.get('seat_fee', None))

    @property
    def currency_code(self):
        """Gets the currency_code of this CurrencyFeatureSetPrice.  # noqa: E501

        Specifies the alternate ISO currency code for the account.   # noqa: E501

        :return: The currency_code of this CurrencyFeatureSetPrice.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CurrencyFeatureSetPrice.

        Specifies the alternate ISO currency code for the account.   # noqa: E501

        :param currency_code: The currency_code of this CurrencyFeatureSetPrice.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this CurrencyFeatureSetPrice.  # noqa: E501

        Specifies the alternate currency symbol for the account.  # noqa: E501

        :return: The currency_symbol of this CurrencyFeatureSetPrice.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CurrencyFeatureSetPrice.

        Specifies the alternate currency symbol for the account.  # noqa: E501

        :param currency_symbol: The currency_symbol of this CurrencyFeatureSetPrice.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def envelope_fee(self):
        """Gets the envelope_fee of this CurrencyFeatureSetPrice.  # noqa: E501

        An incremental envelope cost for plans with envelope overages (when `isEnabled` is set to **true**.)  # noqa: E501

        :return: The envelope_fee of this CurrencyFeatureSetPrice.  # noqa: E501
        :rtype: str
        """
        return self._envelope_fee

    @envelope_fee.setter
    def envelope_fee(self, envelope_fee):
        """Sets the envelope_fee of this CurrencyFeatureSetPrice.

        An incremental envelope cost for plans with envelope overages (when `isEnabled` is set to **true**.)  # noqa: E501

        :param envelope_fee: The envelope_fee of this CurrencyFeatureSetPrice.  # noqa: E501
        :type: str
        """

        self._envelope_fee = envelope_fee

    @property
    def fixed_fee(self):
        """Gets the fixed_fee of this CurrencyFeatureSetPrice.  # noqa: E501

        Specifies a one-time fee associated with the plan (when `isEnabled` is set to **true**.)  # noqa: E501

        :return: The fixed_fee of this CurrencyFeatureSetPrice.  # noqa: E501
        :rtype: str
        """
        return self._fixed_fee

    @fixed_fee.setter
    def fixed_fee(self, fixed_fee):
        """Sets the fixed_fee of this CurrencyFeatureSetPrice.

        Specifies a one-time fee associated with the plan (when `isEnabled` is set to **true**.)  # noqa: E501

        :param fixed_fee: The fixed_fee of this CurrencyFeatureSetPrice.  # noqa: E501
        :type: str
        """

        self._fixed_fee = fixed_fee

    @property
    def seat_fee(self):
        """Gets the seat_fee of this CurrencyFeatureSetPrice.  # noqa: E501

        Specifies an incremental seat cost for seat-based plans (when `isEnabled` is set to **true**.)  # noqa: E501

        :return: The seat_fee of this CurrencyFeatureSetPrice.  # noqa: E501
        :rtype: str
        """
        return self._seat_fee

    @seat_fee.setter
    def seat_fee(self, seat_fee):
        """Sets the seat_fee of this CurrencyFeatureSetPrice.

        Specifies an incremental seat cost for seat-based plans (when `isEnabled` is set to **true**.)  # noqa: E501

        :param seat_fee: The seat_fee of this CurrencyFeatureSetPrice.  # noqa: E501
        :type: str
        """

        self._seat_fee = seat_fee

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
        if issubclass(CurrencyFeatureSetPrice, dict):
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
        if not isinstance(other, CurrencyFeatureSetPrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyFeatureSetPrice):
            return True

        return self.to_dict() != other.to_dict()
