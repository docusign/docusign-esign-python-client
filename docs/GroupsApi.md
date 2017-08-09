# docusign.GroupsApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_groups**](GroupsApi.md#create_groups) | **POST** /v2/accounts/{accountId}/groups | Creates one or more groups for the account.
[**delete_brands**](GroupsApi.md#delete_brands) | **DELETE** /v2/accounts/{accountId}/groups/{groupId}/brands | Deletes brand information from the requested group.
[**delete_group_users**](GroupsApi.md#delete_group_users) | **DELETE** /v2/accounts/{accountId}/groups/{groupId}/users | Deletes one or more users from a gro
[**delete_groups**](GroupsApi.md#delete_groups) | **DELETE** /v2/accounts/{accountId}/groups | Deletes an existing user group.
[**get_brands**](GroupsApi.md#get_brands) | **GET** /v2/accounts/{accountId}/groups/{groupId}/brands | Gets group brand ID Information. 
[**list_group_users**](GroupsApi.md#list_group_users) | **GET** /v2/accounts/{accountId}/groups/{groupId}/users | Gets a list of users in a group.
[**list_groups**](GroupsApi.md#list_groups) | **GET** /v2/accounts/{accountId}/groups | Gets information about groups associated with the account.
[**update_brands**](GroupsApi.md#update_brands) | **PUT** /v2/accounts/{accountId}/groups/{groupId}/brands | Adds group brand ID information to a group.
[**update_group_users**](GroupsApi.md#update_group_users) | **PUT** /v2/accounts/{accountId}/groups/{groupId}/users | Adds one or more users to an existing group.
[**update_groups**](GroupsApi.md#update_groups) | **PUT** /v2/accounts/{accountId}/groups | Updates the group information for a group.


# **create_groups**
> GroupInformation create_groups(account_id, group_information=group_information)

Creates one or more groups for the account.

Creates one or more groups for the account.  Groups can be used to help manage users by associating users with a group. You can associate a group with a Permission Profile, which sets the user permissions for users in that group without having to set the `userSettings` property for each user. You are not required to set Permission Profiles for a group, but it makes it easier to manage user permissions for a large number of users. You can also use groups with template sharing to limit user access to templates.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_information = docusign.GroupInformation() # GroupInformation |  (optional)

try: 
    # Creates one or more groups for the account.
    api_response = api_instance.create_groups(account_id, group_information=group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_information** | [**GroupInformation**](GroupInformation.md)|  | [optional] 

### Return type

[**GroupInformation**](GroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brands**
> BrandsResponse delete_brands(account_id, group_id, brands_request=brands_request)

Deletes brand information from the requested group.

Deletes brand information from the requested group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_id = 'group_id_example' # str | The ID of the group being accessed.
brands_request = docusign.BrandsRequest() # BrandsRequest |  (optional)

try: 
    # Deletes brand information from the requested group.
    api_response = api_instance.delete_brands(account_id, group_id, brands_request=brands_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_brands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_id** | **str**| The ID of the group being accessed. | 
 **brands_request** | [**BrandsRequest**](BrandsRequest.md)|  | [optional] 

### Return type

[**BrandsResponse**](BrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_users**
> UsersResponse delete_group_users(account_id, group_id, user_info_list=user_info_list)

Deletes one or more users from a gro

Deletes one or more users from a group. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_id = 'group_id_example' # str | The ID of the group being accessed.
user_info_list = docusign.UserInfoList() # UserInfoList |  (optional)

try: 
    # Deletes one or more users from a gro
    api_response = api_instance.delete_group_users(account_id, group_id, user_info_list=user_info_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_id** | **str**| The ID of the group being accessed. | 
 **user_info_list** | [**UserInfoList**](UserInfoList.md)|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groups**
> GroupInformation delete_groups(account_id, group_information=group_information)

Deletes an existing user group.

Deletes an existing user group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_information = docusign.GroupInformation() # GroupInformation |  (optional)

try: 
    # Deletes an existing user group.
    api_response = api_instance.delete_groups(account_id, group_information=group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_information** | [**GroupInformation**](GroupInformation.md)|  | [optional] 

### Return type

[**GroupInformation**](GroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brands**
> BrandsResponse get_brands(account_id, group_id)

Gets group brand ID Information. 

Retrieves information about the brands associated with the requested group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_id = 'group_id_example' # str | The ID of the group being accessed.

try: 
    # Gets group brand ID Information. 
    api_response = api_instance.get_brands(account_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_brands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_id** | **str**| The ID of the group being accessed. | 

### Return type

[**BrandsResponse**](BrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_users**
> UsersResponse list_group_users(account_id, group_id, count=count, start_position=start_position)

Gets a list of users in a group.

Retrieves a list of users in a group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_id = 'group_id_example' # str | The ID of the group being accessed.
count = 'count_example' # str | Number of records to return. The number must be greater than 1 and less than or equal to 100.  (optional)
start_position = 'start_position_example' # str | Starting value for the list. (optional)

try: 
    # Gets a list of users in a group.
    api_response = api_instance.list_group_users(account_id, group_id, count=count, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_id** | **str**| The ID of the group being accessed. | 
 **count** | **str**| Number of records to return. The number must be greater than 1 and less than or equal to 100.  | [optional] 
 **start_position** | **str**| Starting value for the list. | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> GroupInformation list_groups(account_id, count=count, group_name=group_name, group_type=group_type, search_text=search_text, start_position=start_position)

Gets information about groups associated with the account.

Retrieves information about groups associated with the account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
count = 'count_example' # str | Number of records to return. The number must be greater than 1 and less than or equal to 100. (optional)
group_name = 'group_name_example' # str | Filters the groups returned by the group name or a sub-string of group name. (optional)
group_type = 'group_type_example' # str |  (optional)
search_text = 'search_text_example' # str |  (optional)
start_position = 'start_position_example' # str | Starting value for the list. (optional)

try: 
    # Gets information about groups associated with the account.
    api_response = api_instance.list_groups(account_id, count=count, group_name=group_name, group_type=group_type, search_text=search_text, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **count** | **str**| Number of records to return. The number must be greater than 1 and less than or equal to 100. | [optional] 
 **group_name** | **str**| Filters the groups returned by the group name or a sub-string of group name. | [optional] 
 **group_type** | **str**|  | [optional] 
 **search_text** | **str**|  | [optional] 
 **start_position** | **str**| Starting value for the list. | [optional] 

### Return type

[**GroupInformation**](GroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brands**
> BrandsResponse update_brands(account_id, group_id, brands_request=brands_request)

Adds group brand ID information to a group.

Adds group brand ID information to a group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_id = 'group_id_example' # str | The ID of the group being accessed.
brands_request = docusign.BrandsRequest() # BrandsRequest |  (optional)

try: 
    # Adds group brand ID information to a group.
    api_response = api_instance.update_brands(account_id, group_id, brands_request=brands_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_brands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_id** | **str**| The ID of the group being accessed. | 
 **brands_request** | [**BrandsRequest**](BrandsRequest.md)|  | [optional] 

### Return type

[**BrandsResponse**](BrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_users**
> UsersResponse update_group_users(account_id, group_id, user_info_list=user_info_list)

Adds one or more users to an existing group.

Adds one or more users to an existing group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_id = 'group_id_example' # str | The ID of the group being accessed.
user_info_list = docusign.UserInfoList() # UserInfoList |  (optional)

try: 
    # Adds one or more users to an existing group.
    api_response = api_instance.update_group_users(account_id, group_id, user_info_list=user_info_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_id** | **str**| The ID of the group being accessed. | 
 **user_info_list** | [**UserInfoList**](UserInfoList.md)|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_groups**
> GroupInformation update_groups(account_id, group_information=group_information)

Updates the group information for a group.

Updates the group name and modifies, or sets, the permission profile for the group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.GroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_information = docusign.GroupInformation() # GroupInformation |  (optional)

try: 
    # Updates the group information for a group.
    api_response = api_instance.update_groups(account_id, group_information=group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_information** | [**GroupInformation**](GroupInformation.md)|  | [optional] 

### Return type

[**GroupInformation**](GroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

