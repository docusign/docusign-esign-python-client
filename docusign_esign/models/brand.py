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


class Brand(object):
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
        'brand_company': 'str',
        'brand_id': 'str',
        'brand_name': 'str',
        'colors': 'list[NameValue]',
        'email_content': 'list[BrandEmailContent]',
        'error_details': 'ErrorDetails',
        'is_overriding_company_name': 'str',
        'is_sending_default': 'str',
        'is_signing_default': 'str',
        'landing_pages': 'list[NameValue]',
        'links': 'list[BrandLink]',
        'logos': 'BrandLogos',
        'resources': 'BrandResourceUrls'
    }

    attribute_map = {
        'brand_company': 'brandCompany',
        'brand_id': 'brandId',
        'brand_name': 'brandName',
        'colors': 'colors',
        'email_content': 'emailContent',
        'error_details': 'errorDetails',
        'is_overriding_company_name': 'isOverridingCompanyName',
        'is_sending_default': 'isSendingDefault',
        'is_signing_default': 'isSigningDefault',
        'landing_pages': 'landingPages',
        'links': 'links',
        'logos': 'logos',
        'resources': 'resources'
    }

    def __init__(self, brand_company=None, brand_id=None, brand_name=None, colors=None, email_content=None, error_details=None, is_overriding_company_name=None, is_sending_default=None, is_signing_default=None, landing_pages=None, links=None, logos=None, resources=None):  # noqa: E501
        """Brand - a model defined in Swagger"""  # noqa: E501

        self._brand_company = None
        self._brand_id = None
        self._brand_name = None
        self._colors = None
        self._email_content = None
        self._error_details = None
        self._is_overriding_company_name = None
        self._is_sending_default = None
        self._is_signing_default = None
        self._landing_pages = None
        self._links = None
        self._logos = None
        self._resources = None
        self.discriminator = None

        if brand_company is not None:
            self.brand_company = brand_company
        if brand_id is not None:
            self.brand_id = brand_id
        if brand_name is not None:
            self.brand_name = brand_name
        if colors is not None:
            self.colors = colors
        if email_content is not None:
            self.email_content = email_content
        if error_details is not None:
            self.error_details = error_details
        if is_overriding_company_name is not None:
            self.is_overriding_company_name = is_overriding_company_name
        if is_sending_default is not None:
            self.is_sending_default = is_sending_default
        if is_signing_default is not None:
            self.is_signing_default = is_signing_default
        if landing_pages is not None:
            self.landing_pages = landing_pages
        if links is not None:
            self.links = links
        if logos is not None:
            self.logos = logos
        if resources is not None:
            self.resources = resources

    @property
    def brand_company(self):
        """Gets the brand_company of this Brand.  # noqa: E501

        The name of the company associated with this brand.  # noqa: E501

        :return: The brand_company of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._brand_company

    @brand_company.setter
    def brand_company(self, brand_company):
        """Sets the brand_company of this Brand.

        The name of the company associated with this brand.  # noqa: E501

        :param brand_company: The brand_company of this Brand.  # noqa: E501
        :type: str
        """

        self._brand_company = brand_company

    @property
    def brand_id(self):
        """Gets the brand_id of this Brand.  # noqa: E501

        The ID used to identify a specific brand in API calls.  # noqa: E501

        :return: The brand_id of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        """Sets the brand_id of this Brand.

        The ID used to identify a specific brand in API calls.  # noqa: E501

        :param brand_id: The brand_id of this Brand.  # noqa: E501
        :type: str
        """

        self._brand_id = brand_id

    @property
    def brand_name(self):
        """Gets the brand_name of this Brand.  # noqa: E501

        The name of the brand.  # noqa: E501

        :return: The brand_name of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this Brand.

        The name of the brand.  # noqa: E501

        :param brand_name: The brand_name of this Brand.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    @property
    def colors(self):
        """Gets the colors of this Brand.  # noqa: E501

          # noqa: E501

        :return: The colors of this Brand.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this Brand.

          # noqa: E501

        :param colors: The colors of this Brand.  # noqa: E501
        :type: list[NameValue]
        """

        self._colors = colors

    @property
    def email_content(self):
        """Gets the email_content of this Brand.  # noqa: E501

          # noqa: E501

        :return: The email_content of this Brand.  # noqa: E501
        :rtype: list[BrandEmailContent]
        """
        return self._email_content

    @email_content.setter
    def email_content(self, email_content):
        """Sets the email_content of this Brand.

          # noqa: E501

        :param email_content: The email_content of this Brand.  # noqa: E501
        :type: list[BrandEmailContent]
        """

        self._email_content = email_content

    @property
    def error_details(self):
        """Gets the error_details of this Brand.  # noqa: E501


        :return: The error_details of this Brand.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Brand.


        :param error_details: The error_details of this Brand.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def is_overriding_company_name(self):
        """Gets the is_overriding_company_name of this Brand.  # noqa: E501

          # noqa: E501

        :return: The is_overriding_company_name of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._is_overriding_company_name

    @is_overriding_company_name.setter
    def is_overriding_company_name(self, is_overriding_company_name):
        """Sets the is_overriding_company_name of this Brand.

          # noqa: E501

        :param is_overriding_company_name: The is_overriding_company_name of this Brand.  # noqa: E501
        :type: str
        """

        self._is_overriding_company_name = is_overriding_company_name

    @property
    def is_sending_default(self):
        """Gets the is_sending_default of this Brand.  # noqa: E501

          # noqa: E501

        :return: The is_sending_default of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._is_sending_default

    @is_sending_default.setter
    def is_sending_default(self, is_sending_default):
        """Sets the is_sending_default of this Brand.

          # noqa: E501

        :param is_sending_default: The is_sending_default of this Brand.  # noqa: E501
        :type: str
        """

        self._is_sending_default = is_sending_default

    @property
    def is_signing_default(self):
        """Gets the is_signing_default of this Brand.  # noqa: E501

          # noqa: E501

        :return: The is_signing_default of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._is_signing_default

    @is_signing_default.setter
    def is_signing_default(self, is_signing_default):
        """Sets the is_signing_default of this Brand.

          # noqa: E501

        :param is_signing_default: The is_signing_default of this Brand.  # noqa: E501
        :type: str
        """

        self._is_signing_default = is_signing_default

    @property
    def landing_pages(self):
        """Gets the landing_pages of this Brand.  # noqa: E501

          # noqa: E501

        :return: The landing_pages of this Brand.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._landing_pages

    @landing_pages.setter
    def landing_pages(self, landing_pages):
        """Sets the landing_pages of this Brand.

          # noqa: E501

        :param landing_pages: The landing_pages of this Brand.  # noqa: E501
        :type: list[NameValue]
        """

        self._landing_pages = landing_pages

    @property
    def links(self):
        """Gets the links of this Brand.  # noqa: E501

          # noqa: E501

        :return: The links of this Brand.  # noqa: E501
        :rtype: list[BrandLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Brand.

          # noqa: E501

        :param links: The links of this Brand.  # noqa: E501
        :type: list[BrandLink]
        """

        self._links = links

    @property
    def logos(self):
        """Gets the logos of this Brand.  # noqa: E501


        :return: The logos of this Brand.  # noqa: E501
        :rtype: BrandLogos
        """
        return self._logos

    @logos.setter
    def logos(self, logos):
        """Sets the logos of this Brand.


        :param logos: The logos of this Brand.  # noqa: E501
        :type: BrandLogos
        """

        self._logos = logos

    @property
    def resources(self):
        """Gets the resources of this Brand.  # noqa: E501


        :return: The resources of this Brand.  # noqa: E501
        :rtype: BrandResourceUrls
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Brand.


        :param resources: The resources of this Brand.  # noqa: E501
        :type: BrandResourceUrls
        """

        self._resources = resources

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
        if issubclass(Brand, dict):
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
        if not isinstance(other, Brand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
