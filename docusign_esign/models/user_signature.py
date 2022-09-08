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


class UserSignature(object):
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
        'adopted_date_time': 'str',
        'created_date_time': 'str',
        'custom_field': 'str',
        'date_stamp_properties': 'DateStampProperties',
        'disallow_user_resize_stamp': 'str',
        'error_details': 'ErrorDetails',
        'external_id': 'str',
        'image_base64': 'str',
        'image_type': 'str',
        'initials150_image_id': 'str',
        'initials_image_uri': 'str',
        'is_default': 'str',
        'last_modified_date_time': 'str',
        'nrds_id': 'str',
        'nrds_last_name': 'str',
        'nrds_status': 'str',
        'phonetic_name': 'str',
        'signature150_image_id': 'str',
        'signature_font': 'str',
        'signature_id': 'str',
        'signature_image_uri': 'str',
        'signature_initials': 'str',
        'signature_name': 'str',
        'signature_rights': 'str',
        'signature_type': 'str',
        'stamp_format': 'str',
        'stamp_image_uri': 'str',
        'stamp_size_mm': 'str',
        'stamp_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'adopted_date_time': 'adoptedDateTime',
        'created_date_time': 'createdDateTime',
        'custom_field': 'customField',
        'date_stamp_properties': 'dateStampProperties',
        'disallow_user_resize_stamp': 'disallowUserResizeStamp',
        'error_details': 'errorDetails',
        'external_id': 'externalID',
        'image_base64': 'imageBase64',
        'image_type': 'imageType',
        'initials150_image_id': 'initials150ImageId',
        'initials_image_uri': 'initialsImageUri',
        'is_default': 'isDefault',
        'last_modified_date_time': 'lastModifiedDateTime',
        'nrds_id': 'nrdsId',
        'nrds_last_name': 'nrdsLastName',
        'nrds_status': 'nrdsStatus',
        'phonetic_name': 'phoneticName',
        'signature150_image_id': 'signature150ImageId',
        'signature_font': 'signatureFont',
        'signature_id': 'signatureId',
        'signature_image_uri': 'signatureImageUri',
        'signature_initials': 'signatureInitials',
        'signature_name': 'signatureName',
        'signature_rights': 'signatureRights',
        'signature_type': 'signatureType',
        'stamp_format': 'stampFormat',
        'stamp_image_uri': 'stampImageUri',
        'stamp_size_mm': 'stampSizeMM',
        'stamp_type': 'stampType',
        'status': 'status'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserSignature - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._adopted_date_time = None
        self._created_date_time = None
        self._custom_field = None
        self._date_stamp_properties = None
        self._disallow_user_resize_stamp = None
        self._error_details = None
        self._external_id = None
        self._image_base64 = None
        self._image_type = None
        self._initials150_image_id = None
        self._initials_image_uri = None
        self._is_default = None
        self._last_modified_date_time = None
        self._nrds_id = None
        self._nrds_last_name = None
        self._nrds_status = None
        self._phonetic_name = None
        self._signature150_image_id = None
        self._signature_font = None
        self._signature_id = None
        self._signature_image_uri = None
        self._signature_initials = None
        self._signature_name = None
        self._signature_rights = None
        self._signature_type = None
        self._stamp_format = None
        self._stamp_image_uri = None
        self._stamp_size_mm = None
        self._stamp_type = None
        self._status = None
        self.discriminator = None

        setattr(self, "_{}".format('adopted_date_time'), kwargs.get('adopted_date_time', None))
        setattr(self, "_{}".format('created_date_time'), kwargs.get('created_date_time', None))
        setattr(self, "_{}".format('custom_field'), kwargs.get('custom_field', None))
        setattr(self, "_{}".format('date_stamp_properties'), kwargs.get('date_stamp_properties', None))
        setattr(self, "_{}".format('disallow_user_resize_stamp'), kwargs.get('disallow_user_resize_stamp', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('external_id'), kwargs.get('external_id', None))
        setattr(self, "_{}".format('image_base64'), kwargs.get('image_base64', None))
        setattr(self, "_{}".format('image_type'), kwargs.get('image_type', None))
        setattr(self, "_{}".format('initials150_image_id'), kwargs.get('initials150_image_id', None))
        setattr(self, "_{}".format('initials_image_uri'), kwargs.get('initials_image_uri', None))
        setattr(self, "_{}".format('is_default'), kwargs.get('is_default', None))
        setattr(self, "_{}".format('last_modified_date_time'), kwargs.get('last_modified_date_time', None))
        setattr(self, "_{}".format('nrds_id'), kwargs.get('nrds_id', None))
        setattr(self, "_{}".format('nrds_last_name'), kwargs.get('nrds_last_name', None))
        setattr(self, "_{}".format('nrds_status'), kwargs.get('nrds_status', None))
        setattr(self, "_{}".format('phonetic_name'), kwargs.get('phonetic_name', None))
        setattr(self, "_{}".format('signature150_image_id'), kwargs.get('signature150_image_id', None))
        setattr(self, "_{}".format('signature_font'), kwargs.get('signature_font', None))
        setattr(self, "_{}".format('signature_id'), kwargs.get('signature_id', None))
        setattr(self, "_{}".format('signature_image_uri'), kwargs.get('signature_image_uri', None))
        setattr(self, "_{}".format('signature_initials'), kwargs.get('signature_initials', None))
        setattr(self, "_{}".format('signature_name'), kwargs.get('signature_name', None))
        setattr(self, "_{}".format('signature_rights'), kwargs.get('signature_rights', None))
        setattr(self, "_{}".format('signature_type'), kwargs.get('signature_type', None))
        setattr(self, "_{}".format('stamp_format'), kwargs.get('stamp_format', None))
        setattr(self, "_{}".format('stamp_image_uri'), kwargs.get('stamp_image_uri', None))
        setattr(self, "_{}".format('stamp_size_mm'), kwargs.get('stamp_size_mm', None))
        setattr(self, "_{}".format('stamp_type'), kwargs.get('stamp_type', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))

    @property
    def adopted_date_time(self):
        """Gets the adopted_date_time of this UserSignature.  # noqa: E501

        The date and time the user adopted their signature.  # noqa: E501

        :return: The adopted_date_time of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._adopted_date_time

    @adopted_date_time.setter
    def adopted_date_time(self, adopted_date_time):
        """Sets the adopted_date_time of this UserSignature.

        The date and time the user adopted their signature.  # noqa: E501

        :param adopted_date_time: The adopted_date_time of this UserSignature.  # noqa: E501
        :type: str
        """

        self._adopted_date_time = adopted_date_time

    @property
    def created_date_time(self):
        """Gets the created_date_time of this UserSignature.  # noqa: E501

        Indicates the date and time the item was created.  # noqa: E501

        :return: The created_date_time of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this UserSignature.

        Indicates the date and time the item was created.  # noqa: E501

        :param created_date_time: The created_date_time of this UserSignature.  # noqa: E501
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def custom_field(self):
        """Gets the custom_field of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The custom_field of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this UserSignature.

          # noqa: E501

        :param custom_field: The custom_field of this UserSignature.  # noqa: E501
        :type: str
        """

        self._custom_field = custom_field

    @property
    def date_stamp_properties(self):
        """Gets the date_stamp_properties of this UserSignature.  # noqa: E501

        Specifies the area in which a date stamp is placed. This parameter uses pixel positioning to draw a rectangle at the center of the stamp area. The stamp is superimposed on top of this central area.  This property contains the following information about the central rectangle:  - `DateAreaX`: The X axis position of the top-left corner. - `DateAreaY`: The Y axis position of the top-left corner. - `DateAreaWidth`: The width of the rectangle. - `DateAreaHeight`: The height of the rectangle.  # noqa: E501

        :return: The date_stamp_properties of this UserSignature.  # noqa: E501
        :rtype: DateStampProperties
        """
        return self._date_stamp_properties

    @date_stamp_properties.setter
    def date_stamp_properties(self, date_stamp_properties):
        """Sets the date_stamp_properties of this UserSignature.

        Specifies the area in which a date stamp is placed. This parameter uses pixel positioning to draw a rectangle at the center of the stamp area. The stamp is superimposed on top of this central area.  This property contains the following information about the central rectangle:  - `DateAreaX`: The X axis position of the top-left corner. - `DateAreaY`: The Y axis position of the top-left corner. - `DateAreaWidth`: The width of the rectangle. - `DateAreaHeight`: The height of the rectangle.  # noqa: E501

        :param date_stamp_properties: The date_stamp_properties of this UserSignature.  # noqa: E501
        :type: DateStampProperties
        """

        self._date_stamp_properties = date_stamp_properties

    @property
    def disallow_user_resize_stamp(self):
        """Gets the disallow_user_resize_stamp of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The disallow_user_resize_stamp of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._disallow_user_resize_stamp

    @disallow_user_resize_stamp.setter
    def disallow_user_resize_stamp(self, disallow_user_resize_stamp):
        """Sets the disallow_user_resize_stamp of this UserSignature.

          # noqa: E501

        :param disallow_user_resize_stamp: The disallow_user_resize_stamp of this UserSignature.  # noqa: E501
        :type: str
        """

        self._disallow_user_resize_stamp = disallow_user_resize_stamp

    @property
    def error_details(self):
        """Gets the error_details of this UserSignature.  # noqa: E501

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :return: The error_details of this UserSignature.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this UserSignature.

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :param error_details: The error_details of this UserSignature.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def external_id(self):
        """Gets the external_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The external_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserSignature.

          # noqa: E501

        :param external_id: The external_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def image_base64(self):
        """Gets the image_base64 of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The image_base64 of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this UserSignature.

          # noqa: E501

        :param image_base64: The image_base64 of this UserSignature.  # noqa: E501
        :type: str
        """

        self._image_base64 = image_base64

    @property
    def image_type(self):
        """Gets the image_type of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The image_type of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this UserSignature.

          # noqa: E501

        :param image_type: The image_type of this UserSignature.  # noqa: E501
        :type: str
        """

        self._image_type = image_type

    @property
    def initials150_image_id(self):
        """Gets the initials150_image_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The initials150_image_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._initials150_image_id

    @initials150_image_id.setter
    def initials150_image_id(self, initials150_image_id):
        """Sets the initials150_image_id of this UserSignature.

          # noqa: E501

        :param initials150_image_id: The initials150_image_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._initials150_image_id = initials150_image_id

    @property
    def initials_image_uri(self):
        """Gets the initials_image_uri of this UserSignature.  # noqa: E501

        Contains the URI for an endpoint that you can use to retrieve the initials image.  # noqa: E501

        :return: The initials_image_uri of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._initials_image_uri

    @initials_image_uri.setter
    def initials_image_uri(self, initials_image_uri):
        """Sets the initials_image_uri of this UserSignature.

        Contains the URI for an endpoint that you can use to retrieve the initials image.  # noqa: E501

        :param initials_image_uri: The initials_image_uri of this UserSignature.  # noqa: E501
        :type: str
        """

        self._initials_image_uri = initials_image_uri

    @property
    def is_default(self):
        """Gets the is_default of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The is_default of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this UserSignature.

          # noqa: E501

        :param is_default: The is_default of this UserSignature.  # noqa: E501
        :type: str
        """

        self._is_default = is_default

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this UserSignature.  # noqa: E501

        The date and time the item was last modified.  # noqa: E501

        :return: The last_modified_date_time of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this UserSignature.

        The date and time the item was last modified.  # noqa: E501

        :param last_modified_date_time: The last_modified_date_time of this UserSignature.  # noqa: E501
        :type: str
        """

        self._last_modified_date_time = last_modified_date_time

    @property
    def nrds_id(self):
        """Gets the nrds_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The nrds_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._nrds_id

    @nrds_id.setter
    def nrds_id(self, nrds_id):
        """Sets the nrds_id of this UserSignature.

          # noqa: E501

        :param nrds_id: The nrds_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._nrds_id = nrds_id

    @property
    def nrds_last_name(self):
        """Gets the nrds_last_name of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The nrds_last_name of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._nrds_last_name

    @nrds_last_name.setter
    def nrds_last_name(self, nrds_last_name):
        """Sets the nrds_last_name of this UserSignature.

          # noqa: E501

        :param nrds_last_name: The nrds_last_name of this UserSignature.  # noqa: E501
        :type: str
        """

        self._nrds_last_name = nrds_last_name

    @property
    def nrds_status(self):
        """Gets the nrds_status of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The nrds_status of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._nrds_status

    @nrds_status.setter
    def nrds_status(self, nrds_status):
        """Sets the nrds_status of this UserSignature.

          # noqa: E501

        :param nrds_status: The nrds_status of this UserSignature.  # noqa: E501
        :type: str
        """

        self._nrds_status = nrds_status

    @property
    def phonetic_name(self):
        """Gets the phonetic_name of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The phonetic_name of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._phonetic_name

    @phonetic_name.setter
    def phonetic_name(self, phonetic_name):
        """Sets the phonetic_name of this UserSignature.

          # noqa: E501

        :param phonetic_name: The phonetic_name of this UserSignature.  # noqa: E501
        :type: str
        """

        self._phonetic_name = phonetic_name

    @property
    def signature150_image_id(self):
        """Gets the signature150_image_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The signature150_image_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature150_image_id

    @signature150_image_id.setter
    def signature150_image_id(self, signature150_image_id):
        """Sets the signature150_image_id of this UserSignature.

          # noqa: E501

        :param signature150_image_id: The signature150_image_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature150_image_id = signature150_image_id

    @property
    def signature_font(self):
        """Gets the signature_font of this UserSignature.  # noqa: E501

        The font type for the signature, if the signature is not drawn. The supported font types are:  \"7_DocuSign\", \"1_DocuSign\", \"6_DocuSign\", \"8_DocuSign\", \"3_DocuSign\", \"Mistral\", \"4_DocuSign\", \"2_DocuSign\", \"5_DocuSign\", \"Rage Italic\"   # noqa: E501

        :return: The signature_font of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_font

    @signature_font.setter
    def signature_font(self, signature_font):
        """Sets the signature_font of this UserSignature.

        The font type for the signature, if the signature is not drawn. The supported font types are:  \"7_DocuSign\", \"1_DocuSign\", \"6_DocuSign\", \"8_DocuSign\", \"3_DocuSign\", \"Mistral\", \"4_DocuSign\", \"2_DocuSign\", \"5_DocuSign\", \"Rage Italic\"   # noqa: E501

        :param signature_font: The signature_font of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_font = signature_font

    @property
    def signature_id(self):
        """Gets the signature_id of this UserSignature.  # noqa: E501

        Specifies the signature ID associated with the signature name. You can use the signature ID in the URI in place of the signature name, and the value stored in the `signatureName` property in the body is used. This allows the use of special characters (such as \"&\", \"<\", \">\") in a the signature name. Note that with each update to signatures, the returned signature ID might change, so the caller will need to trigger off the signature name to get the new signature ID.  # noqa: E501

        :return: The signature_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """Sets the signature_id of this UserSignature.

        Specifies the signature ID associated with the signature name. You can use the signature ID in the URI in place of the signature name, and the value stored in the `signatureName` property in the body is used. This allows the use of special characters (such as \"&\", \"<\", \">\") in a the signature name. Note that with each update to signatures, the returned signature ID might change, so the caller will need to trigger off the signature name to get the new signature ID.  # noqa: E501

        :param signature_id: The signature_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_id = signature_id

    @property
    def signature_image_uri(self):
        """Gets the signature_image_uri of this UserSignature.  # noqa: E501

        Contains the URI for an endpoint that you can use to retrieve the signature image.  # noqa: E501

        :return: The signature_image_uri of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_image_uri

    @signature_image_uri.setter
    def signature_image_uri(self, signature_image_uri):
        """Sets the signature_image_uri of this UserSignature.

        Contains the URI for an endpoint that you can use to retrieve the signature image.  # noqa: E501

        :param signature_image_uri: The signature_image_uri of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_image_uri = signature_image_uri

    @property
    def signature_initials(self):
        """Gets the signature_initials of this UserSignature.  # noqa: E501

         The initials associated with the signature.  # noqa: E501

        :return: The signature_initials of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_initials

    @signature_initials.setter
    def signature_initials(self, signature_initials):
        """Sets the signature_initials of this UserSignature.

         The initials associated with the signature.  # noqa: E501

        :param signature_initials: The signature_initials of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_initials = signature_initials

    @property
    def signature_name(self):
        """Gets the signature_name of this UserSignature.  # noqa: E501

        Specifies the user signature name.  # noqa: E501

        :return: The signature_name of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this UserSignature.

        Specifies the user signature name.  # noqa: E501

        :param signature_name: The signature_name of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_name = signature_name

    @property
    def signature_rights(self):
        """Gets the signature_rights of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The signature_rights of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_rights

    @signature_rights.setter
    def signature_rights(self, signature_rights):
        """Sets the signature_rights of this UserSignature.

          # noqa: E501

        :param signature_rights: The signature_rights of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_rights = signature_rights

    @property
    def signature_type(self):
        """Gets the signature_type of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The signature_type of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this UserSignature.

          # noqa: E501

        :param signature_type: The signature_type of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_type = signature_type

    @property
    def stamp_format(self):
        """Gets the stamp_format of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_format of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_format

    @stamp_format.setter
    def stamp_format(self, stamp_format):
        """Sets the stamp_format of this UserSignature.

          # noqa: E501

        :param stamp_format: The stamp_format of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_format = stamp_format

    @property
    def stamp_image_uri(self):
        """Gets the stamp_image_uri of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_image_uri of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_image_uri

    @stamp_image_uri.setter
    def stamp_image_uri(self, stamp_image_uri):
        """Sets the stamp_image_uri of this UserSignature.

          # noqa: E501

        :param stamp_image_uri: The stamp_image_uri of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_image_uri = stamp_image_uri

    @property
    def stamp_size_mm(self):
        """Gets the stamp_size_mm of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_size_mm of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_size_mm

    @stamp_size_mm.setter
    def stamp_size_mm(self, stamp_size_mm):
        """Sets the stamp_size_mm of this UserSignature.

          # noqa: E501

        :param stamp_size_mm: The stamp_size_mm of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_size_mm = stamp_size_mm

    @property
    def stamp_type(self):
        """Gets the stamp_type of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_type of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_type

    @stamp_type.setter
    def stamp_type(self, stamp_type):
        """Sets the stamp_type of this UserSignature.

          # noqa: E501

        :param stamp_type: The stamp_type of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_type = stamp_type

    @property
    def status(self):
        """Gets the status of this UserSignature.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserSignature.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this UserSignature.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(UserSignature, dict):
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
        if not isinstance(other, UserSignature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSignature):
            return True

        return self.to_dict() != other.to_dict()
