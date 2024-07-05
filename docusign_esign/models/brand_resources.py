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


class BrandResources(object):
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
        'created_by_user_info': 'UserInfo',
        'created_date': 'str',
        'data_not_saved_not_in_master': 'list[str]',
        'modified_by_user_info': 'UserInfo',
        'modified_date': 'str',
        'modified_templates': 'list[str]',
        'resources_content_type': 'str',
        'resources_content_uri': 'str'
    }

    attribute_map = {
        'created_by_user_info': 'createdByUserInfo',
        'created_date': 'createdDate',
        'data_not_saved_not_in_master': 'dataNotSavedNotInMaster',
        'modified_by_user_info': 'modifiedByUserInfo',
        'modified_date': 'modifiedDate',
        'modified_templates': 'modifiedTemplates',
        'resources_content_type': 'resourcesContentType',
        'resources_content_uri': 'resourcesContentUri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BrandResources - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_by_user_info = None
        self._created_date = None
        self._data_not_saved_not_in_master = None
        self._modified_by_user_info = None
        self._modified_date = None
        self._modified_templates = None
        self._resources_content_type = None
        self._resources_content_uri = None
        self.discriminator = None

        setattr(self, "_{}".format('created_by_user_info'), kwargs.get('created_by_user_info', None))
        setattr(self, "_{}".format('created_date'), kwargs.get('created_date', None))
        setattr(self, "_{}".format('data_not_saved_not_in_master'), kwargs.get('data_not_saved_not_in_master', None))
        setattr(self, "_{}".format('modified_by_user_info'), kwargs.get('modified_by_user_info', None))
        setattr(self, "_{}".format('modified_date'), kwargs.get('modified_date', None))
        setattr(self, "_{}".format('modified_templates'), kwargs.get('modified_templates', None))
        setattr(self, "_{}".format('resources_content_type'), kwargs.get('resources_content_type', None))
        setattr(self, "_{}".format('resources_content_uri'), kwargs.get('resources_content_uri', None))

    @property
    def created_by_user_info(self):
        """Gets the created_by_user_info of this BrandResources.  # noqa: E501

        The user ID of the user who created the brand resource.  # noqa: E501

        :return: The created_by_user_info of this BrandResources.  # noqa: E501
        :rtype: UserInfo
        """
        return self._created_by_user_info

    @created_by_user_info.setter
    def created_by_user_info(self, created_by_user_info):
        """Sets the created_by_user_info of this BrandResources.

        The user ID of the user who created the brand resource.  # noqa: E501

        :param created_by_user_info: The created_by_user_info of this BrandResources.  # noqa: E501
        :type: UserInfo
        """

        self._created_by_user_info = created_by_user_info

    @property
    def created_date(self):
        """Gets the created_date of this BrandResources.  # noqa: E501

          # noqa: E501

        :return: The created_date of this BrandResources.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this BrandResources.

          # noqa: E501

        :param created_date: The created_date of this BrandResources.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def data_not_saved_not_in_master(self):
        """Gets the data_not_saved_not_in_master of this BrandResources.  # noqa: E501

          # noqa: E501

        :return: The data_not_saved_not_in_master of this BrandResources.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_not_saved_not_in_master

    @data_not_saved_not_in_master.setter
    def data_not_saved_not_in_master(self, data_not_saved_not_in_master):
        """Sets the data_not_saved_not_in_master of this BrandResources.

          # noqa: E501

        :param data_not_saved_not_in_master: The data_not_saved_not_in_master of this BrandResources.  # noqa: E501
        :type: list[str]
        """

        self._data_not_saved_not_in_master = data_not_saved_not_in_master

    @property
    def modified_by_user_info(self):
        """Gets the modified_by_user_info of this BrandResources.  # noqa: E501

        Information about the user who last modified the brand resource.  # noqa: E501

        :return: The modified_by_user_info of this BrandResources.  # noqa: E501
        :rtype: UserInfo
        """
        return self._modified_by_user_info

    @modified_by_user_info.setter
    def modified_by_user_info(self, modified_by_user_info):
        """Sets the modified_by_user_info of this BrandResources.

        Information about the user who last modified the brand resource.  # noqa: E501

        :param modified_by_user_info: The modified_by_user_info of this BrandResources.  # noqa: E501
        :type: UserInfo
        """

        self._modified_by_user_info = modified_by_user_info

    @property
    def modified_date(self):
        """Gets the modified_date of this BrandResources.  # noqa: E501

          # noqa: E501

        :return: The modified_date of this BrandResources.  # noqa: E501
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this BrandResources.

          # noqa: E501

        :param modified_date: The modified_date of this BrandResources.  # noqa: E501
        :type: str
        """

        self._modified_date = modified_date

    @property
    def modified_templates(self):
        """Gets the modified_templates of this BrandResources.  # noqa: E501

          # noqa: E501

        :return: The modified_templates of this BrandResources.  # noqa: E501
        :rtype: list[str]
        """
        return self._modified_templates

    @modified_templates.setter
    def modified_templates(self, modified_templates):
        """Sets the modified_templates of this BrandResources.

          # noqa: E501

        :param modified_templates: The modified_templates of this BrandResources.  # noqa: E501
        :type: list[str]
        """

        self._modified_templates = modified_templates

    @property
    def resources_content_type(self):
        """Gets the resources_content_type of this BrandResources.  # noqa: E501

          # noqa: E501

        :return: The resources_content_type of this BrandResources.  # noqa: E501
        :rtype: str
        """
        return self._resources_content_type

    @resources_content_type.setter
    def resources_content_type(self, resources_content_type):
        """Sets the resources_content_type of this BrandResources.

          # noqa: E501

        :param resources_content_type: The resources_content_type of this BrandResources.  # noqa: E501
        :type: str
        """

        self._resources_content_type = resources_content_type

    @property
    def resources_content_uri(self):
        """Gets the resources_content_uri of this BrandResources.  # noqa: E501

          # noqa: E501

        :return: The resources_content_uri of this BrandResources.  # noqa: E501
        :rtype: str
        """
        return self._resources_content_uri

    @resources_content_uri.setter
    def resources_content_uri(self, resources_content_uri):
        """Sets the resources_content_uri of this BrandResources.

          # noqa: E501

        :param resources_content_uri: The resources_content_uri of this BrandResources.  # noqa: E501
        :type: str
        """

        self._resources_content_uri = resources_content_uri

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
        if issubclass(BrandResources, dict):
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
        if not isinstance(other, BrandResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrandResources):
            return True

        return self.to_dict() != other.to_dict()
