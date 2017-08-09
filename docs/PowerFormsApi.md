# docusign.PowerFormsApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_power_form**](PowerFormsApi.md#create_power_form) | **POST** /v2/accounts/{accountId}/powerforms | Creates a new PowerForm.
[**delete_power_form**](PowerFormsApi.md#delete_power_form) | **DELETE** /v2/accounts/{accountId}/powerforms/{powerFormId} | Delete a PowerForm.
[**delete_power_forms**](PowerFormsApi.md#delete_power_forms) | **DELETE** /v2/accounts/{accountId}/powerforms | Deletes one or more PowerForms
[**get_power_form**](PowerFormsApi.md#get_power_form) | **GET** /v2/accounts/{accountId}/powerforms/{powerFormId} | Returns a single PowerForm.
[**get_power_form_data**](PowerFormsApi.md#get_power_form_data) | **GET** /v2/accounts/{accountId}/powerforms/{powerFormId}/form_data | Returns the form data associated with the usage of a PowerForm.
[**list_power_form_senders**](PowerFormsApi.md#list_power_form_senders) | **GET** /v2/accounts/{accountId}/powerforms/senders | Returns the list of PowerForms available to the user.
[**list_power_forms**](PowerFormsApi.md#list_power_forms) | **GET** /v2/accounts/{accountId}/powerforms | Returns the list of PowerForms available to the user.
[**update_power_form**](PowerFormsApi.md#update_power_form) | **PUT** /v2/accounts/{accountId}/powerforms/{powerFormId} | Creates a new PowerForm.


# **create_power_form**
> PowerForm create_power_form(account_id, power_form=power_form)

Creates a new PowerForm.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
power_form = docusign.PowerForm() # PowerForm |  (optional)

try: 
    # Creates a new PowerForm.
    api_response = api_instance.create_power_form(account_id, power_form=power_form)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->create_power_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **power_form** | [**PowerForm**](PowerForm.md)|  | [optional] 

### Return type

[**PowerForm**](PowerForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_power_form**
> delete_power_form(account_id, power_form_id)

Delete a PowerForm.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
power_form_id = 'power_form_id_example' # str | 

try: 
    # Delete a PowerForm.
    api_instance.delete_power_form(account_id, power_form_id)
except ApiException as e:
    print("Exception when calling PowerFormsApi->delete_power_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **power_form_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_power_forms**
> PowerFormsResponse delete_power_forms(account_id, power_forms_request=power_forms_request)

Deletes one or more PowerForms

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
power_forms_request = docusign.PowerFormsRequest() # PowerFormsRequest |  (optional)

try: 
    # Deletes one or more PowerForms
    api_response = api_instance.delete_power_forms(account_id, power_forms_request=power_forms_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->delete_power_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **power_forms_request** | [**PowerFormsRequest**](PowerFormsRequest.md)|  | [optional] 

### Return type

[**PowerFormsResponse**](PowerFormsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_form**
> PowerForm get_power_form(account_id, power_form_id)

Returns a single PowerForm.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
power_form_id = 'power_form_id_example' # str | 

try: 
    # Returns a single PowerForm.
    api_response = api_instance.get_power_form(account_id, power_form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->get_power_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **power_form_id** | **str**|  | 

### Return type

[**PowerForm**](PowerForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_form_data**
> PowerFormsFormDataResponse get_power_form_data(account_id, power_form_id, from_date=from_date, to_date=to_date)

Returns the form data associated with the usage of a PowerForm.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
power_form_id = 'power_form_id_example' # str | 
from_date = 'from_date_example' # str |  (optional)
to_date = 'to_date_example' # str |  (optional)

try: 
    # Returns the form data associated with the usage of a PowerForm.
    api_response = api_instance.get_power_form_data(account_id, power_form_id, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->get_power_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **power_form_id** | **str**|  | 
 **from_date** | **str**|  | [optional] 
 **to_date** | **str**|  | [optional] 

### Return type

[**PowerFormsFormDataResponse**](PowerFormsFormDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_power_form_senders**
> PowerFormSendersResponse list_power_form_senders(account_id, start_position=start_position)

Returns the list of PowerForms available to the user.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
start_position = 'start_position_example' # str |  (optional)

try: 
    # Returns the list of PowerForms available to the user.
    api_response = api_instance.list_power_form_senders(account_id, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->list_power_form_senders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **start_position** | **str**|  | [optional] 

### Return type

[**PowerFormSendersResponse**](PowerFormSendersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_power_forms**
> PowerFormsResponse list_power_forms(account_id, from_date=from_date, order=order, order_by=order_by, to_date=to_date)

Returns the list of PowerForms available to the user.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
from_date = 'from_date_example' # str |  (optional)
order = 'order_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
to_date = 'to_date_example' # str |  (optional)

try: 
    # Returns the list of PowerForms available to the user.
    api_response = api_instance.list_power_forms(account_id, from_date=from_date, order=order, order_by=order_by, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->list_power_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **from_date** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **to_date** | **str**|  | [optional] 

### Return type

[**PowerFormsResponse**](PowerFormsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_form**
> PowerForm update_power_form(account_id, power_form_id, power_form=power_form)

Creates a new PowerForm.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.PowerFormsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
power_form_id = 'power_form_id_example' # str | 
power_form = docusign.PowerForm() # PowerForm |  (optional)

try: 
    # Creates a new PowerForm.
    api_response = api_instance.update_power_form(account_id, power_form_id, power_form=power_form)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerFormsApi->update_power_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **power_form_id** | **str**|  | 
 **power_form** | [**PowerForm**](PowerForm.md)|  | [optional] 

### Return type

[**PowerForm**](PowerForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

