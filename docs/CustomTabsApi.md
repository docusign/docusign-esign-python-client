# docusign.CustomTabsApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomTabsApi.md#create) | **POST** /v2/accounts/{accountId}/tab_definitions | Creates a custom tab.
[**delete**](CustomTabsApi.md#delete) | **DELETE** /v2/accounts/{accountId}/tab_definitions/{customTabId} | Deletes custom tab information.
[**get**](CustomTabsApi.md#get) | **GET** /v2/accounts/{accountId}/tab_definitions/{customTabId} | Gets custom tab information.
[**list**](CustomTabsApi.md#list) | **GET** /v2/accounts/{accountId}/tab_definitions | Gets a list of all account tabs.
[**update**](CustomTabsApi.md#update) | **PUT** /v2/accounts/{accountId}/tab_definitions/{customTabId} | Updates custom tab information.  


# **create**
> TabMetadata create(account_id, tab_metadata=tab_metadata)

Creates a custom tab.

Creates a tab with pre-defined properties, such as a text tab with a certain font type and validation pattern. Users can access the custom tabs when sending documents through the DocuSign web application.  Custom tabs can be created for approve, checkbox, company, date, date signed, decline, email, email address, envelope ID, first name, formula, full name, initial here, last name, list, note, number, radio, sign here, signer attachment, SSN, text, title, and zip tabs.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CustomTabsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
tab_metadata = docusign.TabMetadata() # TabMetadata |  (optional)

try: 
    # Creates a custom tab.
    api_response = api_instance.create(account_id, tab_metadata=tab_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTabsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **tab_metadata** | [**TabMetadata**](TabMetadata.md)|  | [optional] 

### Return type

[**TabMetadata**](TabMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(account_id, custom_tab_id)

Deletes custom tab information.

Deletes the custom from the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CustomTabsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
custom_tab_id = 'custom_tab_id_example' # str | 

try: 
    # Deletes custom tab information.
    api_instance.delete(account_id, custom_tab_id)
except ApiException as e:
    print("Exception when calling CustomTabsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **custom_tab_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> TabMetadata get(account_id, custom_tab_id)

Gets custom tab information.

Retrieves information about the requested custom tab on the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CustomTabsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
custom_tab_id = 'custom_tab_id_example' # str | 

try: 
    # Gets custom tab information.
    api_response = api_instance.get(account_id, custom_tab_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTabsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **custom_tab_id** | **str**|  | 

### Return type

[**TabMetadata**](TabMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> TabMetadataList list(account_id, custom_tab_only=custom_tab_only)

Gets a list of all account tabs.

Retrieves a list of all tabs associated with the account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CustomTabsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
custom_tab_only = 'custom_tab_only_example' # str | When set to **true**, only custom tabs are returned in the response.  (optional)

try: 
    # Gets a list of all account tabs.
    api_response = api_instance.list(account_id, custom_tab_only=custom_tab_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTabsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **custom_tab_only** | **str**| When set to **true**, only custom tabs are returned in the response.  | [optional] 

### Return type

[**TabMetadataList**](TabMetadataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> TabMetadata update(account_id, custom_tab_id, tab_metadata=tab_metadata)

Updates custom tab information.  

Updates the information in a custom tab for the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.CustomTabsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
custom_tab_id = 'custom_tab_id_example' # str | 
tab_metadata = docusign.TabMetadata() # TabMetadata |  (optional)

try: 
    # Updates custom tab information.  
    api_response = api_instance.update(account_id, custom_tab_id, tab_metadata=tab_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTabsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **custom_tab_id** | **str**|  | 
 **tab_metadata** | [**TabMetadata**](TabMetadata.md)|  | [optional] 

### Return type

[**TabMetadata**](TabMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

