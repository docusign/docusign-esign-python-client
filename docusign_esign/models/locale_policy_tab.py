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


class LocalePolicyTab(object):
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
        'address_format': 'str',
        'calendar_type': 'str',
        'culture_name': 'str',
        'currency_code': 'str',
        'currency_negative_format': 'str',
        'currency_positive_format': 'str',
        'custom_date_format': 'str',
        'custom_time_format': 'str',
        'date_format': 'str',
        'initial_format': 'str',
        'name_format': 'str',
        'time_format': 'str',
        'time_zone': 'str',
        'use_long_currency_format': 'str'
    }

    attribute_map = {
        'address_format': 'addressFormat',
        'calendar_type': 'calendarType',
        'culture_name': 'cultureName',
        'currency_code': 'currencyCode',
        'currency_negative_format': 'currencyNegativeFormat',
        'currency_positive_format': 'currencyPositiveFormat',
        'custom_date_format': 'customDateFormat',
        'custom_time_format': 'customTimeFormat',
        'date_format': 'dateFormat',
        'initial_format': 'initialFormat',
        'name_format': 'nameFormat',
        'time_format': 'timeFormat',
        'time_zone': 'timeZone',
        'use_long_currency_format': 'useLongCurrencyFormat'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """LocalePolicyTab - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_format = None
        self._calendar_type = None
        self._culture_name = None
        self._currency_code = None
        self._currency_negative_format = None
        self._currency_positive_format = None
        self._custom_date_format = None
        self._custom_time_format = None
        self._date_format = None
        self._initial_format = None
        self._name_format = None
        self._time_format = None
        self._time_zone = None
        self._use_long_currency_format = None
        self.discriminator = None

        setattr(self, "_{}".format('address_format'), kwargs.get('address_format', None))
        setattr(self, "_{}".format('calendar_type'), kwargs.get('calendar_type', None))
        setattr(self, "_{}".format('culture_name'), kwargs.get('culture_name', None))
        setattr(self, "_{}".format('currency_code'), kwargs.get('currency_code', None))
        setattr(self, "_{}".format('currency_negative_format'), kwargs.get('currency_negative_format', None))
        setattr(self, "_{}".format('currency_positive_format'), kwargs.get('currency_positive_format', None))
        setattr(self, "_{}".format('custom_date_format'), kwargs.get('custom_date_format', None))
        setattr(self, "_{}".format('custom_time_format'), kwargs.get('custom_time_format', None))
        setattr(self, "_{}".format('date_format'), kwargs.get('date_format', None))
        setattr(self, "_{}".format('initial_format'), kwargs.get('initial_format', None))
        setattr(self, "_{}".format('name_format'), kwargs.get('name_format', None))
        setattr(self, "_{}".format('time_format'), kwargs.get('time_format', None))
        setattr(self, "_{}".format('time_zone'), kwargs.get('time_zone', None))
        setattr(self, "_{}".format('use_long_currency_format'), kwargs.get('use_long_currency_format', None))

    @property
    def address_format(self):
        """Gets the address_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The address_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._address_format

    @address_format.setter
    def address_format(self, address_format):
        """Sets the address_format of this LocalePolicyTab.

          # noqa: E501

        :param address_format: The address_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._address_format = address_format

    @property
    def calendar_type(self):
        """Gets the calendar_type of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The calendar_type of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this LocalePolicyTab.

          # noqa: E501

        :param calendar_type: The calendar_type of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._calendar_type = calendar_type

    @property
    def culture_name(self):
        """Gets the culture_name of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The culture_name of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._culture_name

    @culture_name.setter
    def culture_name(self, culture_name):
        """Sets the culture_name of this LocalePolicyTab.

          # noqa: E501

        :param culture_name: The culture_name of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._culture_name = culture_name

    @property
    def currency_code(self):
        """Gets the currency_code of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The currency_code of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this LocalePolicyTab.

          # noqa: E501

        :param currency_code: The currency_code of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_negative_format(self):
        """Gets the currency_negative_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The currency_negative_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._currency_negative_format

    @currency_negative_format.setter
    def currency_negative_format(self, currency_negative_format):
        """Sets the currency_negative_format of this LocalePolicyTab.

          # noqa: E501

        :param currency_negative_format: The currency_negative_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._currency_negative_format = currency_negative_format

    @property
    def currency_positive_format(self):
        """Gets the currency_positive_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The currency_positive_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._currency_positive_format

    @currency_positive_format.setter
    def currency_positive_format(self, currency_positive_format):
        """Sets the currency_positive_format of this LocalePolicyTab.

          # noqa: E501

        :param currency_positive_format: The currency_positive_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._currency_positive_format = currency_positive_format

    @property
    def custom_date_format(self):
        """Gets the custom_date_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The custom_date_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._custom_date_format

    @custom_date_format.setter
    def custom_date_format(self, custom_date_format):
        """Sets the custom_date_format of this LocalePolicyTab.

          # noqa: E501

        :param custom_date_format: The custom_date_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._custom_date_format = custom_date_format

    @property
    def custom_time_format(self):
        """Gets the custom_time_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The custom_time_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._custom_time_format

    @custom_time_format.setter
    def custom_time_format(self, custom_time_format):
        """Sets the custom_time_format of this LocalePolicyTab.

          # noqa: E501

        :param custom_time_format: The custom_time_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._custom_time_format = custom_time_format

    @property
    def date_format(self):
        """Gets the date_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The date_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this LocalePolicyTab.

          # noqa: E501

        :param date_format: The date_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def initial_format(self):
        """Gets the initial_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The initial_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._initial_format

    @initial_format.setter
    def initial_format(self, initial_format):
        """Sets the initial_format of this LocalePolicyTab.

          # noqa: E501

        :param initial_format: The initial_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._initial_format = initial_format

    @property
    def name_format(self):
        """Gets the name_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The name_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._name_format

    @name_format.setter
    def name_format(self, name_format):
        """Sets the name_format of this LocalePolicyTab.

          # noqa: E501

        :param name_format: The name_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._name_format = name_format

    @property
    def time_format(self):
        """Gets the time_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The time_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this LocalePolicyTab.

          # noqa: E501

        :param time_format: The time_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._time_format = time_format

    @property
    def time_zone(self):
        """Gets the time_zone of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The time_zone of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this LocalePolicyTab.

          # noqa: E501

        :param time_zone: The time_zone of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def use_long_currency_format(self):
        """Gets the use_long_currency_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The use_long_currency_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._use_long_currency_format

    @use_long_currency_format.setter
    def use_long_currency_format(self, use_long_currency_format):
        """Sets the use_long_currency_format of this LocalePolicyTab.

          # noqa: E501

        :param use_long_currency_format: The use_long_currency_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._use_long_currency_format = use_long_currency_format

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
        if issubclass(LocalePolicyTab, dict):
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
        if not isinstance(other, LocalePolicyTab):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalePolicyTab):
            return True

        return self.to_dict() != other.to_dict()
