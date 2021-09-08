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


class RecipientViewRequest(object):
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
        'client_user_id': 'str',
        'email': 'str',
        'frame_ancestors': 'list[str]',
        'message_origins': 'list[str]',
        'ping_frequency': 'str',
        'ping_url': 'str',
        'recipient_id': 'str',
        'return_url': 'str',
        'security_domain': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'x_frame_options': 'str',
        'x_frame_options_allow_from_url': 'str'
    }

    attribute_map = {
        'assertion_id': 'assertionId',
        'authentication_instant': 'authenticationInstant',
        'authentication_method': 'authenticationMethod',
        'client_ur_ls': 'clientURLs',
        'client_user_id': 'clientUserId',
        'email': 'email',
        'frame_ancestors': 'frameAncestors',
        'message_origins': 'messageOrigins',
        'ping_frequency': 'pingFrequency',
        'ping_url': 'pingUrl',
        'recipient_id': 'recipientId',
        'return_url': 'returnUrl',
        'security_domain': 'securityDomain',
        'user_id': 'userId',
        'user_name': 'userName',
        'x_frame_options': 'xFrameOptions',
        'x_frame_options_allow_from_url': 'xFrameOptionsAllowFromUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientViewRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assertion_id = None
        self._authentication_instant = None
        self._authentication_method = None
        self._client_ur_ls = None
        self._client_user_id = None
        self._email = None
        self._frame_ancestors = None
        self._message_origins = None
        self._ping_frequency = None
        self._ping_url = None
        self._recipient_id = None
        self._return_url = None
        self._security_domain = None
        self._user_id = None
        self._user_name = None
        self._x_frame_options = None
        self._x_frame_options_allow_from_url = None
        self.discriminator = None

        setattr(self, "_{}".format('assertion_id'), kwargs.get('assertion_id', None))
        setattr(self, "_{}".format('authentication_instant'), kwargs.get('authentication_instant', None))
        setattr(self, "_{}".format('authentication_method'), kwargs.get('authentication_method', None))
        setattr(self, "_{}".format('client_ur_ls'), kwargs.get('client_ur_ls', None))
        setattr(self, "_{}".format('client_user_id'), kwargs.get('client_user_id', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('frame_ancestors'), kwargs.get('frame_ancestors', None))
        setattr(self, "_{}".format('message_origins'), kwargs.get('message_origins', None))
        setattr(self, "_{}".format('ping_frequency'), kwargs.get('ping_frequency', None))
        setattr(self, "_{}".format('ping_url'), kwargs.get('ping_url', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('return_url'), kwargs.get('return_url', None))
        setattr(self, "_{}".format('security_domain'), kwargs.get('security_domain', None))
        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))
        setattr(self, "_{}".format('user_name'), kwargs.get('user_name', None))
        setattr(self, "_{}".format('x_frame_options'), kwargs.get('x_frame_options', None))
        setattr(self, "_{}".format('x_frame_options_allow_from_url'), kwargs.get('x_frame_options_allow_from_url', None))

    @property
    def assertion_id(self):
        """Gets the assertion_id of this RecipientViewRequest.  # noqa: E501

        A unique identifier of the authentication event executed by the client application.  # noqa: E501

        :return: The assertion_id of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._assertion_id

    @assertion_id.setter
    def assertion_id(self, assertion_id):
        """Sets the assertion_id of this RecipientViewRequest.

        A unique identifier of the authentication event executed by the client application.  # noqa: E501

        :param assertion_id: The assertion_id of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._assertion_id = assertion_id

    @property
    def authentication_instant(self):
        """Gets the authentication_instant of this RecipientViewRequest.  # noqa: E501

        A sender generated value that indicates the date/time that the signer was authenticated.  # noqa: E501

        :return: The authentication_instant of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_instant

    @authentication_instant.setter
    def authentication_instant(self, authentication_instant):
        """Sets the authentication_instant of this RecipientViewRequest.

        A sender generated value that indicates the date/time that the signer was authenticated.  # noqa: E501

        :param authentication_instant: The authentication_instant of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._authentication_instant = authentication_instant

    @property
    def authentication_method(self):
        """Gets the authentication_method of this RecipientViewRequest.  # noqa: E501

        A sender created value that indicates the convention used to authenticate the signer. This information is included in the Certificate of Completion.  # noqa: E501

        :return: The authentication_method of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this RecipientViewRequest.

        A sender created value that indicates the convention used to authenticate the signer. This information is included in the Certificate of Completion.  # noqa: E501

        :param authentication_method: The authentication_method of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def client_ur_ls(self):
        """Gets the client_ur_ls of this RecipientViewRequest.  # noqa: E501


        :return: The client_ur_ls of this RecipientViewRequest.  # noqa: E501
        :rtype: RecipientTokenClientURLs
        """
        return self._client_ur_ls

    @client_ur_ls.setter
    def client_ur_ls(self, client_ur_ls):
        """Sets the client_ur_ls of this RecipientViewRequest.


        :param client_ur_ls: The client_ur_ls of this RecipientViewRequest.  # noqa: E501
        :type: RecipientTokenClientURLs
        """

        self._client_ur_ls = client_ur_ls

    @property
    def client_user_id(self):
        """Gets the client_user_id of this RecipientViewRequest.  # noqa: E501

        A sender created value that shows the recipient is embedded (captive).   Maximum length: 100 characters.  # noqa: E501

        :return: The client_user_id of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this RecipientViewRequest.

        A sender created value that shows the recipient is embedded (captive).   Maximum length: 100 characters.  # noqa: E501

        :param client_user_id: The client_user_id of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def email(self):
        """Gets the email of this RecipientViewRequest.  # noqa: E501

        Specifies the email of the recipient. You can use either email and userName or userId to identify the recipient.  # noqa: E501

        :return: The email of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RecipientViewRequest.

        Specifies the email of the recipient. You can use either email and userName or userId to identify the recipient.  # noqa: E501

        :param email: The email of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def frame_ancestors(self):
        """Gets the frame_ancestors of this RecipientViewRequest.  # noqa: E501

          # noqa: E501

        :return: The frame_ancestors of this RecipientViewRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._frame_ancestors

    @frame_ancestors.setter
    def frame_ancestors(self, frame_ancestors):
        """Sets the frame_ancestors of this RecipientViewRequest.

          # noqa: E501

        :param frame_ancestors: The frame_ancestors of this RecipientViewRequest.  # noqa: E501
        :type: list[str]
        """

        self._frame_ancestors = frame_ancestors

    @property
    def message_origins(self):
        """Gets the message_origins of this RecipientViewRequest.  # noqa: E501

          # noqa: E501

        :return: The message_origins of this RecipientViewRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._message_origins

    @message_origins.setter
    def message_origins(self, message_origins):
        """Sets the message_origins of this RecipientViewRequest.

          # noqa: E501

        :param message_origins: The message_origins of this RecipientViewRequest.  # noqa: E501
        :type: list[str]
        """

        self._message_origins = message_origins

    @property
    def ping_frequency(self):
        """Gets the ping_frequency of this RecipientViewRequest.  # noqa: E501

        Only used if pingUrl is specified. This is the interval, in seconds, between pings on the pingUrl.  The default is 300 seconds. Valid values are 60-1200 seconds.  # noqa: E501

        :return: The ping_frequency of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._ping_frequency

    @ping_frequency.setter
    def ping_frequency(self, ping_frequency):
        """Sets the ping_frequency of this RecipientViewRequest.

        Only used if pingUrl is specified. This is the interval, in seconds, between pings on the pingUrl.  The default is 300 seconds. Valid values are 60-1200 seconds.  # noqa: E501

        :param ping_frequency: The ping_frequency of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._ping_frequency = ping_frequency

    @property
    def ping_url(self):
        """Gets the ping_url of this RecipientViewRequest.  # noqa: E501

        A client Url to be pinged by the DocuSign Signing experience to indicate to the client that Signing is active. An HTTP Get is executed against the client. The response from the client is ignored. The intent is for the client to reset it's session timer when the request is received.  # noqa: E501

        :return: The ping_url of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._ping_url

    @ping_url.setter
    def ping_url(self, ping_url):
        """Sets the ping_url of this RecipientViewRequest.

        A client Url to be pinged by the DocuSign Signing experience to indicate to the client that Signing is active. An HTTP Get is executed against the client. The response from the client is ignored. The intent is for the client to reset it's session timer when the request is received.  # noqa: E501

        :param ping_url: The ping_url of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._ping_url = ping_url

    @property
    def recipient_id(self):
        """Gets the recipient_id of this RecipientViewRequest.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this RecipientViewRequest.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def return_url(self):
        """Gets the return_url of this RecipientViewRequest.  # noqa: E501

        The url the recipient is redirected to after the signing session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your application. Possible event parameter values:   * cancel (recipient canceled the signing operation) * decline (recipient declined to sign) * exception (an exception occurred) * fax_pending (recipient has a fax pending) * session_timeout (session timed out) * signing_complete (signer completed the signing ceremony) * ttl_expired (the TTL, time to live, timer expired) * viewing_complete (recipient completed viewing the envelope)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers.   # noqa: E501

        :return: The return_url of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this RecipientViewRequest.

        The url the recipient is redirected to after the signing session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your application. Possible event parameter values:   * cancel (recipient canceled the signing operation) * decline (recipient declined to sign) * exception (an exception occurred) * fax_pending (recipient has a fax pending) * session_timeout (session timed out) * signing_complete (signer completed the signing ceremony) * ttl_expired (the TTL, time to live, timer expired) * viewing_complete (recipient completed viewing the envelope)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers.   # noqa: E501

        :param return_url: The return_url of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._return_url = return_url

    @property
    def security_domain(self):
        """Gets the security_domain of this RecipientViewRequest.  # noqa: E501

        The domain in which the user authenticated.  # noqa: E501

        :return: The security_domain of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_domain

    @security_domain.setter
    def security_domain(self, security_domain):
        """Sets the security_domain of this RecipientViewRequest.

        The domain in which the user authenticated.  # noqa: E501

        :param security_domain: The security_domain of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._security_domain = security_domain

    @property
    def user_id(self):
        """Gets the user_id of this RecipientViewRequest.  # noqa: E501

        Specifies the user ID of the recipient. You can use with user ID or email and user name to identify the recipient. If user ID is used and a client user ID is provided, the value in the `userId` property must match a recipient ID (which can be retrieved with a GET recipients call) for the envelope. If a user ID is used and a clientUser ID is not provided, the user ID match the user ID of the authenticating user.  # noqa: E501

        :return: The user_id of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RecipientViewRequest.

        Specifies the user ID of the recipient. You can use with user ID or email and user name to identify the recipient. If user ID is used and a client user ID is provided, the value in the `userId` property must match a recipient ID (which can be retrieved with a GET recipients call) for the envelope. If a user ID is used and a clientUser ID is not provided, the user ID match the user ID of the authenticating user.  # noqa: E501

        :param user_id: The user_id of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this RecipientViewRequest.  # noqa: E501

        Specifies the username of the recipient. You can use either email and userName or userId to identify the recipient.  # noqa: E501

        :return: The user_name of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this RecipientViewRequest.

        Specifies the username of the recipient. You can use either email and userName or userId to identify the recipient.  # noqa: E501

        :param user_name: The user_name of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def x_frame_options(self):
        """Gets the x_frame_options of this RecipientViewRequest.  # noqa: E501

          # noqa: E501

        :return: The x_frame_options of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._x_frame_options

    @x_frame_options.setter
    def x_frame_options(self, x_frame_options):
        """Sets the x_frame_options of this RecipientViewRequest.

          # noqa: E501

        :param x_frame_options: The x_frame_options of this RecipientViewRequest.  # noqa: E501
        :type: str
        """

        self._x_frame_options = x_frame_options

    @property
    def x_frame_options_allow_from_url(self):
        """Gets the x_frame_options_allow_from_url of this RecipientViewRequest.  # noqa: E501

          # noqa: E501

        :return: The x_frame_options_allow_from_url of this RecipientViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._x_frame_options_allow_from_url

    @x_frame_options_allow_from_url.setter
    def x_frame_options_allow_from_url(self, x_frame_options_allow_from_url):
        """Sets the x_frame_options_allow_from_url of this RecipientViewRequest.

          # noqa: E501

        :param x_frame_options_allow_from_url: The x_frame_options_allow_from_url of this RecipientViewRequest.  # noqa: E501
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
        if issubclass(RecipientViewRequest, dict):
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
        if not isinstance(other, RecipientViewRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientViewRequest):
            return True

        return self.to_dict() != other.to_dict()
