# docusign.AuthenticationApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_social_login**](AuthenticationApi.md#delete_social_login) | **DELETE** /v2/accounts/{accountId}/users/{userId}/social | Deletes user&#39;s social account.
[**get_o_auth_token**](AuthenticationApi.md#get_o_auth_token) | **POST** /v2/oauth2/token | Creates an authorization token.
[**list_social_logins**](AuthenticationApi.md#list_social_logins) | **GET** /v2/accounts/{accountId}/users/{userId}/social | Gets a list of a user&#39;s social accounts.
[**login**](AuthenticationApi.md#login) | **GET** /v2/login_information | Gets login information for a specified user.
[**revoke_o_auth_token**](AuthenticationApi.md#revoke_o_auth_token) | **POST** /v2/oauth2/revoke | Revokes an authorization token.
[**update_password**](AuthenticationApi.md#update_password) | **PUT** /v2/login_information/{loginPart} | Updates the password for a specified user.
[**update_social_login**](AuthenticationApi.md#update_social_login) | **PUT** /v2/accounts/{accountId}/users/{userId}/social | Adds social account for a user.


# **delete_social_login**
> delete_social_login(account_id, user_id, social_account_information=social_account_information)

Deletes user's social account.

Deletes a social account from a use's account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
social_account_information = docusign.SocialAccountInformation() # SocialAccountInformation |  (optional)

try: 
    # Deletes user's social account.
    api_instance.delete_social_login(account_id, user_id, social_account_information=social_account_information)
except ApiException as e:
    print("Exception when calling AuthenticationApi->delete_social_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **social_account_information** | [**SocialAccountInformation**](SocialAccountInformation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_token**
> OauthAccess get_o_auth_token()

Creates an authorization token.

Creates an OAuth2 authorization server token endpoint.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()

try: 
    # Creates an authorization token.
    api_response = api_instance.get_o_auth_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_o_auth_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OauthAccess**](OauthAccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_social_logins**
> UserSocialIdResult list_social_logins(account_id, user_id)

Gets a list of a user's social accounts.

Retrieves a list of social accounts linked to a user's account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Gets a list of a user's social accounts.
    api_response = api_instance.list_social_logins(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->list_social_logins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**UserSocialIdResult**](UserSocialIdResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginInformation login(api_password=api_password, embed_account_id_guid=embed_account_id_guid, include_account_id_guid=include_account_id_guid, login_settings=login_settings)

Gets login information for a specified user.

Retrieves login information for a specified user. Each account that is associated with the login credentials is listed. You can use the returned information to determine whether a user is authenticated and select an account to use in future operations.    The `baseUrl` property, returned in the response, is used in all future API calls as the base of the request URL. The `baseUrl` property contains the DocuSign server, the API version, and the `accountId` property that is used for the login. This request uses your DocuSign credentials to retrieve the account information.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()
api_password = 'api_password_example' # str | When set to **true**, shows the account API password in the response. (optional)
embed_account_id_guid = 'embed_account_id_guid_example' # str |  (optional)
include_account_id_guid = 'include_account_id_guid_example' # str | When set to **true**, shows the account ID GUID in the response. (optional)
login_settings = 'login_settings_example' # str | Determines whether login settings are returned in the response.  Valid Values:  * all -  All the login settings are returned.  * none - no login settings are returned. (optional)

try: 
    # Gets login information for a specified user.
    api_response = api_instance.login(api_password=api_password, embed_account_id_guid=embed_account_id_guid, include_account_id_guid=include_account_id_guid, login_settings=login_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_password** | **str**| When set to **true**, shows the account API password in the response. | [optional] 
 **embed_account_id_guid** | **str**|  | [optional] 
 **include_account_id_guid** | **str**| When set to **true**, shows the account ID GUID in the response. | [optional] 
 **login_settings** | **str**| Determines whether login settings are returned in the response.  Valid Values:  * all -  All the login settings are returned.  * none - no login settings are returned. | [optional] 

### Return type

[**LoginInformation**](LoginInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_o_auth_token**
> revoke_o_auth_token()

Revokes an authorization token.

Revokes an OAuth2 authorization server token. After the revocation is complete, a caller must re-authenticate to restore access.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()

try: 
    # Revokes an authorization token.
    api_instance.revoke_o_auth_token()
except ApiException as e:
    print("Exception when calling AuthenticationApi->revoke_o_auth_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(login_part, user_password_information=user_password_information)

Updates the password for a specified user.

Updates the password for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()
login_part = 'login_part_example' # str | Currently, only the value **password** is supported.
user_password_information = docusign.UserPasswordInformation() # UserPasswordInformation |  (optional)

try: 
    # Updates the password for a specified user.
    api_instance.update_password(login_part, user_password_information=user_password_information)
except ApiException as e:
    print("Exception when calling AuthenticationApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_part** | **str**| Currently, only the value **password** is supported. | 
 **user_password_information** | [**UserPasswordInformation**](UserPasswordInformation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_social_login**
> update_social_login(account_id, user_id, social_account_information=social_account_information)

Adds social account for a user.

Adds a new social account to a user's account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AuthenticationApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
social_account_information = docusign.SocialAccountInformation() # SocialAccountInformation |  (optional)

try: 
    # Adds social account for a user.
    api_instance.update_social_login(account_id, user_id, social_account_information=social_account_information)
except ApiException as e:
    print("Exception when calling AuthenticationApi->update_social_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **social_account_information** | [**SocialAccountInformation**](SocialAccountInformation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

