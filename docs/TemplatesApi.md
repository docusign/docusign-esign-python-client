# docusign.TemplatesApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_fields**](TemplatesApi.md#create_custom_fields) | **POST** /v2/accounts/{accountId}/templates/{templateId}/custom_fields | Creates custom document fields in an existing template document.
[**create_document_fields**](TemplatesApi.md#create_document_fields) | **POST** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/fields | Creates custom document fields in an existing template document.
[**create_edit_view**](TemplatesApi.md#create_edit_view) | **POST** /v2/accounts/{accountId}/templates/{templateId}/views/edit | Provides a URL to start an edit view of the Template UI
[**create_lock**](TemplatesApi.md#create_lock) | **POST** /v2/accounts/{accountId}/templates/{templateId}/lock | Lock a template.
[**create_recipients**](TemplatesApi.md#create_recipients) | **POST** /v2/accounts/{accountId}/templates/{templateId}/recipients | Adds tabs for a recipient.
[**create_tabs**](TemplatesApi.md#create_tabs) | **POST** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs | Adds tabs for a recipient.
[**create_template**](TemplatesApi.md#create_template) | **POST** /v2/accounts/{accountId}/templates | Creates an envelope from a template.
[**delete_bulk_recipients**](TemplatesApi.md#delete_bulk_recipients) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/bulk_recipients | Deletes the bulk recipient list on a template.
[**delete_custom_fields**](TemplatesApi.md#delete_custom_fields) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/custom_fields | Deletes envelope custom fields in a template.
[**delete_document_fields**](TemplatesApi.md#delete_document_fields) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/fields | Deletes custom document fields from an existing template document.
[**delete_document_page**](TemplatesApi.md#delete_document_page) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/pages/{pageNumber} | Deletes a page from a document in an template.
[**delete_documents**](TemplatesApi.md#delete_documents) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/documents | Deletes documents from a template.
[**delete_group_share**](TemplatesApi.md#delete_group_share) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/{templatePart} | Removes a member group&#39;s sharing permissions for a template.
[**delete_lock**](TemplatesApi.md#delete_lock) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/lock | Deletes a template lock.
[**delete_recipient**](TemplatesApi.md#delete_recipient) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId} | Deletes the specified recipient file from a template.
[**delete_recipients**](TemplatesApi.md#delete_recipients) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/recipients | Deletes recipients from a template.
[**delete_tabs**](TemplatesApi.md#delete_tabs) | **DELETE** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs | Deletes the tabs associated with a recipient in a template.
[**get**](TemplatesApi.md#get) | **GET** /v2/accounts/{accountId}/templates/{templateId} | Gets a list of templates for a specified account.
[**get_document**](TemplatesApi.md#get_document) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId} | Gets PDF documents from a template.
[**get_document_page_image**](TemplatesApi.md#get_document_page_image) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/pages/{pageNumber}/page_image | Gets a page image from a template for display.
[**get_document_tabs**](TemplatesApi.md#get_document_tabs) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/tabs | Returns tabs on the document.
[**get_lock**](TemplatesApi.md#get_lock) | **GET** /v2/accounts/{accountId}/templates/{templateId}/lock | Gets template lock information.
[**get_notification_settings**](TemplatesApi.md#get_notification_settings) | **GET** /v2/accounts/{accountId}/templates/{templateId}/notification | Gets template notification information.
[**get_page_tabs**](TemplatesApi.md#get_page_tabs) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/pages/{pageNumber}/tabs | Returns tabs on the specified page.
[**get_pages**](TemplatesApi.md#get_pages) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/pages | Returns document page image(s) based on input.
[**list_bulk_recipients**](TemplatesApi.md#list_bulk_recipients) | **GET** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/bulk_recipients | Gets the bulk recipient file from a template.
[**list_custom_fields**](TemplatesApi.md#list_custom_fields) | **GET** /v2/accounts/{accountId}/templates/{templateId}/custom_fields | Gets the custom document fields from a template.
[**list_document_fields**](TemplatesApi.md#list_document_fields) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/fields | Gets the custom document fields for a an existing template document.
[**list_documents**](TemplatesApi.md#list_documents) | **GET** /v2/accounts/{accountId}/templates/{templateId}/documents | Gets a list of documents associated with a template.
[**list_recipients**](TemplatesApi.md#list_recipients) | **GET** /v2/accounts/{accountId}/templates/{templateId}/recipients | Gets recipient information from a template.
[**list_tabs**](TemplatesApi.md#list_tabs) | **GET** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs | Gets the tabs information for a signer or sign-in-person recipient in a template.
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /v2/accounts/{accountId}/templates | Gets the definition of a template.
[**rotate_document_page**](TemplatesApi.md#rotate_document_page) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/pages/{pageNumber}/page_image | Rotates page image from a template for display.
[**update**](TemplatesApi.md#update) | **PUT** /v2/accounts/{accountId}/templates/{templateId} | Updates an existing template.
[**update_bulk_recipients**](TemplatesApi.md#update_bulk_recipients) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/bulk_recipients | Adds or replaces the bulk recipients list in a template.
[**update_custom_fields**](TemplatesApi.md#update_custom_fields) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/custom_fields | Updates envelope custom fields in a template.
[**update_document**](TemplatesApi.md#update_document) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId} | Adds a document to a template document.
[**update_document_fields**](TemplatesApi.md#update_document_fields) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/documents/{documentId}/fields | Updates existing custom document fields in an existing template document.
[**update_documents**](TemplatesApi.md#update_documents) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/documents | Adds documents to a template document.
[**update_group_share**](TemplatesApi.md#update_group_share) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/{templatePart} | Shares a template with a group
[**update_lock**](TemplatesApi.md#update_lock) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/lock | Updates a template lock.
[**update_notification_settings**](TemplatesApi.md#update_notification_settings) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/notification | Updates the notification  structure for an existing template.
[**update_recipients**](TemplatesApi.md#update_recipients) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/recipients | Updates recipients in a template.
[**update_tabs**](TemplatesApi.md#update_tabs) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs | Updates the tabs for a recipient.


# **create_custom_fields**
> CustomFields create_custom_fields(account_id, template_id, template_custom_fields=template_custom_fields)

Creates custom document fields in an existing template document.

Creates custom document fields in an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_custom_fields = docusign.TemplateCustomFields() # TemplateCustomFields |  (optional)

try: 
    # Creates custom document fields in an existing template document.
    api_response = api_instance.create_custom_fields(account_id, template_id, template_custom_fields=template_custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_custom_fields** | [**TemplateCustomFields**](TemplateCustomFields.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_fields**
> DocumentFieldsInformation create_document_fields(account_id, document_id, template_id, document_fields_information=document_fields_information)

Creates custom document fields in an existing template document.

Creates custom document fields in an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
document_fields_information = docusign.DocumentFieldsInformation() # DocumentFieldsInformation |  (optional)

try: 
    # Creates custom document fields in an existing template document.
    api_response = api_instance.create_document_fields(account_id, document_id, template_id, document_fields_information=document_fields_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **document_fields_information** | [**DocumentFieldsInformation**](DocumentFieldsInformation.md)|  | [optional] 

### Return type

[**DocumentFieldsInformation**](DocumentFieldsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edit_view**
> ViewUrl create_edit_view(account_id, template_id, return_url_request=return_url_request)

Provides a URL to start an edit view of the Template UI

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
return_url_request = docusign.ReturnUrlRequest() # ReturnUrlRequest |  (optional)

try: 
    # Provides a URL to start an edit view of the Template UI
    api_response = api_instance.create_edit_view(account_id, template_id, return_url_request=return_url_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_edit_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **return_url_request** | [**ReturnUrlRequest**](ReturnUrlRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lock**
> LockInformation create_lock(account_id, template_id, lock_request=lock_request)

Lock a template.

Locks the specified template, and sets the time until the lock expires, to prevent other users or recipients from accessing and changing the template.  ###### Note: Users must have envelope locking capability enabled to use this function (the userSetting property `canLockEnvelopes` must be set to **true** for the user).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
lock_request = docusign.LockRequest() # LockRequest |  (optional)

try: 
    # Lock a template.
    api_response = api_instance.create_lock(account_id, template_id, lock_request=lock_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **lock_request** | [**LockRequest**](LockRequest.md)|  | [optional] 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recipients**
> Recipients create_recipients(account_id, template_id, resend_envelope=resend_envelope, template_recipients=template_recipients)

Adds tabs for a recipient.

Adds one or more recipients to a template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
resend_envelope = 'resend_envelope_example' # str |  (optional)
template_recipients = docusign.TemplateRecipients() # TemplateRecipients |  (optional)

try: 
    # Adds tabs for a recipient.
    api_response = api_instance.create_recipients(account_id, template_id, resend_envelope=resend_envelope, template_recipients=template_recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **resend_envelope** | **str**|  | [optional] 
 **template_recipients** | [**TemplateRecipients**](TemplateRecipients.md)|  | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tabs**
> Tabs create_tabs(account_id, recipient_id, template_id, template_tabs=template_tabs)

Adds tabs for a recipient.

Adds one or more tabs for a recipient.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_tabs = docusign.TemplateTabs() # TemplateTabs |  (optional)

try: 
    # Adds tabs for a recipient.
    api_response = api_instance.create_tabs(account_id, recipient_id, template_id, template_tabs=template_tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_tabs** | [**TemplateTabs**](TemplateTabs.md)|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> TemplateSummary create_template(account_id, envelope_template=envelope_template)

Creates an envelope from a template.

Creates a template definition using a multipart request.  ###Template Email Subject Merge Fields  Call this endpoint to insert a recipient name and email address merge fields into the email subject line when creating or sending from a template.  The merge fields, based on the recipient’s role name, are added to the `emailSubject` property when the template is created or when the template is used to create an envelope. After a template sender adds the name and email information for the recipient and sends the envelope, the recipient information is automatically merged into the appropriate fields in the email subject line.  Both the sender and the recipients will see the information in the email subject line for any emails associated with the template. This provides an easy way for senders to organize their envelope emails without having to open an envelope to check the recipient. ###### Note: If merging the recipient information into the subject line causes the subject line to exceed 100 characters, then any characters over the 100 character limit are not included in the subject line. For cases where the recipient name or email is expected to be long, you should consider placing the merge field at the start of the email subject.  To add a recipient’s name in the subject line add the following text in the `emailSubject` property when creating the template or when sending an envelope from a template:  [[<roleName>_UserName]]  Example:  `\"emailSubject\":\"[[Signer 1_UserName]], Please sign this NDA\",`  To add a recipient’s email address in the subject line add the following text in the `emailSubject` property when creating the template or when sending an envelope from a template:  [[<roleName>_Email]]  Example:  `\"emailSubject\":\"[[Signer 1_Email]], Please sign this NDA\",`   In both cases the <roleName> is the recipient's contents of the `roleName` property in the template.  For cases where another recipient (such as an Agent, Editor, or Intermediary recipient) is entering the name and email information for the recipient included in the email subject, then [[<roleName>_UserName]] or [[<roleName>_Email]] is shown in the email subject.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_template = docusign.EnvelopeTemplate() # EnvelopeTemplate |  (optional)

try: 
    # Creates an envelope from a template.
    api_response = api_instance.create_template(account_id, envelope_template=envelope_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_template** | [**EnvelopeTemplate**](EnvelopeTemplate.md)|  | [optional] 

### Return type

[**TemplateSummary**](TemplateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_recipients**
> BulkRecipientsUpdateResponse delete_bulk_recipients(account_id, recipient_id, template_id)

Deletes the bulk recipient list on a template.

Deletes the bulk recipient list on a template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Deletes the bulk recipient list on a template.
    api_response = api_instance.delete_bulk_recipients(account_id, recipient_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_bulk_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**BulkRecipientsUpdateResponse**](BulkRecipientsUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_fields**
> CustomFields delete_custom_fields(account_id, template_id, template_custom_fields=template_custom_fields)

Deletes envelope custom fields in a template.

Deletes envelope custom fields in a template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_custom_fields = docusign.TemplateCustomFields() # TemplateCustomFields |  (optional)

try: 
    # Deletes envelope custom fields in a template.
    api_response = api_instance.delete_custom_fields(account_id, template_id, template_custom_fields=template_custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_custom_fields** | [**TemplateCustomFields**](TemplateCustomFields.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_fields**
> DocumentFieldsInformation delete_document_fields(account_id, document_id, template_id, document_fields_information=document_fields_information)

Deletes custom document fields from an existing template document.

Deletes custom document fields from an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
document_fields_information = docusign.DocumentFieldsInformation() # DocumentFieldsInformation |  (optional)

try: 
    # Deletes custom document fields from an existing template document.
    api_response = api_instance.delete_document_fields(account_id, document_id, template_id, document_fields_information=document_fields_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **document_fields_information** | [**DocumentFieldsInformation**](DocumentFieldsInformation.md)|  | [optional] 

### Return type

[**DocumentFieldsInformation**](DocumentFieldsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_page**
> delete_document_page(account_id, document_id, page_number, template_id, page_request=page_request)

Deletes a page from a document in an template.

Deletes a page from a document in a template based on the page number.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
page_number = 'page_number_example' # str | The page number being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
page_request = docusign.PageRequest() # PageRequest |  (optional)

try: 
    # Deletes a page from a document in an template.
    api_instance.delete_document_page(account_id, document_id, page_number, template_id, page_request=page_request)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_document_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **page_number** | **str**| The page number being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **page_request** | [**PageRequest**](PageRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_documents**
> TemplateDocumentsResult delete_documents(account_id, template_id, envelope_definition=envelope_definition)

Deletes documents from a template.

Deletes one or more documents from an existing template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
envelope_definition = docusign.EnvelopeDefinition() # EnvelopeDefinition |  (optional)

try: 
    # Deletes documents from a template.
    api_response = api_instance.delete_documents(account_id, template_id, envelope_definition=envelope_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **envelope_definition** | [**EnvelopeDefinition**](EnvelopeDefinition.md)|  | [optional] 

### Return type

[**TemplateDocumentsResult**](TemplateDocumentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_share**
> GroupInformation delete_group_share(account_id, template_id, template_part, group_information=group_information)

Removes a member group's sharing permissions for a template.

Removes a member group's sharing permissions for a specified template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_part = 'template_part_example' # str | Currently, the only defined part is **groups**.
group_information = docusign.GroupInformation() # GroupInformation |  (optional)

try: 
    # Removes a member group's sharing permissions for a template.
    api_response = api_instance.delete_group_share(account_id, template_id, template_part, group_information=group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_group_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_part** | **str**| Currently, the only defined part is **groups**. | 
 **group_information** | [**GroupInformation**](GroupInformation.md)|  | [optional] 

### Return type

[**GroupInformation**](GroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lock**
> LockInformation delete_lock(account_id, template_id, lock_request=lock_request)

Deletes a template lock.

Deletes the lock from the specified template. The `X-DocuSign-Edit` header must be included in the request.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
lock_request = docusign.LockRequest() # LockRequest |  (optional)

try: 
    # Deletes a template lock.
    api_response = api_instance.delete_lock(account_id, template_id, lock_request=lock_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **lock_request** | [**LockRequest**](LockRequest.md)|  | [optional] 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipient**
> Recipients delete_recipient(account_id, recipient_id, template_id, template_recipients=template_recipients)

Deletes the specified recipient file from a template.

Deletes the specified recipient file from the specified template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_recipients = docusign.TemplateRecipients() # TemplateRecipients |  (optional)

try: 
    # Deletes the specified recipient file from a template.
    api_response = api_instance.delete_recipient(account_id, recipient_id, template_id, template_recipients=template_recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_recipients** | [**TemplateRecipients**](TemplateRecipients.md)|  | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipients**
> Recipients delete_recipients(account_id, template_id, template_recipients=template_recipients)

Deletes recipients from a template.

Deletes one or more recipients from a template. Recipients to be deleted are listed in the request, with the `recipientId` being used as the key for deleting recipients.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_recipients = docusign.TemplateRecipients() # TemplateRecipients |  (optional)

try: 
    # Deletes recipients from a template.
    api_response = api_instance.delete_recipients(account_id, template_id, template_recipients=template_recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_recipients** | [**TemplateRecipients**](TemplateRecipients.md)|  | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tabs**
> Tabs delete_tabs(account_id, recipient_id, template_id, template_tabs=template_tabs)

Deletes the tabs associated with a recipient in a template.

Deletes one or more tabs associated with a recipient in a template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_tabs = docusign.TemplateTabs() # TemplateTabs |  (optional)

try: 
    # Deletes the tabs associated with a recipient in a template.
    api_response = api_instance.delete_tabs(account_id, recipient_id, template_id, template_tabs=template_tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_tabs** | [**TemplateTabs**](TemplateTabs.md)|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> EnvelopeTemplate get(account_id, template_id, include=include)

Gets a list of templates for a specified account.

Retrieves the definition of the specified template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
include = 'include_example' # str |  (optional)

try: 
    # Gets a list of templates for a specified account.
    api_response = api_instance.get(account_id, template_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **include** | **str**|  | [optional] 

### Return type

[**EnvelopeTemplate**](EnvelopeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> file get_document(account_id, document_id, template_id, encrypt=encrypt, show_changes=show_changes)

Gets PDF documents from a template.

Retrieves one or more PDF documents from the specified template.  You can specify the ID of the document to retrieve or can specify `combined` to retrieve all documents in the template as one pdf.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
encrypt = 'encrypt_example' # str |  (optional)
show_changes = 'show_changes_example' # str |  (optional)

try: 
    # Gets PDF documents from a template.
    api_response = api_instance.get_document(account_id, document_id, template_id, encrypt=encrypt, show_changes=show_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **encrypt** | **str**|  | [optional] 
 **show_changes** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_page_image**
> file get_document_page_image(account_id, document_id, page_number, template_id, dpi=dpi, max_height=max_height, max_width=max_width, show_changes=show_changes)

Gets a page image from a template for display.

Retrieves a page image for display from the specified template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
page_number = 'page_number_example' # str | The page number being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
dpi = 'dpi_example' # str |  (optional)
max_height = 'max_height_example' # str |  (optional)
max_width = 'max_width_example' # str |  (optional)
show_changes = 'show_changes_example' # str |  (optional)

try: 
    # Gets a page image from a template for display.
    api_response = api_instance.get_document_page_image(account_id, document_id, page_number, template_id, dpi=dpi, max_height=max_height, max_width=max_width, show_changes=show_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_document_page_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **page_number** | **str**| The page number being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **dpi** | **str**|  | [optional] 
 **max_height** | **str**|  | [optional] 
 **max_width** | **str**|  | [optional] 
 **show_changes** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_tabs**
> Tabs get_document_tabs(account_id, document_id, template_id, page_numbers=page_numbers)

Returns tabs on the document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
page_numbers = 'page_numbers_example' # str |  (optional)

try: 
    # Returns tabs on the document.
    api_response = api_instance.get_document_tabs(account_id, document_id, template_id, page_numbers=page_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_document_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **page_numbers** | **str**|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lock**
> LockInformation get_lock(account_id, template_id)

Gets template lock information.

Retrieves general information about the template lock.  If the call is made by the user who has the lock and the request has the same integrator key as original, then the `X-DocuSign-Edit` header  field and additional lock information is included in the response. This allows users to recover a lost editing session token and the `X-DocuSign-Edit` header.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Gets template lock information.
    api_response = api_instance.get_lock(account_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_settings**
> Notification get_notification_settings(account_id, template_id)

Gets template notification information.

Retrieves the envelope notification, reminders and expirations, information for an existing template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Gets template notification information.
    api_response = api_instance.get_notification_settings(account_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_tabs**
> Tabs get_page_tabs(account_id, document_id, page_number, template_id)

Returns tabs on the specified page.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
page_number = 'page_number_example' # str | The page number being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Returns tabs on the specified page.
    api_response = api_instance.get_page_tabs(account_id, document_id, page_number, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_page_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **page_number** | **str**| The page number being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages**
> PageImages get_pages(account_id, document_id, template_id, count=count, dpi=dpi, max_height=max_height, max_width=max_width, nocache=nocache, show_changes=show_changes, start_position=start_position)

Returns document page image(s) based on input.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
count = 'count_example' # str |  (optional)
dpi = 'dpi_example' # str |  (optional)
max_height = 'max_height_example' # str |  (optional)
max_width = 'max_width_example' # str |  (optional)
nocache = 'nocache_example' # str |  (optional)
show_changes = 'show_changes_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)

try: 
    # Returns document page image(s) based on input.
    api_response = api_instance.get_pages(account_id, document_id, template_id, count=count, dpi=dpi, max_height=max_height, max_width=max_width, nocache=nocache, show_changes=show_changes, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **count** | **str**|  | [optional] 
 **dpi** | **str**|  | [optional] 
 **max_height** | **str**|  | [optional] 
 **max_width** | **str**|  | [optional] 
 **nocache** | **str**|  | [optional] 
 **show_changes** | **str**|  | [optional] 
 **start_position** | **str**|  | [optional] 

### Return type

[**PageImages**](PageImages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bulk_recipients**
> BulkRecipientsResponse list_bulk_recipients(account_id, recipient_id, template_id, include_tabs=include_tabs, start_position=start_position)

Gets the bulk recipient file from a template.

Retrieves the bulk recipient file information from a template that has a bulk recipient.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
include_tabs = 'include_tabs_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)

try: 
    # Gets the bulk recipient file from a template.
    api_response = api_instance.list_bulk_recipients(account_id, recipient_id, template_id, include_tabs=include_tabs, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_bulk_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
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

# **list_custom_fields**
> CustomFields list_custom_fields(account_id, template_id)

Gets the custom document fields from a template.

Retrieves the custom document field information from an existing template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Gets the custom document fields from a template.
    api_response = api_instance.list_custom_fields(account_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_document_fields**
> DocumentFieldsInformation list_document_fields(account_id, document_id, template_id)

Gets the custom document fields for a an existing template document.

Retrieves the custom document fields for an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Gets the custom document fields for a an existing template document.
    api_response = api_instance.list_document_fields(account_id, document_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**DocumentFieldsInformation**](DocumentFieldsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> TemplateDocumentsResult list_documents(account_id, template_id)

Gets a list of documents associated with a template.

Retrieves a list of documents associated with the specified template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Gets a list of documents associated with a template.
    api_response = api_instance.list_documents(account_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**TemplateDocumentsResult**](TemplateDocumentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recipients**
> Recipients list_recipients(account_id, template_id, include_anchor_tab_locations=include_anchor_tab_locations, include_extended=include_extended, include_tabs=include_tabs)

Gets recipient information from a template.

Retrieves the information for all recipients in the specified template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
include_anchor_tab_locations = 'include_anchor_tab_locations_example' # str |  When set to **true** and `include_tabs` is set to **true**, all tabs with anchor tab properties are included in the response.  (optional)
include_extended = 'include_extended_example' # str |  When set to **true**, the extended properties are included in the response.  (optional)
include_tabs = 'include_tabs_example' # str | When set to **true**, the tab information associated with the recipient is included in the response. (optional)

try: 
    # Gets recipient information from a template.
    api_response = api_instance.list_recipients(account_id, template_id, include_anchor_tab_locations=include_anchor_tab_locations, include_extended=include_extended, include_tabs=include_tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **include_anchor_tab_locations** | **str**|  When set to **true** and &#x60;include_tabs&#x60; is set to **true**, all tabs with anchor tab properties are included in the response.  | [optional] 
 **include_extended** | **str**|  When set to **true**, the extended properties are included in the response.  | [optional] 
 **include_tabs** | **str**| When set to **true**, the tab information associated with the recipient is included in the response. | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tabs**
> Tabs list_tabs(account_id, recipient_id, template_id, include_anchor_tab_locations=include_anchor_tab_locations, include_metadata=include_metadata)

Gets the tabs information for a signer or sign-in-person recipient in a template.

Gets the tabs information for a signer or sign-in-person recipient in a template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
include_anchor_tab_locations = 'include_anchor_tab_locations_example' # str | When set to **true**, all tabs with anchor tab properties are included in the response.  (optional)
include_metadata = 'include_metadata_example' # str |  (optional)

try: 
    # Gets the tabs information for a signer or sign-in-person recipient in a template.
    api_response = api_instance.list_tabs(account_id, recipient_id, template_id, include_anchor_tab_locations=include_anchor_tab_locations, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **include_anchor_tab_locations** | **str**| When set to **true**, all tabs with anchor tab properties are included in the response.  | [optional] 
 **include_metadata** | **str**|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> EnvelopeTemplateResults list_templates(account_id, count=count, folder=folder, folder_ids=folder_ids, folder_types=folder_types, from_date=from_date, include=include, order=order, order_by=order_by, search_text=search_text, shared=shared, shared_by_me=shared_by_me, start_position=start_position, to_date=to_date, used_from_date=used_from_date, used_to_date=used_to_date, user_filter=user_filter, user_id=user_id)

Gets the definition of a template.

Retrieves the list of templates for the specified account. The request can be limited to a specific folder.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
count = 'count_example' # str | Number of records to return in the cache. (optional)
folder = 'folder_example' # str | The query value can be a folder name or folder ID. The response will only return templates in the specified folder. (optional)
folder_ids = 'folder_ids_example' # str | A comma separated list of folder ID GUIDs. (optional)
folder_types = 'folder_types_example' # str |  (optional)
from_date = 'from_date_example' # str | Start of the search date range. Only returns templates created on or after this date/time. If no value is specified, there is no limit on the earliest date created. (optional)
include = 'include_example' # str | A comma separated list of additional template attributes to include in the response. Valid values are: recipients, folders, documents, custom_fields, and notifications. (optional)
order = 'order_example' # str | Sets the direction order used to sort the list. Valid values are: -asc = ascending sort order (a to z)  -desc = descending sort order (z to a) (optional)
order_by = 'order_by_example' # str | Sets the file attribute used to sort the list. Valid values are:  -name: template name  -modified: date/time template was last modified.  -used: date/time the template was last used. (optional)
search_text = 'search_text_example' # str | The search text used to search the names of templates. (optional)
shared = 'shared_example' # str |  (optional)
shared_by_me = 'shared_by_me_example' # str | If true, the response only includes templates shared by the user. If false, the response only returns template not shared by the user. If not specified, the response is not affected. (optional)
start_position = 'start_position_example' # str | The starting index for the first template shown in the response. This must be greater than or equal to 0 (zero). (optional)
to_date = 'to_date_example' # str | End of the search date range. Only returns templates created up to this date/time. If no value is provided, this defaults to the current date. (optional)
used_from_date = 'used_from_date_example' # str | Start of the search date range. Only returns templates used or edited on or after this date/time. If no value is specified, there is no limit on the earliest date used. (optional)
used_to_date = 'used_to_date_example' # str | End of the search date range. Only returns templates used or edited up to this date/time. If no value is provided, this defaults to the current date. (optional)
user_filter = 'user_filter_example' # str | Sets if the templates shown in the response Valid values are:  -owned_by_me: only shows templates the user owns.  -shared_with_me: only shows templates that are shared with the user.  -all: shows all templates owned or shared with the user. (optional)
user_id = 'user_id_example' # str |  (optional)

try: 
    # Gets the definition of a template.
    api_response = api_instance.list_templates(account_id, count=count, folder=folder, folder_ids=folder_ids, folder_types=folder_types, from_date=from_date, include=include, order=order, order_by=order_by, search_text=search_text, shared=shared, shared_by_me=shared_by_me, start_position=start_position, to_date=to_date, used_from_date=used_from_date, used_to_date=used_to_date, user_filter=user_filter, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **count** | **str**| Number of records to return in the cache. | [optional] 
 **folder** | **str**| The query value can be a folder name or folder ID. The response will only return templates in the specified folder. | [optional] 
 **folder_ids** | **str**| A comma separated list of folder ID GUIDs. | [optional] 
 **folder_types** | **str**|  | [optional] 
 **from_date** | **str**| Start of the search date range. Only returns templates created on or after this date/time. If no value is specified, there is no limit on the earliest date created. | [optional] 
 **include** | **str**| A comma separated list of additional template attributes to include in the response. Valid values are: recipients, folders, documents, custom_fields, and notifications. | [optional] 
 **order** | **str**| Sets the direction order used to sort the list. Valid values are: -asc &#x3D; ascending sort order (a to z)  -desc &#x3D; descending sort order (z to a) | [optional] 
 **order_by** | **str**| Sets the file attribute used to sort the list. Valid values are:  -name: template name  -modified: date/time template was last modified.  -used: date/time the template was last used. | [optional] 
 **search_text** | **str**| The search text used to search the names of templates. | [optional] 
 **shared** | **str**|  | [optional] 
 **shared_by_me** | **str**| If true, the response only includes templates shared by the user. If false, the response only returns template not shared by the user. If not specified, the response is not affected. | [optional] 
 **start_position** | **str**| The starting index for the first template shown in the response. This must be greater than or equal to 0 (zero). | [optional] 
 **to_date** | **str**| End of the search date range. Only returns templates created up to this date/time. If no value is provided, this defaults to the current date. | [optional] 
 **used_from_date** | **str**| Start of the search date range. Only returns templates used or edited on or after this date/time. If no value is specified, there is no limit on the earliest date used. | [optional] 
 **used_to_date** | **str**| End of the search date range. Only returns templates used or edited up to this date/time. If no value is provided, this defaults to the current date. | [optional] 
 **user_filter** | **str**| Sets if the templates shown in the response Valid values are:  -owned_by_me: only shows templates the user owns.  -shared_with_me: only shows templates that are shared with the user.  -all: shows all templates owned or shared with the user. | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**EnvelopeTemplateResults**](EnvelopeTemplateResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_document_page**
> rotate_document_page(account_id, document_id, page_number, template_id, page_request=page_request)

Rotates page image from a template for display.

Rotates page image from a template for display. The page image can be rotated to the left or right.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
page_number = 'page_number_example' # str | The page number being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
page_request = docusign.PageRequest() # PageRequest |  (optional)

try: 
    # Rotates page image from a template for display.
    api_instance.rotate_document_page(account_id, document_id, page_number, template_id, page_request=page_request)
except ApiException as e:
    print("Exception when calling TemplatesApi->rotate_document_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **page_number** | **str**| The page number being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **page_request** | [**PageRequest**](PageRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> TemplateUpdateSummary update(account_id, template_id, envelope_template=envelope_template)

Updates an existing template.

Updates an existing template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
envelope_template = docusign.EnvelopeTemplate() # EnvelopeTemplate |  (optional)

try: 
    # Updates an existing template.
    api_response = api_instance.update(account_id, template_id, envelope_template=envelope_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **envelope_template** | [**EnvelopeTemplate**](EnvelopeTemplate.md)|  | [optional] 

### Return type

[**TemplateUpdateSummary**](TemplateUpdateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bulk_recipients**
> BulkRecipientsSummaryResponse update_bulk_recipients(account_id, recipient_id, template_id, bulk_recipients_request=bulk_recipients_request)

Adds or replaces the bulk recipients list in a template.

Updates the bulk recipients in a template using a file upload. The Content-Type supported for uploading a bulk recipient file is CSV (text/csv).  The REST API does not support modifying individual rows or values in the bulk recipients file. It only allows the entire file to be added or replaced with a new file.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
bulk_recipients_request = docusign.BulkRecipientsRequest() # BulkRecipientsRequest |  (optional)

try: 
    # Adds or replaces the bulk recipients list in a template.
    api_response = api_instance.update_bulk_recipients(account_id, recipient_id, template_id, bulk_recipients_request=bulk_recipients_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_bulk_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **bulk_recipients_request** | [**BulkRecipientsRequest**](BulkRecipientsRequest.md)|  | [optional] 

### Return type

[**BulkRecipientsSummaryResponse**](BulkRecipientsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_fields**
> CustomFields update_custom_fields(account_id, template_id, template_custom_fields=template_custom_fields)

Updates envelope custom fields in a template.

Updates the custom fields in a template.  Each custom field used in a template must have a unique name.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_custom_fields = docusign.TemplateCustomFields() # TemplateCustomFields |  (optional)

try: 
    # Updates envelope custom fields in a template.
    api_response = api_instance.update_custom_fields(account_id, template_id, template_custom_fields=template_custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_custom_fields** | [**TemplateCustomFields**](TemplateCustomFields.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> EnvelopeDocument update_document(account_id, document_id, template_id, apply_document_fields=apply_document_fields, is_envelope_definition=is_envelope_definition, envelope_definition=envelope_definition)

Adds a document to a template document.

Adds the specified document to an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
apply_document_fields = 'apply_document_fields_example' # str |  (optional)
is_envelope_definition = 'is_envelope_definition_example' # str |  (optional)
envelope_definition = docusign.EnvelopeDefinition() # EnvelopeDefinition |  (optional)

try: 
    # Adds a document to a template document.
    api_response = api_instance.update_document(account_id, document_id, template_id, apply_document_fields=apply_document_fields, is_envelope_definition=is_envelope_definition, envelope_definition=envelope_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **apply_document_fields** | **str**|  | [optional] 
 **is_envelope_definition** | **str**|  | [optional] 
 **envelope_definition** | [**EnvelopeDefinition**](EnvelopeDefinition.md)|  | [optional] 

### Return type

[**EnvelopeDocument**](EnvelopeDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_fields**
> DocumentFieldsInformation update_document_fields(account_id, document_id, template_id, document_fields_information=document_fields_information)

Updates existing custom document fields in an existing template document.

Updates existing custom document fields in an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
document_fields_information = docusign.DocumentFieldsInformation() # DocumentFieldsInformation |  (optional)

try: 
    # Updates existing custom document fields in an existing template document.
    api_response = api_instance.update_document_fields(account_id, document_id, template_id, document_fields_information=document_fields_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **document_fields_information** | [**DocumentFieldsInformation**](DocumentFieldsInformation.md)|  | [optional] 

### Return type

[**DocumentFieldsInformation**](DocumentFieldsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_documents**
> TemplateDocumentsResult update_documents(account_id, template_id, apply_document_fields=apply_document_fields, envelope_definition=envelope_definition)

Adds documents to a template document.

Adds one or more documents to an existing template document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
apply_document_fields = 'apply_document_fields_example' # str |  (optional)
envelope_definition = docusign.EnvelopeDefinition() # EnvelopeDefinition |  (optional)

try: 
    # Adds documents to a template document.
    api_response = api_instance.update_documents(account_id, template_id, apply_document_fields=apply_document_fields, envelope_definition=envelope_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **apply_document_fields** | **str**|  | [optional] 
 **envelope_definition** | [**EnvelopeDefinition**](EnvelopeDefinition.md)|  | [optional] 

### Return type

[**TemplateDocumentsResult**](TemplateDocumentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_share**
> GroupInformation update_group_share(account_id, template_id, template_part, group_information=group_information)

Shares a template with a group

Shares a template with the specified members group.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_part = 'template_part_example' # str | Currently, the only defined part is **groups**.
group_information = docusign.GroupInformation() # GroupInformation |  (optional)

try: 
    # Shares a template with a group
    api_response = api_instance.update_group_share(account_id, template_id, template_part, group_information=group_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_group_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_part** | **str**| Currently, the only defined part is **groups**. | 
 **group_information** | [**GroupInformation**](GroupInformation.md)|  | [optional] 

### Return type

[**GroupInformation**](GroupInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lock**
> LockInformation update_lock(account_id, template_id, lock_request=lock_request)

Updates a template lock.

Updates the lock duration time or update the `lockedByApp` property information for the specified template. The user and integrator key must match the user specified by the `lockByUser` property and integrator key information and the `X-DocuSign-Edit` header must be included or an error will be generated.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
lock_request = docusign.LockRequest() # LockRequest |  (optional)

try: 
    # Updates a template lock.
    api_response = api_instance.update_lock(account_id, template_id, lock_request=lock_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **lock_request** | [**LockRequest**](LockRequest.md)|  | [optional] 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_settings**
> Notification update_notification_settings(account_id, template_id, template_notification_request=template_notification_request)

Updates the notification  structure for an existing template.

Updates the notification structure for an existing template. Use this endpoint to set reminder and expiration notifications.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_notification_request = docusign.TemplateNotificationRequest() # TemplateNotificationRequest |  (optional)

try: 
    # Updates the notification  structure for an existing template.
    api_response = api_instance.update_notification_settings(account_id, template_id, template_notification_request=template_notification_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_notification_request** | [**TemplateNotificationRequest**](TemplateNotificationRequest.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipients**
> RecipientsUpdateSummary update_recipients(account_id, template_id, resend_envelope=resend_envelope, template_recipients=template_recipients)

Updates recipients in a template.

Updates recipients in a template.   You can edit the following properties: `email`, `userName`, `routingOrder`, `faxNumber`, `deliveryMethod`, `accessCode`, and `requireIdLookup`.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
resend_envelope = 'resend_envelope_example' # str |  (optional)
template_recipients = docusign.TemplateRecipients() # TemplateRecipients |  (optional)

try: 
    # Updates recipients in a template.
    api_response = api_instance.update_recipients(account_id, template_id, resend_envelope=resend_envelope, template_recipients=template_recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **resend_envelope** | **str**|  | [optional] 
 **template_recipients** | [**TemplateRecipients**](TemplateRecipients.md)|  | [optional] 

### Return type

[**RecipientsUpdateSummary**](RecipientsUpdateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tabs**
> Tabs update_tabs(account_id, recipient_id, template_id, template_tabs=template_tabs)

Updates the tabs for a recipient.

Updates one or more tabs for a recipient in a template.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.TemplatesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_tabs = docusign.TemplateTabs() # TemplateTabs |  (optional)

try: 
    # Updates the tabs for a recipient.
    api_response = api_instance.update_tabs(account_id, recipient_id, template_id, template_tabs=template_tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_tabs** | [**TemplateTabs**](TemplateTabs.md)|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

