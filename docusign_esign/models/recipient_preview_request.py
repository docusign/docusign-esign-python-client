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


class RecipientPreviewRequest(object):
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
        'assertion_id': 'str',
        'authentication_instant': 'str',
        'authentication_method': 'str',
        'client_ur_ls': 'RecipientTokenClientURLs',
        'ping_frequency': 'str',
        'ping_url': 'str',
        'recipient_id': 'str',
        'return_url': 'str',
        'security_domain': 'str',
        'x_frame_options': 'str',
        'x_frame_options_allow_from_url': 'str'
    }

    attribute_map = {
        'assertion_id': 'assertionId',
        'authentication_instant': 'authenticationInstant',
        'authentication_method': 'authenticationMethod',
        'client_ur_ls': 'clientURLs',
        'ping_frequency': 'pingFrequency',
        'ping_url': 'pingUrl',
        'recipient_id': 'recipientId',
        'return_url': 'returnUrl',
        'security_domain': 'securityDomain',
        'x_frame_options': 'xFrameOptions',
        'x_frame_options_allow_from_url': 'xFrameOptionsAllowFromUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientPreviewRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assertion_id = None
        self._authentication_instant = None
        self._authentication_method = None
        self._client_ur_ls = None
        self._ping_frequency = None
        self._ping_url = None
        self._recipient_id = None
        self._return_url = None
        self._security_domain = None
        self._x_frame_options = None
        self._x_frame_options_allow_from_url = None
        self.discriminator = None

        setattr(self, "_{}".format('assertion_id'), kwargs.get('assertion_id', None))
        setattr(self, "_{}".format('authentication_instant'), kwargs.get('authentication_instant', None))
        setattr(self, "_{}".format('authentication_method'), kwargs.get('authentication_method', None))
        setattr(self, "_{}".format('client_ur_ls'), kwargs.get('client_ur_ls', None))
        setattr(self, "_{}".format('ping_frequency'), kwargs.get('ping_frequency', None))
        setattr(self, "_{}".format('ping_url'), kwargs.get('ping_url', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('return_url'), kwargs.get('return_url', None))
        setattr(self, "_{}".format('security_domain'), kwargs.get('security_domain', None))
        setattr(self, "_{}".format('x_frame_options'), kwargs.get('x_frame_options', None))
        setattr(self, "_{}".format('x_frame_options_allow_from_url'), kwargs.get('x_frame_options_allow_from_url', None))

    @property
    def assertion_id(self):
        """Gets the assertion_id of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The assertion_id of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._assertion_id

    @assertion_id.setter
    def assertion_id(self, assertion_id):
        """Sets the assertion_id of this RecipientPreviewRequest.

          # noqa: E501

        :param assertion_id: The assertion_id of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._assertion_id = assertion_id

    @property
    def authentication_instant(self):
        """Gets the authentication_instant of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The authentication_instant of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_instant

    @authentication_instant.setter
    def authentication_instant(self, authentication_instant):
        """Sets the authentication_instant of this RecipientPreviewRequest.

          # noqa: E501

        :param authentication_instant: The authentication_instant of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._authentication_instant = authentication_instant

    @property
    def authentication_method(self):
        """Gets the authentication_method of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The authentication_method of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this RecipientPreviewRequest.

          # noqa: E501

        :param authentication_method: The authentication_method of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def client_ur_ls(self):
        """Gets the client_ur_ls of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The client_ur_ls of this RecipientPreviewRequest.  # noqa: E501
        :rtype: RecipientTokenClientURLs
        """
        return self._client_ur_ls

    @client_ur_ls.setter
    def client_ur_ls(self, client_ur_ls):
        """Sets the client_ur_ls of this RecipientPreviewRequest.

          # noqa: E501

        :param client_ur_ls: The client_ur_ls of this RecipientPreviewRequest.  # noqa: E501
        :type: RecipientTokenClientURLs
        """

        self._client_ur_ls = client_ur_ls

    @property
    def ping_frequency(self):
        """Gets the ping_frequency of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The ping_frequency of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._ping_frequency

    @ping_frequency.setter
    def ping_frequency(self, ping_frequency):
        """Sets the ping_frequency of this RecipientPreviewRequest.

          # noqa: E501

        :param ping_frequency: The ping_frequency of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._ping_frequency = ping_frequency

    @property
    def ping_url(self):
        """Gets the ping_url of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The ping_url of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._ping_url

    @ping_url.setter
    def ping_url(self, ping_url):
        """Sets the ping_url of this RecipientPreviewRequest.

          # noqa: E501

        :param ping_url: The ping_url of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._ping_url = ping_url

    @property
    def recipient_id(self):
        """Gets the recipient_id of this RecipientPreviewRequest.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this RecipientPreviewRequest.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def return_url(self):
        """Gets the return_url of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The return_url of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this RecipientPreviewRequest.

          # noqa: E501

        :param return_url: The return_url of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._return_url = return_url

    @property
    def security_domain(self):
        """Gets the security_domain of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The security_domain of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_domain

    @security_domain.setter
    def security_domain(self, security_domain):
        """Sets the security_domain of this RecipientPreviewRequest.

          # noqa: E501

        :param security_domain: The security_domain of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._security_domain = security_domain

    @property
    def x_frame_options(self):
        """Gets the x_frame_options of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The x_frame_options of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._x_frame_options

    @x_frame_options.setter
    def x_frame_options(self, x_frame_options):
        """Sets the x_frame_options of this RecipientPreviewRequest.

          # noqa: E501

        :param x_frame_options: The x_frame_options of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._x_frame_options = x_frame_options

    @property
    def x_frame_options_allow_from_url(self):
        """Gets the x_frame_options_allow_from_url of this RecipientPreviewRequest.  # noqa: E501

          # noqa: E501

        :return: The x_frame_options_allow_from_url of this RecipientPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._x_frame_options_allow_from_url

    @x_frame_options_allow_from_url.setter
    def x_frame_options_allow_from_url(self, x_frame_options_allow_from_url):
        """Sets the x_frame_options_allow_from_url of this RecipientPreviewRequest.

          # noqa: E501

        :param x_frame_options_allow_from_url: The x_frame_options_allow_from_url of this RecipientPreviewRequest.  # noqa: E501
        :type: str
        """

        self._x_frame_options_allow_from_url = x_frame_options_allow_from_url

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
        if issubclass(RecipientPreviewRequest, dict):
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
        if not isinstance(other, RecipientPreviewRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientPreviewRequest):
            return True

        return self.to_dict() != other.to_dict()
