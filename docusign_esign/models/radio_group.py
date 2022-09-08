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


class RadioGroup(object):
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
        'conditional_parent_label': 'str',
        'conditional_parent_label_metadata': 'PropertyMetadata',
        'conditional_parent_value': 'str',
        'conditional_parent_value_metadata': 'PropertyMetadata',
        'document_id': 'str',
        'document_id_metadata': 'PropertyMetadata',
        'group_name': 'str',
        'group_name_metadata': 'PropertyMetadata',
        'original_value': 'str',
        'original_value_metadata': 'PropertyMetadata',
        'radios': 'list[Radio]',
        'recipient_id': 'str',
        'recipient_id_guid': 'str',
        'recipient_id_guid_metadata': 'PropertyMetadata',
        'recipient_id_metadata': 'PropertyMetadata',
        'require_all': 'str',
        'require_all_metadata': 'PropertyMetadata',
        'require_initial_on_shared_change': 'str',
        'require_initial_on_shared_change_metadata': 'PropertyMetadata',
        'shared': 'str',
        'shared_metadata': 'PropertyMetadata',
        'share_to_recipients': 'str',
        'share_to_recipients_metadata': 'PropertyMetadata',
        'tab_type': 'str',
        'tab_type_metadata': 'PropertyMetadata',
        'template_locked': 'str',
        'template_locked_metadata': 'PropertyMetadata',
        'template_required': 'str',
        'template_required_metadata': 'PropertyMetadata',
        'tooltip': 'str',
        'tooltip_metadata': 'PropertyMetadata',
        'value': 'str',
        'value_metadata': 'PropertyMetadata'
    }

    attribute_map = {
        'conditional_parent_label': 'conditionalParentLabel',
        'conditional_parent_label_metadata': 'conditionalParentLabelMetadata',
        'conditional_parent_value': 'conditionalParentValue',
        'conditional_parent_value_metadata': 'conditionalParentValueMetadata',
        'document_id': 'documentId',
        'document_id_metadata': 'documentIdMetadata',
        'group_name': 'groupName',
        'group_name_metadata': 'groupNameMetadata',
        'original_value': 'originalValue',
        'original_value_metadata': 'originalValueMetadata',
        'radios': 'radios',
        'recipient_id': 'recipientId',
        'recipient_id_guid': 'recipientIdGuid',
        'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
        'recipient_id_metadata': 'recipientIdMetadata',
        'require_all': 'requireAll',
        'require_all_metadata': 'requireAllMetadata',
        'require_initial_on_shared_change': 'requireInitialOnSharedChange',
        'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
        'shared': 'shared',
        'shared_metadata': 'sharedMetadata',
        'share_to_recipients': 'shareToRecipients',
        'share_to_recipients_metadata': 'shareToRecipientsMetadata',
        'tab_type': 'tabType',
        'tab_type_metadata': 'tabTypeMetadata',
        'template_locked': 'templateLocked',
        'template_locked_metadata': 'templateLockedMetadata',
        'template_required': 'templateRequired',
        'template_required_metadata': 'templateRequiredMetadata',
        'tooltip': 'tooltip',
        'tooltip_metadata': 'tooltipMetadata',
        'value': 'value',
        'value_metadata': 'valueMetadata'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RadioGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._conditional_parent_label = None
        self._conditional_parent_label_metadata = None
        self._conditional_parent_value = None
        self._conditional_parent_value_metadata = None
        self._document_id = None
        self._document_id_metadata = None
        self._group_name = None
        self._group_name_metadata = None
        self._original_value = None
        self._original_value_metadata = None
        self._radios = None
        self._recipient_id = None
        self._recipient_id_guid = None
        self._recipient_id_guid_metadata = None
        self._recipient_id_metadata = None
        self._require_all = None
        self._require_all_metadata = None
        self._require_initial_on_shared_change = None
        self._require_initial_on_shared_change_metadata = None
        self._shared = None
        self._shared_metadata = None
        self._share_to_recipients = None
        self._share_to_recipients_metadata = None
        self._tab_type = None
        self._tab_type_metadata = None
        self._template_locked = None
        self._template_locked_metadata = None
        self._template_required = None
        self._template_required_metadata = None
        self._tooltip = None
        self._tooltip_metadata = None
        self._value = None
        self._value_metadata = None
        self.discriminator = None

        setattr(self, "_{}".format('conditional_parent_label'), kwargs.get('conditional_parent_label', None))
        setattr(self, "_{}".format('conditional_parent_label_metadata'), kwargs.get('conditional_parent_label_metadata', None))
        setattr(self, "_{}".format('conditional_parent_value'), kwargs.get('conditional_parent_value', None))
        setattr(self, "_{}".format('conditional_parent_value_metadata'), kwargs.get('conditional_parent_value_metadata', None))
        setattr(self, "_{}".format('document_id'), kwargs.get('document_id', None))
        setattr(self, "_{}".format('document_id_metadata'), kwargs.get('document_id_metadata', None))
        setattr(self, "_{}".format('group_name'), kwargs.get('group_name', None))
        setattr(self, "_{}".format('group_name_metadata'), kwargs.get('group_name_metadata', None))
        setattr(self, "_{}".format('original_value'), kwargs.get('original_value', None))
        setattr(self, "_{}".format('original_value_metadata'), kwargs.get('original_value_metadata', None))
        setattr(self, "_{}".format('radios'), kwargs.get('radios', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('recipient_id_guid'), kwargs.get('recipient_id_guid', None))
        setattr(self, "_{}".format('recipient_id_guid_metadata'), kwargs.get('recipient_id_guid_metadata', None))
        setattr(self, "_{}".format('recipient_id_metadata'), kwargs.get('recipient_id_metadata', None))
        setattr(self, "_{}".format('require_all'), kwargs.get('require_all', None))
        setattr(self, "_{}".format('require_all_metadata'), kwargs.get('require_all_metadata', None))
        setattr(self, "_{}".format('require_initial_on_shared_change'), kwargs.get('require_initial_on_shared_change', None))
        setattr(self, "_{}".format('require_initial_on_shared_change_metadata'), kwargs.get('require_initial_on_shared_change_metadata', None))
        setattr(self, "_{}".format('shared'), kwargs.get('shared', None))
        setattr(self, "_{}".format('shared_metadata'), kwargs.get('shared_metadata', None))
        setattr(self, "_{}".format('share_to_recipients'), kwargs.get('share_to_recipients', None))
        setattr(self, "_{}".format('share_to_recipients_metadata'), kwargs.get('share_to_recipients_metadata', None))
        setattr(self, "_{}".format('tab_type'), kwargs.get('tab_type', None))
        setattr(self, "_{}".format('tab_type_metadata'), kwargs.get('tab_type_metadata', None))
        setattr(self, "_{}".format('template_locked'), kwargs.get('template_locked', None))
        setattr(self, "_{}".format('template_locked_metadata'), kwargs.get('template_locked_metadata', None))
        setattr(self, "_{}".format('template_required'), kwargs.get('template_required', None))
        setattr(self, "_{}".format('template_required_metadata'), kwargs.get('template_required_metadata', None))
        setattr(self, "_{}".format('tooltip'), kwargs.get('tooltip', None))
        setattr(self, "_{}".format('tooltip_metadata'), kwargs.get('tooltip_metadata', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))
        setattr(self, "_{}".format('value_metadata'), kwargs.get('value_metadata', None))

    @property
    def conditional_parent_label(self):
        """Gets the conditional_parent_label of this RadioGroup.  # noqa: E501

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :return: The conditional_parent_label of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_label

    @conditional_parent_label.setter
    def conditional_parent_label(self, conditional_parent_label):
        """Sets the conditional_parent_label of this RadioGroup.

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :param conditional_parent_label: The conditional_parent_label of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._conditional_parent_label = conditional_parent_label

    @property
    def conditional_parent_label_metadata(self):
        """Gets the conditional_parent_label_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `conditionalParentLabel` property is editable.  # noqa: E501

        :return: The conditional_parent_label_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._conditional_parent_label_metadata

    @conditional_parent_label_metadata.setter
    def conditional_parent_label_metadata(self, conditional_parent_label_metadata):
        """Sets the conditional_parent_label_metadata of this RadioGroup.

        Metadata that indicates whether the `conditionalParentLabel` property is editable.  # noqa: E501

        :param conditional_parent_label_metadata: The conditional_parent_label_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._conditional_parent_label_metadata = conditional_parent_label_metadata

    @property
    def conditional_parent_value(self):
        """Gets the conditional_parent_value of this RadioGroup.  # noqa: E501

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :return: The conditional_parent_value of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_value

    @conditional_parent_value.setter
    def conditional_parent_value(self, conditional_parent_value):
        """Sets the conditional_parent_value of this RadioGroup.

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :param conditional_parent_value: The conditional_parent_value of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._conditional_parent_value = conditional_parent_value

    @property
    def conditional_parent_value_metadata(self):
        """Gets the conditional_parent_value_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `conditionalParentValue` property is editable.  # noqa: E501

        :return: The conditional_parent_value_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._conditional_parent_value_metadata

    @conditional_parent_value_metadata.setter
    def conditional_parent_value_metadata(self, conditional_parent_value_metadata):
        """Sets the conditional_parent_value_metadata of this RadioGroup.

        Metadata that indicates whether the `conditionalParentValue` property is editable.  # noqa: E501

        :param conditional_parent_value_metadata: The conditional_parent_value_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._conditional_parent_value_metadata = conditional_parent_value_metadata

    @property
    def document_id(self):
        """Gets the document_id of this RadioGroup.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this RadioGroup.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_id_metadata(self):
        """Gets the document_id_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `documentId` property is editable.  # noqa: E501

        :return: The document_id_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._document_id_metadata

    @document_id_metadata.setter
    def document_id_metadata(self, document_id_metadata):
        """Sets the document_id_metadata of this RadioGroup.

        Metadata that indicates whether the `documentId` property is editable.  # noqa: E501

        :param document_id_metadata: The document_id_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._document_id_metadata = document_id_metadata

    @property
    def group_name(self):
        """Gets the group_name of this RadioGroup.  # noqa: E501

        The name of the group.  # noqa: E501

        :return: The group_name of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RadioGroup.

        The name of the group.  # noqa: E501

        :param group_name: The group_name of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_name_metadata(self):
        """Gets the group_name_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `groupName` property is editable.  # noqa: E501

        :return: The group_name_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._group_name_metadata

    @group_name_metadata.setter
    def group_name_metadata(self, group_name_metadata):
        """Sets the group_name_metadata of this RadioGroup.

        Metadata that indicates whether the `groupName` property is editable.  # noqa: E501

        :param group_name_metadata: The group_name_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._group_name_metadata = group_name_metadata

    @property
    def original_value(self):
        """Gets the original_value of this RadioGroup.  # noqa: E501

        The initial value of the tab when it was sent to the recipient.   # noqa: E501

        :return: The original_value of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """Sets the original_value of this RadioGroup.

        The initial value of the tab when it was sent to the recipient.   # noqa: E501

        :param original_value: The original_value of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._original_value = original_value

    @property
    def original_value_metadata(self):
        """Gets the original_value_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `originalValue` property is editable.  # noqa: E501

        :return: The original_value_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._original_value_metadata

    @original_value_metadata.setter
    def original_value_metadata(self, original_value_metadata):
        """Sets the original_value_metadata of this RadioGroup.

        Metadata that indicates whether the `originalValue` property is editable.  # noqa: E501

        :param original_value_metadata: The original_value_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._original_value_metadata = original_value_metadata

    @property
    def radios(self):
        """Gets the radios of this RadioGroup.  # noqa: E501

        Specifies the locations and status for radio buttons that are grouped together.  # noqa: E501

        :return: The radios of this RadioGroup.  # noqa: E501
        :rtype: list[Radio]
        """
        return self._radios

    @radios.setter
    def radios(self, radios):
        """Sets the radios of this RadioGroup.

        Specifies the locations and status for radio buttons that are grouped together.  # noqa: E501

        :param radios: The radios of this RadioGroup.  # noqa: E501
        :type: list[Radio]
        """

        self._radios = radios

    @property
    def recipient_id(self):
        """Gets the recipient_id of this RadioGroup.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this RadioGroup.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def recipient_id_guid(self):
        """Gets the recipient_id_guid of this RadioGroup.  # noqa: E501

          # noqa: E501

        :return: The recipient_id_guid of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id_guid

    @recipient_id_guid.setter
    def recipient_id_guid(self, recipient_id_guid):
        """Sets the recipient_id_guid of this RadioGroup.

          # noqa: E501

        :param recipient_id_guid: The recipient_id_guid of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._recipient_id_guid = recipient_id_guid

    @property
    def recipient_id_guid_metadata(self):
        """Gets the recipient_id_guid_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `recipientIdGuid` property is editable.  # noqa: E501

        :return: The recipient_id_guid_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._recipient_id_guid_metadata

    @recipient_id_guid_metadata.setter
    def recipient_id_guid_metadata(self, recipient_id_guid_metadata):
        """Sets the recipient_id_guid_metadata of this RadioGroup.

        Metadata that indicates whether the `recipientIdGuid` property is editable.  # noqa: E501

        :param recipient_id_guid_metadata: The recipient_id_guid_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._recipient_id_guid_metadata = recipient_id_guid_metadata

    @property
    def recipient_id_metadata(self):
        """Gets the recipient_id_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `recipientId` property is editable.  # noqa: E501

        :return: The recipient_id_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._recipient_id_metadata

    @recipient_id_metadata.setter
    def recipient_id_metadata(self, recipient_id_metadata):
        """Sets the recipient_id_metadata of this RadioGroup.

        Metadata that indicates whether the `recipientId` property is editable.  # noqa: E501

        :param recipient_id_metadata: The recipient_id_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._recipient_id_metadata = recipient_id_metadata

    @property
    def require_all(self):
        """Gets the require_all of this RadioGroup.  # noqa: E501

        When set to **true** and shared is true, information must be entered in this field to complete the envelope.   # noqa: E501

        :return: The require_all of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._require_all

    @require_all.setter
    def require_all(self, require_all):
        """Sets the require_all of this RadioGroup.

        When set to **true** and shared is true, information must be entered in this field to complete the envelope.   # noqa: E501

        :param require_all: The require_all of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._require_all = require_all

    @property
    def require_all_metadata(self):
        """Gets the require_all_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `requireAll` property is editable.  # noqa: E501

        :return: The require_all_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._require_all_metadata

    @require_all_metadata.setter
    def require_all_metadata(self, require_all_metadata):
        """Sets the require_all_metadata of this RadioGroup.

        Metadata that indicates whether the `requireAll` property is editable.  # noqa: E501

        :param require_all_metadata: The require_all_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._require_all_metadata = require_all_metadata

    @property
    def require_initial_on_shared_change(self):
        """Gets the require_initial_on_shared_change of this RadioGroup.  # noqa: E501

        Optional element for field markup. When set to **true**, the signer is required to initial when they modify a shared field.  # noqa: E501

        :return: The require_initial_on_shared_change of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._require_initial_on_shared_change

    @require_initial_on_shared_change.setter
    def require_initial_on_shared_change(self, require_initial_on_shared_change):
        """Sets the require_initial_on_shared_change of this RadioGroup.

        Optional element for field markup. When set to **true**, the signer is required to initial when they modify a shared field.  # noqa: E501

        :param require_initial_on_shared_change: The require_initial_on_shared_change of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._require_initial_on_shared_change = require_initial_on_shared_change

    @property
    def require_initial_on_shared_change_metadata(self):
        """Gets the require_initial_on_shared_change_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `requireInitialOnSharedChange` property is editable.  # noqa: E501

        :return: The require_initial_on_shared_change_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._require_initial_on_shared_change_metadata

    @require_initial_on_shared_change_metadata.setter
    def require_initial_on_shared_change_metadata(self, require_initial_on_shared_change_metadata):
        """Sets the require_initial_on_shared_change_metadata of this RadioGroup.

        Metadata that indicates whether the `requireInitialOnSharedChange` property is editable.  # noqa: E501

        :param require_initial_on_shared_change_metadata: The require_initial_on_shared_change_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._require_initial_on_shared_change_metadata = require_initial_on_shared_change_metadata

    @property
    def shared(self):
        """Gets the shared of this RadioGroup.  # noqa: E501

        When set to **true**, this custom tab is shared.  # noqa: E501

        :return: The shared of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this RadioGroup.

        When set to **true**, this custom tab is shared.  # noqa: E501

        :param shared: The shared of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._shared = shared

    @property
    def shared_metadata(self):
        """Gets the shared_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `shared` property is editable.  # noqa: E501

        :return: The shared_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._shared_metadata

    @shared_metadata.setter
    def shared_metadata(self, shared_metadata):
        """Sets the shared_metadata of this RadioGroup.

        Metadata that indicates whether the `shared` property is editable.  # noqa: E501

        :param shared_metadata: The shared_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._shared_metadata = shared_metadata

    @property
    def share_to_recipients(self):
        """Gets the share_to_recipients of this RadioGroup.  # noqa: E501

          # noqa: E501

        :return: The share_to_recipients of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._share_to_recipients

    @share_to_recipients.setter
    def share_to_recipients(self, share_to_recipients):
        """Sets the share_to_recipients of this RadioGroup.

          # noqa: E501

        :param share_to_recipients: The share_to_recipients of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._share_to_recipients = share_to_recipients

    @property
    def share_to_recipients_metadata(self):
        """Gets the share_to_recipients_metadata of this RadioGroup.  # noqa: E501

        Reserved for DocuSign.  # noqa: E501

        :return: The share_to_recipients_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._share_to_recipients_metadata

    @share_to_recipients_metadata.setter
    def share_to_recipients_metadata(self, share_to_recipients_metadata):
        """Sets the share_to_recipients_metadata of this RadioGroup.

        Reserved for DocuSign.  # noqa: E501

        :param share_to_recipients_metadata: The share_to_recipients_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._share_to_recipients_metadata = share_to_recipients_metadata

    @property
    def tab_type(self):
        """Gets the tab_type of this RadioGroup.  # noqa: E501

          # noqa: E501

        :return: The tab_type of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._tab_type

    @tab_type.setter
    def tab_type(self, tab_type):
        """Sets the tab_type of this RadioGroup.

          # noqa: E501

        :param tab_type: The tab_type of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._tab_type = tab_type

    @property
    def tab_type_metadata(self):
        """Gets the tab_type_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `tabType` property is editable.  # noqa: E501

        :return: The tab_type_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._tab_type_metadata

    @tab_type_metadata.setter
    def tab_type_metadata(self, tab_type_metadata):
        """Sets the tab_type_metadata of this RadioGroup.

        Metadata that indicates whether the `tabType` property is editable.  # noqa: E501

        :param tab_type_metadata: The tab_type_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._tab_type_metadata = tab_type_metadata

    @property
    def template_locked(self):
        """Gets the template_locked of this RadioGroup.  # noqa: E501

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :return: The template_locked of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """Sets the template_locked of this RadioGroup.

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :param template_locked: The template_locked of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_locked_metadata(self):
        """Gets the template_locked_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `templateLocked` property is editable.  # noqa: E501

        :return: The template_locked_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._template_locked_metadata

    @template_locked_metadata.setter
    def template_locked_metadata(self, template_locked_metadata):
        """Sets the template_locked_metadata of this RadioGroup.

        Metadata that indicates whether the `templateLocked` property is editable.  # noqa: E501

        :param template_locked_metadata: The template_locked_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._template_locked_metadata = template_locked_metadata

    @property
    def template_required(self):
        """Gets the template_required of this RadioGroup.  # noqa: E501

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :return: The template_required of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """Sets the template_required of this RadioGroup.

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :param template_required: The template_required of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._template_required = template_required

    @property
    def template_required_metadata(self):
        """Gets the template_required_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `templateRequired` property is editable.  # noqa: E501

        :return: The template_required_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._template_required_metadata

    @template_required_metadata.setter
    def template_required_metadata(self, template_required_metadata):
        """Sets the template_required_metadata of this RadioGroup.

        Metadata that indicates whether the `templateRequired` property is editable.  # noqa: E501

        :param template_required_metadata: The template_required_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._template_required_metadata = template_required_metadata

    @property
    def tooltip(self):
        """Gets the tooltip of this RadioGroup.  # noqa: E501

          # noqa: E501

        :return: The tooltip of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this RadioGroup.

          # noqa: E501

        :param tooltip: The tooltip of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

    @property
    def tooltip_metadata(self):
        """Gets the tooltip_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `tooltip` property is editable.  # noqa: E501

        :return: The tooltip_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._tooltip_metadata

    @tooltip_metadata.setter
    def tooltip_metadata(self, tooltip_metadata):
        """Sets the tooltip_metadata of this RadioGroup.

        Metadata that indicates whether the `tooltip` property is editable.  # noqa: E501

        :param tooltip_metadata: The tooltip_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._tooltip_metadata = tooltip_metadata

    @property
    def value(self):
        """Gets the value of this RadioGroup.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this RadioGroup.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RadioGroup.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this RadioGroup.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_metadata(self):
        """Gets the value_metadata of this RadioGroup.  # noqa: E501

        Metadata that indicates whether the `value` property is editable.  # noqa: E501

        :return: The value_metadata of this RadioGroup.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._value_metadata

    @value_metadata.setter
    def value_metadata(self, value_metadata):
        """Sets the value_metadata of this RadioGroup.

        Metadata that indicates whether the `value` property is editable.  # noqa: E501

        :param value_metadata: The value_metadata of this RadioGroup.  # noqa: E501
        :type: PropertyMetadata
        """

        self._value_metadata = value_metadata

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
        if issubclass(RadioGroup, dict):
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
        if not isinstance(other, RadioGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RadioGroup):
            return True

        return self.to_dict() != other.to_dict()
