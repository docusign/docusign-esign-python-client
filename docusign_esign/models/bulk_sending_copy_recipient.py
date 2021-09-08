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


class BulkSendingCopyRecipient(object):
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
        'client_user_id': 'str',
        'custom_fields': 'list[str]',
        'delivery_method': 'str',
        'email': 'str',
        'email_notification': 'RecipientEmailNotification',
        'embedded_recipient_start_url': 'str',
        'fax_number': 'str',
        'host_email': 'str',
        'host_name': 'str',
        'id_check_configuration_name': 'str',
        'id_check_information_input': 'IdCheckInformationInput',
        'identification_method': 'str',
        'name': 'str',
        'note': 'str',
        'phone_authentication': 'RecipientPhoneAuthentication',
        'recipient_id': 'str',
        'recipient_signature_providers': 'list[RecipientSignatureProvider]',
        'role_name': 'str',
        'signer_name': 'str',
        'signing_group_id': 'str',
        'sms_authentication': 'RecipientSMSAuthentication',
        'social_authentications': 'list[SocialAuthentication]',
        'tabs': 'list[BulkSendingCopyTab]'
    }

    attribute_map = {
        'access_code': 'accessCode',
        'client_user_id': 'clientUserId',
        'custom_fields': 'customFields',
        'delivery_method': 'deliveryMethod',
        'email': 'email',
        'email_notification': 'emailNotification',
        'embedded_recipient_start_url': 'embeddedRecipientStartURL',
        'fax_number': 'faxNumber',
        'host_email': 'hostEmail',
        'host_name': 'hostName',
        'id_check_configuration_name': 'idCheckConfigurationName',
        'id_check_information_input': 'idCheckInformationInput',
        'identification_method': 'identificationMethod',
        'name': 'name',
        'note': 'note',
        'phone_authentication': 'phoneAuthentication',
        'recipient_id': 'recipientId',
        'recipient_signature_providers': 'recipientSignatureProviders',
        'role_name': 'roleName',
        'signer_name': 'signerName',
        'signing_group_id': 'signingGroupId',
        'sms_authentication': 'smsAuthentication',
        'social_authentications': 'socialAuthentications',
        'tabs': 'tabs'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendingCopyRecipient - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_code = None
        self._client_user_id = None
        self._custom_fields = None
        self._delivery_method = None
        self._email = None
        self._email_notification = None
        self._embedded_recipient_start_url = None
        self._fax_number = None
        self._host_email = None
        self._host_name = None
        self._id_check_configuration_name = None
        self._id_check_information_input = None
        self._identification_method = None
        self._name = None
        self._note = None
        self._phone_authentication = None
        self._recipient_id = None
        self._recipient_signature_providers = None
        self._role_name = None
        self._signer_name = None
        self._signing_group_id = None
        self._sms_authentication = None
        self._social_authentications = None
        self._tabs = None
        self.discriminator = None

        setattr(self, "_{}".format('access_code'), kwargs.get('access_code', None))
        setattr(self, "_{}".format('client_user_id'), kwargs.get('client_user_id', None))
        setattr(self, "_{}".format('custom_fields'), kwargs.get('custom_fields', None))
        setattr(self, "_{}".format('delivery_method'), kwargs.get('delivery_method', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('email_notification'), kwargs.get('email_notification', None))
        setattr(self, "_{}".format('embedded_recipient_start_url'), kwargs.get('embedded_recipient_start_url', None))
        setattr(self, "_{}".format('fax_number'), kwargs.get('fax_number', None))
        setattr(self, "_{}".format('host_email'), kwargs.get('host_email', None))
        setattr(self, "_{}".format('host_name'), kwargs.get('host_name', None))
        setattr(self, "_{}".format('id_check_configuration_name'), kwargs.get('id_check_configuration_name', None))
        setattr(self, "_{}".format('id_check_information_input'), kwargs.get('id_check_information_input', None))
        setattr(self, "_{}".format('identification_method'), kwargs.get('identification_method', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('note'), kwargs.get('note', None))
        setattr(self, "_{}".format('phone_authentication'), kwargs.get('phone_authentication', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('recipient_signature_providers'), kwargs.get('recipient_signature_providers', None))
        setattr(self, "_{}".format('role_name'), kwargs.get('role_name', None))
        setattr(self, "_{}".format('signer_name'), kwargs.get('signer_name', None))
        setattr(self, "_{}".format('signing_group_id'), kwargs.get('signing_group_id', None))
        setattr(self, "_{}".format('sms_authentication'), kwargs.get('sms_authentication', None))
        setattr(self, "_{}".format('social_authentications'), kwargs.get('social_authentications', None))
        setattr(self, "_{}".format('tabs'), kwargs.get('tabs', None))

    @property
    def access_code(self):
        """Gets the access_code of this BulkSendingCopyRecipient.  # noqa: E501

        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.  # noqa: E501

        :return: The access_code of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this BulkSendingCopyRecipient.

        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.  # noqa: E501

        :param access_code: The access_code of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._access_code = access_code

    @property
    def client_user_id(self):
        """Gets the client_user_id of this BulkSendingCopyRecipient.  # noqa: E501

        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters.   # noqa: E501

        :return: The client_user_id of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this BulkSendingCopyRecipient.

        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters.   # noqa: E501

        :param client_user_id: The client_user_id of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this BulkSendingCopyRecipient.  # noqa: E501

        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.  # noqa: E501

        :return: The custom_fields of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this BulkSendingCopyRecipient.

        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.  # noqa: E501

        :param custom_fields: The custom_fields of this BulkSendingCopyRecipient.  # noqa: E501
        :type: list[str]
        """

        self._custom_fields = custom_fields

    @property
    def delivery_method(self):
        """Gets the delivery_method of this BulkSendingCopyRecipient.  # noqa: E501

        Reserved: For DocuSign use only.  # noqa: E501

        :return: The delivery_method of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this BulkSendingCopyRecipient.

        Reserved: For DocuSign use only.  # noqa: E501

        :param delivery_method: The delivery_method of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._delivery_method = delivery_method

    @property
    def email(self):
        """Gets the email of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The email of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BulkSendingCopyRecipient.

          # noqa: E501

        :param email: The email of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_notification(self):
        """Gets the email_notification of this BulkSendingCopyRecipient.  # noqa: E501


        :return: The email_notification of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: RecipientEmailNotification
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this BulkSendingCopyRecipient.


        :param email_notification: The email_notification of this BulkSendingCopyRecipient.  # noqa: E501
        :type: RecipientEmailNotification
        """

        self._email_notification = email_notification

    @property
    def embedded_recipient_start_url(self):
        """Gets the embedded_recipient_start_url of this BulkSendingCopyRecipient.  # noqa: E501

        Specifies a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from DocuSign, just as a remote recipient would. When the document link in the email is clicked the recipient is redirected, through DocuSign, to the supplied URL to complete their actions. When routing to the URL, the sender's system (the server responding to the URL) must request a recipient token to launch a signing session.   If set to `SIGN_AT_DOCUSIGN`, the recipient is directed to an embedded signing or viewing process directly at DocuSign. The signing or viewing action is initiated by the DocuSign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that is launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application, DocuSign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets `EmbeddedRecipientStartURL=SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, DocuSign recommends that you use one of the normal DocuSign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) to verify the identity of the recipient.  If the `clientUserId` property is NOT set, and the `embeddedRecipientStartURL` is set, DocuSign will ignore the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the embedded recipient start URL using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The `customFields` property must be set fort the recipient or envelope. The merge fields are enclosed in double brackets.   *Example*:   `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]`   # noqa: E501

        :return: The embedded_recipient_start_url of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._embedded_recipient_start_url

    @embedded_recipient_start_url.setter
    def embedded_recipient_start_url(self, embedded_recipient_start_url):
        """Sets the embedded_recipient_start_url of this BulkSendingCopyRecipient.

        Specifies a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from DocuSign, just as a remote recipient would. When the document link in the email is clicked the recipient is redirected, through DocuSign, to the supplied URL to complete their actions. When routing to the URL, the sender's system (the server responding to the URL) must request a recipient token to launch a signing session.   If set to `SIGN_AT_DOCUSIGN`, the recipient is directed to an embedded signing or viewing process directly at DocuSign. The signing or viewing action is initiated by the DocuSign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that is launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application, DocuSign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets `EmbeddedRecipientStartURL=SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, DocuSign recommends that you use one of the normal DocuSign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) to verify the identity of the recipient.  If the `clientUserId` property is NOT set, and the `embeddedRecipientStartURL` is set, DocuSign will ignore the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the embedded recipient start URL using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The `customFields` property must be set fort the recipient or envelope. The merge fields are enclosed in double brackets.   *Example*:   `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]`   # noqa: E501

        :param embedded_recipient_start_url: The embedded_recipient_start_url of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._embedded_recipient_start_url = embedded_recipient_start_url

    @property
    def fax_number(self):
        """Gets the fax_number of this BulkSendingCopyRecipient.  # noqa: E501

        Reserved:  # noqa: E501

        :return: The fax_number of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this BulkSendingCopyRecipient.

        Reserved:  # noqa: E501

        :param fax_number: The fax_number of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._fax_number = fax_number

    @property
    def host_email(self):
        """Gets the host_email of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The host_email of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._host_email

    @host_email.setter
    def host_email(self, host_email):
        """Sets the host_email of this BulkSendingCopyRecipient.

          # noqa: E501

        :param host_email: The host_email of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._host_email = host_email

    @property
    def host_name(self):
        """Gets the host_name of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The host_name of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this BulkSendingCopyRecipient.

          # noqa: E501

        :param host_name: The host_name of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def id_check_configuration_name(self):
        """Gets the id_check_configuration_name of this BulkSendingCopyRecipient.  # noqa: E501

        Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient,) This overrides any default authentication setting.  *Example*: Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the idCheckConfigurationName should be 'ID Check '. If you wanted to use SMS, it would be 'SMS Auth $' and you would need to add you would need to add phone number information to the `smsAuthentication` node.  # noqa: E501

        :return: The id_check_configuration_name of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._id_check_configuration_name

    @id_check_configuration_name.setter
    def id_check_configuration_name(self, id_check_configuration_name):
        """Sets the id_check_configuration_name of this BulkSendingCopyRecipient.

        Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient,) This overrides any default authentication setting.  *Example*: Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the idCheckConfigurationName should be 'ID Check '. If you wanted to use SMS, it would be 'SMS Auth $' and you would need to add you would need to add phone number information to the `smsAuthentication` node.  # noqa: E501

        :param id_check_configuration_name: The id_check_configuration_name of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._id_check_configuration_name = id_check_configuration_name

    @property
    def id_check_information_input(self):
        """Gets the id_check_information_input of this BulkSendingCopyRecipient.  # noqa: E501


        :return: The id_check_information_input of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: IdCheckInformationInput
        """
        return self._id_check_information_input

    @id_check_information_input.setter
    def id_check_information_input(self, id_check_information_input):
        """Sets the id_check_information_input of this BulkSendingCopyRecipient.


        :param id_check_information_input: The id_check_information_input of this BulkSendingCopyRecipient.  # noqa: E501
        :type: IdCheckInformationInput
        """

        self._id_check_information_input = id_check_information_input

    @property
    def identification_method(self):
        """Gets the identification_method of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The identification_method of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._identification_method

    @identification_method.setter
    def identification_method(self, identification_method):
        """Sets the identification_method of this BulkSendingCopyRecipient.

          # noqa: E501

        :param identification_method: The identification_method of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._identification_method = identification_method

    @property
    def name(self):
        """Gets the name of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The name of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BulkSendingCopyRecipient.

          # noqa: E501

        :param name: The name of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def note(self):
        """Gets the note of this BulkSendingCopyRecipient.  # noqa: E501

        Specifies a note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen.  Maximum Length: 1000 characters.  # noqa: E501

        :return: The note of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this BulkSendingCopyRecipient.

        Specifies a note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen.  Maximum Length: 1000 characters.  # noqa: E501

        :param note: The note of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def phone_authentication(self):
        """Gets the phone_authentication of this BulkSendingCopyRecipient.  # noqa: E501


        :return: The phone_authentication of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: RecipientPhoneAuthentication
        """
        return self._phone_authentication

    @phone_authentication.setter
    def phone_authentication(self, phone_authentication):
        """Sets the phone_authentication of this BulkSendingCopyRecipient.


        :param phone_authentication: The phone_authentication of this BulkSendingCopyRecipient.  # noqa: E501
        :type: RecipientPhoneAuthentication
        """

        self._phone_authentication = phone_authentication

    @property
    def recipient_id(self):
        """Gets the recipient_id of this BulkSendingCopyRecipient.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this BulkSendingCopyRecipient.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def recipient_signature_providers(self):
        """Gets the recipient_signature_providers of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The recipient_signature_providers of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: list[RecipientSignatureProvider]
        """
        return self._recipient_signature_providers

    @recipient_signature_providers.setter
    def recipient_signature_providers(self, recipient_signature_providers):
        """Sets the recipient_signature_providers of this BulkSendingCopyRecipient.

          # noqa: E501

        :param recipient_signature_providers: The recipient_signature_providers of this BulkSendingCopyRecipient.  # noqa: E501
        :type: list[RecipientSignatureProvider]
        """

        self._recipient_signature_providers = recipient_signature_providers

    @property
    def role_name(self):
        """Gets the role_name of this BulkSendingCopyRecipient.  # noqa: E501

        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.  # noqa: E501

        :return: The role_name of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this BulkSendingCopyRecipient.

        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.  # noqa: E501

        :param role_name: The role_name of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def signer_name(self):
        """Gets the signer_name of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The signer_name of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._signer_name

    @signer_name.setter
    def signer_name(self, signer_name):
        """Sets the signer_name of this BulkSendingCopyRecipient.

          # noqa: E501

        :param signer_name: The signer_name of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._signer_name = signer_name

    @property
    def signing_group_id(self):
        """Gets the signing_group_id of this BulkSendingCopyRecipient.  # noqa: E501

        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).  # noqa: E501

        :return: The signing_group_id of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: str
        """
        return self._signing_group_id

    @signing_group_id.setter
    def signing_group_id(self, signing_group_id):
        """Sets the signing_group_id of this BulkSendingCopyRecipient.

        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).  # noqa: E501

        :param signing_group_id: The signing_group_id of this BulkSendingCopyRecipient.  # noqa: E501
        :type: str
        """

        self._signing_group_id = signing_group_id

    @property
    def sms_authentication(self):
        """Gets the sms_authentication of this BulkSendingCopyRecipient.  # noqa: E501


        :return: The sms_authentication of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: RecipientSMSAuthentication
        """
        return self._sms_authentication

    @sms_authentication.setter
    def sms_authentication(self, sms_authentication):
        """Sets the sms_authentication of this BulkSendingCopyRecipient.


        :param sms_authentication: The sms_authentication of this BulkSendingCopyRecipient.  # noqa: E501
        :type: RecipientSMSAuthentication
        """

        self._sms_authentication = sms_authentication

    @property
    def social_authentications(self):
        """Gets the social_authentications of this BulkSendingCopyRecipient.  # noqa: E501

         Lists the social ID type that can be used for recipient authentication.  # noqa: E501

        :return: The social_authentications of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: list[SocialAuthentication]
        """
        return self._social_authentications

    @social_authentications.setter
    def social_authentications(self, social_authentications):
        """Sets the social_authentications of this BulkSendingCopyRecipient.

         Lists the social ID type that can be used for recipient authentication.  # noqa: E501

        :param social_authentications: The social_authentications of this BulkSendingCopyRecipient.  # noqa: E501
        :type: list[SocialAuthentication]
        """

        self._social_authentications = social_authentications

    @property
    def tabs(self):
        """Gets the tabs of this BulkSendingCopyRecipient.  # noqa: E501

          # noqa: E501

        :return: The tabs of this BulkSendingCopyRecipient.  # noqa: E501
        :rtype: list[BulkSendingCopyTab]
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """Sets the tabs of this BulkSendingCopyRecipient.

          # noqa: E501

        :param tabs: The tabs of this BulkSendingCopyRecipient.  # noqa: E501
        :type: list[BulkSendingCopyTab]
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
        if issubclass(BulkSendingCopyRecipient, dict):
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
        if not isinstance(other, BulkSendingCopyRecipient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendingCopyRecipient):
            return True

        return self.to_dict() != other.to_dict()
