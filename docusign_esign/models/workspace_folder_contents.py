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


class WorkspaceFolderContents(object):
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
        'end_position': 'str',
        'folder': 'WorkspaceItem',
        'items': 'list[WorkspaceItem]',
        'parent_folders': 'list[WorkspaceItem]',
        'result_set_size': 'str',
        'start_position': 'str',
        'total_set_size': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'end_position': 'endPosition',
        'folder': 'folder',
        'items': 'items',
        'parent_folders': 'parentFolders',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'total_set_size': 'totalSetSize',
        'workspace_id': 'workspaceId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """WorkspaceFolderContents - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_position = None
        self._folder = None
        self._items = None
        self._parent_folders = None
        self._result_set_size = None
        self._start_position = None
        self._total_set_size = None
        self._workspace_id = None
        self.discriminator = None

        setattr(self, "_{}".format('end_position'), kwargs.get('end_position', None))
        setattr(self, "_{}".format('folder'), kwargs.get('folder', None))
        setattr(self, "_{}".format('items'), kwargs.get('items', None))
        setattr(self, "_{}".format('parent_folders'), kwargs.get('parent_folders', None))
        setattr(self, "_{}".format('result_set_size'), kwargs.get('result_set_size', None))
        setattr(self, "_{}".format('start_position'), kwargs.get('start_position', None))
        setattr(self, "_{}".format('total_set_size'), kwargs.get('total_set_size', None))
        setattr(self, "_{}".format('workspace_id'), kwargs.get('workspace_id', None))

    @property
    def end_position(self):
        """Gets the end_position of this WorkspaceFolderContents.  # noqa: E501

        The last position in the result set.   # noqa: E501

        :return: The end_position of this WorkspaceFolderContents.  # noqa: E501
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this WorkspaceFolderContents.

        The last position in the result set.   # noqa: E501

        :param end_position: The end_position of this WorkspaceFolderContents.  # noqa: E501
        :type: str
        """

        self._end_position = end_position

    @property
    def folder(self):
        """Gets the folder of this WorkspaceFolderContents.  # noqa: E501

        The folder from which to return items. You can enter either the folder name or folder ID.  # noqa: E501

        :return: The folder of this WorkspaceFolderContents.  # noqa: E501
        :rtype: WorkspaceItem
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this WorkspaceFolderContents.

        The folder from which to return items. You can enter either the folder name or folder ID.  # noqa: E501

        :param folder: The folder of this WorkspaceFolderContents.  # noqa: E501
        :type: WorkspaceItem
        """

        self._folder = folder

    @property
    def items(self):
        """Gets the items of this WorkspaceFolderContents.  # noqa: E501

          # noqa: E501

        :return: The items of this WorkspaceFolderContents.  # noqa: E501
        :rtype: list[WorkspaceItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this WorkspaceFolderContents.

          # noqa: E501

        :param items: The items of this WorkspaceFolderContents.  # noqa: E501
        :type: list[WorkspaceItem]
        """

        self._items = items

    @property
    def parent_folders(self):
        """Gets the parent_folders of this WorkspaceFolderContents.  # noqa: E501

          # noqa: E501

        :return: The parent_folders of this WorkspaceFolderContents.  # noqa: E501
        :rtype: list[WorkspaceItem]
        """
        return self._parent_folders

    @parent_folders.setter
    def parent_folders(self, parent_folders):
        """Sets the parent_folders of this WorkspaceFolderContents.

          # noqa: E501

        :param parent_folders: The parent_folders of this WorkspaceFolderContents.  # noqa: E501
        :type: list[WorkspaceItem]
        """

        self._parent_folders = parent_folders

    @property
    def result_set_size(self):
        """Gets the result_set_size of this WorkspaceFolderContents.  # noqa: E501

        The number of results returned in this response.   # noqa: E501

        :return: The result_set_size of this WorkspaceFolderContents.  # noqa: E501
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this WorkspaceFolderContents.

        The number of results returned in this response.   # noqa: E501

        :param result_set_size: The result_set_size of this WorkspaceFolderContents.  # noqa: E501
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this WorkspaceFolderContents.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this WorkspaceFolderContents.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this WorkspaceFolderContents.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this WorkspaceFolderContents.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this WorkspaceFolderContents.  # noqa: E501

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :return: The total_set_size of this WorkspaceFolderContents.  # noqa: E501
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this WorkspaceFolderContents.

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :param total_set_size: The total_set_size of this WorkspaceFolderContents.  # noqa: E501
        :type: str
        """

        self._total_set_size = total_set_size

    @property
    def workspace_id(self):
        """Gets the workspace_id of this WorkspaceFolderContents.  # noqa: E501

        The id of the workspace, always populated.  # noqa: E501

        :return: The workspace_id of this WorkspaceFolderContents.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this WorkspaceFolderContents.

        The id of the workspace, always populated.  # noqa: E501

        :param workspace_id: The workspace_id of this WorkspaceFolderContents.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

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
        if issubclass(WorkspaceFolderContents, dict):
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
        if not isinstance(other, WorkspaceFolderContents):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceFolderContents):
            return True

        return self.to_dict() != other.to_dict()
