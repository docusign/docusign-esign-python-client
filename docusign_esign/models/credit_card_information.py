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


class CreditCardInformation(object):
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
        'address': 'AddressInformation',
        'card_last_digits': 'str',
        'card_number': 'str',
        'card_type': 'str',
        'cv_number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'name_on_card': 'str',
        'tokenized_card': 'str'
    }

    attribute_map = {
        'address': 'address',
        'card_last_digits': 'cardLastDigits',
        'card_number': 'cardNumber',
        'card_type': 'cardType',
        'cv_number': 'cvNumber',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'name_on_card': 'nameOnCard',
        'tokenized_card': 'tokenizedCard'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CreditCardInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._card_last_digits = None
        self._card_number = None
        self._card_type = None
        self._cv_number = None
        self._expiration_month = None
        self._expiration_year = None
        self._name_on_card = None
        self._tokenized_card = None
        self.discriminator = None

        setattr(self, "_{}".format('address'), kwargs.get('address', None))
        setattr(self, "_{}".format('card_last_digits'), kwargs.get('card_last_digits', None))
        setattr(self, "_{}".format('card_number'), kwargs.get('card_number', None))
        setattr(self, "_{}".format('card_type'), kwargs.get('card_type', None))
        setattr(self, "_{}".format('cv_number'), kwargs.get('cv_number', None))
        setattr(self, "_{}".format('expiration_month'), kwargs.get('expiration_month', None))
        setattr(self, "_{}".format('expiration_year'), kwargs.get('expiration_year', None))
        setattr(self, "_{}".format('name_on_card'), kwargs.get('name_on_card', None))
        setattr(self, "_{}".format('tokenized_card'), kwargs.get('tokenized_card', None))

    @property
    def address(self):
        """Gets the address of this CreditCardInformation.  # noqa: E501

        A complex element containing the credit card billing address information.  # noqa: E501

        :return: The address of this CreditCardInformation.  # noqa: E501
        :rtype: AddressInformation
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreditCardInformation.

        A complex element containing the credit card billing address information.  # noqa: E501

        :param address: The address of this CreditCardInformation.  # noqa: E501
        :type: AddressInformation
        """

        self._address = address

    @property
    def card_last_digits(self):
        """Gets the card_last_digits of this CreditCardInformation.  # noqa: E501

          # noqa: E501

        :return: The card_last_digits of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._card_last_digits

    @card_last_digits.setter
    def card_last_digits(self, card_last_digits):
        """Sets the card_last_digits of this CreditCardInformation.

          # noqa: E501

        :param card_last_digits: The card_last_digits of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._card_last_digits = card_last_digits

    @property
    def card_number(self):
        """Gets the card_number of this CreditCardInformation.  # noqa: E501

        The number on the credit card.  # noqa: E501

        :return: The card_number of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this CreditCardInformation.

        The number on the credit card.  # noqa: E501

        :param card_number: The card_number of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def card_type(self):
        """Gets the card_type of this CreditCardInformation.  # noqa: E501

        The credit card type. Valid values are: visa, mastercard, or amex.  # noqa: E501

        :return: The card_type of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this CreditCardInformation.

        The credit card type. Valid values are: visa, mastercard, or amex.  # noqa: E501

        :param card_type: The card_type of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def cv_number(self):
        """Gets the cv_number of this CreditCardInformation.  # noqa: E501

          # noqa: E501

        :return: The cv_number of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._cv_number

    @cv_number.setter
    def cv_number(self, cv_number):
        """Sets the cv_number of this CreditCardInformation.

          # noqa: E501

        :param cv_number: The cv_number of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._cv_number = cv_number

    @property
    def expiration_month(self):
        """Gets the expiration_month of this CreditCardInformation.  # noqa: E501

        The month that the credit card expires (1-12).  # noqa: E501

        :return: The expiration_month of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this CreditCardInformation.

        The month that the credit card expires (1-12).  # noqa: E501

        :param expiration_month: The expiration_month of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this CreditCardInformation.  # noqa: E501

        The year 4 digit year in which the credit card expires.  # noqa: E501

        :return: The expiration_year of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this CreditCardInformation.

        The year 4 digit year in which the credit card expires.  # noqa: E501

        :param expiration_year: The expiration_year of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def name_on_card(self):
        """Gets the name_on_card of this CreditCardInformation.  # noqa: E501

        The exact name printed on the credit card.  # noqa: E501

        :return: The name_on_card of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """Sets the name_on_card of this CreditCardInformation.

        The exact name printed on the credit card.  # noqa: E501

        :param name_on_card: The name_on_card of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._name_on_card = name_on_card

    @property
    def tokenized_card(self):
        """Gets the tokenized_card of this CreditCardInformation.  # noqa: E501

          # noqa: E501

        :return: The tokenized_card of this CreditCardInformation.  # noqa: E501
        :rtype: str
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """Sets the tokenized_card of this CreditCardInformation.

          # noqa: E501

        :param tokenized_card: The tokenized_card of this CreditCardInformation.  # noqa: E501
        :type: str
        """

        self._tokenized_card = tokenized_card

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
        if issubclass(CreditCardInformation, dict):
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
        if not isinstance(other, CreditCardInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditCardInformation):
            return True

        return self.to_dict() != other.to_dict()
