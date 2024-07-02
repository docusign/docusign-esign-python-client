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


class AuthenticationApi(object):
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

    def delete_social_login(self, account_id, user_id, **kwargs):
        """
        Deletes user's social account.
        Deletes a social account from a use's account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_social_login(account_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str user_id: The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. (required)
        :param SocialAccountInformation social_account_information:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_social_login_with_http_info(account_id, user_id, **kwargs)
        else:
            (data) = self.delete_social_login_with_http_info(account_id, user_id, **kwargs)
            return data

    def delete_social_login_with_http_info(self, account_id, user_id, **kwargs):
        """
        Deletes user's social account.
        Deletes a social account from a use's account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_social_login_with_http_info(account_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str user_id: The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. (required)
        :param SocialAccountInformation social_account_information:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'user_id', 'social_account_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_social_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_social_login`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_social_login`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/users/{userId}/social'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'social_account_information' in params:
            body_params = params['social_account_information']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
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

    def get_o_auth_token(self, **kwargs):
        """
        Creates an authorization token.
        Creates an OAuth2 authorization server token endpoint.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_o_auth_token(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: OauthAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_o_auth_token_with_http_info(**kwargs)
        else:
            (data) = self.get_o_auth_token_with_http_info(**kwargs)
            return data

    def get_o_auth_token_with_http_info(self, **kwargs):
        """
        Creates an authorization token.
        Creates an OAuth2 authorization server token endpoint.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_o_auth_token_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: OauthAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_o_auth_token" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/v2.1/oauth2/token'.replace('{format}', 'json')
        path_params = {}

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

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OauthAccess',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_social_logins(self, account_id, user_id, **kwargs):
        """
        Gets a list of a user's social accounts.
        Retrieves a list of social accounts linked to a user's account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_social_logins(account_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str user_id: The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. (required)
        :return: UserSocialIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_social_logins_with_http_info(account_id, user_id, **kwargs)
        else:
            (data) = self.list_social_logins_with_http_info(account_id, user_id, **kwargs)
            return data

    def list_social_logins_with_http_info(self, account_id, user_id, **kwargs):
        """
        Gets a list of a user's social accounts.
        Retrieves a list of social accounts linked to a user's account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_social_logins_with_http_info(account_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str user_id: The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. (required)
        :return: UserSocialIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_social_logins" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_social_logins`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `list_social_logins`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/users/{userId}/social'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                        response_type='UserSocialIdResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def login(self, **kwargs):
        """
        Gets login information for a specified user.
        Retrieves login information for a specified user. Each account that is associated with the login credentials is listed. You can use the returned information to determine whether a user is authenticated and select an account to use in future operations.    The `baseUrl` property, returned in the response, is used in all future API calls as the base of the request URL. The `baseUrl` property contains the DocuSign server, the API version, and the `accountId` property that is used for the login. This request uses your DocuSign credentials to retrieve the account information.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.login(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_password: When set to **true**, shows the account API password in the response.
        :param str embed_account_id_guid:
        :param str include_account_id_guid: When set to **true**, shows the account ID GUID in the response.
        :param str login_settings: Determines whether login settings are returned in the response.  Valid Values:  * all -  All the login settings are returned.  * none - no login settings are returned.
        :return: LoginInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.login_with_http_info(**kwargs)
        else:
            (data) = self.login_with_http_info(**kwargs)
            return data

    def login_with_http_info(self, **kwargs):
        """
        Gets login information for a specified user.
        Retrieves login information for a specified user. Each account that is associated with the login credentials is listed. You can use the returned information to determine whether a user is authenticated and select an account to use in future operations.    The `baseUrl` property, returned in the response, is used in all future API calls as the base of the request URL. The `baseUrl` property contains the DocuSign server, the API version, and the `accountId` property that is used for the login. This request uses your DocuSign credentials to retrieve the account information.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.login_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_password: When set to **true**, shows the account API password in the response.
        :param str embed_account_id_guid:
        :param str include_account_id_guid: When set to **true**, shows the account ID GUID in the response.
        :param str login_settings: Determines whether login settings are returned in the response.  Valid Values:  * all -  All the login settings are returned.  * none - no login settings are returned.
        :return: LoginInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_password', 'embed_account_id_guid', 'include_account_id_guid', 'login_settings']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v2.1/login_information'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'api_password' in params:
            query_params['api_password'] = params['api_password']
        if 'embed_account_id_guid' in params:
            query_params['embed_account_id_guid'] = params['embed_account_id_guid']
        if 'include_account_id_guid' in params:
            query_params['include_account_id_guid'] = params['include_account_id_guid']
        if 'login_settings' in params:
            query_params['login_settings'] = params['login_settings']

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
                                        response_type='LoginInformation',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def revoke_o_auth_token(self, **kwargs):
        """
        Revokes an authorization token.
        Revokes an OAuth2 authorization server token. After the revocation is complete, a caller must re-authenticate to restore access.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.revoke_o_auth_token(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.revoke_o_auth_token_with_http_info(**kwargs)
        else:
            (data) = self.revoke_o_auth_token_with_http_info(**kwargs)
            return data

    def revoke_o_auth_token_with_http_info(self, **kwargs):
        """
        Revokes an authorization token.
        Revokes an OAuth2 authorization server token. After the revocation is complete, a caller must re-authenticate to restore access.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.revoke_o_auth_token_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_o_auth_token" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/v2.1/oauth2/revoke'.replace('{format}', 'json')
        path_params = {}

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

        return self.api_client.call_api(resource_path, 'POST',
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

    def update_password(self, login_part, **kwargs):
        """
        Updates the password for a specified user.
        Updates the password for a specified user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_password(login_part, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str login_part: Currently, only the value **password** is supported. (required)
        :param UserPasswordInformation user_password_information:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_password_with_http_info(login_part, **kwargs)
        else:
            (data) = self.update_password_with_http_info(login_part, **kwargs)
            return data

    def update_password_with_http_info(self, login_part, **kwargs):
        """
        Updates the password for a specified user.
        Updates the password for a specified user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_password_with_http_info(login_part, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str login_part: Currently, only the value **password** is supported. (required)
        :param UserPasswordInformation user_password_information:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login_part', 'user_password_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'login_part' is set
        if ('login_part' not in params) or (params['login_part'] is None):
            raise ValueError("Missing the required parameter `login_part` when calling `update_password`")


        collection_formats = {}

        resource_path = '/v2.1/login_information/{loginPart}'.replace('{format}', 'json')
        path_params = {}
        if 'login_part' in params:
            path_params['loginPart'] = params['login_part']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_password_information' in params:
            body_params = params['user_password_information']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
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

    def update_social_login(self, account_id, user_id, **kwargs):
        """
        Adds social account for a user.
        Adds a new social account to a user's account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_social_login(account_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str user_id: The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. (required)
        :param SocialAccountInformation social_account_information:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_social_login_with_http_info(account_id, user_id, **kwargs)
        else:
            (data) = self.update_social_login_with_http_info(account_id, user_id, **kwargs)
            return data

    def update_social_login_with_http_info(self, account_id, user_id, **kwargs):
        """
        Adds social account for a user.
        Adds a new social account to a user's account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_social_login_with_http_info(account_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str user_id: The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. (required)
        :param SocialAccountInformation social_account_information:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'user_id', 'social_account_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_social_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_social_login`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_social_login`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/users/{userId}/social'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'social_account_information' in params:
            body_params = params['social_account_information']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
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
