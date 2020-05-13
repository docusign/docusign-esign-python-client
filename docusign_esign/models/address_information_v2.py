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


class AddressInformationV2(object):
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
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'fax': 'str',
        'phone': 'str',
        'postal_code': 'str',
        'state_or_province': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'fax': 'fax',
        'phone': 'phone',
        'postal_code': 'postalCode',
        'state_or_province': 'stateOrProvince'
    }

    def __init__(self, address1=None, address2=None, city=None, country=None, fax=None, phone=None, postal_code=None, state_or_province=None):  # noqa: E501
        """AddressInformationV2 - a model defined in Swagger"""  # noqa: E501

        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._fax = None
        self._phone = None
        self._postal_code = None
        self._state_or_province = None
        self.discriminator = None

        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if fax is not None:
            self.fax = fax
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if state_or_province is not None:
            self.state_or_province = state_or_province

    @property
    def address1(self):
        """Gets the address1 of this AddressInformationV2.  # noqa: E501

        First Line of the address. Maximum length: 100 characters.  # noqa: E501

        :return: The address1 of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this AddressInformationV2.

        First Line of the address. Maximum length: 100 characters.  # noqa: E501

        :param address1: The address1 of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this AddressInformationV2.  # noqa: E501

        Second Line of the address. Maximum length: 100 characters.  # noqa: E501

        :return: The address2 of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this AddressInformationV2.

        Second Line of the address. Maximum length: 100 characters.  # noqa: E501

        :param address2: The address2 of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this AddressInformationV2.  # noqa: E501

          # noqa: E501

        :return: The city of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressInformationV2.

          # noqa: E501

        :param city: The city of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this AddressInformationV2.  # noqa: E501

        Specifies the country associated with the address.  # noqa: E501

        :return: The country of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressInformationV2.

        Specifies the country associated with the address.  # noqa: E501

        :param country: The country of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def fax(self):
        """Gets the fax of this AddressInformationV2.  # noqa: E501

          # noqa: E501

        :return: The fax of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this AddressInformationV2.

          # noqa: E501

        :param fax: The fax of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this AddressInformationV2.  # noqa: E501

          # noqa: E501

        :return: The phone of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AddressInformationV2.

          # noqa: E501

        :param phone: The phone of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this AddressInformationV2.  # noqa: E501

          # noqa: E501

        :return: The postal_code of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AddressInformationV2.

          # noqa: E501

        :param postal_code: The postal_code of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_or_province(self):
        """Gets the state_or_province of this AddressInformationV2.  # noqa: E501

        The state or province associated with the address.  # noqa: E501

        :return: The state_or_province of this AddressInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this AddressInformationV2.

        The state or province associated with the address.  # noqa: E501

        :param state_or_province: The state_or_province of this AddressInformationV2.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

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
        if issubclass(AddressInformationV2, dict):
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
        if not isinstance(other, AddressInformationV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
