# coding: utf-8

"""
    Docusign eSignature REST API

    The Docusign eSignature REST API provides you with a powerful, convenient, and simple Web services API for interacting with Docusign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..client.configuration import Configuration
from ..client.api_client import ApiClient


class OrganizationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_report_v2(self, organization_id, report_correlation_id, **kwargs):
        """
        Retrieves org level report by correlation id and site.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_report_v2(organization_id, report_correlation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: (required)
        :param str report_correlation_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_report_v2_with_http_info(organization_id, report_correlation_id, **kwargs)
        else:
            (data) = self.get_report_v2_with_http_info(organization_id, report_correlation_id, **kwargs)
            return data

    def get_report_v2_with_http_info(self, organization_id, report_correlation_id, **kwargs):
        """
        Retrieves org level report by correlation id and site.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_report_v2_with_http_info(organization_id, report_correlation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: (required)
        :param str report_correlation_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'report_correlation_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in params) or (params['organization_id'] is None):
            raise ValueError("Missing the required parameter `organization_id` when calling `get_report_v2`")
        # verify the required parameter 'report_correlation_id' is set
        if ('report_correlation_id' not in params) or (params['report_correlation_id'] is None):
            raise ValueError("Missing the required parameter `report_correlation_id` when calling `get_report_v2`")


        collection_formats = {}

        resource_path = '/v2.1/organization_reporting/{organizationId}/reportsv2/{reportCorrelationId}'.replace('{format}', 'json')
        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']
        if 'report_correlation_id' in params:
            path_params['reportCorrelationId'] = params['report_correlation_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
