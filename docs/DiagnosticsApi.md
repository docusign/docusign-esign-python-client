# docusign.DiagnosticsApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_request_logs**](DiagnosticsApi.md#delete_request_logs) | **DELETE** /v2/diagnostics/request_logs | Deletes the request log files.
[**get_request_log**](DiagnosticsApi.md#get_request_log) | **GET** /v2/diagnostics/request_logs/{requestLogId} | Gets a request logging log file.
[**get_request_log_settings**](DiagnosticsApi.md#get_request_log_settings) | **GET** /v2/diagnostics/settings | Gets the API request logging settings.
[**get_resources**](DiagnosticsApi.md#get_resources) | **GET** /v2 | Lists resources for REST version specified
[**get_service**](DiagnosticsApi.md#get_service) | **GET** /service_information | Retrieves the available REST API versions.
[**list_request_logs**](DiagnosticsApi.md#list_request_logs) | **GET** /v2/diagnostics/request_logs | Gets the API request logging log files.
[**update_request_log_settings**](DiagnosticsApi.md#update_request_log_settings) | **PUT** /v2/diagnostics/settings | Enables or disables API request logging for troubleshooting.


# **delete_request_logs**
> delete_request_logs()

Deletes the request log files.

Deletes the request log files.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()

try: 
    # Deletes the request log files.
    api_instance.delete_request_logs()
except ApiException as e:
    print("Exception when calling DiagnosticsApi->delete_request_logs: %s\n" % e)
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

# **get_request_log**
> file get_request_log(request_log_id)

Gets a request logging log file.

Retrieves information for a single log entry.  **Request** The `requestLogfId` property can be retrieved by getting the list of log entries. The Content-Transfer-Encoding header can be set to base64 to retrieve the API request/response as base 64 string. Otherwise the bytes of the request/response are returned.  **Response** If the Content-Transfer-Encoding header was set to base64, the log is returned as a base64 string.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()
request_log_id = 'request_log_id_example' # str | 

try: 
    # Gets a request logging log file.
    api_response = api_instance.get_request_log(request_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->get_request_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_log_id** | **str**|  | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_log_settings**
> DiagnosticsSettingsInformation get_request_log_settings()

Gets the API request logging settings.

Retrieves the current API request logging setting for the user and remaining log entries.  **Response** The response includes the current API request logging setting for the user, along with the maximum log entries and remaining log entries.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()

try: 
    # Gets the API request logging settings.
    api_response = api_instance.get_request_log_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->get_request_log_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsSettingsInformation**](DiagnosticsSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> ResourceInformation get_resources()

Lists resources for REST version specified

Retrieves the base resources available for the DocuSign REST APIs.  You do not need an integrator key to view the REST API versions and resources.  Example: https://demo.docusign.net/restapi/v2 lists all of the base resources available in version 2 of the REST API on the DocuSign Demo system.  To view descriptions and samples of the service operations for all versions, remove the version number and add /help to the URL.  Example: https://demo.docusign.net/restapi/help lists the REST API operations on the DocuSign Demo system with XML and JSON request and response samples.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()

try: 
    # Lists resources for REST version specified
    api_response = api_instance.get_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->get_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceInformation**](ResourceInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ServiceInformation get_service()

Retrieves the available REST API versions.

Retrieves the available REST API versions.  DocuSign Production system: https://www.docusign.net/restapi/service_information DocuSign Demo system: https://demo.docusign.net/restapi/service_information  You do not need an integrator key to view the REST API versions and resources.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()

try: 
    # Retrieves the available REST API versions.
    api_response = api_instance.get_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->get_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceInformation**](ServiceInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_request_logs**
> ApiRequestLogsResult list_request_logs(encoding=encoding)

Gets the API request logging log files.

Retrieves a list of log entries as a JSON or xml object or as a zip file containing the entries.  If the Accept header is set to application/zip, the response is a zip file containing individual text files, each representing an API request.  If the Accept header is set to `application/json` or `application/xml`, the response returns list of log entries in either JSON or XML. An example JSON response body is shown below. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()
encoding = 'encoding_example' # str |  (optional)

try: 
    # Gets the API request logging log files.
    api_response = api_instance.list_request_logs(encoding=encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->list_request_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding** | **str**|  | [optional] 

### Return type

[**ApiRequestLogsResult**](ApiRequestLogsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_request_log_settings**
> DiagnosticsSettingsInformation update_request_log_settings(diagnostics_settings_information=diagnostics_settings_information)

Enables or disables API request logging for troubleshooting.

Enables or disables API request logging for troubleshooting.  When enabled (`apiRequestLogging` is set to true), REST API requests and responses for the user are added to a log. A log can have up to 50 requests/responses and the current number of log entries can be determined by getting the settings. Logging is automatically disabled when the log limit of 50 is reached.  You can call [ML:GetRequestLog] or [ML:GetRequestLogs] to download the log files (individually or as a zip file). Call [ML:DeleteRequestLogs] to clear the log by deleting current entries.  Private information, such as passwords and integrator key information, which is normally located in the call header is omitted from the request/response log.  ###### Note: API request logging only captures requests from the authenticated user. Any call that does not authenticate the user and resolve a userId isn't logged. Meaning that login_information, NewAccounts, or other distributor-credential calls are not logged. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.DiagnosticsApi()
diagnostics_settings_information = docusign.DiagnosticsSettingsInformation() # DiagnosticsSettingsInformation |  (optional)

try: 
    # Enables or disables API request logging for troubleshooting.
    api_response = api_instance.update_request_log_settings(diagnostics_settings_information=diagnostics_settings_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->update_request_log_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_settings_information** | [**DiagnosticsSettingsInformation**](DiagnosticsSettingsInformation.md)|  | [optional] 

### Return type

[**DiagnosticsSettingsInformation**](DiagnosticsSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

