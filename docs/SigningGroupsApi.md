# docusign.SigningGroupsApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_list**](SigningGroupsApi.md#create_list) | **POST** /v2/accounts/{accountId}/signing_groups | Creates a signing group. 
[**delete_list**](SigningGroupsApi.md#delete_list) | **DELETE** /v2/accounts/{accountId}/signing_groups | Deletes one or more signing groups.
[**delete_users**](SigningGroupsApi.md#delete_users) | **DELETE** /v2/accounts/{accountId}/signing_groups/{signingGroupId}/users | Deletes  one or more members from a signing group.
[**get**](SigningGroupsApi.md#get) | **GET** /v2/accounts/{accountId}/signing_groups/{signingGroupId} | Gets information about a signing group. 
[**list**](SigningGroupsApi.md#list) | **GET** /v2/accounts/{accountId}/signing_groups | Gets a list of the Signing Groups in an account.
[**list_users**](SigningGroupsApi.md#list_users) | **GET** /v2/accounts/{accountId}/signing_groups/{signingGroupId}/users | Gets a list of members in a Signing Group.
[**update**](SigningGroupsApi.md#update) | **PUT** /v2/accounts/{accountId}/signing_groups/{signingGroupId} | Updates a signing group. 
[**update_list**](SigningGroupsApi.md#update_list) | **PUT** /v2/accounts/{accountId}/signing_groups | Updates signing group names.
[**update_users**](SigningGroupsApi.md#update_users) | **PUT** /v2/accounts/{accountId}/signing_groups/{signingGroupId}/users | Adds members to a signing group. 


# **create_list**
> SigningGroupInformation create_list(account_id, signing_group_information=signing_group_information)

Creates a signing group. 

Creates one or more signing groups.   Multiple signing groups can be created in one call. Only users with account administrator privileges can create signing groups.   An account can have a maximum of 50 signing groups. Each signing group can have a maximum of 50 group members.   Signing groups can be used by any account user.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_information = docusign.SigningGroupInformation() # SigningGroupInformation |  (optional)

try: 
    # Creates a signing group. 
    api_response = api_instance.create_list(account_id, signing_group_information=signing_group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->create_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_information** | [**SigningGroupInformation**](SigningGroupInformation.md)|  | [optional] 

### Return type

[**SigningGroupInformation**](SigningGroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> SigningGroupInformation delete_list(account_id, signing_group_information=signing_group_information)

Deletes one or more signing groups.

Deletes one or more signing groups in the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_information = docusign.SigningGroupInformation() # SigningGroupInformation |  (optional)

try: 
    # Deletes one or more signing groups.
    api_response = api_instance.delete_list(account_id, signing_group_information=signing_group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->delete_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_information** | [**SigningGroupInformation**](SigningGroupInformation.md)|  | [optional] 

### Return type

[**SigningGroupInformation**](SigningGroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users**
> SigningGroupUsers delete_users(account_id, signing_group_id, signing_group_users=signing_group_users)

Deletes  one or more members from a signing group.

Deletes  one or more members from the specified signing group. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_id = 'signing_group_id_example' # str | 
signing_group_users = docusign.SigningGroupUsers() # SigningGroupUsers |  (optional)

try: 
    # Deletes  one or more members from a signing group.
    api_response = api_instance.delete_users(account_id, signing_group_id, signing_group_users=signing_group_users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->delete_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_id** | **str**|  | 
 **signing_group_users** | [**SigningGroupUsers**](SigningGroupUsers.md)|  | [optional] 

### Return type

[**SigningGroupUsers**](SigningGroupUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> SigningGroup get(account_id, signing_group_id)

Gets information about a signing group. 

Retrieves information, including group member information, for the specified signing group. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_id = 'signing_group_id_example' # str | 

try: 
    # Gets information about a signing group. 
    api_response = api_instance.get(account_id, signing_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_id** | **str**|  | 

### Return type

[**SigningGroup**](SigningGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> SigningGroupInformation list(account_id, group_type=group_type, include_users=include_users)

Gets a list of the Signing Groups in an account.

Retrieves a list of all signing groups in the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
group_type = 'group_type_example' # str |  (optional)
include_users = 'include_users_example' # str | When set to **true**, the response includes the signing group members.  (optional)

try: 
    # Gets a list of the Signing Groups in an account.
    api_response = api_instance.list(account_id, group_type=group_type, include_users=include_users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **group_type** | **str**|  | [optional] 
 **include_users** | **str**| When set to **true**, the response includes the signing group members.  | [optional] 

### Return type

[**SigningGroupInformation**](SigningGroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> SigningGroupUsers list_users(account_id, signing_group_id)

Gets a list of members in a Signing Group.

Retrieves the list of members in the specified Signing Group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_id = 'signing_group_id_example' # str | 

try: 
    # Gets a list of members in a Signing Group.
    api_response = api_instance.list_users(account_id, signing_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_id** | **str**|  | 

### Return type

[**SigningGroupUsers**](SigningGroupUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SigningGroup update(account_id, signing_group_id, signing_group=signing_group)

Updates a signing group. 

Updates signing group name and member information. You can also add new members to the signing group. A signing group can have a maximum of 50 members. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_id = 'signing_group_id_example' # str | 
signing_group = docusign.SigningGroup() # SigningGroup |  (optional)

try: 
    # Updates a signing group. 
    api_response = api_instance.update(account_id, signing_group_id, signing_group=signing_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_id** | **str**|  | 
 **signing_group** | [**SigningGroup**](SigningGroup.md)|  | [optional] 

### Return type

[**SigningGroup**](SigningGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> SigningGroupInformation update_list(account_id, signing_group_information=signing_group_information)

Updates signing group names.

Updates the name of one or more existing signing groups. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_information = docusign.SigningGroupInformation() # SigningGroupInformation |  (optional)

try: 
    # Updates signing group names.
    api_response = api_instance.update_list(account_id, signing_group_information=signing_group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_information** | [**SigningGroupInformation**](SigningGroupInformation.md)|  | [optional] 

### Return type

[**SigningGroupInformation**](SigningGroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users**
> SigningGroupUsers update_users(account_id, signing_group_id, signing_group_users=signing_group_users)

Adds members to a signing group. 

Adds one or more new members to a signing group. A signing group can have a maximum of 50 members. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.SigningGroupsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signing_group_id = 'signing_group_id_example' # str | 
signing_group_users = docusign.SigningGroupUsers() # SigningGroupUsers |  (optional)

try: 
    # Adds members to a signing group. 
    api_response = api_instance.update_users(account_id, signing_group_id, signing_group_users=signing_group_users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigningGroupsApi->update_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signing_group_id** | **str**|  | 
 **signing_group_users** | [**SigningGroupUsers**](SigningGroupUsers.md)|  | [optional] 

### Return type

[**SigningGroupUsers**](SigningGroupUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

