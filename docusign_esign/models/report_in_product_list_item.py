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


class ReportInProductListItem(object):
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
        'get_uri': 'str',
        'last_scheduled_execution_date': 'str',
        'last_scheduled_execution_success_date': 'str',
        'report_customized_id': 'str',
        'report_description': 'str',
        'report_id': 'str',
        'report_name': 'str',
        'report_type': 'str',
        'run_uri': 'str',
        'save_uri': 'str',
        'schedule_create_date': 'str',
        'schedule_end_date': 'str',
        'schedule_id': 'str',
        'schedule_renew_duration_days': 'str'
    }

    attribute_map = {
        'get_uri': 'getUri',
        'last_scheduled_execution_date': 'lastScheduledExecutionDate',
        'last_scheduled_execution_success_date': 'lastScheduledExecutionSuccessDate',
        'report_customized_id': 'reportCustomizedId',
        'report_description': 'reportDescription',
        'report_id': 'reportId',
        'report_name': 'reportName',
        'report_type': 'reportType',
        'run_uri': 'runUri',
        'save_uri': 'saveUri',
        'schedule_create_date': 'scheduleCreateDate',
        'schedule_end_date': 'scheduleEndDate',
        'schedule_id': 'scheduleId',
        'schedule_renew_duration_days': 'scheduleRenewDurationDays'
    }

    def __init__(self, get_uri=None, last_scheduled_execution_date=None, last_scheduled_execution_success_date=None, report_customized_id=None, report_description=None, report_id=None, report_name=None, report_type=None, run_uri=None, save_uri=None, schedule_create_date=None, schedule_end_date=None, schedule_id=None, schedule_renew_duration_days=None):  # noqa: E501
        """ReportInProductListItem - a model defined in Swagger"""  # noqa: E501

        self._get_uri = None
        self._last_scheduled_execution_date = None
        self._last_scheduled_execution_success_date = None
        self._report_customized_id = None
        self._report_description = None
        self._report_id = None
        self._report_name = None
        self._report_type = None
        self._run_uri = None
        self._save_uri = None
        self._schedule_create_date = None
        self._schedule_end_date = None
        self._schedule_id = None
        self._schedule_renew_duration_days = None
        self.discriminator = None

        if get_uri is not None:
            self.get_uri = get_uri
        if last_scheduled_execution_date is not None:
            self.last_scheduled_execution_date = last_scheduled_execution_date
        if last_scheduled_execution_success_date is not None:
            self.last_scheduled_execution_success_date = last_scheduled_execution_success_date
        if report_customized_id is not None:
            self.report_customized_id = report_customized_id
        if report_description is not None:
            self.report_description = report_description
        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if report_type is not None:
            self.report_type = report_type
        if run_uri is not None:
            self.run_uri = run_uri
        if save_uri is not None:
            self.save_uri = save_uri
        if schedule_create_date is not None:
            self.schedule_create_date = schedule_create_date
        if schedule_end_date is not None:
            self.schedule_end_date = schedule_end_date
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if schedule_renew_duration_days is not None:
            self.schedule_renew_duration_days = schedule_renew_duration_days

    @property
    def get_uri(self):
        """Gets the get_uri of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The get_uri of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._get_uri

    @get_uri.setter
    def get_uri(self, get_uri):
        """Sets the get_uri of this ReportInProductListItem.

          # noqa: E501

        :param get_uri: The get_uri of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._get_uri = get_uri

    @property
    def last_scheduled_execution_date(self):
        """Gets the last_scheduled_execution_date of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The last_scheduled_execution_date of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._last_scheduled_execution_date

    @last_scheduled_execution_date.setter
    def last_scheduled_execution_date(self, last_scheduled_execution_date):
        """Sets the last_scheduled_execution_date of this ReportInProductListItem.

          # noqa: E501

        :param last_scheduled_execution_date: The last_scheduled_execution_date of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._last_scheduled_execution_date = last_scheduled_execution_date

    @property
    def last_scheduled_execution_success_date(self):
        """Gets the last_scheduled_execution_success_date of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The last_scheduled_execution_success_date of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._last_scheduled_execution_success_date

    @last_scheduled_execution_success_date.setter
    def last_scheduled_execution_success_date(self, last_scheduled_execution_success_date):
        """Sets the last_scheduled_execution_success_date of this ReportInProductListItem.

          # noqa: E501

        :param last_scheduled_execution_success_date: The last_scheduled_execution_success_date of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._last_scheduled_execution_success_date = last_scheduled_execution_success_date

    @property
    def report_customized_id(self):
        """Gets the report_customized_id of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The report_customized_id of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._report_customized_id

    @report_customized_id.setter
    def report_customized_id(self, report_customized_id):
        """Sets the report_customized_id of this ReportInProductListItem.

          # noqa: E501

        :param report_customized_id: The report_customized_id of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._report_customized_id = report_customized_id

    @property
    def report_description(self):
        """Gets the report_description of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The report_description of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._report_description

    @report_description.setter
    def report_description(self, report_description):
        """Sets the report_description of this ReportInProductListItem.

          # noqa: E501

        :param report_description: The report_description of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._report_description = report_description

    @property
    def report_id(self):
        """Gets the report_id of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The report_id of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportInProductListItem.

          # noqa: E501

        :param report_id: The report_id of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def report_name(self):
        """Gets the report_name of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The report_name of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ReportInProductListItem.

          # noqa: E501

        :param report_name: The report_name of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_type(self):
        """Gets the report_type of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The report_type of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportInProductListItem.

          # noqa: E501

        :param report_type: The report_type of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def run_uri(self):
        """Gets the run_uri of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The run_uri of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._run_uri

    @run_uri.setter
    def run_uri(self, run_uri):
        """Sets the run_uri of this ReportInProductListItem.

          # noqa: E501

        :param run_uri: The run_uri of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._run_uri = run_uri

    @property
    def save_uri(self):
        """Gets the save_uri of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The save_uri of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._save_uri

    @save_uri.setter
    def save_uri(self, save_uri):
        """Sets the save_uri of this ReportInProductListItem.

          # noqa: E501

        :param save_uri: The save_uri of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._save_uri = save_uri

    @property
    def schedule_create_date(self):
        """Gets the schedule_create_date of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The schedule_create_date of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_create_date

    @schedule_create_date.setter
    def schedule_create_date(self, schedule_create_date):
        """Sets the schedule_create_date of this ReportInProductListItem.

          # noqa: E501

        :param schedule_create_date: The schedule_create_date of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._schedule_create_date = schedule_create_date

    @property
    def schedule_end_date(self):
        """Gets the schedule_end_date of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The schedule_end_date of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_end_date

    @schedule_end_date.setter
    def schedule_end_date(self, schedule_end_date):
        """Sets the schedule_end_date of this ReportInProductListItem.

          # noqa: E501

        :param schedule_end_date: The schedule_end_date of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._schedule_end_date = schedule_end_date

    @property
    def schedule_id(self):
        """Gets the schedule_id of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The schedule_id of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this ReportInProductListItem.

          # noqa: E501

        :param schedule_id: The schedule_id of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def schedule_renew_duration_days(self):
        """Gets the schedule_renew_duration_days of this ReportInProductListItem.  # noqa: E501

          # noqa: E501

        :return: The schedule_renew_duration_days of this ReportInProductListItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_renew_duration_days

    @schedule_renew_duration_days.setter
    def schedule_renew_duration_days(self, schedule_renew_duration_days):
        """Sets the schedule_renew_duration_days of this ReportInProductListItem.

          # noqa: E501

        :param schedule_renew_duration_days: The schedule_renew_duration_days of this ReportInProductListItem.  # noqa: E501
        :type: str
        """

        self._schedule_renew_duration_days = schedule_renew_duration_days

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
        if issubclass(ReportInProductListItem, dict):
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
        if not isinstance(other, ReportInProductListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
