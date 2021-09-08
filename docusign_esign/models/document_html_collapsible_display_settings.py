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


class DocumentHtmlCollapsibleDisplaySettings(object):
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
        'arrow_closed': 'str',
        'arrow_color': 'str',
        'arrow_location': 'str',
        'arrow_open': 'str',
        'arrow_size': 'str',
        'arrow_style': 'str',
        'container_style': 'str',
        'label_style': 'str',
        'only_arrow_is_clickable': 'bool',
        'outer_label_and_arrow_style': 'str'
    }

    attribute_map = {
        'arrow_closed': 'arrowClosed',
        'arrow_color': 'arrowColor',
        'arrow_location': 'arrowLocation',
        'arrow_open': 'arrowOpen',
        'arrow_size': 'arrowSize',
        'arrow_style': 'arrowStyle',
        'container_style': 'containerStyle',
        'label_style': 'labelStyle',
        'only_arrow_is_clickable': 'onlyArrowIsClickable',
        'outer_label_and_arrow_style': 'outerLabelAndArrowStyle'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DocumentHtmlCollapsibleDisplaySettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._arrow_closed = None
        self._arrow_color = None
        self._arrow_location = None
        self._arrow_open = None
        self._arrow_size = None
        self._arrow_style = None
        self._container_style = None
        self._label_style = None
        self._only_arrow_is_clickable = None
        self._outer_label_and_arrow_style = None
        self.discriminator = None

        setattr(self, "_{}".format('arrow_closed'), kwargs.get('arrow_closed', None))
        setattr(self, "_{}".format('arrow_color'), kwargs.get('arrow_color', None))
        setattr(self, "_{}".format('arrow_location'), kwargs.get('arrow_location', None))
        setattr(self, "_{}".format('arrow_open'), kwargs.get('arrow_open', None))
        setattr(self, "_{}".format('arrow_size'), kwargs.get('arrow_size', None))
        setattr(self, "_{}".format('arrow_style'), kwargs.get('arrow_style', None))
        setattr(self, "_{}".format('container_style'), kwargs.get('container_style', None))
        setattr(self, "_{}".format('label_style'), kwargs.get('label_style', None))
        setattr(self, "_{}".format('only_arrow_is_clickable'), kwargs.get('only_arrow_is_clickable', None))
        setattr(self, "_{}".format('outer_label_and_arrow_style'), kwargs.get('outer_label_and_arrow_style', None))

    @property
    def arrow_closed(self):
        """Gets the arrow_closed of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The arrow_closed of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._arrow_closed

    @arrow_closed.setter
    def arrow_closed(self, arrow_closed):
        """Sets the arrow_closed of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param arrow_closed: The arrow_closed of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._arrow_closed = arrow_closed

    @property
    def arrow_color(self):
        """Gets the arrow_color of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The arrow_color of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._arrow_color

    @arrow_color.setter
    def arrow_color(self, arrow_color):
        """Sets the arrow_color of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param arrow_color: The arrow_color of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._arrow_color = arrow_color

    @property
    def arrow_location(self):
        """Gets the arrow_location of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The arrow_location of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._arrow_location

    @arrow_location.setter
    def arrow_location(self, arrow_location):
        """Sets the arrow_location of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param arrow_location: The arrow_location of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._arrow_location = arrow_location

    @property
    def arrow_open(self):
        """Gets the arrow_open of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The arrow_open of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._arrow_open

    @arrow_open.setter
    def arrow_open(self, arrow_open):
        """Sets the arrow_open of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param arrow_open: The arrow_open of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._arrow_open = arrow_open

    @property
    def arrow_size(self):
        """Gets the arrow_size of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The arrow_size of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._arrow_size

    @arrow_size.setter
    def arrow_size(self, arrow_size):
        """Sets the arrow_size of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param arrow_size: The arrow_size of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._arrow_size = arrow_size

    @property
    def arrow_style(self):
        """Gets the arrow_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The arrow_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._arrow_style

    @arrow_style.setter
    def arrow_style(self, arrow_style):
        """Sets the arrow_style of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param arrow_style: The arrow_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._arrow_style = arrow_style

    @property
    def container_style(self):
        """Gets the container_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The container_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._container_style

    @container_style.setter
    def container_style(self, container_style):
        """Sets the container_style of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param container_style: The container_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._container_style = container_style

    @property
    def label_style(self):
        """Gets the label_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The label_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._label_style

    @label_style.setter
    def label_style(self, label_style):
        """Sets the label_style of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param label_style: The label_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._label_style = label_style

    @property
    def only_arrow_is_clickable(self):
        """Gets the only_arrow_is_clickable of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The only_arrow_is_clickable of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: bool
        """
        return self._only_arrow_is_clickable

    @only_arrow_is_clickable.setter
    def only_arrow_is_clickable(self, only_arrow_is_clickable):
        """Sets the only_arrow_is_clickable of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param only_arrow_is_clickable: The only_arrow_is_clickable of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: bool
        """

        self._only_arrow_is_clickable = only_arrow_is_clickable

    @property
    def outer_label_and_arrow_style(self):
        """Gets the outer_label_and_arrow_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501

          # noqa: E501

        :return: The outer_label_and_arrow_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._outer_label_and_arrow_style

    @outer_label_and_arrow_style.setter
    def outer_label_and_arrow_style(self, outer_label_and_arrow_style):
        """Sets the outer_label_and_arrow_style of this DocumentHtmlCollapsibleDisplaySettings.

          # noqa: E501

        :param outer_label_and_arrow_style: The outer_label_and_arrow_style of this DocumentHtmlCollapsibleDisplaySettings.  # noqa: E501
        :type: str
        """

        self._outer_label_and_arrow_style = outer_label_and_arrow_style

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
        if issubclass(DocumentHtmlCollapsibleDisplaySettings, dict):
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
        if not isinstance(other, DocumentHtmlCollapsibleDisplaySettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentHtmlCollapsibleDisplaySettings):
            return True

        return self.to_dict() != other.to_dict()
