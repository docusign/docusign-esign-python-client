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


class DocumentHtmlDefinition(object):
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
        'display_anchor_prefix': 'str',
        'display_anchors': 'list[DocumentHtmlDisplayAnchor]',
        'display_order': 'str',
        'display_page_number': 'str',
        'document_guid': 'str',
        'document_id': 'str',
        'header_label': 'str',
        'max_screen_width': 'str',
        'remove_empty_tags': 'str',
        'show_mobile_optimized_toggle': 'str',
        'source': 'str'
    }

    attribute_map = {
        'display_anchor_prefix': 'displayAnchorPrefix',
        'display_anchors': 'displayAnchors',
        'display_order': 'displayOrder',
        'display_page_number': 'displayPageNumber',
        'document_guid': 'documentGuid',
        'document_id': 'documentId',
        'header_label': 'headerLabel',
        'max_screen_width': 'maxScreenWidth',
        'remove_empty_tags': 'removeEmptyTags',
        'show_mobile_optimized_toggle': 'showMobileOptimizedToggle',
        'source': 'source'
    }

    def __init__(self, display_anchor_prefix=None, display_anchors=None, display_order=None, display_page_number=None, document_guid=None, document_id=None, header_label=None, max_screen_width=None, remove_empty_tags=None, show_mobile_optimized_toggle=None, source=None):  # noqa: E501
        """DocumentHtmlDefinition - a model defined in Swagger"""  # noqa: E501

        self._display_anchor_prefix = None
        self._display_anchors = None
        self._display_order = None
        self._display_page_number = None
        self._document_guid = None
        self._document_id = None
        self._header_label = None
        self._max_screen_width = None
        self._remove_empty_tags = None
        self._show_mobile_optimized_toggle = None
        self._source = None
        self.discriminator = None

        if display_anchor_prefix is not None:
            self.display_anchor_prefix = display_anchor_prefix
        if display_anchors is not None:
            self.display_anchors = display_anchors
        if display_order is not None:
            self.display_order = display_order
        if display_page_number is not None:
            self.display_page_number = display_page_number
        if document_guid is not None:
            self.document_guid = document_guid
        if document_id is not None:
            self.document_id = document_id
        if header_label is not None:
            self.header_label = header_label
        if max_screen_width is not None:
            self.max_screen_width = max_screen_width
        if remove_empty_tags is not None:
            self.remove_empty_tags = remove_empty_tags
        if show_mobile_optimized_toggle is not None:
            self.show_mobile_optimized_toggle = show_mobile_optimized_toggle
        if source is not None:
            self.source = source

    @property
    def display_anchor_prefix(self):
        """Gets the display_anchor_prefix of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The display_anchor_prefix of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_anchor_prefix

    @display_anchor_prefix.setter
    def display_anchor_prefix(self, display_anchor_prefix):
        """Sets the display_anchor_prefix of this DocumentHtmlDefinition.

          # noqa: E501

        :param display_anchor_prefix: The display_anchor_prefix of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._display_anchor_prefix = display_anchor_prefix

    @property
    def display_anchors(self):
        """Gets the display_anchors of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The display_anchors of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: list[DocumentHtmlDisplayAnchor]
        """
        return self._display_anchors

    @display_anchors.setter
    def display_anchors(self, display_anchors):
        """Sets the display_anchors of this DocumentHtmlDefinition.

          # noqa: E501

        :param display_anchors: The display_anchors of this DocumentHtmlDefinition.  # noqa: E501
        :type: list[DocumentHtmlDisplayAnchor]
        """

        self._display_anchors = display_anchors

    @property
    def display_order(self):
        """Gets the display_order of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The display_order of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this DocumentHtmlDefinition.

          # noqa: E501

        :param display_order: The display_order of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._display_order = display_order

    @property
    def display_page_number(self):
        """Gets the display_page_number of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The display_page_number of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_page_number

    @display_page_number.setter
    def display_page_number(self, display_page_number):
        """Sets the display_page_number of this DocumentHtmlDefinition.

          # noqa: E501

        :param display_page_number: The display_page_number of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._display_page_number = display_page_number

    @property
    def document_guid(self):
        """Gets the document_guid of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The document_guid of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._document_guid

    @document_guid.setter
    def document_guid(self, document_guid):
        """Sets the document_guid of this DocumentHtmlDefinition.

          # noqa: E501

        :param document_guid: The document_guid of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._document_guid = document_guid

    @property
    def document_id(self):
        """Gets the document_id of this DocumentHtmlDefinition.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentHtmlDefinition.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def header_label(self):
        """Gets the header_label of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The header_label of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._header_label

    @header_label.setter
    def header_label(self, header_label):
        """Sets the header_label of this DocumentHtmlDefinition.

          # noqa: E501

        :param header_label: The header_label of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._header_label = header_label

    @property
    def max_screen_width(self):
        """Gets the max_screen_width of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The max_screen_width of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._max_screen_width

    @max_screen_width.setter
    def max_screen_width(self, max_screen_width):
        """Sets the max_screen_width of this DocumentHtmlDefinition.

          # noqa: E501

        :param max_screen_width: The max_screen_width of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._max_screen_width = max_screen_width

    @property
    def remove_empty_tags(self):
        """Gets the remove_empty_tags of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The remove_empty_tags of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._remove_empty_tags

    @remove_empty_tags.setter
    def remove_empty_tags(self, remove_empty_tags):
        """Sets the remove_empty_tags of this DocumentHtmlDefinition.

          # noqa: E501

        :param remove_empty_tags: The remove_empty_tags of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._remove_empty_tags = remove_empty_tags

    @property
    def show_mobile_optimized_toggle(self):
        """Gets the show_mobile_optimized_toggle of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The show_mobile_optimized_toggle of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._show_mobile_optimized_toggle

    @show_mobile_optimized_toggle.setter
    def show_mobile_optimized_toggle(self, show_mobile_optimized_toggle):
        """Sets the show_mobile_optimized_toggle of this DocumentHtmlDefinition.

          # noqa: E501

        :param show_mobile_optimized_toggle: The show_mobile_optimized_toggle of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._show_mobile_optimized_toggle = show_mobile_optimized_toggle

    @property
    def source(self):
        """Gets the source of this DocumentHtmlDefinition.  # noqa: E501

          # noqa: E501

        :return: The source of this DocumentHtmlDefinition.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DocumentHtmlDefinition.

          # noqa: E501

        :param source: The source of this DocumentHtmlDefinition.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if issubclass(DocumentHtmlDefinition, dict):
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
        if not isinstance(other, DocumentHtmlDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
