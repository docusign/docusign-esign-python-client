# docusign.FoldersApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](FoldersApi.md#list) | **GET** /v2/accounts/{accountId}/folders | Gets a list of the folders for the account.
[**list_items**](FoldersApi.md#list_items) | **GET** /v2/accounts/{accountId}/folders/{folderId} | Gets a list of the envelopes in the specified folder.
[**move_envelopes**](FoldersApi.md#move_envelopes) | **PUT** /v2/accounts/{accountId}/folders/{folderId} | Moves an envelope from its current folder to the specified folder.
[**search**](FoldersApi.md#search) | **GET** /v2/accounts/{accountId}/search_folders/{searchFolderId} | Gets a list of envelopes in folders matching the specified criteria.


# **list**
> FoldersResponse list(account_id, include=include, include_items=include_items, start_position=start_position, template=template, user_filter=user_filter)

Gets a list of the folders for the account.

Retrieves a list of the folders for the account, including the folder hierarchy. You can specify whether to return just the template folder or template folder and normal folders by setting the `template` query string parameter.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.FoldersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
include = 'include_example' # str |  (optional)
include_items = 'include_items_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)
template = 'template_example' # str | Specifies the items that are returned. Valid values are:   * include - The folder list will return normal folders plus template folders.  * only - Only the list of template folders are returned. (optional)
user_filter = 'user_filter_example' # str |  (optional)

try: 
    # Gets a list of the folders for the account.
    api_response = api_instance.list(account_id, include=include, include_items=include_items, start_position=start_position, template=template, user_filter=user_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **include** | **str**|  | [optional] 
 **include_items** | **str**|  | [optional] 
 **start_position** | **str**|  | [optional] 
 **template** | **str**| Specifies the items that are returned. Valid values are:   * include - The folder list will return normal folders plus template folders.  * only - Only the list of template folders are returned. | [optional] 
 **user_filter** | **str**|  | [optional] 

### Return type

[**FoldersResponse**](FoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> FolderItemsResponse list_items(account_id, folder_id, from_date=from_date, include_items=include_items, owner_email=owner_email, owner_name=owner_name, search_text=search_text, start_position=start_position, status=status, to_date=to_date)

Gets a list of the envelopes in the specified folder.

Retrieves a list of the envelopes in the specified folder. You can narrow the query by specifying search criteria in the query string parameters.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.FoldersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
from_date = 'from_date_example' # str |  Only return items on or after this date. If no value is provided, the default search is the previous 30 days.  (optional)
include_items = 'include_items_example' # str |  (optional)
owner_email = 'owner_email_example' # str |  The email of the folder owner.  (optional)
owner_name = 'owner_name_example' # str |  The name of the folder owner.  (optional)
search_text = 'search_text_example' # str |  The search text used to search the items of the envelope. The search looks at recipient names and emails, envelope custom fields, sender name, and subject.  (optional)
start_position = 'start_position_example' # str | The position of the folder items to return. This is used for repeated calls, when the number of envelopes returned is too much for one return (calls return 100 envelopes at a time). The default value is 0. (optional)
status = 'status_example' # str | The current status of the envelope. If no value is provided, the default search is all/any status. (optional)
to_date = 'to_date_example' # str | Only return items up to this date. If no value is provided, the default search is to the current date. (optional)

try: 
    # Gets a list of the envelopes in the specified folder.
    api_response = api_instance.list_items(account_id, folder_id, from_date=from_date, include_items=include_items, owner_email=owner_email, owner_name=owner_name, search_text=search_text, start_position=start_position, status=status, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **from_date** | **str**|  Only return items on or after this date. If no value is provided, the default search is the previous 30 days.  | [optional] 
 **include_items** | **str**|  | [optional] 
 **owner_email** | **str**|  The email of the folder owner.  | [optional] 
 **owner_name** | **str**|  The name of the folder owner.  | [optional] 
 **search_text** | **str**|  The search text used to search the items of the envelope. The search looks at recipient names and emails, envelope custom fields, sender name, and subject.  | [optional] 
 **start_position** | **str**| The position of the folder items to return. This is used for repeated calls, when the number of envelopes returned is too much for one return (calls return 100 envelopes at a time). The default value is 0. | [optional] 
 **status** | **str**| The current status of the envelope. If no value is provided, the default search is all/any status. | [optional] 
 **to_date** | **str**| Only return items up to this date. If no value is provided, the default search is to the current date. | [optional] 

### Return type

[**FolderItemsResponse**](FolderItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_envelopes**
> FoldersResponse move_envelopes(account_id, folder_id, folders_request=folders_request)

Moves an envelope from its current folder to the specified folder.

Moves envelopes to the specified folder.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.FoldersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
folders_request = docusign.FoldersRequest() # FoldersRequest |  (optional)

try: 
    # Moves an envelope from its current folder to the specified folder.
    api_response = api_instance.move_envelopes(account_id, folder_id, folders_request=folders_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->move_envelopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **folders_request** | [**FoldersRequest**](FoldersRequest.md)|  | [optional] 

### Return type

[**FoldersResponse**](FoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> FolderItemResponse search(account_id, search_folder_id, all=all, count=count, from_date=from_date, include_recipients=include_recipients, order=order, order_by=order_by, start_position=start_position, to_date=to_date)

Gets a list of envelopes in folders matching the specified criteria.

Retrieves a list of envelopes that match the criteria specified in the query.  If the user ID of the user making the call is the same as the user ID for any returned recipient, then the userId property is added to the returned information for those recipients.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.FoldersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
search_folder_id = 'search_folder_id_example' # str | Specifies the envelope group that is searched by the request. These are logical groupings, not actual folder names. Valid values are: drafts, awaiting_my_signature, completed, out_for_signature.
all = 'all_example' # str | Specifies that all envelopes that match the criteria are returned. (optional)
count = 'count_example' # str | Specifies the number of records returned in the cache. The number must be greater than 0 and less than or equal to 100. (optional)
from_date = 'from_date_example' # str | Specifies the start of the date range to return. If no value is provided, the default search is the previous 30 days. (optional)
include_recipients = 'include_recipients_example' # str | When set to **true**, the recipient information is returned in the response. (optional)
order = 'order_example' # str | Specifies the order in which the list is returned. Valid values are: `asc` for ascending order, and `desc` for descending order. (optional)
order_by = 'order_by_example' # str | Specifies the property used to sort the list. Valid values are: `action_required`, `created`, `completed`, `sent`, `signer_list`, `status`, or `subject`. (optional)
start_position = 'start_position_example' # str | Specifies the the starting location in the result set of the items that are returned. (optional)
to_date = 'to_date_example' # str | Specifies the end of the date range to return. (optional)

try: 
    # Gets a list of envelopes in folders matching the specified criteria.
    api_response = api_instance.search(account_id, search_folder_id, all=all, count=count, from_date=from_date, include_recipients=include_recipients, order=order, order_by=order_by, start_position=start_position, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **search_folder_id** | **str**| Specifies the envelope group that is searched by the request. These are logical groupings, not actual folder names. Valid values are: drafts, awaiting_my_signature, completed, out_for_signature. | 
 **all** | **str**| Specifies that all envelopes that match the criteria are returned. | [optional] 
 **count** | **str**| Specifies the number of records returned in the cache. The number must be greater than 0 and less than or equal to 100. | [optional] 
 **from_date** | **str**| Specifies the start of the date range to return. If no value is provided, the default search is the previous 30 days. | [optional] 
 **include_recipients** | **str**| When set to **true**, the recipient information is returned in the response. | [optional] 
 **order** | **str**| Specifies the order in which the list is returned. Valid values are: &#x60;asc&#x60; for ascending order, and &#x60;desc&#x60; for descending order. | [optional] 
 **order_by** | **str**| Specifies the property used to sort the list. Valid values are: &#x60;action_required&#x60;, &#x60;created&#x60;, &#x60;completed&#x60;, &#x60;sent&#x60;, &#x60;signer_list&#x60;, &#x60;status&#x60;, or &#x60;subject&#x60;. | [optional] 
 **start_position** | **str**| Specifies the the starting location in the result set of the items that are returned. | [optional] 
 **to_date** | **str**| Specifies the end of the date range to return. | [optional] 

### Return type

[**FolderItemResponse**](FolderItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

