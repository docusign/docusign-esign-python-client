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


class ServiceInformation(object):
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
        'build_branch': 'str',
        'build_branch_deployed_date_time': 'str',
        'build_sha': 'str',
        'build_version': 'str',
        'linked_sites': 'list[str]',
        'service_versions': 'list[ServiceVersion]'
    }

    attribute_map = {
        'build_branch': 'buildBranch',
        'build_branch_deployed_date_time': 'buildBranchDeployedDateTime',
        'build_sha': 'buildSHA',
        'build_version': 'buildVersion',
        'linked_sites': 'linkedSites',
        'service_versions': 'serviceVersions'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ServiceInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._build_branch = None
        self._build_branch_deployed_date_time = None
        self._build_sha = None
        self._build_version = None
        self._linked_sites = None
        self._service_versions = None
        self.discriminator = None

        setattr(self, "_{}".format('build_branch'), kwargs.get('build_branch', None))
        setattr(self, "_{}".format('build_branch_deployed_date_time'), kwargs.get('build_branch_deployed_date_time', None))
        setattr(self, "_{}".format('build_sha'), kwargs.get('build_sha', None))
        setattr(self, "_{}".format('build_version'), kwargs.get('build_version', None))
        setattr(self, "_{}".format('linked_sites'), kwargs.get('linked_sites', None))
        setattr(self, "_{}".format('service_versions'), kwargs.get('service_versions', None))

    @property
    def build_branch(self):
        """Gets the build_branch of this ServiceInformation.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The build_branch of this ServiceInformation.  # noqa: E501
        :rtype: str
        """
        return self._build_branch

    @build_branch.setter
    def build_branch(self, build_branch):
        """Sets the build_branch of this ServiceInformation.

        Reserved: TBD  # noqa: E501

        :param build_branch: The build_branch of this ServiceInformation.  # noqa: E501
        :type: str
        """

        self._build_branch = build_branch

    @property
    def build_branch_deployed_date_time(self):
        """Gets the build_branch_deployed_date_time of this ServiceInformation.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The build_branch_deployed_date_time of this ServiceInformation.  # noqa: E501
        :rtype: str
        """
        return self._build_branch_deployed_date_time

    @build_branch_deployed_date_time.setter
    def build_branch_deployed_date_time(self, build_branch_deployed_date_time):
        """Sets the build_branch_deployed_date_time of this ServiceInformation.

        Reserved: TBD  # noqa: E501

        :param build_branch_deployed_date_time: The build_branch_deployed_date_time of this ServiceInformation.  # noqa: E501
        :type: str
        """

        self._build_branch_deployed_date_time = build_branch_deployed_date_time

    @property
    def build_sha(self):
        """Gets the build_sha of this ServiceInformation.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The build_sha of this ServiceInformation.  # noqa: E501
        :rtype: str
        """
        return self._build_sha

    @build_sha.setter
    def build_sha(self, build_sha):
        """Sets the build_sha of this ServiceInformation.

        Reserved: TBD  # noqa: E501

        :param build_sha: The build_sha of this ServiceInformation.  # noqa: E501
        :type: str
        """

        self._build_sha = build_sha

    @property
    def build_version(self):
        """Gets the build_version of this ServiceInformation.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The build_version of this ServiceInformation.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this ServiceInformation.

        Reserved: TBD  # noqa: E501

        :param build_version: The build_version of this ServiceInformation.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

    @property
    def linked_sites(self):
        """Gets the linked_sites of this ServiceInformation.  # noqa: E501

          # noqa: E501

        :return: The linked_sites of this ServiceInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._linked_sites

    @linked_sites.setter
    def linked_sites(self, linked_sites):
        """Sets the linked_sites of this ServiceInformation.

          # noqa: E501

        :param linked_sites: The linked_sites of this ServiceInformation.  # noqa: E501
        :type: list[str]
        """

        self._linked_sites = linked_sites

    @property
    def service_versions(self):
        """Gets the service_versions of this ServiceInformation.  # noqa: E501

          # noqa: E501

        :return: The service_versions of this ServiceInformation.  # noqa: E501
        :rtype: list[ServiceVersion]
        """
        return self._service_versions

    @service_versions.setter
    def service_versions(self, service_versions):
        """Sets the service_versions of this ServiceInformation.

          # noqa: E501

        :param service_versions: The service_versions of this ServiceInformation.  # noqa: E501
        :type: list[ServiceVersion]
        """

        self._service_versions = service_versions

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
        if issubclass(ServiceInformation, dict):
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
        if not isinstance(other, ServiceInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceInformation):
            return True

        return self.to_dict() != other.to_dict()
