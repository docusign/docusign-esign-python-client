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


class TemplateRole(object):
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
        'access_code': 'str',
        'additional_notifications': 'list[RecipientAdditionalNotification]',
        'client_user_id': 'str',
        'default_recipient': 'str',
        'email': 'str',
        'email_notification': 'RecipientEmailNotification',
        'embedded_recipient_start_url': 'str',
        'in_person_signer_name': 'str',
        'name': 'str',
        'phone_number': 'RecipientPhoneNumber',
        'recipient_signature_providers': 'list[RecipientSignatureProvider]',
        'role_name': 'str',
        'routing_order': 'str',
        'signing_group_id': 'str',
        'tabs': 'Tabs'
    }

    attribute_map = {
        'access_code': 'accessCode',
        'additional_notifications': 'additionalNotifications',
        'client_user_id': 'clientUserId',
        'default_recipient': 'defaultRecipient',
        'email': 'email',
        'email_notification': 'emailNotification',
        'embedded_recipient_start_url': 'embeddedRecipientStartURL',
        'in_person_signer_name': 'inPersonSignerName',
        'name': 'name',
        'phone_number': 'phoneNumber',
        'recipient_signature_providers': 'recipientSignatureProviders',
        'role_name': 'roleName',
        'routing_order': 'routingOrder',
        'signing_group_id': 'signingGroupId',
        'tabs': 'tabs'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """TemplateRole - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_code = None
        self._additional_notifications = None
        self._client_user_id = None
        self._default_recipient = None
        self._email = None
        self._email_notification = None
        self._embedded_recipient_start_url = None
        self._in_person_signer_name = None
        self._name = None
        self._phone_number = None
        self._recipient_signature_providers = None
        self._role_name = None
        self._routing_order = None
        self._signing_group_id = None
        self._tabs = None
        self.discriminator = None

        setattr(self, "_{}".format('access_code'), kwargs.get('access_code', None))
        setattr(self, "_{}".format('additional_notifications'), kwargs.get('additional_notifications', None))
        setattr(self, "_{}".format('client_user_id'), kwargs.get('client_user_id', None))
        setattr(self, "_{}".format('default_recipient'), kwargs.get('default_recipient', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('email_notification'), kwargs.get('email_notification', None))
        setattr(self, "_{}".format('embedded_recipient_start_url'), kwargs.get('embedded_recipient_start_url', None))
        setattr(self, "_{}".format('in_person_signer_name'), kwargs.get('in_person_signer_name', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('phone_number'), kwargs.get('phone_number', None))
        setattr(self, "_{}".format('recipient_signature_providers'), kwargs.get('recipient_signature_providers', None))
        setattr(self, "_{}".format('role_name'), kwargs.get('role_name', None))
        setattr(self, "_{}".format('routing_order'), kwargs.get('routing_order', None))
        setattr(self, "_{}".format('signing_group_id'), kwargs.get('signing_group_id', None))
        setattr(self, "_{}".format('tabs'), kwargs.get('tabs', None))

    @property
    def access_code(self):
        """Gets the access_code of this TemplateRole.  # noqa: E501

        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.  # noqa: E501

        :return: The access_code of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this TemplateRole.

        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.  # noqa: E501

        :param access_code: The access_code of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._access_code = access_code

    @property
    def additional_notifications(self):
        """Gets the additional_notifications of this TemplateRole.  # noqa: E501

          # noqa: E501

        :return: The additional_notifications of this TemplateRole.  # noqa: E501
        :rtype: list[RecipientAdditionalNotification]
        """
        return self._additional_notifications

    @additional_notifications.setter
    def additional_notifications(self, additional_notifications):
        """Sets the additional_notifications of this TemplateRole.

          # noqa: E501

        :param additional_notifications: The additional_notifications of this TemplateRole.  # noqa: E501
        :type: list[RecipientAdditionalNotification]
        """

        self._additional_notifications = additional_notifications

    @property
    def client_user_id(self):
        """Gets the client_user_id of this TemplateRole.  # noqa: E501

        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters.   # noqa: E501

        :return: The client_user_id of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this TemplateRole.

        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters.   # noqa: E501

        :param client_user_id: The client_user_id of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def default_recipient(self):
        """Gets the default_recipient of this TemplateRole.  # noqa: E501

        When set to **true**, this recipient is the default recipient and any tabs generated by the transformPdfFields option are mapped to this recipient.  # noqa: E501

        :return: The default_recipient of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._default_recipient

    @default_recipient.setter
    def default_recipient(self, default_recipient):
        """Sets the default_recipient of this TemplateRole.

        When set to **true**, this recipient is the default recipient and any tabs generated by the transformPdfFields option are mapped to this recipient.  # noqa: E501

        :param default_recipient: The default_recipient of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._default_recipient = default_recipient

    @property
    def email(self):
        """Gets the email of this TemplateRole.  # noqa: E501

        Specifies the email associated with a role name.  # noqa: E501

        :return: The email of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TemplateRole.

        Specifies the email associated with a role name.  # noqa: E501

        :param email: The email of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_notification(self):
        """Gets the email_notification of this TemplateRole.  # noqa: E501

        An optional complex type that sets a specific email subject and body for this recipient's notification email.   **Note:** You can set the `emailNotification` property separately for each recipient. If you set the value only for certain recipients, the other recipients will inherit the this value from the top-level `emailSubject` and `emailBlurb`.   # noqa: E501

        :return: The email_notification of this TemplateRole.  # noqa: E501
        :rtype: RecipientEmailNotification
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this TemplateRole.

        An optional complex type that sets a specific email subject and body for this recipient's notification email.   **Note:** You can set the `emailNotification` property separately for each recipient. If you set the value only for certain recipients, the other recipients will inherit the this value from the top-level `emailSubject` and `emailBlurb`.   # noqa: E501

        :param email_notification: The email_notification of this TemplateRole.  # noqa: E501
        :type: RecipientEmailNotification
        """

        self._email_notification = email_notification

    @property
    def embedded_recipient_start_url(self):
        """Gets the embedded_recipient_start_url of this TemplateRole.  # noqa: E501

        Specifies a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from DocuSign, just as a remote recipient would. When the document link in the email is clicked the recipient is redirected, through DocuSign, to the supplied URL to complete their actions. When routing to the URL, the sender's system (the server responding to the URL) must request a recipient token to launch a signing session.   If set to `SIGN_AT_DOCUSIGN`, the recipient is directed to an embedded signing or viewing process directly at DocuSign. The signing or viewing action is initiated by the DocuSign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that is launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application, DocuSign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets `EmbeddedRecipientStartURL=SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, DocuSign recommends that you use one of the normal DocuSign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) to verify the identity of the recipient.  If the `clientUserId` property is NOT set, and the `embeddedRecipientStartURL` is set, DocuSign will ignore the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the embedded recipient start URL using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The `customFields` property must be set fort the recipient or envelope. The merge fields are enclosed in double brackets.   *Example*:   `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]`   # noqa: E501

        :return: The embedded_recipient_start_url of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._embedded_recipient_start_url

    @embedded_recipient_start_url.setter
    def embedded_recipient_start_url(self, embedded_recipient_start_url):
        """Sets the embedded_recipient_start_url of this TemplateRole.

        Specifies a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from DocuSign, just as a remote recipient would. When the document link in the email is clicked the recipient is redirected, through DocuSign, to the supplied URL to complete their actions. When routing to the URL, the sender's system (the server responding to the URL) must request a recipient token to launch a signing session.   If set to `SIGN_AT_DOCUSIGN`, the recipient is directed to an embedded signing or viewing process directly at DocuSign. The signing or viewing action is initiated by the DocuSign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that is launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application, DocuSign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets `EmbeddedRecipientStartURL=SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, DocuSign recommends that you use one of the normal DocuSign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) to verify the identity of the recipient.  If the `clientUserId` property is NOT set, and the `embeddedRecipientStartURL` is set, DocuSign will ignore the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the embedded recipient start URL using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The `customFields` property must be set fort the recipient or envelope. The merge fields are enclosed in double brackets.   *Example*:   `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]`   # noqa: E501

        :param embedded_recipient_start_url: The embedded_recipient_start_url of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._embedded_recipient_start_url = embedded_recipient_start_url

    @property
    def in_person_signer_name(self):
        """Gets the in_person_signer_name of this TemplateRole.  # noqa: E501

        Specifies the full legal name of the signer in person signer template roles.  Maximum Length: 100 characters.  # noqa: E501

        :return: The in_person_signer_name of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._in_person_signer_name

    @in_person_signer_name.setter
    def in_person_signer_name(self, in_person_signer_name):
        """Sets the in_person_signer_name of this TemplateRole.

        Specifies the full legal name of the signer in person signer template roles.  Maximum Length: 100 characters.  # noqa: E501

        :param in_person_signer_name: The in_person_signer_name of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._in_person_signer_name = in_person_signer_name

    @property
    def name(self):
        """Gets the name of this TemplateRole.  # noqa: E501

        Specifies the recipient's name.  # noqa: E501

        :return: The name of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateRole.

        Specifies the recipient's name.  # noqa: E501

        :param name: The name of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_number(self):
        """Gets the phone_number of this TemplateRole.  # noqa: E501

        Describes the recipient phone number.  # noqa: E501

        :return: The phone_number of this TemplateRole.  # noqa: E501
        :rtype: RecipientPhoneNumber
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this TemplateRole.

        Describes the recipient phone number.  # noqa: E501

        :param phone_number: The phone_number of this TemplateRole.  # noqa: E501
        :type: RecipientPhoneNumber
        """

        self._phone_number = phone_number

    @property
    def recipient_signature_providers(self):
        """Gets the recipient_signature_providers of this TemplateRole.  # noqa: E501

          # noqa: E501

        :return: The recipient_signature_providers of this TemplateRole.  # noqa: E501
        :rtype: list[RecipientSignatureProvider]
        """
        return self._recipient_signature_providers

    @recipient_signature_providers.setter
    def recipient_signature_providers(self, recipient_signature_providers):
        """Sets the recipient_signature_providers of this TemplateRole.

          # noqa: E501

        :param recipient_signature_providers: The recipient_signature_providers of this TemplateRole.  # noqa: E501
        :type: list[RecipientSignatureProvider]
        """

        self._recipient_signature_providers = recipient_signature_providers

    @property
    def role_name(self):
        """Gets the role_name of this TemplateRole.  # noqa: E501

        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.  # noqa: E501

        :return: The role_name of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this TemplateRole.

        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.  # noqa: E501

        :param role_name: The role_name of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def routing_order(self):
        """Gets the routing_order of this TemplateRole.  # noqa: E501

        Specifies the routing order of the recipient in the envelope.   # noqa: E501

        :return: The routing_order of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._routing_order

    @routing_order.setter
    def routing_order(self, routing_order):
        """Sets the routing_order of this TemplateRole.

        Specifies the routing order of the recipient in the envelope.   # noqa: E501

        :param routing_order: The routing_order of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._routing_order = routing_order

    @property
    def signing_group_id(self):
        """Gets the signing_group_id of this TemplateRole.  # noqa: E501

        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).  # noqa: E501

        :return: The signing_group_id of this TemplateRole.  # noqa: E501
        :rtype: str
        """
        return self._signing_group_id

    @signing_group_id.setter
    def signing_group_id(self, signing_group_id):
        """Sets the signing_group_id of this TemplateRole.

        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).  # noqa: E501

        :param signing_group_id: The signing_group_id of this TemplateRole.  # noqa: E501
        :type: str
        """

        self._signing_group_id = signing_group_id

    @property
    def tabs(self):
        """Gets the tabs of this TemplateRole.  # noqa: E501

        A list of tabs, which are represented graphically as symbols on documents at the time of signing. Tabs show recipients where to sign, initial, or enter data. They may also display data to the recipients.  # noqa: E501

        :return: The tabs of this TemplateRole.  # noqa: E501
        :rtype: Tabs
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """Sets the tabs of this TemplateRole.

        A list of tabs, which are represented graphically as symbols on documents at the time of signing. Tabs show recipients where to sign, initial, or enter data. They may also display data to the recipients.  # noqa: E501

        :param tabs: The tabs of this TemplateRole.  # noqa: E501
        :type: Tabs
        """

        self._tabs = tabs

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
        if issubclass(TemplateRole, dict):
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
        if not isinstance(other, TemplateRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateRole):
            return True

        return self.to_dict() != other.to_dict()
