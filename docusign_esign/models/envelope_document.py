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


class EnvelopeDocument(object):
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
        'added_recipient_ids': 'list[str]',
        'attachment_tab_id': 'str',
        'authoritative_copy': 'str',
        'authoritative_copy_metadata': 'PropertyMetadata',
        'available_document_types': 'list[SignatureType]',
        'contains_pdf_form_fields': 'str',
        'display': 'str',
        'display_metadata': 'PropertyMetadata',
        'doc_gen_document_status': 'str',
        'doc_gen_errors': 'list[DocGenSyntaxError]',
        'doc_gen_form_fields': 'list[DocGenFormField]',
        'document_base64': 'str',
        'document_fields': 'list[NameValue]',
        'document_id': 'str',
        'document_id_guid': 'str',
        'error_details': 'ErrorDetails',
        'include_in_download': 'str',
        'include_in_download_metadata': 'PropertyMetadata',
        'is_ace_gen_document': 'str',
        'is_doc_gen_document': 'str',
        'name': 'str',
        'name_metadata': 'PropertyMetadata',
        'order': 'str',
        'pages': 'list[Page]',
        'signer_must_acknowledge': 'str',
        'signer_must_acknowledge_metadata': 'PropertyMetadata',
        'size_bytes': 'str',
        'template_locked': 'str',
        'template_required': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'added_recipient_ids': 'addedRecipientIds',
        'attachment_tab_id': 'attachmentTabId',
        'authoritative_copy': 'authoritativeCopy',
        'authoritative_copy_metadata': 'authoritativeCopyMetadata',
        'available_document_types': 'availableDocumentTypes',
        'contains_pdf_form_fields': 'containsPdfFormFields',
        'display': 'display',
        'display_metadata': 'displayMetadata',
        'doc_gen_document_status': 'docGenDocumentStatus',
        'doc_gen_errors': 'docGenErrors',
        'doc_gen_form_fields': 'docGenFormFields',
        'document_base64': 'documentBase64',
        'document_fields': 'documentFields',
        'document_id': 'documentId',
        'document_id_guid': 'documentIdGuid',
        'error_details': 'errorDetails',
        'include_in_download': 'includeInDownload',
        'include_in_download_metadata': 'includeInDownloadMetadata',
        'is_ace_gen_document': 'isAceGenDocument',
        'is_doc_gen_document': 'isDocGenDocument',
        'name': 'name',
        'name_metadata': 'nameMetadata',
        'order': 'order',
        'pages': 'pages',
        'signer_must_acknowledge': 'signerMustAcknowledge',
        'signer_must_acknowledge_metadata': 'signerMustAcknowledgeMetadata',
        'size_bytes': 'sizeBytes',
        'template_locked': 'templateLocked',
        'template_required': 'templateRequired',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopeDocument - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._added_recipient_ids = None
        self._attachment_tab_id = None
        self._authoritative_copy = None
        self._authoritative_copy_metadata = None
        self._available_document_types = None
        self._contains_pdf_form_fields = None
        self._display = None
        self._display_metadata = None
        self._doc_gen_document_status = None
        self._doc_gen_errors = None
        self._doc_gen_form_fields = None
        self._document_base64 = None
        self._document_fields = None
        self._document_id = None
        self._document_id_guid = None
        self._error_details = None
        self._include_in_download = None
        self._include_in_download_metadata = None
        self._is_ace_gen_document = None
        self._is_doc_gen_document = None
        self._name = None
        self._name_metadata = None
        self._order = None
        self._pages = None
        self._signer_must_acknowledge = None
        self._signer_must_acknowledge_metadata = None
        self._size_bytes = None
        self._template_locked = None
        self._template_required = None
        self._type = None
        self._uri = None
        self.discriminator = None

        setattr(self, "_{}".format('added_recipient_ids'), kwargs.get('added_recipient_ids', None))
        setattr(self, "_{}".format('attachment_tab_id'), kwargs.get('attachment_tab_id', None))
        setattr(self, "_{}".format('authoritative_copy'), kwargs.get('authoritative_copy', None))
        setattr(self, "_{}".format('authoritative_copy_metadata'), kwargs.get('authoritative_copy_metadata', None))
        setattr(self, "_{}".format('available_document_types'), kwargs.get('available_document_types', None))
        setattr(self, "_{}".format('contains_pdf_form_fields'), kwargs.get('contains_pdf_form_fields', None))
        setattr(self, "_{}".format('display'), kwargs.get('display', None))
        setattr(self, "_{}".format('display_metadata'), kwargs.get('display_metadata', None))
        setattr(self, "_{}".format('doc_gen_document_status'), kwargs.get('doc_gen_document_status', None))
        setattr(self, "_{}".format('doc_gen_errors'), kwargs.get('doc_gen_errors', None))
        setattr(self, "_{}".format('doc_gen_form_fields'), kwargs.get('doc_gen_form_fields', None))
        setattr(self, "_{}".format('document_base64'), kwargs.get('document_base64', None))
        setattr(self, "_{}".format('document_fields'), kwargs.get('document_fields', None))
        setattr(self, "_{}".format('document_id'), kwargs.get('document_id', None))
        setattr(self, "_{}".format('document_id_guid'), kwargs.get('document_id_guid', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('include_in_download'), kwargs.get('include_in_download', None))
        setattr(self, "_{}".format('include_in_download_metadata'), kwargs.get('include_in_download_metadata', None))
        setattr(self, "_{}".format('is_ace_gen_document'), kwargs.get('is_ace_gen_document', None))
        setattr(self, "_{}".format('is_doc_gen_document'), kwargs.get('is_doc_gen_document', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('name_metadata'), kwargs.get('name_metadata', None))
        setattr(self, "_{}".format('order'), kwargs.get('order', None))
        setattr(self, "_{}".format('pages'), kwargs.get('pages', None))
        setattr(self, "_{}".format('signer_must_acknowledge'), kwargs.get('signer_must_acknowledge', None))
        setattr(self, "_{}".format('signer_must_acknowledge_metadata'), kwargs.get('signer_must_acknowledge_metadata', None))
        setattr(self, "_{}".format('size_bytes'), kwargs.get('size_bytes', None))
        setattr(self, "_{}".format('template_locked'), kwargs.get('template_locked', None))
        setattr(self, "_{}".format('template_required'), kwargs.get('template_required', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))
        setattr(self, "_{}".format('uri'), kwargs.get('uri', None))

    @property
    def added_recipient_ids(self):
        """Gets the added_recipient_ids of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The added_recipient_ids of this EnvelopeDocument.  # noqa: E501
        :rtype: list[str]
        """
        return self._added_recipient_ids

    @added_recipient_ids.setter
    def added_recipient_ids(self, added_recipient_ids):
        """Sets the added_recipient_ids of this EnvelopeDocument.

          # noqa: E501

        :param added_recipient_ids: The added_recipient_ids of this EnvelopeDocument.  # noqa: E501
        :type: list[str]
        """

        self._added_recipient_ids = added_recipient_ids

    @property
    def attachment_tab_id(self):
        """Gets the attachment_tab_id of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The attachment_tab_id of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._attachment_tab_id

    @attachment_tab_id.setter
    def attachment_tab_id(self, attachment_tab_id):
        """Sets the attachment_tab_id of this EnvelopeDocument.

          # noqa: E501

        :param attachment_tab_id: The attachment_tab_id of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._attachment_tab_id = attachment_tab_id

    @property
    def authoritative_copy(self):
        """Gets the authoritative_copy of this EnvelopeDocument.  # noqa: E501

        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.  # noqa: E501

        :return: The authoritative_copy of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._authoritative_copy

    @authoritative_copy.setter
    def authoritative_copy(self, authoritative_copy):
        """Sets the authoritative_copy of this EnvelopeDocument.

        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.  # noqa: E501

        :param authoritative_copy: The authoritative_copy of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._authoritative_copy = authoritative_copy

    @property
    def authoritative_copy_metadata(self):
        """Gets the authoritative_copy_metadata of this EnvelopeDocument.  # noqa: E501

        Metadata that indicates if the sender can edit the `authoritativeCopy` property. Not applicable for template documents.  # noqa: E501

        :return: The authoritative_copy_metadata of this EnvelopeDocument.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._authoritative_copy_metadata

    @authoritative_copy_metadata.setter
    def authoritative_copy_metadata(self, authoritative_copy_metadata):
        """Sets the authoritative_copy_metadata of this EnvelopeDocument.

        Metadata that indicates if the sender can edit the `authoritativeCopy` property. Not applicable for template documents.  # noqa: E501

        :param authoritative_copy_metadata: The authoritative_copy_metadata of this EnvelopeDocument.  # noqa: E501
        :type: PropertyMetadata
        """

        self._authoritative_copy_metadata = authoritative_copy_metadata

    @property
    def available_document_types(self):
        """Gets the available_document_types of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The available_document_types of this EnvelopeDocument.  # noqa: E501
        :rtype: list[SignatureType]
        """
        return self._available_document_types

    @available_document_types.setter
    def available_document_types(self, available_document_types):
        """Sets the available_document_types of this EnvelopeDocument.

          # noqa: E501

        :param available_document_types: The available_document_types of this EnvelopeDocument.  # noqa: E501
        :type: list[SignatureType]
        """

        self._available_document_types = available_document_types

    @property
    def contains_pdf_form_fields(self):
        """Gets the contains_pdf_form_fields of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The contains_pdf_form_fields of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._contains_pdf_form_fields

    @contains_pdf_form_fields.setter
    def contains_pdf_form_fields(self, contains_pdf_form_fields):
        """Sets the contains_pdf_form_fields of this EnvelopeDocument.

          # noqa: E501

        :param contains_pdf_form_fields: The contains_pdf_form_fields of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._contains_pdf_form_fields = contains_pdf_form_fields

    @property
    def display(self):
        """Gets the display of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The display of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this EnvelopeDocument.

          # noqa: E501

        :param display: The display of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._display = display

    @property
    def display_metadata(self):
        """Gets the display_metadata of this EnvelopeDocument.  # noqa: E501

        Metadata that indicates if the sender can edit the `display` property. Not applicable for template documents.  # noqa: E501

        :return: The display_metadata of this EnvelopeDocument.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._display_metadata

    @display_metadata.setter
    def display_metadata(self, display_metadata):
        """Sets the display_metadata of this EnvelopeDocument.

        Metadata that indicates if the sender can edit the `display` property. Not applicable for template documents.  # noqa: E501

        :param display_metadata: The display_metadata of this EnvelopeDocument.  # noqa: E501
        :type: PropertyMetadata
        """

        self._display_metadata = display_metadata

    @property
    def doc_gen_document_status(self):
        """Gets the doc_gen_document_status of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The doc_gen_document_status of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._doc_gen_document_status

    @doc_gen_document_status.setter
    def doc_gen_document_status(self, doc_gen_document_status):
        """Sets the doc_gen_document_status of this EnvelopeDocument.

          # noqa: E501

        :param doc_gen_document_status: The doc_gen_document_status of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._doc_gen_document_status = doc_gen_document_status

    @property
    def doc_gen_errors(self):
        """Gets the doc_gen_errors of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The doc_gen_errors of this EnvelopeDocument.  # noqa: E501
        :rtype: list[DocGenSyntaxError]
        """
        return self._doc_gen_errors

    @doc_gen_errors.setter
    def doc_gen_errors(self, doc_gen_errors):
        """Sets the doc_gen_errors of this EnvelopeDocument.

          # noqa: E501

        :param doc_gen_errors: The doc_gen_errors of this EnvelopeDocument.  # noqa: E501
        :type: list[DocGenSyntaxError]
        """

        self._doc_gen_errors = doc_gen_errors

    @property
    def doc_gen_form_fields(self):
        """Gets the doc_gen_form_fields of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The doc_gen_form_fields of this EnvelopeDocument.  # noqa: E501
        :rtype: list[DocGenFormField]
        """
        return self._doc_gen_form_fields

    @doc_gen_form_fields.setter
    def doc_gen_form_fields(self, doc_gen_form_fields):
        """Sets the doc_gen_form_fields of this EnvelopeDocument.

          # noqa: E501

        :param doc_gen_form_fields: The doc_gen_form_fields of this EnvelopeDocument.  # noqa: E501
        :type: list[DocGenFormField]
        """

        self._doc_gen_form_fields = doc_gen_form_fields

    @property
    def document_base64(self):
        """Gets the document_base64 of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The document_base64 of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_base64

    @document_base64.setter
    def document_base64(self, document_base64):
        """Sets the document_base64 of this EnvelopeDocument.

          # noqa: E501

        :param document_base64: The document_base64 of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._document_base64 = document_base64

    @property
    def document_fields(self):
        """Gets the document_fields of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The document_fields of this EnvelopeDocument.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._document_fields

    @document_fields.setter
    def document_fields(self, document_fields):
        """Sets the document_fields of this EnvelopeDocument.

          # noqa: E501

        :param document_fields: The document_fields of this EnvelopeDocument.  # noqa: E501
        :type: list[NameValue]
        """

        self._document_fields = document_fields

    @property
    def document_id(self):
        """Gets the document_id of this EnvelopeDocument.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this EnvelopeDocument.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_id_guid(self):
        """Gets the document_id_guid of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The document_id_guid of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_id_guid

    @document_id_guid.setter
    def document_id_guid(self, document_id_guid):
        """Sets the document_id_guid of this EnvelopeDocument.

          # noqa: E501

        :param document_id_guid: The document_id_guid of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._document_id_guid = document_id_guid

    @property
    def error_details(self):
        """Gets the error_details of this EnvelopeDocument.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this EnvelopeDocument.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this EnvelopeDocument.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this EnvelopeDocument.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def include_in_download(self):
        """Gets the include_in_download of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The include_in_download of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._include_in_download

    @include_in_download.setter
    def include_in_download(self, include_in_download):
        """Sets the include_in_download of this EnvelopeDocument.

          # noqa: E501

        :param include_in_download: The include_in_download of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._include_in_download = include_in_download

    @property
    def include_in_download_metadata(self):
        """Gets the include_in_download_metadata of this EnvelopeDocument.  # noqa: E501

        Metadata that indicates if the sender can edit the `includeInDownload` property. Not applicable for template documents.  # noqa: E501

        :return: The include_in_download_metadata of this EnvelopeDocument.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._include_in_download_metadata

    @include_in_download_metadata.setter
    def include_in_download_metadata(self, include_in_download_metadata):
        """Sets the include_in_download_metadata of this EnvelopeDocument.

        Metadata that indicates if the sender can edit the `includeInDownload` property. Not applicable for template documents.  # noqa: E501

        :param include_in_download_metadata: The include_in_download_metadata of this EnvelopeDocument.  # noqa: E501
        :type: PropertyMetadata
        """

        self._include_in_download_metadata = include_in_download_metadata

    @property
    def is_ace_gen_document(self):
        """Gets the is_ace_gen_document of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The is_ace_gen_document of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._is_ace_gen_document

    @is_ace_gen_document.setter
    def is_ace_gen_document(self, is_ace_gen_document):
        """Sets the is_ace_gen_document of this EnvelopeDocument.

          # noqa: E501

        :param is_ace_gen_document: The is_ace_gen_document of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._is_ace_gen_document = is_ace_gen_document

    @property
    def is_doc_gen_document(self):
        """Gets the is_doc_gen_document of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The is_doc_gen_document of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._is_doc_gen_document

    @is_doc_gen_document.setter
    def is_doc_gen_document(self, is_doc_gen_document):
        """Sets the is_doc_gen_document of this EnvelopeDocument.

          # noqa: E501

        :param is_doc_gen_document: The is_doc_gen_document of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._is_doc_gen_document = is_doc_gen_document

    @property
    def name(self):
        """Gets the name of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The name of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvelopeDocument.

          # noqa: E501

        :param name: The name of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_metadata(self):
        """Gets the name_metadata of this EnvelopeDocument.  # noqa: E501

        Metadata that indicates if the sender can edit the `name` property. Not applicable for template documents.  # noqa: E501

        :return: The name_metadata of this EnvelopeDocument.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._name_metadata

    @name_metadata.setter
    def name_metadata(self, name_metadata):
        """Sets the name_metadata of this EnvelopeDocument.

        Metadata that indicates if the sender can edit the `name` property. Not applicable for template documents.  # noqa: E501

        :param name_metadata: The name_metadata of this EnvelopeDocument.  # noqa: E501
        :type: PropertyMetadata
        """

        self._name_metadata = name_metadata

    @property
    def order(self):
        """Gets the order of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The order of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this EnvelopeDocument.

          # noqa: E501

        :param order: The order of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def pages(self):
        """Gets the pages of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The pages of this EnvelopeDocument.  # noqa: E501
        :rtype: list[Page]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this EnvelopeDocument.

          # noqa: E501

        :param pages: The pages of this EnvelopeDocument.  # noqa: E501
        :type: list[Page]
        """

        self._pages = pages

    @property
    def signer_must_acknowledge(self):
        """Gets the signer_must_acknowledge of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The signer_must_acknowledge of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._signer_must_acknowledge

    @signer_must_acknowledge.setter
    def signer_must_acknowledge(self, signer_must_acknowledge):
        """Sets the signer_must_acknowledge of this EnvelopeDocument.

          # noqa: E501

        :param signer_must_acknowledge: The signer_must_acknowledge of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._signer_must_acknowledge = signer_must_acknowledge

    @property
    def signer_must_acknowledge_metadata(self):
        """Gets the signer_must_acknowledge_metadata of this EnvelopeDocument.  # noqa: E501

        Metadata that indicates if the sender can edit the `signerMustAcknowledge` property. Not applicable for template documents.  # noqa: E501

        :return: The signer_must_acknowledge_metadata of this EnvelopeDocument.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._signer_must_acknowledge_metadata

    @signer_must_acknowledge_metadata.setter
    def signer_must_acknowledge_metadata(self, signer_must_acknowledge_metadata):
        """Sets the signer_must_acknowledge_metadata of this EnvelopeDocument.

        Metadata that indicates if the sender can edit the `signerMustAcknowledge` property. Not applicable for template documents.  # noqa: E501

        :param signer_must_acknowledge_metadata: The signer_must_acknowledge_metadata of this EnvelopeDocument.  # noqa: E501
        :type: PropertyMetadata
        """

        self._signer_must_acknowledge_metadata = signer_must_acknowledge_metadata

    @property
    def size_bytes(self):
        """Gets the size_bytes of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The size_bytes of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this EnvelopeDocument.

          # noqa: E501

        :param size_bytes: The size_bytes of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._size_bytes = size_bytes

    @property
    def template_locked(self):
        """Gets the template_locked of this EnvelopeDocument.  # noqa: E501

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :return: The template_locked of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """Sets the template_locked of this EnvelopeDocument.

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :param template_locked: The template_locked of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_required(self):
        """Gets the template_required of this EnvelopeDocument.  # noqa: E501

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :return: The template_required of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """Sets the template_required of this EnvelopeDocument.

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :param template_required: The template_required of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._template_required = template_required

    @property
    def type(self):
        """Gets the type of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The type of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EnvelopeDocument.

          # noqa: E501

        :param type: The type of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this EnvelopeDocument.  # noqa: E501

          # noqa: E501

        :return: The uri of this EnvelopeDocument.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EnvelopeDocument.

          # noqa: E501

        :param uri: The uri of this EnvelopeDocument.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(EnvelopeDocument, dict):
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
        if not isinstance(other, EnvelopeDocument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopeDocument):
            return True

        return self.to_dict() != other.to_dict()
