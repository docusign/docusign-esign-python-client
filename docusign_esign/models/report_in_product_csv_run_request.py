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


class ReportInProductCsvRunRequest(object):
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
        'authentication_success_filter': 'str',
        'custom_field_filter': 'str',
        'date_range_custom_from_date': 'str',
        'date_range_custom_to_date': 'str',
        'date_range_filter': 'str',
        'envelope_date_type_filter': 'str',
        'envelope_recipient_name_contains_filter': 'str',
        'envelope_status_filter': 'str',
        'envelope_subject_contains_filter': 'str',
        'fields': 'list[ReportInProductField]',
        'for_download': 'str',
        'is_dashboard': 'str',
        'new_line': 'str',
        'override_timezone_key': 'str',
        'period_length_filter': 'str',
        'quote': 'str',
        'report_customized_id': 'str',
        'report_description': 'str',
        'report_id': 'str',
        'report_invocation_type': 'str',
        'report_name': 'str',
        'sent_by_filter': 'str',
        'sent_by_ids': 'str',
        'separator': 'str',
        'sort_direction': 'str',
        'sort_field': 'str',
        'start_position': 'str',
        'verification_status_filter': 'str'
    }

    attribute_map = {
        'authentication_success_filter': 'authenticationSuccessFilter',
        'custom_field_filter': 'customFieldFilter',
        'date_range_custom_from_date': 'dateRangeCustomFromDate',
        'date_range_custom_to_date': 'dateRangeCustomToDate',
        'date_range_filter': 'dateRangeFilter',
        'envelope_date_type_filter': 'envelopeDateTypeFilter',
        'envelope_recipient_name_contains_filter': 'envelopeRecipientNameContainsFilter',
        'envelope_status_filter': 'envelopeStatusFilter',
        'envelope_subject_contains_filter': 'envelopeSubjectContainsFilter',
        'fields': 'fields',
        'for_download': 'forDownload',
        'is_dashboard': 'isDashboard',
        'new_line': 'newLine',
        'override_timezone_key': 'overrideTimezoneKey',
        'period_length_filter': 'periodLengthFilter',
        'quote': 'quote',
        'report_customized_id': 'reportCustomizedId',
        'report_description': 'reportDescription',
        'report_id': 'reportId',
        'report_invocation_type': 'reportInvocationType',
        'report_name': 'reportName',
        'sent_by_filter': 'sentByFilter',
        'sent_by_ids': 'sentByIds',
        'separator': 'separator',
        'sort_direction': 'sortDirection',
        'sort_field': 'sortField',
        'start_position': 'startPosition',
        'verification_status_filter': 'verificationStatusFilter'
    }

    def __init__(self, authentication_success_filter=None, custom_field_filter=None, date_range_custom_from_date=None, date_range_custom_to_date=None, date_range_filter=None, envelope_date_type_filter=None, envelope_recipient_name_contains_filter=None, envelope_status_filter=None, envelope_subject_contains_filter=None, fields=None, for_download=None, is_dashboard=None, new_line=None, override_timezone_key=None, period_length_filter=None, quote=None, report_customized_id=None, report_description=None, report_id=None, report_invocation_type=None, report_name=None, sent_by_filter=None, sent_by_ids=None, separator=None, sort_direction=None, sort_field=None, start_position=None, verification_status_filter=None):  # noqa: E501
        """ReportInProductCsvRunRequest - a model defined in Swagger"""  # noqa: E501

        self._authentication_success_filter = None
        self._custom_field_filter = None
        self._date_range_custom_from_date = None
        self._date_range_custom_to_date = None
        self._date_range_filter = None
        self._envelope_date_type_filter = None
        self._envelope_recipient_name_contains_filter = None
        self._envelope_status_filter = None
        self._envelope_subject_contains_filter = None
        self._fields = None
        self._for_download = None
        self._is_dashboard = None
        self._new_line = None
        self._override_timezone_key = None
        self._period_length_filter = None
        self._quote = None
        self._report_customized_id = None
        self._report_description = None
        self._report_id = None
        self._report_invocation_type = None
        self._report_name = None
        self._sent_by_filter = None
        self._sent_by_ids = None
        self._separator = None
        self._sort_direction = None
        self._sort_field = None
        self._start_position = None
        self._verification_status_filter = None
        self.discriminator = None

        if authentication_success_filter is not None:
            self.authentication_success_filter = authentication_success_filter
        if custom_field_filter is not None:
            self.custom_field_filter = custom_field_filter
        if date_range_custom_from_date is not None:
            self.date_range_custom_from_date = date_range_custom_from_date
        if date_range_custom_to_date is not None:
            self.date_range_custom_to_date = date_range_custom_to_date
        if date_range_filter is not None:
            self.date_range_filter = date_range_filter
        if envelope_date_type_filter is not None:
            self.envelope_date_type_filter = envelope_date_type_filter
        if envelope_recipient_name_contains_filter is not None:
            self.envelope_recipient_name_contains_filter = envelope_recipient_name_contains_filter
        if envelope_status_filter is not None:
            self.envelope_status_filter = envelope_status_filter
        if envelope_subject_contains_filter is not None:
            self.envelope_subject_contains_filter = envelope_subject_contains_filter
        if fields is not None:
            self.fields = fields
        if for_download is not None:
            self.for_download = for_download
        if is_dashboard is not None:
            self.is_dashboard = is_dashboard
        if new_line is not None:
            self.new_line = new_line
        if override_timezone_key is not None:
            self.override_timezone_key = override_timezone_key
        if period_length_filter is not None:
            self.period_length_filter = period_length_filter
        if quote is not None:
            self.quote = quote
        if report_customized_id is not None:
            self.report_customized_id = report_customized_id
        if report_description is not None:
            self.report_description = report_description
        if report_id is not None:
            self.report_id = report_id
        if report_invocation_type is not None:
            self.report_invocation_type = report_invocation_type
        if report_name is not None:
            self.report_name = report_name
        if sent_by_filter is not None:
            self.sent_by_filter = sent_by_filter
        if sent_by_ids is not None:
            self.sent_by_ids = sent_by_ids
        if separator is not None:
            self.separator = separator
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if sort_field is not None:
            self.sort_field = sort_field
        if start_position is not None:
            self.start_position = start_position
        if verification_status_filter is not None:
            self.verification_status_filter = verification_status_filter

    @property
    def authentication_success_filter(self):
        """Gets the authentication_success_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The authentication_success_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_success_filter

    @authentication_success_filter.setter
    def authentication_success_filter(self, authentication_success_filter):
        """Sets the authentication_success_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param authentication_success_filter: The authentication_success_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._authentication_success_filter = authentication_success_filter

    @property
    def custom_field_filter(self):
        """Gets the custom_field_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The custom_field_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_field_filter

    @custom_field_filter.setter
    def custom_field_filter(self, custom_field_filter):
        """Sets the custom_field_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param custom_field_filter: The custom_field_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._custom_field_filter = custom_field_filter

    @property
    def date_range_custom_from_date(self):
        """Gets the date_range_custom_from_date of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The date_range_custom_from_date of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_range_custom_from_date

    @date_range_custom_from_date.setter
    def date_range_custom_from_date(self, date_range_custom_from_date):
        """Sets the date_range_custom_from_date of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param date_range_custom_from_date: The date_range_custom_from_date of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._date_range_custom_from_date = date_range_custom_from_date

    @property
    def date_range_custom_to_date(self):
        """Gets the date_range_custom_to_date of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The date_range_custom_to_date of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_range_custom_to_date

    @date_range_custom_to_date.setter
    def date_range_custom_to_date(self, date_range_custom_to_date):
        """Sets the date_range_custom_to_date of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param date_range_custom_to_date: The date_range_custom_to_date of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._date_range_custom_to_date = date_range_custom_to_date

    @property
    def date_range_filter(self):
        """Gets the date_range_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The date_range_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_range_filter

    @date_range_filter.setter
    def date_range_filter(self, date_range_filter):
        """Sets the date_range_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param date_range_filter: The date_range_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._date_range_filter = date_range_filter

    @property
    def envelope_date_type_filter(self):
        """Gets the envelope_date_type_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The envelope_date_type_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_date_type_filter

    @envelope_date_type_filter.setter
    def envelope_date_type_filter(self, envelope_date_type_filter):
        """Sets the envelope_date_type_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param envelope_date_type_filter: The envelope_date_type_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._envelope_date_type_filter = envelope_date_type_filter

    @property
    def envelope_recipient_name_contains_filter(self):
        """Gets the envelope_recipient_name_contains_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The envelope_recipient_name_contains_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_recipient_name_contains_filter

    @envelope_recipient_name_contains_filter.setter
    def envelope_recipient_name_contains_filter(self, envelope_recipient_name_contains_filter):
        """Sets the envelope_recipient_name_contains_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param envelope_recipient_name_contains_filter: The envelope_recipient_name_contains_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._envelope_recipient_name_contains_filter = envelope_recipient_name_contains_filter

    @property
    def envelope_status_filter(self):
        """Gets the envelope_status_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The envelope_status_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_status_filter

    @envelope_status_filter.setter
    def envelope_status_filter(self, envelope_status_filter):
        """Sets the envelope_status_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param envelope_status_filter: The envelope_status_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._envelope_status_filter = envelope_status_filter

    @property
    def envelope_subject_contains_filter(self):
        """Gets the envelope_subject_contains_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The envelope_subject_contains_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_subject_contains_filter

    @envelope_subject_contains_filter.setter
    def envelope_subject_contains_filter(self, envelope_subject_contains_filter):
        """Sets the envelope_subject_contains_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param envelope_subject_contains_filter: The envelope_subject_contains_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._envelope_subject_contains_filter = envelope_subject_contains_filter

    @property
    def fields(self):
        """Gets the fields of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The fields of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: list[ReportInProductField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param fields: The fields of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: list[ReportInProductField]
        """

        self._fields = fields

    @property
    def for_download(self):
        """Gets the for_download of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The for_download of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._for_download

    @for_download.setter
    def for_download(self, for_download):
        """Sets the for_download of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param for_download: The for_download of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._for_download = for_download

    @property
    def is_dashboard(self):
        """Gets the is_dashboard of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The is_dashboard of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._is_dashboard

    @is_dashboard.setter
    def is_dashboard(self, is_dashboard):
        """Sets the is_dashboard of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param is_dashboard: The is_dashboard of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._is_dashboard = is_dashboard

    @property
    def new_line(self):
        """Gets the new_line of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The new_line of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_line

    @new_line.setter
    def new_line(self, new_line):
        """Sets the new_line of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param new_line: The new_line of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._new_line = new_line

    @property
    def override_timezone_key(self):
        """Gets the override_timezone_key of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The override_timezone_key of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._override_timezone_key

    @override_timezone_key.setter
    def override_timezone_key(self, override_timezone_key):
        """Sets the override_timezone_key of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param override_timezone_key: The override_timezone_key of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._override_timezone_key = override_timezone_key

    @property
    def period_length_filter(self):
        """Gets the period_length_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The period_length_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_length_filter

    @period_length_filter.setter
    def period_length_filter(self, period_length_filter):
        """Sets the period_length_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param period_length_filter: The period_length_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._period_length_filter = period_length_filter

    @property
    def quote(self):
        """Gets the quote of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The quote of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param quote: The quote of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._quote = quote

    @property
    def report_customized_id(self):
        """Gets the report_customized_id of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The report_customized_id of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_customized_id

    @report_customized_id.setter
    def report_customized_id(self, report_customized_id):
        """Sets the report_customized_id of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param report_customized_id: The report_customized_id of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._report_customized_id = report_customized_id

    @property
    def report_description(self):
        """Gets the report_description of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The report_description of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_description

    @report_description.setter
    def report_description(self, report_description):
        """Sets the report_description of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param report_description: The report_description of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._report_description = report_description

    @property
    def report_id(self):
        """Gets the report_id of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The report_id of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param report_id: The report_id of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def report_invocation_type(self):
        """Gets the report_invocation_type of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The report_invocation_type of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_invocation_type

    @report_invocation_type.setter
    def report_invocation_type(self, report_invocation_type):
        """Sets the report_invocation_type of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param report_invocation_type: The report_invocation_type of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._report_invocation_type = report_invocation_type

    @property
    def report_name(self):
        """Gets the report_name of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The report_name of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param report_name: The report_name of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def sent_by_filter(self):
        """Gets the sent_by_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The sent_by_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._sent_by_filter

    @sent_by_filter.setter
    def sent_by_filter(self, sent_by_filter):
        """Sets the sent_by_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param sent_by_filter: The sent_by_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._sent_by_filter = sent_by_filter

    @property
    def sent_by_ids(self):
        """Gets the sent_by_ids of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The sent_by_ids of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._sent_by_ids

    @sent_by_ids.setter
    def sent_by_ids(self, sent_by_ids):
        """Sets the sent_by_ids of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param sent_by_ids: The sent_by_ids of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._sent_by_ids = sent_by_ids

    @property
    def separator(self):
        """Gets the separator of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The separator of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param separator: The separator of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._separator = separator

    @property
    def sort_direction(self):
        """Gets the sort_direction of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The sort_direction of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param sort_direction: The sort_direction of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._sort_direction = sort_direction

    @property
    def sort_field(self):
        """Gets the sort_field of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The sort_field of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param sort_field: The sort_field of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._sort_field = sort_field

    @property
    def start_position(self):
        """Gets the start_position of this ReportInProductCsvRunRequest.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this ReportInProductCsvRunRequest.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def verification_status_filter(self):
        """Gets the verification_status_filter of this ReportInProductCsvRunRequest.  # noqa: E501

          # noqa: E501

        :return: The verification_status_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._verification_status_filter

    @verification_status_filter.setter
    def verification_status_filter(self, verification_status_filter):
        """Sets the verification_status_filter of this ReportInProductCsvRunRequest.

          # noqa: E501

        :param verification_status_filter: The verification_status_filter of this ReportInProductCsvRunRequest.  # noqa: E501
        :type: str
        """

        self._verification_status_filter = verification_status_filter

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
        if issubclass(ReportInProductCsvRunRequest, dict):
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
        if not isinstance(other, ReportInProductCsvRunRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
