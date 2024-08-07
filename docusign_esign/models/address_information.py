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


class AddressInformation(object):
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
        'state_or_province': 'str',
        'zip_plus4': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'fax': 'fax',
        'phone': 'phone',
        'postal_code': 'postalCode',
        'state_or_province': 'stateOrProvince',
        'zip_plus4': 'zipPlus4'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AddressInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._fax = None
        self._phone = None
        self._postal_code = None
        self._state_or_province = None
        self._zip_plus4 = None
        self.discriminator = None

        setattr(self, "_{}".format('address1'), kwargs.get('address1', None))
        setattr(self, "_{}".format('address2'), kwargs.get('address2', None))
        setattr(self, "_{}".format('city'), kwargs.get('city', None))
        setattr(self, "_{}".format('country'), kwargs.get('country', None))
        setattr(self, "_{}".format('fax'), kwargs.get('fax', None))
        setattr(self, "_{}".format('phone'), kwargs.get('phone', None))
        setattr(self, "_{}".format('postal_code'), kwargs.get('postal_code', None))
        setattr(self, "_{}".format('state_or_province'), kwargs.get('state_or_province', None))
        setattr(self, "_{}".format('zip_plus4'), kwargs.get('zip_plus4', None))

    @property
    def address1(self):
        """Gets the address1 of this AddressInformation.  # noqa: E501

        First Line of the address. Maximum length: 100 characters.  # noqa: E501

        :return: The address1 of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this AddressInformation.

        First Line of the address. Maximum length: 100 characters.  # noqa: E501

        :param address1: The address1 of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this AddressInformation.  # noqa: E501

        Second Line of the address. Maximum length: 100 characters.  # noqa: E501

        :return: The address2 of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this AddressInformation.

        Second Line of the address. Maximum length: 100 characters.  # noqa: E501

        :param address2: The address2 of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this AddressInformation.  # noqa: E501

        The city associated with the address.  # noqa: E501

        :return: The city of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressInformation.

        The city associated with the address.  # noqa: E501

        :param city: The city of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this AddressInformation.  # noqa: E501

        Specifies the country associated with the address.  # noqa: E501

        :return: The country of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressInformation.

        Specifies the country associated with the address.  # noqa: E501

        :param country: The country of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def fax(self):
        """Gets the fax of this AddressInformation.  # noqa: E501

        A Fax number associated with the address if one is available.  # noqa: E501

        :return: The fax of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this AddressInformation.

        A Fax number associated with the address if one is available.  # noqa: E501

        :param fax: The fax of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this AddressInformation.  # noqa: E501

        A phone number associated with the address.  # noqa: E501

        :return: The phone of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AddressInformation.

        A phone number associated with the address.  # noqa: E501

        :param phone: The phone of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this AddressInformation.  # noqa: E501

          # noqa: E501

        :return: The postal_code of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AddressInformation.

          # noqa: E501

        :param postal_code: The postal_code of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_or_province(self):
        """Gets the state_or_province of this AddressInformation.  # noqa: E501

          # noqa: E501

        :return: The state_or_province of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this AddressInformation.

          # noqa: E501

        :param state_or_province: The state_or_province of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

    @property
    def zip_plus4(self):
        """Gets the zip_plus4 of this AddressInformation.  # noqa: E501

          # noqa: E501

        :return: The zip_plus4 of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._zip_plus4

    @zip_plus4.setter
    def zip_plus4(self, zip_plus4):
        """Sets the zip_plus4 of this AddressInformation.

          # noqa: E501

        :param zip_plus4: The zip_plus4 of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._zip_plus4 = zip_plus4

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
        if issubclass(AddressInformation, dict):
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
        if not isinstance(other, AddressInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressInformation):
            return True

        return self.to_dict() != other.to_dict()
