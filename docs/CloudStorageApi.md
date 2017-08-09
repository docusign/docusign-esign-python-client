# docusign.CloudStorageApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider**](CloudStorageApi.md#create_provider) | **POST** /v2/accounts/{accountId}/users/{userId}/cloud_storage | Configures the redirect URL information  for one or more cloud storage providers for the specified user.
[**delete_provider**](CloudStorageApi.md#delete_provider) | **DELETE** /v2/accounts/{accountId}/users/{userId}/cloud_storage/{serviceId} | Deletes the user authentication information for the specified cloud storage provider.
[**delete_providers**](CloudStorageApi.md#delete_providers) | **DELETE** /v2/accounts/{accountId}/users/{userId}/cloud_storage | Deletes the user authentication information for one or more cloud storage providers.
[**get_provider**](CloudStorageApi.md#get_provider) | **GET** /v2/accounts/{accountId}/users/{userId}/cloud_storage/{serviceId} | Gets the specified Cloud Storage Provider configuration for the User.
[**list**](CloudStorageApi.md#list) | **GET** /v2/accounts/{accountId}/users/{userId}/cloud_storage/{serviceId}/folders/{folderId} | Gets a list of all the items from the specified cloud storage provider.
[**list_folders**](CloudStorageApi.md#list_folders) | **GET** /v2/accounts/{accountId}/users/{userId}/cloud_storage/{serviceId}/folders | Retrieves a list of all the items in a specified folder from the specified cloud storage provider.
[**list_providers**](CloudStorageApi.md#list_providers) | **GET** /v2/accounts/{accountId}/users/{userId}/cloud_storage | Get the Cloud Storage Provider configuration for the specified user.


# **create_provider**
> CloudStorageProviders create_provider(account_id, user_id, cloud_storage_providers=cloud_storage_providers)

Configures the redirect URL information  for one or more cloud storage providers for the specified user.

Configures the redirect URL information  for one or more cloud storage providers for the specified user. The redirect URL is added to the authentication URL to complete the return route.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
cloud_storage_providers = docusign.CloudStorageProviders() # CloudStorageProviders |  (optional)

try: 
    # Configures the redirect URL information  for one or more cloud storage providers for the specified user.
    api_response = api_instance.create_provider(account_id, user_id, cloud_storage_providers=cloud_storage_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->create_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **cloud_storage_providers** | [**CloudStorageProviders**](CloudStorageProviders.md)|  | [optional] 

### Return type

[**CloudStorageProviders**](CloudStorageProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider**
> CloudStorageProviders delete_provider(account_id, service_id, user_id)

Deletes the user authentication information for the specified cloud storage provider.

Deletes the user authentication information for the specified cloud storage provider. The next time the user tries to access the cloud storage provider, they must pass normal authentication for this cloud storage provider.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
service_id = 'service_id_example' # str | The ID of the service to access.   Valid values are the service name (\"Box\") or the numerical serviceId (\"4136\").
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Deletes the user authentication information for the specified cloud storage provider.
    api_response = api_instance.delete_provider(account_id, service_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->delete_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **service_id** | **str**| The ID of the service to access.   Valid values are the service name (\&quot;Box\&quot;) or the numerical serviceId (\&quot;4136\&quot;). | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**CloudStorageProviders**](CloudStorageProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers**
> CloudStorageProviders delete_providers(account_id, user_id, cloud_storage_providers=cloud_storage_providers)

Deletes the user authentication information for one or more cloud storage providers.

Deletes the user authentication information for one or more cloud storage providers. The next time the user tries to access the cloud storage provider, they must pass normal authentication.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
cloud_storage_providers = docusign.CloudStorageProviders() # CloudStorageProviders |  (optional)

try: 
    # Deletes the user authentication information for one or more cloud storage providers.
    api_response = api_instance.delete_providers(account_id, user_id, cloud_storage_providers=cloud_storage_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->delete_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **cloud_storage_providers** | [**CloudStorageProviders**](CloudStorageProviders.md)|  | [optional] 

### Return type

[**CloudStorageProviders**](CloudStorageProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> CloudStorageProviders get_provider(account_id, service_id, user_id, redirect_url=redirect_url)

Gets the specified Cloud Storage Provider configuration for the User.

Retrieves the list of cloud storage providers enabled for the account and the configuration information for the user.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
service_id = 'service_id_example' # str | The ID of the service to access.   Valid values are the service name (\"Box\") or the numerical serviceId (\"4136\").
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
redirect_url = 'redirect_url_example' # str |  The URL the user is redirected to after the cloud storage provider authenticates the user. Using this will append the redirectUrl to the authenticationUrl.  The redirectUrl is restricted to URLs in the docusign.com or docusign.net domains.   (optional)

try: 
    # Gets the specified Cloud Storage Provider configuration for the User.
    api_response = api_instance.get_provider(account_id, service_id, user_id, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **service_id** | **str**| The ID of the service to access.   Valid values are the service name (\&quot;Box\&quot;) or the numerical serviceId (\&quot;4136\&quot;). | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **redirect_url** | **str**|  The URL the user is redirected to after the cloud storage provider authenticates the user. Using this will append the redirectUrl to the authenticationUrl.  The redirectUrl is restricted to URLs in the docusign.com or docusign.net domains.   | [optional] 

### Return type

[**CloudStorageProviders**](CloudStorageProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ExternalFolder list(account_id, folder_id, service_id, user_id, cloud_storage_folder_path=cloud_storage_folder_path, count=count, order=order, order_by=order_by, search_text=search_text, start_position=start_position)

Gets a list of all the items from the specified cloud storage provider.

Retrieves a list of all the items in all  the folders associated with the user from the specified cloud storage provider. You can limit the scope of the returned items by providing a comma separated list of folder IDs in the request.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
service_id = 'service_id_example' # str | The ID of the service to access.   Valid values are the service name (\"Box\") or the numerical serviceId (\"4136\").
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
cloud_storage_folder_path = 'cloud_storage_folder_path_example' # str |  (optional)
count = 'count_example' # str | An optional value that sets how many items are included in the response.   The default setting for this is 25.  (optional)
order = 'order_example' # str | An optional value that sets the direction order used to sort the item list.   Valid values are:   * asc = ascending sort order * desc = descending sort order  (optional)
order_by = 'order_by_example' # str | An optional value that sets the file attribute used to sort the item list.   Valid values are:   * modified * name   (optional)
search_text = 'search_text_example' # str |  (optional)
start_position = 'start_position_example' # str | Indicates the starting point of the first item included in the response set. It uses a 0-based index. The default setting for this is 0.   (optional)

try: 
    # Gets a list of all the items from the specified cloud storage provider.
    api_response = api_instance.list(account_id, folder_id, service_id, user_id, cloud_storage_folder_path=cloud_storage_folder_path, count=count, order=order, order_by=order_by, search_text=search_text, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **service_id** | **str**| The ID of the service to access.   Valid values are the service name (\&quot;Box\&quot;) or the numerical serviceId (\&quot;4136\&quot;). | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **cloud_storage_folder_path** | **str**|  | [optional] 
 **count** | **str**| An optional value that sets how many items are included in the response.   The default setting for this is 25.  | [optional] 
 **order** | **str**| An optional value that sets the direction order used to sort the item list.   Valid values are:   * asc &#x3D; ascending sort order * desc &#x3D; descending sort order  | [optional] 
 **order_by** | **str**| An optional value that sets the file attribute used to sort the item list.   Valid values are:   * modified * name   | [optional] 
 **search_text** | **str**|  | [optional] 
 **start_position** | **str**| Indicates the starting point of the first item included in the response set. It uses a 0-based index. The default setting for this is 0.   | [optional] 

### Return type

[**ExternalFolder**](ExternalFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> ExternalFolder list_folders(account_id, service_id, user_id, cloud_storage_folder_path=cloud_storage_folder_path, count=count, order=order, order_by=order_by, search_text=search_text, start_position=start_position)

Retrieves a list of all the items in a specified folder from the specified cloud storage provider.

Retrieves a list of all the items in a specified folder from the specified cloud storage provider. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
service_id = 'service_id_example' # str | The ID of the service to access.   Valid values are the service name (\"Box\") or the numerical serviceId (\"4136\").
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
cloud_storage_folder_path = 'cloud_storage_folder_path_example' # str | A comma separated list of folder IDs included in the request.  (optional)
count = 'count_example' # str | An optional value that sets how many items are included in the response.   The default setting for this is 25.  (optional)
order = 'order_example' # str | An optional value that sets the direction order used to sort the item list.   Valid values are:   * asc = ascending sort order * desc = descending sort order  (optional)
order_by = 'order_by_example' # str | An optional value that sets the file attribute used to sort the item list.   Valid values are:   * modified * name   (optional)
search_text = 'search_text_example' # str |  (optional)
start_position = 'start_position_example' # str | Indicates the starting point of the first item included in the response set. It uses a 0-based index. The default setting for this is 0.   (optional)

try: 
    # Retrieves a list of all the items in a specified folder from the specified cloud storage provider.
    api_response = api_instance.list_folders(account_id, service_id, user_id, cloud_storage_folder_path=cloud_storage_folder_path, count=count, order=order, order_by=order_by, search_text=search_text, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->list_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **service_id** | **str**| The ID of the service to access.   Valid values are the service name (\&quot;Box\&quot;) or the numerical serviceId (\&quot;4136\&quot;). | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **cloud_storage_folder_path** | **str**| A comma separated list of folder IDs included in the request.  | [optional] 
 **count** | **str**| An optional value that sets how many items are included in the response.   The default setting for this is 25.  | [optional] 
 **order** | **str**| An optional value that sets the direction order used to sort the item list.   Valid values are:   * asc &#x3D; ascending sort order * desc &#x3D; descending sort order  | [optional] 
 **order_by** | **str**| An optional value that sets the file attribute used to sort the item list.   Valid values are:   * modified * name   | [optional] 
 **search_text** | **str**|  | [optional] 
 **start_position** | **str**| Indicates the starting point of the first item included in the response set. It uses a 0-based index. The default setting for this is 0.   | [optional] 

### Return type

[**ExternalFolder**](ExternalFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> CloudStorageProviders list_providers(account_id, user_id, redirect_url=redirect_url)

Get the Cloud Storage Provider configuration for the specified user.

Retrieves the list of cloud storage providers enabled for the account and the configuration information for the user.  The {serviceId} parameter can be either the service name or serviceId.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CloudStorageApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
redirect_url = 'redirect_url_example' # str |  The URL the user is redirected to after the cloud storage provider authenticates the user. Using this will append the redirectUrl to the authenticationUrl.  The redirectUrl is restricted to URLs in the docusign.com or docusign.net domains.   (optional)

try: 
    # Get the Cloud Storage Provider configuration for the specified user.
    api_response = api_instance.list_providers(account_id, user_id, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudStorageApi->list_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **redirect_url** | **str**|  The URL the user is redirected to after the cloud storage provider authenticates the user. Using this will append the redirectUrl to the authenticationUrl.  The redirectUrl is restricted to URLs in the docusign.com or docusign.net domains.   | [optional] 

### Return type

[**CloudStorageProviders**](CloudStorageProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

