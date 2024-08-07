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


class UserProfile(object):
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
        'authentication_methods': 'list[AuthenticationMethod]',
        'company_name': 'str',
        'display_organization_info': 'str',
        'display_personal_info': 'str',
        'display_profile': 'str',
        'display_usage_history': 'str',
        'profile_image_uri': 'str',
        'title': 'str',
        'usage_history': 'UsageHistory',
        'user_details': 'UserInformation',
        'user_profile_last_modified_date': 'str'
    }

    attribute_map = {
        'address': 'address',
        'authentication_methods': 'authenticationMethods',
        'company_name': 'companyName',
        'display_organization_info': 'displayOrganizationInfo',
        'display_personal_info': 'displayPersonalInfo',
        'display_profile': 'displayProfile',
        'display_usage_history': 'displayUsageHistory',
        'profile_image_uri': 'profileImageUri',
        'title': 'title',
        'usage_history': 'usageHistory',
        'user_details': 'userDetails',
        'user_profile_last_modified_date': 'userProfileLastModifiedDate'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._authentication_methods = None
        self._company_name = None
        self._display_organization_info = None
        self._display_personal_info = None
        self._display_profile = None
        self._display_usage_history = None
        self._profile_image_uri = None
        self._title = None
        self._usage_history = None
        self._user_details = None
        self._user_profile_last_modified_date = None
        self.discriminator = None

        setattr(self, "_{}".format('address'), kwargs.get('address', None))
        setattr(self, "_{}".format('authentication_methods'), kwargs.get('authentication_methods', None))
        setattr(self, "_{}".format('company_name'), kwargs.get('company_name', None))
        setattr(self, "_{}".format('display_organization_info'), kwargs.get('display_organization_info', None))
        setattr(self, "_{}".format('display_personal_info'), kwargs.get('display_personal_info', None))
        setattr(self, "_{}".format('display_profile'), kwargs.get('display_profile', None))
        setattr(self, "_{}".format('display_usage_history'), kwargs.get('display_usage_history', None))
        setattr(self, "_{}".format('profile_image_uri'), kwargs.get('profile_image_uri', None))
        setattr(self, "_{}".format('title'), kwargs.get('title', None))
        setattr(self, "_{}".format('usage_history'), kwargs.get('usage_history', None))
        setattr(self, "_{}".format('user_details'), kwargs.get('user_details', None))
        setattr(self, "_{}".format('user_profile_last_modified_date'), kwargs.get('user_profile_last_modified_date', None))

    @property
    def address(self):
        """Gets the address of this UserProfile.  # noqa: E501

        The user's address.  # noqa: E501

        :return: The address of this UserProfile.  # noqa: E501
        :rtype: AddressInformation
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UserProfile.

        The user's address.  # noqa: E501

        :param address: The address of this UserProfile.  # noqa: E501
        :type: AddressInformation
        """

        self._address = address

    @property
    def authentication_methods(self):
        """Gets the authentication_methods of this UserProfile.  # noqa: E501

        These properties cannot be modified in the PUT.   Indicates the authentication methods used by the user.  # noqa: E501

        :return: The authentication_methods of this UserProfile.  # noqa: E501
        :rtype: list[AuthenticationMethod]
        """
        return self._authentication_methods

    @authentication_methods.setter
    def authentication_methods(self, authentication_methods):
        """Sets the authentication_methods of this UserProfile.

        These properties cannot be modified in the PUT.   Indicates the authentication methods used by the user.  # noqa: E501

        :param authentication_methods: The authentication_methods of this UserProfile.  # noqa: E501
        :type: list[AuthenticationMethod]
        """

        self._authentication_methods = authentication_methods

    @property
    def company_name(self):
        """Gets the company_name of this UserProfile.  # noqa: E501

        The name of the user's Company.  # noqa: E501

        :return: The company_name of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UserProfile.

        The name of the user's Company.  # noqa: E501

        :param company_name: The company_name of this UserProfile.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def display_organization_info(self):
        """Gets the display_organization_info of this UserProfile.  # noqa: E501

         When set to **true**, the user's company and title information are shown on the ID card.   # noqa: E501

        :return: The display_organization_info of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_organization_info

    @display_organization_info.setter
    def display_organization_info(self, display_organization_info):
        """Sets the display_organization_info of this UserProfile.

         When set to **true**, the user's company and title information are shown on the ID card.   # noqa: E501

        :param display_organization_info: The display_organization_info of this UserProfile.  # noqa: E501
        :type: str
        """

        self._display_organization_info = display_organization_info

    @property
    def display_personal_info(self):
        """Gets the display_personal_info of this UserProfile.  # noqa: E501

        When set to **true**, the user's Address and Phone number are shown on the ID card.  # noqa: E501

        :return: The display_personal_info of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_personal_info

    @display_personal_info.setter
    def display_personal_info(self, display_personal_info):
        """Sets the display_personal_info of this UserProfile.

        When set to **true**, the user's Address and Phone number are shown on the ID card.  # noqa: E501

        :param display_personal_info: The display_personal_info of this UserProfile.  # noqa: E501
        :type: str
        """

        self._display_personal_info = display_personal_info

    @property
    def display_profile(self):
        """Gets the display_profile of this UserProfile.  # noqa: E501

        When set to **true**, the user's ID card can be viewed from signed documents and envelope history.  # noqa: E501

        :return: The display_profile of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_profile

    @display_profile.setter
    def display_profile(self, display_profile):
        """Sets the display_profile of this UserProfile.

        When set to **true**, the user's ID card can be viewed from signed documents and envelope history.  # noqa: E501

        :param display_profile: The display_profile of this UserProfile.  # noqa: E501
        :type: str
        """

        self._display_profile = display_profile

    @property
    def display_usage_history(self):
        """Gets the display_usage_history of this UserProfile.  # noqa: E501

        When set to **true**, the user's usage information is shown on the ID card.  # noqa: E501

        :return: The display_usage_history of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_usage_history

    @display_usage_history.setter
    def display_usage_history(self, display_usage_history):
        """Sets the display_usage_history of this UserProfile.

        When set to **true**, the user's usage information is shown on the ID card.  # noqa: E501

        :param display_usage_history: The display_usage_history of this UserProfile.  # noqa: E501
        :type: str
        """

        self._display_usage_history = display_usage_history

    @property
    def profile_image_uri(self):
        """Gets the profile_image_uri of this UserProfile.  # noqa: E501

          # noqa: E501

        :return: The profile_image_uri of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._profile_image_uri

    @profile_image_uri.setter
    def profile_image_uri(self, profile_image_uri):
        """Sets the profile_image_uri of this UserProfile.

          # noqa: E501

        :param profile_image_uri: The profile_image_uri of this UserProfile.  # noqa: E501
        :type: str
        """

        self._profile_image_uri = profile_image_uri

    @property
    def title(self):
        """Gets the title of this UserProfile.  # noqa: E501

          # noqa: E501

        :return: The title of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserProfile.

          # noqa: E501

        :param title: The title of this UserProfile.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def usage_history(self):
        """Gets the usage_history of this UserProfile.  # noqa: E501

        A complex element consisting of:   - `lastSentDateTime`: The date and time the user last sent an envelope.  - `lastSignedDateTime`: The date and time the user last signed an envelope. - `sentCount`: The number of envelopes the user has sent. - `signedCount`: The number of envelopes the user has signed.    # noqa: E501

        :return: The usage_history of this UserProfile.  # noqa: E501
        :rtype: UsageHistory
        """
        return self._usage_history

    @usage_history.setter
    def usage_history(self, usage_history):
        """Sets the usage_history of this UserProfile.

        A complex element consisting of:   - `lastSentDateTime`: The date and time the user last sent an envelope.  - `lastSignedDateTime`: The date and time the user last signed an envelope. - `sentCount`: The number of envelopes the user has sent. - `signedCount`: The number of envelopes the user has signed.    # noqa: E501

        :param usage_history: The usage_history of this UserProfile.  # noqa: E501
        :type: UsageHistory
        """

        self._usage_history = usage_history

    @property
    def user_details(self):
        """Gets the user_details of this UserProfile.  # noqa: E501

          # noqa: E501

        :return: The user_details of this UserProfile.  # noqa: E501
        :rtype: UserInformation
        """
        return self._user_details

    @user_details.setter
    def user_details(self, user_details):
        """Sets the user_details of this UserProfile.

          # noqa: E501

        :param user_details: The user_details of this UserProfile.  # noqa: E501
        :type: UserInformation
        """

        self._user_details = user_details

    @property
    def user_profile_last_modified_date(self):
        """Gets the user_profile_last_modified_date of this UserProfile.  # noqa: E501

          # noqa: E501

        :return: The user_profile_last_modified_date of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._user_profile_last_modified_date

    @user_profile_last_modified_date.setter
    def user_profile_last_modified_date(self, user_profile_last_modified_date):
        """Sets the user_profile_last_modified_date of this UserProfile.

          # noqa: E501

        :param user_profile_last_modified_date: The user_profile_last_modified_date of this UserProfile.  # noqa: E501
        :type: str
        """

        self._user_profile_last_modified_date = user_profile_last_modified_date

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProfile):
            return True

        return self.to_dict() != other.to_dict()
