# docusign.BulkEnvelopesApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recipients**](BulkEnvelopesApi.md#delete_recipients) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/bulk_recipients | Deletes the bulk recipient file from an envelope.
[**get**](BulkEnvelopesApi.md#get) | **GET** /v2/accounts/{accountId}/bulk_envelopes/{batchId} | Gets the status of a specified bulk send operation.
[**get_recipients**](BulkEnvelopesApi.md#get_recipients) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/bulk_recipients | Gets the bulk recipient file from an envelope.
[**list**](BulkEnvelopesApi.md#list) | **GET** /v2/accounts/{accountId}/bulk_envelopes | Gets status information about bulk recipient batches.
[**update_recipients**](BulkEnvelopesApi.md#update_recipients) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/bulk_recipients | Adds or replaces envelope bulk recipients.


# **delete_recipients**
> BulkRecipientsUpdateResponse delete_recipients(account_id, envelope_id, recipient_id)

Deletes the bulk recipient file from an envelope.

Deletes the bulk recipient file from an envelope. This cannot be used if the envelope has been sent.  After using this, the `bulkRecipientsUri` property is not returned in subsequent GET calls for the envelope, but the recipient will remain as a bulk recipient.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BulkEnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.

try: 
    # Deletes the bulk recipient file from an envelope.
    api_response = api_instance.delete_recipients(account_id, envelope_id, recipient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnvelopesApi->delete_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 

### Return type

[**BulkRecipientsUpdateResponse**](BulkRecipientsUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> BulkEnvelopeStatus get(account_id, batch_id, count=count, include=include, start_position=start_position)

Gets the status of a specified bulk send operation.

Retrieves the status information of a single bulk recipient batch. A bulk recipient batch is the set of envelopes sent from a single bulk recipient file. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BulkEnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
batch_id = 'batch_id_example' # str | 
count = 'count_example' # str | Specifies the number of entries to return. (optional)
include = 'include_example' # str | Specifies which entries are included in the response. Multiple entries can be included by using commas in the query string (example: ?include=”failed,queued”)   Valid values are:   * all - Returns all entries. If present, overrides all other query settings. This is the default if no query string is provided. * failed - This only returns entries with a failed status. * queued - This only returns entries with a queued status. * sent – This only returns entries with a sent status.   (optional)
start_position = 'start_position_example' # str | Specifies the location in the list of envelopes from which to start. (optional)

try: 
    # Gets the status of a specified bulk send operation.
    api_response = api_instance.get(account_id, batch_id, count=count, include=include, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnvelopesApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **batch_id** | **str**|  | 
 **count** | **str**| Specifies the number of entries to return. | [optional] 
 **include** | **str**| Specifies which entries are included in the response. Multiple entries can be included by using commas in the query string (example: ?include&#x3D;”failed,queued”)   Valid values are:   * all - Returns all entries. If present, overrides all other query settings. This is the default if no query string is provided. * failed - This only returns entries with a failed status. * queued - This only returns entries with a queued status. * sent – This only returns entries with a sent status.   | [optional] 
 **start_position** | **str**| Specifies the location in the list of envelopes from which to start. | [optional] 

### Return type

[**BulkEnvelopeStatus**](BulkEnvelopeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipients**
> BulkRecipientsResponse get_recipients(account_id, envelope_id, recipient_id, include_tabs=include_tabs, start_position=start_position)

Gets the bulk recipient file from an envelope.

Retrieves the bulk recipient file information from an envelope that has a bulk recipient.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BulkEnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
include_tabs = 'include_tabs_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)

try: 
    # Gets the bulk recipient file from an envelope.
    api_response = api_instance.get_recipients(account_id, envelope_id, recipient_id, include_tabs=include_tabs, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnvelopesApi->get_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **include_tabs** | **str**|  | [optional] 
 **start_position** | **str**|  | [optional] 

### Return type

[**BulkRecipientsResponse**](BulkRecipientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> BulkEnvelopesResponse list(account_id, count=count, include=include, start_position=start_position)

Gets status information about bulk recipient batches.

Retrieves status information about all the bulk recipient batches. A bulk recipient batch is the set of envelopes sent from a single bulk recipient file. The response includes general information about each bulk recipient batch.   The response returns information about the envelopes sent with bulk recipient batches, including the `batchId` property, which can be used to retrieve a more detailed status of individual bulk recipient batches.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BulkEnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
count = 'count_example' # str | The number of results to return. This can be 1 to 20. (optional)
include = 'include_example' # str |  (optional)
start_position = 'start_position_example' # str | The position of the bulk envelope items in the response. This is used for repeated calls, when the number of bulk envelopes returned is too large for one return. The default value is 0. (optional)

try: 
    # Gets status information about bulk recipient batches.
    api_response = api_instance.list(account_id, count=count, include=include, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnvelopesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **count** | **str**| The number of results to return. This can be 1 to 20. | [optional] 
 **include** | **str**|  | [optional] 
 **start_position** | **str**| The position of the bulk envelope items in the response. This is used for repeated calls, when the number of bulk envelopes returned is too large for one return. The default value is 0. | [optional] 

### Return type

[**BulkEnvelopesResponse**](BulkEnvelopesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipients**
> BulkRecipientsSummaryResponse update_recipients(account_id, envelope_id, recipient_id, bulk_recipients_request=bulk_recipients_request)

Adds or replaces envelope bulk recipients.

Updates the bulk recipients in a draft envelope using a file upload. The Content-Type supported for uploading a bulk recipient file is CSV (text/csv).  The REST API does not support modifying individual rows or values in the bulk recipients file. It only allows the entire file to be added or replaced with a new file.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BulkEnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
bulk_recipients_request = docusign.BulkRecipientsRequest() # BulkRecipientsRequest |  (optional)

try: 
    # Adds or replaces envelope bulk recipients.
    api_response = api_instance.update_recipients(account_id, envelope_id, recipient_id, bulk_recipients_request=bulk_recipients_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnvelopesApi->update_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **bulk_recipients_request** | [**BulkRecipientsRequest**](BulkRecipientsRequest.md)|  | [optional] 

### Return type

[**BulkRecipientsSummaryResponse**](BulkRecipientsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

