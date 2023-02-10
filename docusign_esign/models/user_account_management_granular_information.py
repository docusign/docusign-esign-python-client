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


class UserAccountManagementGranularInformation(object):
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
        'can_manage_account_security_settings': 'str',
        'can_manage_account_security_settings_metadata': 'SettingsMetadata',
        'can_manage_account_settings': 'str',
        'can_manage_account_settings_metadata': 'SettingsMetadata',
        'can_manage_admins': 'str',
        'can_manage_admins_metadata': 'SettingsMetadata',
        'can_manage_connect': 'str',
        'can_manage_connect_metadata': 'SettingsMetadata',
        'can_manage_document_retention': 'str',
        'can_manage_document_retention_metadata': 'SettingsMetadata',
        'can_manage_envelope_transfer': 'str',
        'can_manage_envelope_transfer_metadata': 'SettingsMetadata',
        'can_manage_groups_but_not_users': 'str',
        'can_manage_groups_but_not_users_metadata': 'SettingsMetadata',
        'can_manage_joint_agreements': 'str',
        'can_manage_joint_agreements_metadata': 'SettingsMetadata',
        'can_manage_reporting': 'str',
        'can_manage_reporting_metadata': 'SettingsMetadata',
        'can_manage_sharing': 'str',
        'can_manage_sharing_metadata': 'SettingsMetadata',
        'can_manage_signing_groups': 'str',
        'can_manage_signing_groups_metadata': 'SettingsMetadata',
        'can_manage_stamps': 'str',
        'can_manage_stamps_metadata': 'SettingsMetadata',
        'can_manage_users': 'str',
        'can_manage_users_metadata': 'SettingsMetadata',
        'can_view_users': 'str'
    }

    attribute_map = {
        'can_manage_account_security_settings': 'canManageAccountSecuritySettings',
        'can_manage_account_security_settings_metadata': 'canManageAccountSecuritySettingsMetadata',
        'can_manage_account_settings': 'canManageAccountSettings',
        'can_manage_account_settings_metadata': 'canManageAccountSettingsMetadata',
        'can_manage_admins': 'canManageAdmins',
        'can_manage_admins_metadata': 'canManageAdminsMetadata',
        'can_manage_connect': 'canManageConnect',
        'can_manage_connect_metadata': 'canManageConnectMetadata',
        'can_manage_document_retention': 'canManageDocumentRetention',
        'can_manage_document_retention_metadata': 'canManageDocumentRetentionMetadata',
        'can_manage_envelope_transfer': 'canManageEnvelopeTransfer',
        'can_manage_envelope_transfer_metadata': 'canManageEnvelopeTransferMetadata',
        'can_manage_groups_but_not_users': 'canManageGroupsButNotUsers',
        'can_manage_groups_but_not_users_metadata': 'canManageGroupsButNotUsersMetadata',
        'can_manage_joint_agreements': 'canManageJointAgreements',
        'can_manage_joint_agreements_metadata': 'canManageJointAgreementsMetadata',
        'can_manage_reporting': 'canManageReporting',
        'can_manage_reporting_metadata': 'canManageReportingMetadata',
        'can_manage_sharing': 'canManageSharing',
        'can_manage_sharing_metadata': 'canManageSharingMetadata',
        'can_manage_signing_groups': 'canManageSigningGroups',
        'can_manage_signing_groups_metadata': 'canManageSigningGroupsMetadata',
        'can_manage_stamps': 'canManageStamps',
        'can_manage_stamps_metadata': 'canManageStampsMetadata',
        'can_manage_users': 'canManageUsers',
        'can_manage_users_metadata': 'canManageUsersMetadata',
        'can_view_users': 'canViewUsers'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserAccountManagementGranularInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_manage_account_security_settings = None
        self._can_manage_account_security_settings_metadata = None
        self._can_manage_account_settings = None
        self._can_manage_account_settings_metadata = None
        self._can_manage_admins = None
        self._can_manage_admins_metadata = None
        self._can_manage_connect = None
        self._can_manage_connect_metadata = None
        self._can_manage_document_retention = None
        self._can_manage_document_retention_metadata = None
        self._can_manage_envelope_transfer = None
        self._can_manage_envelope_transfer_metadata = None
        self._can_manage_groups_but_not_users = None
        self._can_manage_groups_but_not_users_metadata = None
        self._can_manage_joint_agreements = None
        self._can_manage_joint_agreements_metadata = None
        self._can_manage_reporting = None
        self._can_manage_reporting_metadata = None
        self._can_manage_sharing = None
        self._can_manage_sharing_metadata = None
        self._can_manage_signing_groups = None
        self._can_manage_signing_groups_metadata = None
        self._can_manage_stamps = None
        self._can_manage_stamps_metadata = None
        self._can_manage_users = None
        self._can_manage_users_metadata = None
        self._can_view_users = None
        self.discriminator = None

        setattr(self, "_{}".format('can_manage_account_security_settings'), kwargs.get('can_manage_account_security_settings', None))
        setattr(self, "_{}".format('can_manage_account_security_settings_metadata'), kwargs.get('can_manage_account_security_settings_metadata', None))
        setattr(self, "_{}".format('can_manage_account_settings'), kwargs.get('can_manage_account_settings', None))
        setattr(self, "_{}".format('can_manage_account_settings_metadata'), kwargs.get('can_manage_account_settings_metadata', None))
        setattr(self, "_{}".format('can_manage_admins'), kwargs.get('can_manage_admins', None))
        setattr(self, "_{}".format('can_manage_admins_metadata'), kwargs.get('can_manage_admins_metadata', None))
        setattr(self, "_{}".format('can_manage_connect'), kwargs.get('can_manage_connect', None))
        setattr(self, "_{}".format('can_manage_connect_metadata'), kwargs.get('can_manage_connect_metadata', None))
        setattr(self, "_{}".format('can_manage_document_retention'), kwargs.get('can_manage_document_retention', None))
        setattr(self, "_{}".format('can_manage_document_retention_metadata'), kwargs.get('can_manage_document_retention_metadata', None))
        setattr(self, "_{}".format('can_manage_envelope_transfer'), kwargs.get('can_manage_envelope_transfer', None))
        setattr(self, "_{}".format('can_manage_envelope_transfer_metadata'), kwargs.get('can_manage_envelope_transfer_metadata', None))
        setattr(self, "_{}".format('can_manage_groups_but_not_users'), kwargs.get('can_manage_groups_but_not_users', None))
        setattr(self, "_{}".format('can_manage_groups_but_not_users_metadata'), kwargs.get('can_manage_groups_but_not_users_metadata', None))
        setattr(self, "_{}".format('can_manage_joint_agreements'), kwargs.get('can_manage_joint_agreements', None))
        setattr(self, "_{}".format('can_manage_joint_agreements_metadata'), kwargs.get('can_manage_joint_agreements_metadata', None))
        setattr(self, "_{}".format('can_manage_reporting'), kwargs.get('can_manage_reporting', None))
        setattr(self, "_{}".format('can_manage_reporting_metadata'), kwargs.get('can_manage_reporting_metadata', None))
        setattr(self, "_{}".format('can_manage_sharing'), kwargs.get('can_manage_sharing', None))
        setattr(self, "_{}".format('can_manage_sharing_metadata'), kwargs.get('can_manage_sharing_metadata', None))
        setattr(self, "_{}".format('can_manage_signing_groups'), kwargs.get('can_manage_signing_groups', None))
        setattr(self, "_{}".format('can_manage_signing_groups_metadata'), kwargs.get('can_manage_signing_groups_metadata', None))
        setattr(self, "_{}".format('can_manage_stamps'), kwargs.get('can_manage_stamps', None))
        setattr(self, "_{}".format('can_manage_stamps_metadata'), kwargs.get('can_manage_stamps_metadata', None))
        setattr(self, "_{}".format('can_manage_users'), kwargs.get('can_manage_users', None))
        setattr(self, "_{}".format('can_manage_users_metadata'), kwargs.get('can_manage_users_metadata', None))
        setattr(self, "_{}".format('can_view_users'), kwargs.get('can_view_users', None))

    @property
    def can_manage_account_security_settings(self):
        """Gets the can_manage_account_security_settings of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_account_security_settings of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_account_security_settings

    @can_manage_account_security_settings.setter
    def can_manage_account_security_settings(self, can_manage_account_security_settings):
        """Sets the can_manage_account_security_settings of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_account_security_settings: The can_manage_account_security_settings of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_account_security_settings = can_manage_account_security_settings

    @property
    def can_manage_account_security_settings_metadata(self):
        """Gets the can_manage_account_security_settings_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_account_security_settings_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_account_security_settings_metadata

    @can_manage_account_security_settings_metadata.setter
    def can_manage_account_security_settings_metadata(self, can_manage_account_security_settings_metadata):
        """Sets the can_manage_account_security_settings_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_account_security_settings_metadata: The can_manage_account_security_settings_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_account_security_settings_metadata = can_manage_account_security_settings_metadata

    @property
    def can_manage_account_settings(self):
        """Gets the can_manage_account_settings of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_account_settings of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_account_settings

    @can_manage_account_settings.setter
    def can_manage_account_settings(self, can_manage_account_settings):
        """Sets the can_manage_account_settings of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_account_settings: The can_manage_account_settings of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_account_settings = can_manage_account_settings

    @property
    def can_manage_account_settings_metadata(self):
        """Gets the can_manage_account_settings_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_account_settings_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_account_settings_metadata

    @can_manage_account_settings_metadata.setter
    def can_manage_account_settings_metadata(self, can_manage_account_settings_metadata):
        """Sets the can_manage_account_settings_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_account_settings_metadata: The can_manage_account_settings_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_account_settings_metadata = can_manage_account_settings_metadata

    @property
    def can_manage_admins(self):
        """Gets the can_manage_admins of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_admins of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_admins

    @can_manage_admins.setter
    def can_manage_admins(self, can_manage_admins):
        """Sets the can_manage_admins of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_admins: The can_manage_admins of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_admins = can_manage_admins

    @property
    def can_manage_admins_metadata(self):
        """Gets the can_manage_admins_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

        Metadata that indicates whether the `canManageAdmins` property is editable.   # noqa: E501

        :return: The can_manage_admins_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_admins_metadata

    @can_manage_admins_metadata.setter
    def can_manage_admins_metadata(self, can_manage_admins_metadata):
        """Sets the can_manage_admins_metadata of this UserAccountManagementGranularInformation.

        Metadata that indicates whether the `canManageAdmins` property is editable.   # noqa: E501

        :param can_manage_admins_metadata: The can_manage_admins_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_admins_metadata = can_manage_admins_metadata

    @property
    def can_manage_connect(self):
        """Gets the can_manage_connect of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_connect of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_connect

    @can_manage_connect.setter
    def can_manage_connect(self, can_manage_connect):
        """Sets the can_manage_connect of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_connect: The can_manage_connect of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_connect = can_manage_connect

    @property
    def can_manage_connect_metadata(self):
        """Gets the can_manage_connect_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_connect_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_connect_metadata

    @can_manage_connect_metadata.setter
    def can_manage_connect_metadata(self, can_manage_connect_metadata):
        """Sets the can_manage_connect_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_connect_metadata: The can_manage_connect_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_connect_metadata = can_manage_connect_metadata

    @property
    def can_manage_document_retention(self):
        """Gets the can_manage_document_retention of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_document_retention of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_document_retention

    @can_manage_document_retention.setter
    def can_manage_document_retention(self, can_manage_document_retention):
        """Sets the can_manage_document_retention of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_document_retention: The can_manage_document_retention of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_document_retention = can_manage_document_retention

    @property
    def can_manage_document_retention_metadata(self):
        """Gets the can_manage_document_retention_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_document_retention_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_document_retention_metadata

    @can_manage_document_retention_metadata.setter
    def can_manage_document_retention_metadata(self, can_manage_document_retention_metadata):
        """Sets the can_manage_document_retention_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_document_retention_metadata: The can_manage_document_retention_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_document_retention_metadata = can_manage_document_retention_metadata

    @property
    def can_manage_envelope_transfer(self):
        """Gets the can_manage_envelope_transfer of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_envelope_transfer of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_envelope_transfer

    @can_manage_envelope_transfer.setter
    def can_manage_envelope_transfer(self, can_manage_envelope_transfer):
        """Sets the can_manage_envelope_transfer of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_envelope_transfer: The can_manage_envelope_transfer of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_envelope_transfer = can_manage_envelope_transfer

    @property
    def can_manage_envelope_transfer_metadata(self):
        """Gets the can_manage_envelope_transfer_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_envelope_transfer_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_envelope_transfer_metadata

    @can_manage_envelope_transfer_metadata.setter
    def can_manage_envelope_transfer_metadata(self, can_manage_envelope_transfer_metadata):
        """Sets the can_manage_envelope_transfer_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_envelope_transfer_metadata: The can_manage_envelope_transfer_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_envelope_transfer_metadata = can_manage_envelope_transfer_metadata

    @property
    def can_manage_groups_but_not_users(self):
        """Gets the can_manage_groups_but_not_users of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_groups_but_not_users of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_groups_but_not_users

    @can_manage_groups_but_not_users.setter
    def can_manage_groups_but_not_users(self, can_manage_groups_but_not_users):
        """Sets the can_manage_groups_but_not_users of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_groups_but_not_users: The can_manage_groups_but_not_users of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_groups_but_not_users = can_manage_groups_but_not_users

    @property
    def can_manage_groups_but_not_users_metadata(self):
        """Gets the can_manage_groups_but_not_users_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_groups_but_not_users_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_groups_but_not_users_metadata

    @can_manage_groups_but_not_users_metadata.setter
    def can_manage_groups_but_not_users_metadata(self, can_manage_groups_but_not_users_metadata):
        """Sets the can_manage_groups_but_not_users_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_groups_but_not_users_metadata: The can_manage_groups_but_not_users_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_groups_but_not_users_metadata = can_manage_groups_but_not_users_metadata

    @property
    def can_manage_joint_agreements(self):
        """Gets the can_manage_joint_agreements of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_joint_agreements of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_joint_agreements

    @can_manage_joint_agreements.setter
    def can_manage_joint_agreements(self, can_manage_joint_agreements):
        """Sets the can_manage_joint_agreements of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_joint_agreements: The can_manage_joint_agreements of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_joint_agreements = can_manage_joint_agreements

    @property
    def can_manage_joint_agreements_metadata(self):
        """Gets the can_manage_joint_agreements_metadata of this UserAccountManagementGranularInformation.  # noqa: E501


        :return: The can_manage_joint_agreements_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_joint_agreements_metadata

    @can_manage_joint_agreements_metadata.setter
    def can_manage_joint_agreements_metadata(self, can_manage_joint_agreements_metadata):
        """Sets the can_manage_joint_agreements_metadata of this UserAccountManagementGranularInformation.


        :param can_manage_joint_agreements_metadata: The can_manage_joint_agreements_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_joint_agreements_metadata = can_manage_joint_agreements_metadata

    @property
    def can_manage_reporting(self):
        """Gets the can_manage_reporting of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_reporting of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_reporting

    @can_manage_reporting.setter
    def can_manage_reporting(self, can_manage_reporting):
        """Sets the can_manage_reporting of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_reporting: The can_manage_reporting of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_reporting = can_manage_reporting

    @property
    def can_manage_reporting_metadata(self):
        """Gets the can_manage_reporting_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_reporting_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_reporting_metadata

    @can_manage_reporting_metadata.setter
    def can_manage_reporting_metadata(self, can_manage_reporting_metadata):
        """Sets the can_manage_reporting_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_reporting_metadata: The can_manage_reporting_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_reporting_metadata = can_manage_reporting_metadata

    @property
    def can_manage_sharing(self):
        """Gets the can_manage_sharing of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_sharing of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_sharing

    @can_manage_sharing.setter
    def can_manage_sharing(self, can_manage_sharing):
        """Sets the can_manage_sharing of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_sharing: The can_manage_sharing of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_sharing = can_manage_sharing

    @property
    def can_manage_sharing_metadata(self):
        """Gets the can_manage_sharing_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

        Metadata that indicates whether the `canManageSharing` property is editable.   # noqa: E501

        :return: The can_manage_sharing_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_sharing_metadata

    @can_manage_sharing_metadata.setter
    def can_manage_sharing_metadata(self, can_manage_sharing_metadata):
        """Sets the can_manage_sharing_metadata of this UserAccountManagementGranularInformation.

        Metadata that indicates whether the `canManageSharing` property is editable.   # noqa: E501

        :param can_manage_sharing_metadata: The can_manage_sharing_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_sharing_metadata = can_manage_sharing_metadata

    @property
    def can_manage_signing_groups(self):
        """Gets the can_manage_signing_groups of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_signing_groups of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_signing_groups

    @can_manage_signing_groups.setter
    def can_manage_signing_groups(self, can_manage_signing_groups):
        """Sets the can_manage_signing_groups of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_signing_groups: The can_manage_signing_groups of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_signing_groups = can_manage_signing_groups

    @property
    def can_manage_signing_groups_metadata(self):
        """Gets the can_manage_signing_groups_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_signing_groups_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_signing_groups_metadata

    @can_manage_signing_groups_metadata.setter
    def can_manage_signing_groups_metadata(self, can_manage_signing_groups_metadata):
        """Sets the can_manage_signing_groups_metadata of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_signing_groups_metadata: The can_manage_signing_groups_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_signing_groups_metadata = can_manage_signing_groups_metadata

    @property
    def can_manage_stamps(self):
        """Gets the can_manage_stamps of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_stamps of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_stamps

    @can_manage_stamps.setter
    def can_manage_stamps(self, can_manage_stamps):
        """Sets the can_manage_stamps of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_stamps: The can_manage_stamps of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_stamps = can_manage_stamps

    @property
    def can_manage_stamps_metadata(self):
        """Gets the can_manage_stamps_metadata of this UserAccountManagementGranularInformation.  # noqa: E501


        :return: The can_manage_stamps_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_stamps_metadata

    @can_manage_stamps_metadata.setter
    def can_manage_stamps_metadata(self, can_manage_stamps_metadata):
        """Sets the can_manage_stamps_metadata of this UserAccountManagementGranularInformation.


        :param can_manage_stamps_metadata: The can_manage_stamps_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_stamps_metadata = can_manage_stamps_metadata

    @property
    def can_manage_users(self):
        """Gets the can_manage_users of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_manage_users of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_manage_users

    @can_manage_users.setter
    def can_manage_users(self, can_manage_users):
        """Sets the can_manage_users of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_manage_users: The can_manage_users of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_manage_users = can_manage_users

    @property
    def can_manage_users_metadata(self):
        """Gets the can_manage_users_metadata of this UserAccountManagementGranularInformation.  # noqa: E501

        Metadata that indicates whether the `canManageUsers` property is editable.   # noqa: E501

        :return: The can_manage_users_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: SettingsMetadata
        """
        return self._can_manage_users_metadata

    @can_manage_users_metadata.setter
    def can_manage_users_metadata(self, can_manage_users_metadata):
        """Sets the can_manage_users_metadata of this UserAccountManagementGranularInformation.

        Metadata that indicates whether the `canManageUsers` property is editable.   # noqa: E501

        :param can_manage_users_metadata: The can_manage_users_metadata of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: SettingsMetadata
        """

        self._can_manage_users_metadata = can_manage_users_metadata

    @property
    def can_view_users(self):
        """Gets the can_view_users of this UserAccountManagementGranularInformation.  # noqa: E501

          # noqa: E501

        :return: The can_view_users of this UserAccountManagementGranularInformation.  # noqa: E501
        :rtype: str
        """
        return self._can_view_users

    @can_view_users.setter
    def can_view_users(self, can_view_users):
        """Sets the can_view_users of this UserAccountManagementGranularInformation.

          # noqa: E501

        :param can_view_users: The can_view_users of this UserAccountManagementGranularInformation.  # noqa: E501
        :type: str
        """

        self._can_view_users = can_view_users

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
        if issubclass(UserAccountManagementGranularInformation, dict):
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
        if not isinstance(other, UserAccountManagementGranularInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAccountManagementGranularInformation):
            return True

        return self.to_dict() != other.to_dict()
