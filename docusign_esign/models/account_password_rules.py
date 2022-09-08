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


class AccountPasswordRules(object):
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
        'expire_password': 'str',
        'expire_password_days': 'str',
        'expire_password_days_metadata': 'AccountPasswordExpirePasswordDays',
        'lockout_duration_minutes': 'str',
        'lockout_duration_minutes_metadata': 'AccountPasswordLockoutDurationMinutes',
        'lockout_duration_type': 'str',
        'lockout_duration_type_metadata': 'AccountPasswordLockoutDurationType',
        'minimum_password_age_days': 'str',
        'minimum_password_age_days_metadata': 'AccountPasswordMinimumPasswordAgeDays',
        'minimum_password_length': 'str',
        'minimum_password_length_metadata': 'AccountMinimumPasswordLength',
        'password_include_digit': 'str',
        'password_include_digit_or_special_character': 'str',
        'password_include_lower_case': 'str',
        'password_include_special_character': 'str',
        'password_include_upper_case': 'str',
        'password_strength_type': 'str',
        'password_strength_type_metadata': 'AccountPasswordStrengthType',
        'questions_required': 'str',
        'questions_required_metadata': 'AccountPasswordQuestionsRequired'
    }

    attribute_map = {
        'expire_password': 'expirePassword',
        'expire_password_days': 'expirePasswordDays',
        'expire_password_days_metadata': 'expirePasswordDaysMetadata',
        'lockout_duration_minutes': 'lockoutDurationMinutes',
        'lockout_duration_minutes_metadata': 'lockoutDurationMinutesMetadata',
        'lockout_duration_type': 'lockoutDurationType',
        'lockout_duration_type_metadata': 'lockoutDurationTypeMetadata',
        'minimum_password_age_days': 'minimumPasswordAgeDays',
        'minimum_password_age_days_metadata': 'minimumPasswordAgeDaysMetadata',
        'minimum_password_length': 'minimumPasswordLength',
        'minimum_password_length_metadata': 'minimumPasswordLengthMetadata',
        'password_include_digit': 'passwordIncludeDigit',
        'password_include_digit_or_special_character': 'passwordIncludeDigitOrSpecialCharacter',
        'password_include_lower_case': 'passwordIncludeLowerCase',
        'password_include_special_character': 'passwordIncludeSpecialCharacter',
        'password_include_upper_case': 'passwordIncludeUpperCase',
        'password_strength_type': 'passwordStrengthType',
        'password_strength_type_metadata': 'passwordStrengthTypeMetadata',
        'questions_required': 'questionsRequired',
        'questions_required_metadata': 'questionsRequiredMetadata'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AccountPasswordRules - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expire_password = None
        self._expire_password_days = None
        self._expire_password_days_metadata = None
        self._lockout_duration_minutes = None
        self._lockout_duration_minutes_metadata = None
        self._lockout_duration_type = None
        self._lockout_duration_type_metadata = None
        self._minimum_password_age_days = None
        self._minimum_password_age_days_metadata = None
        self._minimum_password_length = None
        self._minimum_password_length_metadata = None
        self._password_include_digit = None
        self._password_include_digit_or_special_character = None
        self._password_include_lower_case = None
        self._password_include_special_character = None
        self._password_include_upper_case = None
        self._password_strength_type = None
        self._password_strength_type_metadata = None
        self._questions_required = None
        self._questions_required_metadata = None
        self.discriminator = None

        setattr(self, "_{}".format('expire_password'), kwargs.get('expire_password', None))
        setattr(self, "_{}".format('expire_password_days'), kwargs.get('expire_password_days', None))
        setattr(self, "_{}".format('expire_password_days_metadata'), kwargs.get('expire_password_days_metadata', None))
        setattr(self, "_{}".format('lockout_duration_minutes'), kwargs.get('lockout_duration_minutes', None))
        setattr(self, "_{}".format('lockout_duration_minutes_metadata'), kwargs.get('lockout_duration_minutes_metadata', None))
        setattr(self, "_{}".format('lockout_duration_type'), kwargs.get('lockout_duration_type', None))
        setattr(self, "_{}".format('lockout_duration_type_metadata'), kwargs.get('lockout_duration_type_metadata', None))
        setattr(self, "_{}".format('minimum_password_age_days'), kwargs.get('minimum_password_age_days', None))
        setattr(self, "_{}".format('minimum_password_age_days_metadata'), kwargs.get('minimum_password_age_days_metadata', None))
        setattr(self, "_{}".format('minimum_password_length'), kwargs.get('minimum_password_length', None))
        setattr(self, "_{}".format('minimum_password_length_metadata'), kwargs.get('minimum_password_length_metadata', None))
        setattr(self, "_{}".format('password_include_digit'), kwargs.get('password_include_digit', None))
        setattr(self, "_{}".format('password_include_digit_or_special_character'), kwargs.get('password_include_digit_or_special_character', None))
        setattr(self, "_{}".format('password_include_lower_case'), kwargs.get('password_include_lower_case', None))
        setattr(self, "_{}".format('password_include_special_character'), kwargs.get('password_include_special_character', None))
        setattr(self, "_{}".format('password_include_upper_case'), kwargs.get('password_include_upper_case', None))
        setattr(self, "_{}".format('password_strength_type'), kwargs.get('password_strength_type', None))
        setattr(self, "_{}".format('password_strength_type_metadata'), kwargs.get('password_strength_type_metadata', None))
        setattr(self, "_{}".format('questions_required'), kwargs.get('questions_required', None))
        setattr(self, "_{}".format('questions_required_metadata'), kwargs.get('questions_required_metadata', None))

    @property
    def expire_password(self):
        """Gets the expire_password of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The expire_password of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._expire_password

    @expire_password.setter
    def expire_password(self, expire_password):
        """Sets the expire_password of this AccountPasswordRules.

          # noqa: E501

        :param expire_password: The expire_password of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._expire_password = expire_password

    @property
    def expire_password_days(self):
        """Gets the expire_password_days of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The expire_password_days of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._expire_password_days

    @expire_password_days.setter
    def expire_password_days(self, expire_password_days):
        """Sets the expire_password_days of this AccountPasswordRules.

          # noqa: E501

        :param expire_password_days: The expire_password_days of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._expire_password_days = expire_password_days

    @property
    def expire_password_days_metadata(self):
        """Gets the expire_password_days_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `expirePasswordDays` property is editable.   # noqa: E501

        :return: The expire_password_days_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountPasswordExpirePasswordDays
        """
        return self._expire_password_days_metadata

    @expire_password_days_metadata.setter
    def expire_password_days_metadata(self, expire_password_days_metadata):
        """Sets the expire_password_days_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `expirePasswordDays` property is editable.   # noqa: E501

        :param expire_password_days_metadata: The expire_password_days_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountPasswordExpirePasswordDays
        """

        self._expire_password_days_metadata = expire_password_days_metadata

    @property
    def lockout_duration_minutes(self):
        """Gets the lockout_duration_minutes of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The lockout_duration_minutes of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._lockout_duration_minutes

    @lockout_duration_minutes.setter
    def lockout_duration_minutes(self, lockout_duration_minutes):
        """Sets the lockout_duration_minutes of this AccountPasswordRules.

          # noqa: E501

        :param lockout_duration_minutes: The lockout_duration_minutes of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._lockout_duration_minutes = lockout_duration_minutes

    @property
    def lockout_duration_minutes_metadata(self):
        """Gets the lockout_duration_minutes_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `lockoutDurationMinutes` property is editable.   # noqa: E501

        :return: The lockout_duration_minutes_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountPasswordLockoutDurationMinutes
        """
        return self._lockout_duration_minutes_metadata

    @lockout_duration_minutes_metadata.setter
    def lockout_duration_minutes_metadata(self, lockout_duration_minutes_metadata):
        """Sets the lockout_duration_minutes_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `lockoutDurationMinutes` property is editable.   # noqa: E501

        :param lockout_duration_minutes_metadata: The lockout_duration_minutes_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountPasswordLockoutDurationMinutes
        """

        self._lockout_duration_minutes_metadata = lockout_duration_minutes_metadata

    @property
    def lockout_duration_type(self):
        """Gets the lockout_duration_type of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The lockout_duration_type of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._lockout_duration_type

    @lockout_duration_type.setter
    def lockout_duration_type(self, lockout_duration_type):
        """Sets the lockout_duration_type of this AccountPasswordRules.

          # noqa: E501

        :param lockout_duration_type: The lockout_duration_type of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._lockout_duration_type = lockout_duration_type

    @property
    def lockout_duration_type_metadata(self):
        """Gets the lockout_duration_type_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `lockoutDurationType` property is editable.   # noqa: E501

        :return: The lockout_duration_type_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountPasswordLockoutDurationType
        """
        return self._lockout_duration_type_metadata

    @lockout_duration_type_metadata.setter
    def lockout_duration_type_metadata(self, lockout_duration_type_metadata):
        """Sets the lockout_duration_type_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `lockoutDurationType` property is editable.   # noqa: E501

        :param lockout_duration_type_metadata: The lockout_duration_type_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountPasswordLockoutDurationType
        """

        self._lockout_duration_type_metadata = lockout_duration_type_metadata

    @property
    def minimum_password_age_days(self):
        """Gets the minimum_password_age_days of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The minimum_password_age_days of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._minimum_password_age_days

    @minimum_password_age_days.setter
    def minimum_password_age_days(self, minimum_password_age_days):
        """Sets the minimum_password_age_days of this AccountPasswordRules.

          # noqa: E501

        :param minimum_password_age_days: The minimum_password_age_days of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._minimum_password_age_days = minimum_password_age_days

    @property
    def minimum_password_age_days_metadata(self):
        """Gets the minimum_password_age_days_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `minimumPasswordAgeDays` property is editable.   # noqa: E501

        :return: The minimum_password_age_days_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountPasswordMinimumPasswordAgeDays
        """
        return self._minimum_password_age_days_metadata

    @minimum_password_age_days_metadata.setter
    def minimum_password_age_days_metadata(self, minimum_password_age_days_metadata):
        """Sets the minimum_password_age_days_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `minimumPasswordAgeDays` property is editable.   # noqa: E501

        :param minimum_password_age_days_metadata: The minimum_password_age_days_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountPasswordMinimumPasswordAgeDays
        """

        self._minimum_password_age_days_metadata = minimum_password_age_days_metadata

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The minimum_password_length of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this AccountPasswordRules.

          # noqa: E501

        :param minimum_password_length: The minimum_password_length of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._minimum_password_length = minimum_password_length

    @property
    def minimum_password_length_metadata(self):
        """Gets the minimum_password_length_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `minimumPasswordLength` property is editable.   # noqa: E501

        :return: The minimum_password_length_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountMinimumPasswordLength
        """
        return self._minimum_password_length_metadata

    @minimum_password_length_metadata.setter
    def minimum_password_length_metadata(self, minimum_password_length_metadata):
        """Sets the minimum_password_length_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `minimumPasswordLength` property is editable.   # noqa: E501

        :param minimum_password_length_metadata: The minimum_password_length_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountMinimumPasswordLength
        """

        self._minimum_password_length_metadata = minimum_password_length_metadata

    @property
    def password_include_digit(self):
        """Gets the password_include_digit of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The password_include_digit of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._password_include_digit

    @password_include_digit.setter
    def password_include_digit(self, password_include_digit):
        """Sets the password_include_digit of this AccountPasswordRules.

          # noqa: E501

        :param password_include_digit: The password_include_digit of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._password_include_digit = password_include_digit

    @property
    def password_include_digit_or_special_character(self):
        """Gets the password_include_digit_or_special_character of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The password_include_digit_or_special_character of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._password_include_digit_or_special_character

    @password_include_digit_or_special_character.setter
    def password_include_digit_or_special_character(self, password_include_digit_or_special_character):
        """Sets the password_include_digit_or_special_character of this AccountPasswordRules.

          # noqa: E501

        :param password_include_digit_or_special_character: The password_include_digit_or_special_character of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._password_include_digit_or_special_character = password_include_digit_or_special_character

    @property
    def password_include_lower_case(self):
        """Gets the password_include_lower_case of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The password_include_lower_case of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._password_include_lower_case

    @password_include_lower_case.setter
    def password_include_lower_case(self, password_include_lower_case):
        """Sets the password_include_lower_case of this AccountPasswordRules.

          # noqa: E501

        :param password_include_lower_case: The password_include_lower_case of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._password_include_lower_case = password_include_lower_case

    @property
    def password_include_special_character(self):
        """Gets the password_include_special_character of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The password_include_special_character of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._password_include_special_character

    @password_include_special_character.setter
    def password_include_special_character(self, password_include_special_character):
        """Sets the password_include_special_character of this AccountPasswordRules.

          # noqa: E501

        :param password_include_special_character: The password_include_special_character of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._password_include_special_character = password_include_special_character

    @property
    def password_include_upper_case(self):
        """Gets the password_include_upper_case of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The password_include_upper_case of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._password_include_upper_case

    @password_include_upper_case.setter
    def password_include_upper_case(self, password_include_upper_case):
        """Sets the password_include_upper_case of this AccountPasswordRules.

          # noqa: E501

        :param password_include_upper_case: The password_include_upper_case of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._password_include_upper_case = password_include_upper_case

    @property
    def password_strength_type(self):
        """Gets the password_strength_type of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The password_strength_type of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._password_strength_type

    @password_strength_type.setter
    def password_strength_type(self, password_strength_type):
        """Sets the password_strength_type of this AccountPasswordRules.

          # noqa: E501

        :param password_strength_type: The password_strength_type of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._password_strength_type = password_strength_type

    @property
    def password_strength_type_metadata(self):
        """Gets the password_strength_type_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `passwordStrengthType` property is editable.   # noqa: E501

        :return: The password_strength_type_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountPasswordStrengthType
        """
        return self._password_strength_type_metadata

    @password_strength_type_metadata.setter
    def password_strength_type_metadata(self, password_strength_type_metadata):
        """Sets the password_strength_type_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `passwordStrengthType` property is editable.   # noqa: E501

        :param password_strength_type_metadata: The password_strength_type_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountPasswordStrengthType
        """

        self._password_strength_type_metadata = password_strength_type_metadata

    @property
    def questions_required(self):
        """Gets the questions_required of this AccountPasswordRules.  # noqa: E501

          # noqa: E501

        :return: The questions_required of this AccountPasswordRules.  # noqa: E501
        :rtype: str
        """
        return self._questions_required

    @questions_required.setter
    def questions_required(self, questions_required):
        """Sets the questions_required of this AccountPasswordRules.

          # noqa: E501

        :param questions_required: The questions_required of this AccountPasswordRules.  # noqa: E501
        :type: str
        """

        self._questions_required = questions_required

    @property
    def questions_required_metadata(self):
        """Gets the questions_required_metadata of this AccountPasswordRules.  # noqa: E501

        Metadata that indicates whether the `questionsRequired` property is editable.   # noqa: E501

        :return: The questions_required_metadata of this AccountPasswordRules.  # noqa: E501
        :rtype: AccountPasswordQuestionsRequired
        """
        return self._questions_required_metadata

    @questions_required_metadata.setter
    def questions_required_metadata(self, questions_required_metadata):
        """Sets the questions_required_metadata of this AccountPasswordRules.

        Metadata that indicates whether the `questionsRequired` property is editable.   # noqa: E501

        :param questions_required_metadata: The questions_required_metadata of this AccountPasswordRules.  # noqa: E501
        :type: AccountPasswordQuestionsRequired
        """

        self._questions_required_metadata = questions_required_metadata

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
        if issubclass(AccountPasswordRules, dict):
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
        if not isinstance(other, AccountPasswordRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountPasswordRules):
            return True

        return self.to_dict() != other.to_dict()
