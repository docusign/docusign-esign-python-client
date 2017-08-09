# docusign.EnvelopesApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_template**](EnvelopesApi.md#apply_template) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/templates | Adds templates to an envelope.
[**apply_template_to_document**](EnvelopesApi.md#apply_template_to_document) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/templates | Adds templates to a document in an  envelope.
[**create_chunked_upload**](EnvelopesApi.md#create_chunked_upload) | **POST** /v2/accounts/{accountId}/chunked_uploads | Initiate a new ChunkedUpload.
[**create_console_view**](EnvelopesApi.md#create_console_view) | **POST** /v2/accounts/{accountId}/views/console | Returns a URL to the authentication view UI.
[**create_correct_view**](EnvelopesApi.md#create_correct_view) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/views/correct | Returns a URL to the envelope correction UI.
[**create_custom_fields**](EnvelopesApi.md#create_custom_fields) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/custom_fields | Updates envelope custom fields for an envelope.
[**create_document_fields**](EnvelopesApi.md#create_document_fields) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/fields | Creates custom document fields in an existing envelope document.
[**create_edit_view**](EnvelopesApi.md#create_edit_view) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/views/edit | Returns a URL to the edit view UI.
[**create_email_settings**](EnvelopesApi.md#create_email_settings) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/email_settings | Adds email setting overrides to an envelope.
[**create_envelope**](EnvelopesApi.md#create_envelope) | **POST** /v2/accounts/{accountId}/envelopes | Creates an envelope.
[**create_lock**](EnvelopesApi.md#create_lock) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/lock | Lock an envelope.
[**create_recipient**](EnvelopesApi.md#create_recipient) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients | Adds one or more recipients to an envelope.
[**create_recipient_view**](EnvelopesApi.md#create_recipient_view) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/views/recipient | Returns a URL to the recipient view UI.
[**create_sender_view**](EnvelopesApi.md#create_sender_view) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/views/sender | Returns a URL to the sender view UI.
[**create_tabs**](EnvelopesApi.md#create_tabs) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs | Adds tabs for a recipient.
[**create_view_link**](EnvelopesApi.md#create_view_link) | **POST** /v2/accounts/{accountId}/envelopes/{envelopeId}/views/viewlink | Reserved: Returns a URL to the secure link view UI.
[**delete_attachments**](EnvelopesApi.md#delete_attachments) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/attachments | Delete one or more attachments from a DRAFT envelope.
[**delete_chunked_upload**](EnvelopesApi.md#delete_chunked_upload) | **DELETE** /v2/accounts/{accountId}/chunked_uploads/{chunkedUploadId} | Delete an existing ChunkedUpload.
[**delete_custom_fields**](EnvelopesApi.md#delete_custom_fields) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/custom_fields | Deletes envelope custom fields for draft and in-process envelopes.
[**delete_document_fields**](EnvelopesApi.md#delete_document_fields) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/fields | Deletes custom document fields from an existing envelope document.
[**delete_document_page**](EnvelopesApi.md#delete_document_page) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber} | Deletes a page from a document in an envelope.
[**delete_documents**](EnvelopesApi.md#delete_documents) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents | Deletes documents from a draft envelope.
[**delete_email_settings**](EnvelopesApi.md#delete_email_settings) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/email_settings | Deletes the email setting overrides for an envelope.
[**delete_lock**](EnvelopesApi.md#delete_lock) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/lock | Deletes an envelope lock.
[**delete_recipient**](EnvelopesApi.md#delete_recipient) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId} | Deletes a recipient from an envelope.
[**delete_recipients**](EnvelopesApi.md#delete_recipients) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients | Deletes recipients from an envelope.
[**delete_tabs**](EnvelopesApi.md#delete_tabs) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs | Deletes the tabs associated with a recipient.
[**delete_templates_from_document**](EnvelopesApi.md#delete_templates_from_document) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/templates/{templateId} | Deletes a template from a document in an existing envelope.
[**delete_view_link**](EnvelopesApi.md#delete_view_link) | **DELETE** /v2/accounts/{accountId}/envelopes/{envelopeId}/views/viewlink | Reserved: Expires a secure view link.
[**get_attachment**](EnvelopesApi.md#get_attachment) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/attachments/{attachmentId} | Retrieves an attachment from the envelope.
[**get_attachments**](EnvelopesApi.md#get_attachments) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/attachments | Returns a list of attachments associated with the specified envelope
[**get_chunked_upload**](EnvelopesApi.md#get_chunked_upload) | **GET** /v2/accounts/{accountId}/chunked_uploads/{chunkedUploadId} | Retrieves the current metadata of a ChunkedUpload.
[**get_consumer_disclosure**](EnvelopesApi.md#get_consumer_disclosure) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/consumer_disclosure/{langCode} | Reserved: Gets the Electronic Record and Signature Disclosure associated with the account.
[**get_consumer_disclosure_default**](EnvelopesApi.md#get_consumer_disclosure_default) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/consumer_disclosure | Gets the Electronic Record and Signature Disclosure associated with the account.
[**get_document**](EnvelopesApi.md#get_document) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId} | Gets a document from an envelope.
[**get_document_page_image**](EnvelopesApi.md#get_document_page_image) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber}/page_image | Gets a page image from an envelope for display.
[**get_document_tabs**](EnvelopesApi.md#get_document_tabs) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/tabs | Returns tabs on the document.
[**get_email_settings**](EnvelopesApi.md#get_email_settings) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/email_settings | Gets the email setting overrides for an envelope.
[**get_envelope**](EnvelopesApi.md#get_envelope) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId} | Gets the status of a envelope.
[**get_form_data**](EnvelopesApi.md#get_form_data) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/form_data | Returns envelope form data for an existing envelope.
[**get_lock**](EnvelopesApi.md#get_lock) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/lock | Gets envelope lock information.
[**get_notification_settings**](EnvelopesApi.md#get_notification_settings) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/notification | Gets envelope notification information.
[**get_page_tabs**](EnvelopesApi.md#get_page_tabs) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber}/tabs | Returns tabs on the specified page.
[**get_pages**](EnvelopesApi.md#get_pages) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages | Returns document page image(s) based on input.
[**get_recipient_document_visibility**](EnvelopesApi.md#get_recipient_document_visibility) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/document_visibility | Returns document visibility for the recipients
[**get_recipient_initials_image**](EnvelopesApi.md#get_recipient_initials_image) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/initials_image | Gets the initials image for a user.
[**get_recipient_signature**](EnvelopesApi.md#get_recipient_signature) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature | Gets signature information for a signer or sign-in-person recipient.
[**get_recipient_signature_image**](EnvelopesApi.md#get_recipient_signature_image) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature_image | Retrieve signature image information for a signer/sign-in-person recipient.
[**get_template_recipient_document_visibility**](EnvelopesApi.md#get_template_recipient_document_visibility) | **GET** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/document_visibility | Returns document visibility for the recipients
[**list_audit_events**](EnvelopesApi.md#list_audit_events) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/audit_events | Gets the envelope audit events for an envelope.
[**list_custom_fields**](EnvelopesApi.md#list_custom_fields) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/custom_fields | Gets the custom field information for the specified envelope.
[**list_document_fields**](EnvelopesApi.md#list_document_fields) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/fields | Gets the custom document fields from an  existing envelope document.
[**list_documents**](EnvelopesApi.md#list_documents) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents | Gets a list of envelope documents.
[**list_recipients**](EnvelopesApi.md#list_recipients) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients | Gets the status of recipients for an envelope.
[**list_status**](EnvelopesApi.md#list_status) | **PUT** /v2/accounts/{accountId}/envelopes/status | Gets the envelope status for the specified envelopes.
[**list_status_changes**](EnvelopesApi.md#list_status_changes) | **GET** /v2/accounts/{accountId}/envelopes | Gets status changes for one or more envelopes.
[**list_tabs**](EnvelopesApi.md#list_tabs) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs | Gets the tabs information for a signer or sign-in-person recipient in an envelope.
[**list_templates**](EnvelopesApi.md#list_templates) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/templates | Get List of Templates used in an Envelope
[**list_templates_for_document**](EnvelopesApi.md#list_templates_for_document) | **GET** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/templates | Gets the templates associated with a document in an existing envelope.
[**put_attachment**](EnvelopesApi.md#put_attachment) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/attachments/{attachmentId} | Add an attachment to a DRAFT or IN-PROCESS envelope.
[**put_attachments**](EnvelopesApi.md#put_attachments) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/attachments | Add one or more attachments to a DRAFT or IN-PROCESS envelope.
[**rotate_document_page**](EnvelopesApi.md#rotate_document_page) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber}/page_image | Rotates page image from an envelope for display.
[**update**](EnvelopesApi.md#update) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId} | Send Draft Envelope/Void Envelope/Move/Purge Envelope/Modify draft
[**update_chunked_upload**](EnvelopesApi.md#update_chunked_upload) | **PUT** /v2/accounts/{accountId}/chunked_uploads/{chunkedUploadId} | Integrity-Check and Commit a ChunkedUpload, readying it for use elsewhere.
[**update_chunked_upload_part**](EnvelopesApi.md#update_chunked_upload_part) | **PUT** /v2/accounts/{accountId}/chunked_uploads/{chunkedUploadId}/{chunkedUploadPartSeq} | Add a chunk, a chunk &#39;part&#39;, to an existing ChunkedUpload.
[**update_custom_fields**](EnvelopesApi.md#update_custom_fields) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/custom_fields | Updates envelope custom fields in an envelope.
[**update_document**](EnvelopesApi.md#update_document) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId} | Adds a document to an existing draft envelope.
[**update_document_fields**](EnvelopesApi.md#update_document_fields) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/fields | Updates existing custom document fields in an existing envelope document.
[**update_documents**](EnvelopesApi.md#update_documents) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/documents | Adds one or more documents to an existing envelope document.
[**update_email_settings**](EnvelopesApi.md#update_email_settings) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/email_settings | Updates the email setting overrides for an envelope.
[**update_lock**](EnvelopesApi.md#update_lock) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/lock | Updates an envelope lock.
[**update_notification_settings**](EnvelopesApi.md#update_notification_settings) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/notification | Sets envelope notification (Reminders/Expirations) structure for an existing envelope.
[**update_recipient_document_visibility**](EnvelopesApi.md#update_recipient_document_visibility) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/document_visibility | Updates document visibility for the recipients
[**update_recipient_initials_image**](EnvelopesApi.md#update_recipient_initials_image) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/initials_image | Sets the initials image for an accountless signer.
[**update_recipient_signature_image**](EnvelopesApi.md#update_recipient_signature_image) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature_image | Sets the signature image for an accountless signer.
[**update_recipients**](EnvelopesApi.md#update_recipients) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients | Updates recipients in a draft envelope or corrects recipient information for an in process envelope.
[**update_recipients_document_visibility**](EnvelopesApi.md#update_recipients_document_visibility) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/document_visibility | Updates document visibility for the recipients
[**update_tabs**](EnvelopesApi.md#update_tabs) | **PUT** /v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs | Updates the tabs for a recipient.  
[**update_template_recipient_document_visibility**](EnvelopesApi.md#update_template_recipient_document_visibility) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/document_visibility | Updates document visibility for the recipients
[**update_template_recipients_document_visibility**](EnvelopesApi.md#update_template_recipients_document_visibility) | **PUT** /v2/accounts/{accountId}/templates/{templateId}/recipients/document_visibility | Updates document visibility for the recipients


# **apply_template**
> DocumentTemplateList apply_template(account_id, envelope_id, document_template_list=document_template_list)

Adds templates to an envelope.

Adds templates to the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
document_template_list = docusign.DocumentTemplateList() # DocumentTemplateList |  (optional)

try: 
    # Adds templates to an envelope.
    api_response = api_instance.apply_template(account_id, envelope_id, document_template_list=document_template_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->apply_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **document_template_list** | [**DocumentTemplateList**](DocumentTemplateList.md)|  | [optional] 

### Return type

[**DocumentTemplateList**](DocumentTemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_template_to_document**
> DocumentTemplateList apply_template_to_document(account_id, document_id, envelope_id, document_template_list=document_template_list)

Adds templates to a document in an  envelope.

Adds templates to a document in the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
document_template_list = docusign.DocumentTemplateList() # DocumentTemplateList |  (optional)

try: 
    # Adds templates to a document in an  envelope.
    api_response = api_instance.apply_template_to_document(account_id, document_id, envelope_id, document_template_list=document_template_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->apply_template_to_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **document_template_list** | [**DocumentTemplateList**](DocumentTemplateList.md)|  | [optional] 

### Return type

[**DocumentTemplateList**](DocumentTemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chunked_upload**
> ChunkedUploadResponse create_chunked_upload(account_id, chunked_upload_request=chunked_upload_request)

Initiate a new ChunkedUpload.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
chunked_upload_request = docusign.ChunkedUploadRequest() # ChunkedUploadRequest |  (optional)

try: 
    # Initiate a new ChunkedUpload.
    api_response = api_instance.create_chunked_upload(account_id, chunked_upload_request=chunked_upload_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_chunked_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **chunked_upload_request** | [**ChunkedUploadRequest**](ChunkedUploadRequest.md)|  | [optional] 

### Return type

[**ChunkedUploadResponse**](ChunkedUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_console_view**
> ViewUrl create_console_view(account_id, console_view_request=console_view_request)

Returns a URL to the authentication view UI.

Returns a URL that allows you to embed the authentication view of the DocuSign UI in your applications.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
console_view_request = docusign.ConsoleViewRequest() # ConsoleViewRequest |  (optional)

try: 
    # Returns a URL to the authentication view UI.
    api_response = api_instance.create_console_view(account_id, console_view_request=console_view_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_console_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **console_view_request** | [**ConsoleViewRequest**](ConsoleViewRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_correct_view**
> ViewUrl create_correct_view(account_id, envelope_id, correct_view_request=correct_view_request)

Returns a URL to the envelope correction UI.

Returns a URL that allows you to embed the envelope correction view of the DocuSign UI in your applications.  Important: iFrames should not be used for embedded operations on mobile devices due to screen space issues. For iOS devices DocuSign recommends using a WebView. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
correct_view_request = docusign.CorrectViewRequest() # CorrectViewRequest |  (optional)

try: 
    # Returns a URL to the envelope correction UI.
    api_response = api_instance.create_correct_view(account_id, envelope_id, correct_view_request=correct_view_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_correct_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **correct_view_request** | [**CorrectViewRequest**](CorrectViewRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_fields**
> CustomFields create_custom_fields(account_id, envelope_id, custom_fields=custom_fields)

Updates envelope custom fields for an envelope.

Updates the envelope custom fields for draft and in-process envelopes.  Each custom field used in an envelope must have a unique name.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
custom_fields = docusign.CustomFields() # CustomFields |  (optional)

try: 
    # Updates envelope custom fields for an envelope.
    api_response = api_instance.create_custom_fields(account_id, envelope_id, custom_fields=custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **custom_fields** | [**CustomFields**](CustomFields.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_fields**
> DocumentFieldsInformation create_document_fields(account_id, document_id, envelope_id, document_fields_information=document_fields_information)

Creates custom document fields in an existing envelope document.

Creates custom document fields in an existing envelope document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
document_fields_information = docusign.DocumentFieldsInformation() # DocumentFieldsInformation |  (optional)

try: 
    # Creates custom document fields in an existing envelope document.
    api_response = api_instance.create_document_fields(account_id, document_id, envelope_id, document_fields_information=document_fields_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
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
> ViewUrl create_edit_view(account_id, envelope_id, return_url_request=return_url_request)

Returns a URL to the edit view UI.

Returns a URL that allows you to embed the edit view of the DocuSign UI in your applications. This is a one-time use login token that allows the user to be placed into the DocuSign editing view.   Upon sending completion, the user is returned to the return URL provided by the API application.  Important: iFrames should not be used for embedded operations on mobile devices due to screen space issues. For iOS devices DocuSign recommends using a WebView. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
return_url_request = docusign.ReturnUrlRequest() # ReturnUrlRequest |  (optional)

try: 
    # Returns a URL to the edit view UI.
    api_response = api_instance.create_edit_view(account_id, envelope_id, return_url_request=return_url_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_edit_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **return_url_request** | [**ReturnUrlRequest**](ReturnUrlRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_settings**
> EmailSettings create_email_settings(account_id, envelope_id, email_settings=email_settings)

Adds email setting overrides to an envelope.

Adds email override settings, changing the email address to reply to an email address, name, or the BCC for email archive information, for the envelope. Note that adding email settings will only affect email communications that occur after the addition was made.  ### Important: The BCC Email address feature is designed to provide a copy of all email communications for external archiving purposes. DocuSign recommends that envelopes sent using the BCC for Email Archive feature, including the BCC Email Override option, include additional signer authentication options. To send a copy of the envelope to a recipient who does not need to sign, use a Carbon Copies or Certified Deliveries Recipient Type.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
email_settings = docusign.EmailSettings() # EmailSettings |  (optional)

try: 
    # Adds email setting overrides to an envelope.
    api_response = api_instance.create_email_settings(account_id, envelope_id, email_settings=email_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **email_settings** | [**EmailSettings**](EmailSettings.md)|  | [optional] 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_envelope**
> EnvelopeSummary create_envelope(account_id, cdse_mode=cdse_mode, completed_documents_only=completed_documents_only, merge_roles_on_draft=merge_roles_on_draft, envelope_definition=envelope_definition)

Creates an envelope.

Creates an envelope.   Using this function you can: * Create an envelope and send it. * Create an envelope from an existing template and send it.  In either case, you can choose to save the envelope as a draft envelope instead of sending it by setting the request’s `status` property to `created` instead of `sent`.  ## Sending Envelopes  Documents can be included with the Envelopes::create call itself or a template can include documents. Documents can be added by using a multi-part/form request or by using the `documentBase64` field of the [`document` object](#/definitions/document)  ### Recipient Types An [`envelopeDefinition` object](#/definitions/envelopeDefinition) is used as the method’s body. Envelope recipients can be defined in the envelope or in templates. The `envelopeDefinition` object’s `recipients` field is an [`EnvelopeRecipients` resource object](#/definitions/EnvelopeRecipients). It includes arrays of the seven types of recipients defined by DocuSign:  Recipient type | Object definition -------------- | ----------------- agent (can add name and email information for later recipients/signers) | [`agent`](#/definitions/agent) carbon copy (receives a copy of the documents) | [`carbonCopy`](#/definitions/carbonCopy) certified delivery  (receives a copy of the documents and must acknowledge receipt) | [`certifiedDelivery`](#/definitions/certifiedDelivery) editor (can change recipients and document fields for later recipients/signers) | [`editor`](#/definitions/editor) in-person signer (“hosts” someone who signs in-person) | [`inPersonSigner`](#/definitions/inPersonSigner) intermediary (can add name and email information for some later recipients/signers.) | [`intermediary`](#/definitions/intermediary) signer (signs and/or updates document fields) | [`signer`](#/definitions/signer)  Additional information about the different types of recipients is available from the [`EnvelopeRecipients` resource page](../../EnvelopeRecipients) and from the [Developer Center](https://www.docusign.com/developer-center/explore/features/recipients)  ### Tabs Tabs (also referred to as `tags` and as `fields` in the web sending user interface), can be defined in the `envelopeDefinition`, in templates, by transforming PDF Form Fields, or by using Composite Templates (see below).  Defining tabs: the `inPersonSigner`, and `signer` recipient objects include a `tabs` field. It is an [`EnvelopeTabs` resource object](#/definitions/EnvelopeTabs). It includes arrays of the 24 different tab types available. See the [`EnvelopeTabs` resource](../../EnvelopeTabs) for more information.  ## Using Templates Envelopes use specific people or groups as recipients. Templates can specify a role, eg `account_manager.` When a template is used in an envelope, the roles must be replaced with specific people or groups.  When you create an envelope using a `templateId`, the different recipient type objects within the [`EnvelopeRecipients` object](#/definitions/EnvelopeRecipients) are used to assign recipients to the template’s roles via the `roleName` property. The recipient objects can also override settings that were specified in the template, and set values for tab fields that were defined in the template.  ### Message Lock When a template is added or applied to an envelope and the template has a locked email subject and message, that subject and message are used for the envelope and cannot be changed even if another locked template is subsequently added or applied to the envelope. The field `messageLock` is used to lock the email subject and message.  If an email subject or message is entered before adding or applying a template with `messageLock` **true**, the email subject and message is overwritten with the locked email subject and message from the template.  ## Envelope Status The status of sent envelopes can be determined through the DocuSign webhook system or by polling. Webhooks are highly recommended: they provide your application with the quickest updates when an envelope’s status changes. DocuSign limits polling to once every 15 minutes or less frequently.  When a webhook is used, DocuSign calls your application, via the URL you provide, with a notification XML message.   See the [Webhook recipe](https://www.docusign.com/developer-center/recipes/webhook-status) for examples and live demos of using webhooks.  ## Webhook Options The two webhook options, *eventNotification* and *Connect* use the same notification mechanism and message formats. eventNotification is used to create a webhook for a specific envelope sent via the API. Connect webhooks can be used for any envelope sent from an account, from any user, from any client.   ### eventNotification Webhooks The Envelopes::create method includes an optional [eventNotification object](#definition-eventNotification) that adds a webhook to the envelope. eventNotification webhooks are available for all DocuSign accounts with API access.  ### Connect Webhooks Connect can be used to create a webhook for all envelopes sent by all users in an account, either through the API or via other DocuSign clients (web, mobile, etc). Connect configurations are independent of specific envelopes. A Connect configuration includes a filter that may be used to limit the webhook to specific users, envelope statuses, etc.   Connect configurations may be created and managed using the [ConnectConfigurations resource](../../Connect/ConnectConfigurations). Configurations can also be created and managed from the Administration tool accessed by selecting “Go to Admin” from the menu next to your picture on the DocuSign web app. See the Integrations/Connect section of the Admin tool. For repeatability, and to minimize support questions, creating Connect configurations via the API is recommended, especially for ISVs.  Connect is available for some DocuSign account types. Please contact DocuSign Sales for more information.  ## Composite Templates  The Composite Templates feature, like [compositing in film production](https://en.wikipedia.org/wiki/Compositing), enables you to *overlay* document, recipient, and tab definitions from multiple sources, including PDF Form Field definitions, templates defined on the server, and more.  Each Composite Template consists of optional elements: server templates, inline templates, PDF Metadata templates, and documents.  * The Composite Template ID is an optional element used to identify the composite template. It is used as a reference when adding document object information via a multi-part HTTP message. If used, the document content-disposition must include the `compositeTemplateId` to which the document should be added. If `compositeTemplateId` is not specified in the content-disposition, the document is applied based on the `documentId` only. If no document object is specified, the composite template inherits the first document.  * Server Templates are server-side templates stored on the DocuSign platform. If supplied, they are overlaid into the envelope in the order of their Sequence value.  * Inline Templates provide a container to add documents, recipients, tabs, and custom fields. If inline templates are supplied, they are overlaid into the envelope in the order of their Sequence value.  * Document objects are optional structures that provide a container to pass in a document or form. If this object is not included, the composite template inherits the *first* document it finds from a server template or inline template, starting with the lowest sequence value.  PDF Form objects are only transformed from the document object. DocuSign does not derive PDF form properties from server templates or inline templates. To instruct DocuSign to transform fields from the PDF form, set `transformPdfFields` to \"true\" for the document. See the Transform PDF Fields section for more information about process.  * PDF Metadata Templates provide a container to embed design-time template information into a PDF document. DocuSign uses this information when processing the Envelope. This convention allows the document to carry the signing instructions with it, so that less information needs to be provided at run-time through an inline template or synchronized with an external structure like a server template. PDF Metadata templates are stored in the Metadata layer of a PDF in accordance with Acrobat's XMP specification. DocuSign will only find PDF Metadata templates inside documents passed in the Document object (see below). If supplied, the PDF metadata template will be overlaid into the envelope in the order of its Sequence value.  ### Compositing the definitions Each Composite Template adds a new document and templates overlay into the envelope. For each Composite Template these rules are applied:  * Templates are overlaid in the order of their Sequence value. * If Document is not passed into the Composite Template’s `document` field, the *first* template’s document (based on the template’s Sequence value) is used. * Last in wins in all cases except for the document (i.e. envelope information, recipient information, secure field information). There is no special casing.  For example, if you want higher security on a tab, then that needs to be specified in a later template (by sequence number) then where the tab is included. If you want higher security on a role recipient, then it needs to be in a later template then where that role recipient is specified.  * Recipient matching is based on Recipient Role and Routing Order. If there are matches, the recipient information is merged together. A final pass is done on all Composite Templates, after all template overlays have been applied, to collapse recipients with the same email, username and routing order. This prevents having the same recipients at the same routing order.  * If you specify in a template that a recipient is locked, once that recipient is overlaid the recipient attributes can no longer be changed. The only items that can be changed for the recipient in this case are the email, username, access code and IDCheckInformationInput.  * Tab matching is based on Tab Labels, Tab Types and Documents. If a Tab Label matches but the Document is not supplied, the Tab is overlaid for all the Documents.  For example, if you have a simple inline template with only one tab in it with a label and a value, the Signature, Initial, Company, Envelope ID, User Name tabs will only be matched and collapsed if they fall in the exact same X and Y locations.  * roleName and tabLabel matching is case sensitive.  * The defaultRecipient field enables you to specify which recipient the generated tabs from a PDF form are mapped to. You can also set PDF form generated tabs to a recipient other than the DefaultRecipient by specifying the mapping of the tab label that is created to one of the template recipients.  * You can use tabLabel wild carding to map a series of tabs from the PDF form. To use this you must end a tab label with “\\*” and then the system matches tabs that start with the label.  * If no DefaultRecipient is specified, tabs must be explicitly mapped to recipients in order to be generated from the form. Unmapped form objects will not be generated into their DocuSign equivalents. (In the case of Signature/Initials, the tabs will be disregarded entirely; in the case of pdf text fields, the field data will be flattened on the Envelope document, but there will not be a corresponding DocuSign data tab.)  ### Including the Document Content for Composite Templates Document content can be supplied inline, using the `documentBase64` or can be included in a multi-part HTTP message.  If a multi-part message is used and there are multiple Composite Templates, the document content-disposition can include the `compositeTemplateId` to which the document should be added. Using the `compositeTemplateId` sets which documents are associated with particular composite templates. An example of this usage is:  ```    --5cd3320a-5aac-4453-b3a4-cbb52a4cba5d    Content-Type: application/pdf    Content-Disposition: file; filename=\"eula.pdf\"; documentId=1; compositeTemplateId=\"1\"    Content-Transfer-Encoding: base64 ```  ### PDF Form Field Transformation Only the following PDF Form FieldTypes will be transformed to DocuSign tabs: CheckBox, DateTime, ListBox, Numeric, Password, Radio, Signature, and Text  Field Properties that will be transformed: Read Only, Required, Max Length, Positions, and Initial Data.  When transforming a *PDF Form Digital Signature Field,* the following rules are used:  If the PDF Field Name Contains | Then the DocuSign Tab Will be ------- | -------- DocuSignSignHere or eSignSignHere | Signature DocuSignSignHereOptional or eSignSignHereOptional | Optional Signature DocuSignInitialHere or eSignInitialHere | Initials DocuSignInitialHereOptional or eSignInitialHereOptional | Optional Initials  Any other PDF Form Digital Signature Field will be transformed to a DocuSign Signature tab  When transforming *PDF Form Text Fields,* the following rules are used:  If the PDF Field Name Contains | Then the DocuSign Tab Will be ------- | -------- DocuSignSignHere or eSignSignHere | Signature DocuSignSignHereOptional or eSignSignHereOptional | Optional Signature DocuSignInitialHere or eSignInitialHere | Initials DocuSignInitialHereOptional or eSignInitialHereOptional | Optional Initials DocuSignEnvelopeID or eSignEnvelopeID | EnvelopeID DocuSignCompany or eSignCompany | Company DocuSignDateSigned or eSignDateSigned | Date Signed DocuSignTitle or eSignTitle | Title DocuSignFullName or eSignFullName |  Full Name DocuSignSignerAttachmentOptional or eSignSignerAttachmentOptional | Optional Signer Attachment  Any other PDF Form Text Field will be transformed to a DocuSign data (text) tab.  PDF Form Field Names that include “DocuSignIgnoreTransform” or “eSignIgnoreTransform” will not be transformed.  PDF Form Date fields will be transformed to Date Signed fields if their name includes DocuSignDateSigned or eSignDateSigned.  ## Template Email Subject Merge Fields This feature enables you to insert recipient name and email address merge fields into the email subject line when creating or sending from a template.  The merge fields, based on the recipient’s `roleName`, are added to the `emailSubject` when the template is created or when the template is used to create an envelope. After a template sender adds the name and email information for the recipient and sends the envelope, the recipient information is automatically merged into the appropriate fields in the email subject line.  Both the sender and the recipients will see the information in the email subject line for any emails associated with the template. This provides an easy way for senders to organize their envelope emails without having to open an envelope to check the recipient.  If merging the recipient information into the subject line causes the subject line to exceed 100 characters, then any characters over the 100 character limit are not included in the subject line. For cases where the recipient name or email is expected to be long, you should consider placing the merge field at the start of the email subject.  * To add a recipient’s name in the subject line add the following text in the `emailSubject` when creating the template or when sending an envelope from a template:     [[<roleName>_UserName]]     Example:     `\"emailSubject\":\"[[Signer 1_UserName]], Please sign this NDA\",`  * To add a recipient’s email address in the subject line add the following text in the emailSubject when creating the template or when sending an envelope from a template:     [[<roleName>_Email]]     Example:     `\"emailSubject\":\"[[Signer 1_Email]], Please sign this NDA\",`  In both cases the <roleName> is the recipient’s `roleName` in the template.  For cases where another recipient (such as an Agent, Editor, or Intermediary recipient) is entering the name and email information for the recipient included in the email subject, then [[<roleName>_UserName]] or [[<roleName>_Email]] is shown in the email subject.  ## Branding an envelope The following rules are used to determine the `brandId` used in an envelope:  * If a `brandId` is specified in the envelope/template and that brandId is available to the account, that brand is used in the envelope. * If more than one template is used in an envelope and more than one `brandId` is specified, the first `brandId` specified is used throughout the envelope. * In cases where no brand is specified and the sender belongs to a Group; if there is only one brand associated with the Group, then that brand is used in the envelope. Otherwise, the account’s default signing brand is used. * For envelopes that do not meet any of the previous criteria, the account’s default signing brand is used for the envelope.  ## BCC Email address feature  The BCC Email address feature is designed to provide a copy of all email communications for external archiving purposes. DocuSign recommends that envelopes sent using the BCC for Email Archive feature, including the BCC Email Override option, include additional signer authentication options. To send a copy of the envelope to a recipient who does not need to sign, don’t use the BCC Email field. Use a Carbon Copy or Certified Delivery Recipient type.  ## Merge Recipient Roles for Draft Envelopes When an envelope with multiple templates is sent, the recipients from the templates are merged according to the template roles, and empty recipients are removed. When creating an envelope with multiple templates, but not sending it (keeping it in a created state), duplicate recipients are not merged, which could cause leave duplicate recipients in the envelope.  To prevent this, the query parameter `merge_roles_on_draft` should be added when posting a draft envelope (status=created) with multiple templates. Doing this will merge template roles and remove empty recipients.  ###### Note: DocuSign recommends that the `merge_roles_on_draft` query parameter be used anytime you are creating an envelope with multiple templates and keeping it in draft (created) status.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
cdse_mode = 'cdse_mode_example' # str |  (optional)
completed_documents_only = 'completed_documents_only_example' # str | If set to true then we want to set the sourceEnvelopeId to indicate that this is a\"forward\" envelope action (optional)
merge_roles_on_draft = 'merge_roles_on_draft_example' # str | When set to **true**, merges template roles and remove empty recipients when you create an envelope with multiple templates. (optional)
envelope_definition = docusign.EnvelopeDefinition() # EnvelopeDefinition |  (optional)

try: 
    # Creates an envelope.
    api_response = api_instance.create_envelope(account_id, cdse_mode=cdse_mode, completed_documents_only=completed_documents_only, merge_roles_on_draft=merge_roles_on_draft, envelope_definition=envelope_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_envelope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **cdse_mode** | **str**|  | [optional] 
 **completed_documents_only** | **str**| If set to true then we want to set the sourceEnvelopeId to indicate that this is a\&quot;forward\&quot; envelope action | [optional] 
 **merge_roles_on_draft** | **str**| When set to **true**, merges template roles and remove empty recipients when you create an envelope with multiple templates. | [optional] 
 **envelope_definition** | [**EnvelopeDefinition**](EnvelopeDefinition.md)|  | [optional] 

### Return type

[**EnvelopeSummary**](EnvelopeSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lock**
> LockInformation create_lock(account_id, envelope_id, lock_request=lock_request)

Lock an envelope.

Locks the specified envelope, and sets the time until the lock expires, to prevent other users or recipients from accessing and changing the envelope.  ###### Note: Users must have envelope locking capability enabled to use this function (userSetting `canLockEnvelopes` must be  set to true for the user).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
lock_request = docusign.LockRequest() # LockRequest |  (optional)

try: 
    # Lock an envelope.
    api_response = api_instance.create_lock(account_id, envelope_id, lock_request=lock_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **lock_request** | [**LockRequest**](LockRequest.md)|  | [optional] 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recipient**
> Recipients create_recipient(account_id, envelope_id, resend_envelope=resend_envelope, recipients=recipients)

Adds one or more recipients to an envelope.

Adds one or more recipients to an envelope.  For an in process envelope, one that has been sent and has not been completed or voided, an email is sent to a new recipient when they are reached in the routing order. If the new recipient's routing order is before or the same as the envelope's next recipient, an email is only sent if the optional `resend_envelope` query string is set to **true**.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
resend_envelope = 'resend_envelope_example' # str | When set to **true**, resends the   envelope if the new recipient's routing order is before or the same as the envelope’s next recipient. (optional)
recipients = docusign.Recipients() # Recipients |  (optional)

try: 
    # Adds one or more recipients to an envelope.
    api_response = api_instance.create_recipient(account_id, envelope_id, resend_envelope=resend_envelope, recipients=recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **resend_envelope** | **str**| When set to **true**, resends the   envelope if the new recipient&#39;s routing order is before or the same as the envelope’s next recipient. | [optional] 
 **recipients** | [**Recipients**](Recipients.md)|  | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recipient_view**
> ViewUrl create_recipient_view(account_id, envelope_id, recipient_view_request=recipient_view_request)

Returns a URL to the recipient view UI.

Returns a URL that allows you to embed the recipient view of the DocuSign UI in your applications. This call cannot be used to view draft envelopes, since those envelopes have not been sent.   Important: iFrames should not be used for embedded operations on mobile devices due to screen space issues. For iOS devices DocuSign recommends using a WebView.   An entry is added into the Security Level section of the DocuSign Certificate of Completion that reflects the `securityDomain` and `authenticationMethod` properties used to verify the user identity.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_view_request = docusign.RecipientViewRequest() # RecipientViewRequest |  (optional)

try: 
    # Returns a URL to the recipient view UI.
    api_response = api_instance.create_recipient_view(account_id, envelope_id, recipient_view_request=recipient_view_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_recipient_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_view_request** | [**RecipientViewRequest**](RecipientViewRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sender_view**
> ViewUrl create_sender_view(account_id, envelope_id, return_url_request=return_url_request)

Returns a URL to the sender view UI.

Returns a URL that allows you to embed the sender view of the DocuSign UI in your applications. This is a one-time use login token that allows the user to be placed into the DocuSign sending view.   Upon sending completion, the user is returned to the return URL provided by the API application.  Important: iFrames should not be used for embedded operations on mobile devices due to screen space issues. For iOS devices DocuSign recommends using a WebView. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
return_url_request = docusign.ReturnUrlRequest() # ReturnUrlRequest |  (optional)

try: 
    # Returns a URL to the sender view UI.
    api_response = api_instance.create_sender_view(account_id, envelope_id, return_url_request=return_url_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_sender_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **return_url_request** | [**ReturnUrlRequest**](ReturnUrlRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tabs**
> Tabs create_tabs(account_id, envelope_id, recipient_id, tabs=tabs)

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
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
tabs = docusign.Tabs() # Tabs |  (optional)

try: 
    # Adds tabs for a recipient.
    api_response = api_instance.create_tabs(account_id, envelope_id, recipient_id, tabs=tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **tabs** | [**Tabs**](Tabs.md)|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_view_link**
> ViewUrl create_view_link(account_id, envelope_id, view_link_request=view_link_request)

Reserved: Returns a URL to the secure link view UI.

Reserved: Returns a URL that allows you to embed the secure link view of the DocuSign UI in your applications.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
view_link_request = docusign.ViewLinkRequest() # ViewLinkRequest |  (optional)

try: 
    # Reserved: Returns a URL to the secure link view UI.
    api_response = api_instance.create_view_link(account_id, envelope_id, view_link_request=view_link_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->create_view_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **view_link_request** | [**ViewLinkRequest**](ViewLinkRequest.md)|  | [optional] 

### Return type

[**ViewUrl**](ViewUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachments**
> EnvelopeAttachmentsResult delete_attachments(account_id, envelope_id, envelope_attachments_request=envelope_attachments_request)

Delete one or more attachments from a DRAFT envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
envelope_attachments_request = docusign.EnvelopeAttachmentsRequest() # EnvelopeAttachmentsRequest |  (optional)

try: 
    # Delete one or more attachments from a DRAFT envelope.
    api_response = api_instance.delete_attachments(account_id, envelope_id, envelope_attachments_request=envelope_attachments_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **envelope_attachments_request** | [**EnvelopeAttachmentsRequest**](EnvelopeAttachmentsRequest.md)|  | [optional] 

### Return type

[**EnvelopeAttachmentsResult**](EnvelopeAttachmentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunked_upload**
> ChunkedUploadResponse delete_chunked_upload(account_id, chunked_upload_id)

Delete an existing ChunkedUpload.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
chunked_upload_id = 'chunked_upload_id_example' # str | 

try: 
    # Delete an existing ChunkedUpload.
    api_response = api_instance.delete_chunked_upload(account_id, chunked_upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_chunked_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **chunked_upload_id** | **str**|  | 

### Return type

[**ChunkedUploadResponse**](ChunkedUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_fields**
> CustomFields delete_custom_fields(account_id, envelope_id, custom_fields=custom_fields)

Deletes envelope custom fields for draft and in-process envelopes.

Deletes envelope custom fields for draft and in-process envelopes.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
custom_fields = docusign.CustomFields() # CustomFields |  (optional)

try: 
    # Deletes envelope custom fields for draft and in-process envelopes.
    api_response = api_instance.delete_custom_fields(account_id, envelope_id, custom_fields=custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **custom_fields** | [**CustomFields**](CustomFields.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_fields**
> DocumentFieldsInformation delete_document_fields(account_id, document_id, envelope_id, document_fields_information=document_fields_information)

Deletes custom document fields from an existing envelope document.

Deletes custom document fields from an existing envelope document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
document_fields_information = docusign.DocumentFieldsInformation() # DocumentFieldsInformation |  (optional)

try: 
    # Deletes custom document fields from an existing envelope document.
    api_response = api_instance.delete_document_fields(account_id, document_id, envelope_id, document_fields_information=document_fields_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
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
> delete_document_page(account_id, document_id, envelope_id, page_number)

Deletes a page from a document in an envelope.

Deletes a page from a document in an envelope based on the page number.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
page_number = 'page_number_example' # str | The page number being accessed.

try: 
    # Deletes a page from a document in an envelope.
    api_instance.delete_document_page(account_id, document_id, envelope_id, page_number)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_document_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **page_number** | **str**| The page number being accessed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_documents**
> EnvelopeDocumentsResult delete_documents(account_id, envelope_id, envelope_definition=envelope_definition)

Deletes documents from a draft envelope.

Deletes one or more documents from an existing draft envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
envelope_definition = docusign.EnvelopeDefinition() # EnvelopeDefinition |  (optional)

try: 
    # Deletes documents from a draft envelope.
    api_response = api_instance.delete_documents(account_id, envelope_id, envelope_definition=envelope_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **envelope_definition** | [**EnvelopeDefinition**](EnvelopeDefinition.md)|  | [optional] 

### Return type

[**EnvelopeDocumentsResult**](EnvelopeDocumentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_settings**
> EmailSettings delete_email_settings(account_id, envelope_id)

Deletes the email setting overrides for an envelope.

Deletes all existing email override settings for the envelope. If you want to delete an individual email override setting, use the PUT and set the value to an empty string. Note that deleting email settings will only affect email communications that occur after the deletion and the normal account email settings are used for future email communications.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Deletes the email setting overrides for an envelope.
    api_response = api_instance.delete_email_settings(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lock**
> LockInformation delete_lock(account_id, envelope_id)

Deletes an envelope lock.

Deletes the lock from the specified envelope. The `X-DocuSign-Edit` header must be included in the request.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Deletes an envelope lock.
    api_response = api_instance.delete_lock(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipient**
> Recipients delete_recipient(account_id, envelope_id, recipient_id)

Deletes a recipient from an envelope.

Deletes the specified recipient file from the specified envelope. This cannot be used if the envelope has been sent.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.

try: 
    # Deletes a recipient from an envelope.
    api_response = api_instance.delete_recipient(account_id, envelope_id, recipient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipients**
> Recipients delete_recipients(account_id, envelope_id, recipients=recipients)

Deletes recipients from an envelope.

Deletes one or more recipients from a draft or sent envelope. Recipients to be deleted are listed in the request, with the `recipientId` being used as the key for deleting recipients.  If the envelope is `In Process`, meaning that it has been sent and has not  been completed or voided, recipients that have completed their actions cannot be deleted.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipients = docusign.Recipients() # Recipients |  (optional)

try: 
    # Deletes recipients from an envelope.
    api_response = api_instance.delete_recipients(account_id, envelope_id, recipients=recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipients** | [**Recipients**](Recipients.md)|  | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tabs**
> Tabs delete_tabs(account_id, envelope_id, recipient_id, tabs=tabs)

Deletes the tabs associated with a recipient.

Deletes one or more tabs associated with a recipient in a draft envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
tabs = docusign.Tabs() # Tabs |  (optional)

try: 
    # Deletes the tabs associated with a recipient.
    api_response = api_instance.delete_tabs(account_id, envelope_id, recipient_id, tabs=tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **tabs** | [**Tabs**](Tabs.md)|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates_from_document**
> delete_templates_from_document(account_id, document_id, envelope_id, template_id)

Deletes a template from a document in an existing envelope.

Deletes the specified template from a document in an existing envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Deletes a template from a document in an existing envelope.
    api_instance.delete_templates_from_document(account_id, document_id, envelope_id, template_id)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_templates_from_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view_link**
> delete_view_link(account_id, envelope_id)

Reserved: Expires a secure view link.

Reserved: Expires a secure view link

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Reserved: Expires a secure view link.
    api_instance.delete_view_link(account_id, envelope_id)
except ApiException as e:
    print("Exception when calling EnvelopesApi->delete_view_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> get_attachment(account_id, attachment_id, envelope_id)

Retrieves an attachment from the envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
attachment_id = 'attachment_id_example' # str | 
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Retrieves an attachment from the envelope.
    api_instance.get_attachment(account_id, attachment_id, envelope_id)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **attachment_id** | **str**|  | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> EnvelopeAttachmentsResult get_attachments(account_id, envelope_id)

Returns a list of attachments associated with the specified envelope

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Returns a list of attachments associated with the specified envelope
    api_response = api_instance.get_attachments(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**EnvelopeAttachmentsResult**](EnvelopeAttachmentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunked_upload**
> ChunkedUploadResponse get_chunked_upload(account_id, chunked_upload_id, include=include)

Retrieves the current metadata of a ChunkedUpload.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
chunked_upload_id = 'chunked_upload_id_example' # str | 
include = 'include_example' # str |  (optional)

try: 
    # Retrieves the current metadata of a ChunkedUpload.
    api_response = api_instance.get_chunked_upload(account_id, chunked_upload_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_chunked_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **chunked_upload_id** | **str**|  | 
 **include** | **str**|  | [optional] 

### Return type

[**ChunkedUploadResponse**](ChunkedUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_disclosure**
> ConsumerDisclosure get_consumer_disclosure(account_id, envelope_id, lang_code, recipient_id, lang_code2=lang_code2)

Reserved: Gets the Electronic Record and Signature Disclosure associated with the account.

Reserved: Retrieves the Electronic Record and Signature Disclosure, with HTML formatting, associated with the account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
lang_code = 'lang_code_example' # str | The simple type enumeration the language used in the response. The supported languages, with the language value shown in parenthesis, are:Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi). Additionally, the value can be set to �browser� to automatically detect the browser language being used by the viewer and display the disclosure in that language.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
lang_code2 = 'lang_code_example' # str |  (optional)

try: 
    # Reserved: Gets the Electronic Record and Signature Disclosure associated with the account.
    api_response = api_instance.get_consumer_disclosure(account_id, envelope_id, lang_code, recipient_id, lang_code2=lang_code2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_consumer_disclosure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **lang_code** | **str**| The simple type enumeration the language used in the response. The supported languages, with the language value shown in parenthesis, are:Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi). Additionally, the value can be set to �browser� to automatically detect the browser language being used by the viewer and display the disclosure in that language. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **lang_code2** | **str**|  | [optional] 

### Return type

[**ConsumerDisclosure**](ConsumerDisclosure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_disclosure_default**
> ConsumerDisclosure get_consumer_disclosure_default(account_id, envelope_id, recipient_id, lang_code=lang_code)

Gets the Electronic Record and Signature Disclosure associated with the account.

Retrieves the Electronic Record and Signature Disclosure, with html formatting, associated with the account. You can use an optional query string to set the language for the disclosure.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
lang_code = 'lang_code_example' # str |  (optional)

try: 
    # Gets the Electronic Record and Signature Disclosure associated with the account.
    api_response = api_instance.get_consumer_disclosure_default(account_id, envelope_id, recipient_id, lang_code=lang_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_consumer_disclosure_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **lang_code** | **str**|  | [optional] 

### Return type

[**ConsumerDisclosure**](ConsumerDisclosure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> file get_document(account_id, document_id, envelope_id, certificate=certificate, encoding=encoding, encrypt=encrypt, language=language, recipient_id=recipient_id, show_changes=show_changes, watermark=watermark)

Gets a document from an envelope.

Retrieves the specified document from the envelope. If the account has the Highlight Data Changes feature enabled, there is an option to request that any changes in the envelope be highlighted.  You can also use this method to retrieve a PDF containing the combined content of all documents and the certificate. If the account has the Highlight Data Changes feature enabled, there is an option to request that any changes in the envelope be highlighted.   To retrieve the combined content replace the `{documentId}` parameter in the endpoint with `combined`. /accounts/{accountId}/envelopes/{envelopeId}/documents/combined

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
certificate = 'certificate_example' # str | When set to **false**, the envelope signing certificate is removed from the download. (optional)
encoding = 'encoding_example' # str |  (optional)
encrypt = 'encrypt_example' # str | When set to **true**, the PDF bytes returned in the response are encrypted for all the key managers configured on your DocuSign account. The documents can be decrypted with the KeyManager Decrypt Document API. (optional)
language = 'language_example' # str | Specifies the language for the Certificate of Completion in the response. The supported languages, with the language value shown in parenthesis, are: Chinese Simplified (zh_CN), , Chinese Traditional (zh_TW), Dutch (nl), English US (en), French (fr), German (de), Italian (it), Japanese (ja), Korean (ko), Portuguese (pt), Portuguese (Brazil) (pt_BR), Russian (ru), Spanish (es).  (optional)
recipient_id = 'recipient_id_example' # str |  (optional)
show_changes = 'show_changes_example' # str | When set to **true**, any changed fields for the returned PDF are highlighted in yellow and optional signatures or initials outlined in red.  (optional)
watermark = 'watermark_example' # str | When set to **true**, the account has the watermark feature enabled, and the envelope is not complete, the watermark for the account is added to the PDF documents. This option can remove the watermark.  (optional)

try: 
    # Gets a document from an envelope.
    api_response = api_instance.get_document(account_id, document_id, envelope_id, certificate=certificate, encoding=encoding, encrypt=encrypt, language=language, recipient_id=recipient_id, show_changes=show_changes, watermark=watermark)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **certificate** | **str**| When set to **false**, the envelope signing certificate is removed from the download. | [optional] 
 **encoding** | **str**|  | [optional] 
 **encrypt** | **str**| When set to **true**, the PDF bytes returned in the response are encrypted for all the key managers configured on your DocuSign account. The documents can be decrypted with the KeyManager Decrypt Document API. | [optional] 
 **language** | **str**| Specifies the language for the Certificate of Completion in the response. The supported languages, with the language value shown in parenthesis, are: Chinese Simplified (zh_CN), , Chinese Traditional (zh_TW), Dutch (nl), English US (en), French (fr), German (de), Italian (it), Japanese (ja), Korean (ko), Portuguese (pt), Portuguese (Brazil) (pt_BR), Russian (ru), Spanish (es).  | [optional] 
 **recipient_id** | **str**|  | [optional] 
 **show_changes** | **str**| When set to **true**, any changed fields for the returned PDF are highlighted in yellow and optional signatures or initials outlined in red.  | [optional] 
 **watermark** | **str**| When set to **true**, the account has the watermark feature enabled, and the envelope is not complete, the watermark for the account is added to the PDF documents. This option can remove the watermark.  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_page_image**
> file get_document_page_image(account_id, document_id, envelope_id, page_number, dpi=dpi, max_height=max_height, max_width=max_width, show_changes=show_changes)

Gets a page image from an envelope for display.

Retrieves a page image for display from the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
page_number = 'page_number_example' # str | The page number being accessed.
dpi = 'dpi_example' # str | Sets the dpi for the image. (optional)
max_height = 'max_height_example' # str | Sets the maximum height for the page image in pixels. The dpi is recalculated based on this setting. (optional)
max_width = 'max_width_example' # str | Sets the maximum width for the page image in pixels. The dpi is recalculated based on this setting. (optional)
show_changes = 'show_changes_example' # str |  (optional)

try: 
    # Gets a page image from an envelope for display.
    api_response = api_instance.get_document_page_image(account_id, document_id, envelope_id, page_number, dpi=dpi, max_height=max_height, max_width=max_width, show_changes=show_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_document_page_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **page_number** | **str**| The page number being accessed. | 
 **dpi** | **str**| Sets the dpi for the image. | [optional] 
 **max_height** | **str**| Sets the maximum height for the page image in pixels. The dpi is recalculated based on this setting. | [optional] 
 **max_width** | **str**| Sets the maximum width for the page image in pixels. The dpi is recalculated based on this setting. | [optional] 
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
> Tabs get_document_tabs(account_id, document_id, envelope_id, page_numbers=page_numbers)

Returns tabs on the document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
page_numbers = 'page_numbers_example' # str |  (optional)

try: 
    # Returns tabs on the document.
    api_response = api_instance.get_document_tabs(account_id, document_id, envelope_id, page_numbers=page_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_document_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **page_numbers** | **str**|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_settings**
> EmailSettings get_email_settings(account_id, envelope_id)

Gets the email setting overrides for an envelope.

Retrieves the email override settings for the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Gets the email setting overrides for an envelope.
    api_response = api_instance.get_email_settings(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_envelope**
> Envelope get_envelope(account_id, envelope_id, advanced_update=advanced_update, include=include)

Gets the status of a envelope.

Retrieves the overall status for the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
advanced_update = 'advanced_update_example' # str | When true, envelope information can be added or modified. (optional)
include = 'include_example' # str |  (optional)

try: 
    # Gets the status of a envelope.
    api_response = api_instance.get_envelope(account_id, envelope_id, advanced_update=advanced_update, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_envelope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **advanced_update** | **str**| When true, envelope information can be added or modified. | [optional] 
 **include** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_data**
> EnvelopeFormData get_form_data(account_id, envelope_id)

Returns envelope form data for an existing envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Returns envelope form data for an existing envelope.
    api_response = api_instance.get_form_data(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**EnvelopeFormData**](EnvelopeFormData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lock**
> LockInformation get_lock(account_id, envelope_id)

Gets envelope lock information.

Retrieves general information about the envelope lock.  If the call is made by the locked by user and the request has the same integrator key as original, then the `X-DocuSign-Edit` header and additional lock information is included in the response. This allows users to recover a lost editing session token and the `X-DocuSign-Edit` header.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Gets envelope lock information.
    api_response = api_instance.get_lock(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**LockInformation**](LockInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_settings**
> Notification get_notification_settings(account_id, envelope_id)

Gets envelope notification information.

Retrieves the envelope notification, reminders and expirations, information for an existing envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Gets envelope notification information.
    api_response = api_instance.get_notification_settings(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_tabs**
> Tabs get_page_tabs(account_id, document_id, envelope_id, page_number)

Returns tabs on the specified page.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
page_number = 'page_number_example' # str | The page number being accessed.

try: 
    # Returns tabs on the specified page.
    api_response = api_instance.get_page_tabs(account_id, document_id, envelope_id, page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_page_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **page_number** | **str**| The page number being accessed. | 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages**
> PageImages get_pages(account_id, document_id, envelope_id, count=count, dpi=dpi, max_height=max_height, max_width=max_width, nocache=nocache, show_changes=show_changes, start_position=start_position)

Returns document page image(s) based on input.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
count = 'count_example' # str |  (optional)
dpi = 'dpi_example' # str |  (optional)
max_height = 'max_height_example' # str |  (optional)
max_width = 'max_width_example' # str |  (optional)
nocache = 'nocache_example' # str |  (optional)
show_changes = 'show_changes_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)

try: 
    # Returns document page image(s) based on input.
    api_response = api_instance.get_pages(account_id, document_id, envelope_id, count=count, dpi=dpi, max_height=max_height, max_width=max_width, nocache=nocache, show_changes=show_changes, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
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

# **get_recipient_document_visibility**
> DocumentVisibilityList get_recipient_document_visibility(account_id, envelope_id, recipient_id)

Returns document visibility for the recipients

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.

try: 
    # Returns document visibility for the recipients
    api_response = api_instance.get_recipient_document_visibility(account_id, envelope_id, recipient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_recipient_document_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 

### Return type

[**DocumentVisibilityList**](DocumentVisibilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_initials_image**
> file get_recipient_initials_image(account_id, envelope_id, recipient_id, include_chrome=include_chrome)

Gets the initials image for a user.

Retrieves the initials image for the specified user. The image is returned in the same format as it was uploaded. In the request you can specify if the chrome (the added line and identifier around the initial image) is returned with the image.  The userId specified in the endpoint must match the authenticated user's user id and the user must be a member of the account.  The `signatureIdOrName` paramter accepts signature ID or signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly URL encode. If you use the user name, it is likely that the name includes spaces and you might need to URL encode the name before using it in the endpoint.   For example: \"Bob Smith\" to \"Bob%20Smith\"  Older envelopes might only contain chromed images. If getting the non-chromed image fails, try getting the chromed image.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
include_chrome = 'include_chrome_example' # str | The added line and identifier around the initial image. Note: Older envelopes might only have chromed images. If getting the non-chromed image fails, try getting the chromed image. (optional)

try: 
    # Gets the initials image for a user.
    api_response = api_instance.get_recipient_initials_image(account_id, envelope_id, recipient_id, include_chrome=include_chrome)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_recipient_initials_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **include_chrome** | **str**| The added line and identifier around the initial image. Note: Older envelopes might only have chromed images. If getting the non-chromed image fails, try getting the chromed image. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_signature**
> UserSignature get_recipient_signature(account_id, envelope_id, recipient_id)

Gets signature information for a signer or sign-in-person recipient.

Retrieves signature information for a signer or sign-in-person recipient.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.

try: 
    # Gets signature information for a signer or sign-in-person recipient.
    api_response = api_instance.get_recipient_signature(account_id, envelope_id, recipient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_recipient_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 

### Return type

[**UserSignature**](UserSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_signature_image**
> file get_recipient_signature_image(account_id, envelope_id, recipient_id, include_chrome=include_chrome)

Retrieve signature image information for a signer/sign-in-person recipient.

Retrieves the specified user signature image. The image is returned in the same format as uploaded. In the request you can specify if the chrome (the added line and identifier around the initial image) is returned with the image.  The userId specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureIdOrName` parameter accepts signature ID or signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that don't properly URL encode. If you use the user name, it is likely that the name includes spaces and you might need to URL encode the name before using it in the endpoint.   For example: \"Bob Smith\" to \"Bob%20Smith\"  Older envelopes might only have chromed images. If getting the non-chromed image fails, try getting the chromed image.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
include_chrome = 'include_chrome_example' # str | When set to **true**, indicates the chromed version of the signature image should be retrieved. (optional)

try: 
    # Retrieve signature image information for a signer/sign-in-person recipient.
    api_response = api_instance.get_recipient_signature_image(account_id, envelope_id, recipient_id, include_chrome=include_chrome)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_recipient_signature_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **include_chrome** | **str**| When set to **true**, indicates the chromed version of the signature image should be retrieved. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_recipient_document_visibility**
> DocumentVisibilityList get_template_recipient_document_visibility(account_id, recipient_id, template_id)

Returns document visibility for the recipients

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.

try: 
    # Returns document visibility for the recipients
    api_response = api_instance.get_template_recipient_document_visibility(account_id, recipient_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->get_template_recipient_document_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 

### Return type

[**DocumentVisibilityList**](DocumentVisibilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_events**
> EnvelopeAuditEventResponse list_audit_events(account_id, envelope_id)

Gets the envelope audit events for an envelope.

Gets the envelope audit events for the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Gets the envelope audit events for an envelope.
    api_response = api_instance.list_audit_events(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_audit_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**EnvelopeAuditEventResponse**](EnvelopeAuditEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_fields**
> CustomFieldsEnvelope list_custom_fields(account_id, envelope_id)

Gets the custom field information for the specified envelope.

Retrieves the custom field information for the specified envelope. You can use these fields in the envelopes for your account to record information about the envelope, help search for envelopes, and track information. The envelope custom fields are shown in the Envelope Settings section when a user is creating an envelope in the DocuSign member console. The envelope custom fields are not seen by the envelope recipients.  There are two types of envelope custom fields, text, and list. A text custom field lets the sender enter the value for the field. With a list custom field, the sender selects the value of the field from a pre-made list.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Gets the custom field information for the specified envelope.
    api_response = api_instance.list_custom_fields(account_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**CustomFieldsEnvelope**](CustomFieldsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_document_fields**
> DocumentFieldsInformation list_document_fields(account_id, document_id, envelope_id)

Gets the custom document fields from an  existing envelope document.

Retrieves the custom document field information from an existing envelope document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.

try: 
    # Gets the custom document fields from an  existing envelope document.
    api_response = api_instance.list_document_fields(account_id, document_id, envelope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 

### Return type

[**DocumentFieldsInformation**](DocumentFieldsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> EnvelopeDocumentsResult list_documents(account_id, envelope_id, include_metadata=include_metadata)

Gets a list of envelope documents.

Retrieves a list of documents associated with the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
include_metadata = 'include_metadata_example' # str |  (optional)

try: 
    # Gets a list of envelope documents.
    api_response = api_instance.list_documents(account_id, envelope_id, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **include_metadata** | **str**|  | [optional] 

### Return type

[**EnvelopeDocumentsResult**](EnvelopeDocumentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recipients**
> Recipients list_recipients(account_id, envelope_id, include_anchor_tab_locations=include_anchor_tab_locations, include_extended=include_extended, include_metadata=include_metadata, include_tabs=include_tabs)

Gets the status of recipients for an envelope.

Retrieves the status of all recipients in a single envelope and identifies the current recipient in the routing list.   The `currentRoutingOrder` property of the response contains the `routingOrder` value of the current recipient indicating that the envelope has been sent to the recipient, but the recipient has not completed their actions.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
include_anchor_tab_locations = 'include_anchor_tab_locations_example' # str |  When set to **true** and `include_tabs` is set to **true**, all tabs with anchor tab properties are included in the response.  (optional)
include_extended = 'include_extended_example' # str |  When set to **true**, the extended properties are included in the response.  (optional)
include_metadata = 'include_metadata_example' # str |  (optional)
include_tabs = 'include_tabs_example' # str | When set to **true**, the tab information associated with the recipient is included in the response. (optional)

try: 
    # Gets the status of recipients for an envelope.
    api_response = api_instance.list_recipients(account_id, envelope_id, include_anchor_tab_locations=include_anchor_tab_locations, include_extended=include_extended, include_metadata=include_metadata, include_tabs=include_tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **include_anchor_tab_locations** | **str**|  When set to **true** and &#x60;include_tabs&#x60; is set to **true**, all tabs with anchor tab properties are included in the response.  | [optional] 
 **include_extended** | **str**|  When set to **true**, the extended properties are included in the response.  | [optional] 
 **include_metadata** | **str**|  | [optional] 
 **include_tabs** | **str**| When set to **true**, the tab information associated with the recipient is included in the response. | [optional] 

### Return type

[**Recipients**](Recipients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_status**
> EnvelopesInformation list_status(account_id, email=email, from_date=from_date, start_position=start_position, to_date=to_date, envelope_ids_request=envelope_ids_request)

Gets the envelope status for the specified envelopes.

Retrieves the envelope status for the specified envelopes.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
email = 'email_example' # str |  (optional)
from_date = 'from_date_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)
to_date = 'to_date_example' # str |  (optional)
envelope_ids_request = docusign.EnvelopeIdsRequest() # EnvelopeIdsRequest |  (optional)

try: 
    # Gets the envelope status for the specified envelopes.
    api_response = api_instance.list_status(account_id, email=email, from_date=from_date, start_position=start_position, to_date=to_date, envelope_ids_request=envelope_ids_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **email** | **str**|  | [optional] 
 **from_date** | **str**|  | [optional] 
 **start_position** | **str**|  | [optional] 
 **to_date** | **str**|  | [optional] 
 **envelope_ids_request** | [**EnvelopeIdsRequest**](EnvelopeIdsRequest.md)|  | [optional] 

### Return type

[**EnvelopesInformation**](EnvelopesInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_status_changes**
> EnvelopesInformation list_status_changes(account_id, ac_status=ac_status, block=block, count=count, custom_field=custom_field, email=email, envelope_ids=envelope_ids, exclude=exclude, folder_ids=folder_ids, folder_types=folder_types, from_date=from_date, from_to_status=from_to_status, include=include, include_purge_information=include_purge_information, intersecting_folder_ids=intersecting_folder_ids, order=order, order_by=order_by, powerformids=powerformids, search_text=search_text, start_position=start_position, status=status, to_date=to_date, transaction_ids=transaction_ids, user_filter=user_filter, user_id=user_id, user_name=user_name)

Gets status changes for one or more envelopes.

Retrieves envelope status changes for all envelopes. You can modify the information returned by adding query strings to limit the request to check between certain dates and times, or for certain envelopes, or for certain status codes. It is recommended that you use one or more of the query strings in order to limit the size of the response.  ### Important: Unless you are requesting the status for specific envelopes (using the `envelopeIds` or `transactionIds` properties), you must add a set the `from_date` property in the request.  Getting envelope status using `transactionIds` is useful for offline signing situations where it can be used determine if an envelope was created or not, for the cases where a network connection was lost, before the envelope status could be returned.  ### Request Envelope Status Notes ###  The REST API GET /envelopes call uses certain filters to find results. In some cases requests are check for \"any status change\" instead of the just the single status requested. In these cases, more envelopes might be returned by the request than otherwise would be. For example, for a request with the begin date is set to Jan 1st, an end date set to Jan 7th and the status qualifier (`from_to_status`) set to `Delivered` &mdash; the response set might contain envelopes that were created during that time period, but not delivered during the time period.  To avoid unnecessary database queries, the DocuSign system checks requests to ensure that the added filters will not result in a zero-size response before acting on the request. The following table shows the valid envelope statuses (in the Valid Current Statuses column) for the status qualifiers in the request. If the status and status qualifiers in the API request do not contain any of the values shown in the valid current statuses column, then an empty list is returned.  For example, a request with a status qualifier (from_to_status) of `Delivered` and a status of \"`Created`,`Sent`\", DocuSign will always return an empty list. This is because the request essentially translates to: find the envelopes that were delivered between the begin and end dates that have a current status of `Created` or `Sent`, and since an envelope that has been delivered can never have a status of `Created` or `Sent`, a zero-size response would be generated. In this case, DocuSign does not run the request, but just returns the empty list.  Client applications should check that the statuses they are requesting make sense for a given status qualifier.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
ac_status = 'ac_status_example' # str | Specifies the Authoritative Copy Status for the envelopes. The possible values are: Unknown, Original, Transferred, AuthoritativeCopy, AuthoritativeCopyExportPending, AuthoritativeCopyExported, DepositPending, Deposited, DepositedEO, or DepositFailed. (optional)
block = 'block_example' # str |  (optional)
count = 'count_example' # str |  (optional)
custom_field = 'custom_field_example' # str | This specifies the envelope custom field name and value searched for in the envelope information. The value portion of the query can use partial strings by adding '%' (percent sign) around the custom field query value.   Example 1: If you have an envelope custom field called \"Region\" and you want to search for all envelopes where the value is \"West\" you would use the query: `?custom_field=Region=West`.   Example 2: To search for envelopes where the `ApplicationID` custom field has the value or partial value of \"DocuSign\" in field, the query would be: `?custom_field=ApplicationId=%DocuSign%` This would find envelopes where the custom field value is \"DocuSign for Salesforce\" or \"DocuSign envelope.\"   (optional)
email = 'email_example' # str |  (optional)
envelope_ids = 'envelope_ids_example' # str |  (optional)
exclude = 'exclude_example' # str |  (optional)
folder_ids = 'folder_ids_example' # str |  (optional)
folder_types = 'folder_types_example' # str |  (optional)
from_date = 'from_date_example' # str | The date/time setting that specifies the date/time when the request begins checking for status changes for envelopes in the account.  This is required unless 'envelopeId's are used. (optional)
from_to_status = 'from_to_status_example' # str | This is the status type checked for in the `from_date`/`to_date` period. If `changed` is specified, then envelopes that changed status during the period are found. If for example, `created` is specified, then envelopes created during the period are found. Default is `changed`.   Possible values are: Voided, Changed, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut and Processing. (optional)
include = 'include_example' # str |  (optional)
include_purge_information = 'include_purge_information_example' # str |  (optional)
intersecting_folder_ids = 'intersecting_folder_ids_example' # str |  (optional)
order = 'order_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
powerformids = 'powerformids_example' # str |  (optional)
search_text = 'search_text_example' # str |  (optional)
start_position = 'start_position_example' # str |  (optional)
status = 'status_example' # str | The list of current statuses to include in the response. By default, all envelopes found are returned. If values are specified, then of the envelopes found, only those with the current status specified are returned in the results.   Possible values are: Voided, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut and Processing. (optional)
to_date = 'to_date_example' # str | Optional date/time setting that specifies the date/time when the request stops for status changes for envelopes in the account. If no entry, the system uses the time of the call as the `to_date`.  (optional)
transaction_ids = 'transaction_ids_example' # str | If included in the query string, this is a comma separated list of envelope `transactionId`s.   If included in the `request_body`, this is a list of envelope `transactionId`s.   ###### Note: `transactionId`s are only valid in the DocuSign system for seven days.  (optional)
user_filter = 'user_filter_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)
user_name = 'user_name_example' # str |  (optional)

try: 
    # Gets status changes for one or more envelopes.
    api_response = api_instance.list_status_changes(account_id, ac_status=ac_status, block=block, count=count, custom_field=custom_field, email=email, envelope_ids=envelope_ids, exclude=exclude, folder_ids=folder_ids, folder_types=folder_types, from_date=from_date, from_to_status=from_to_status, include=include, include_purge_information=include_purge_information, intersecting_folder_ids=intersecting_folder_ids, order=order, order_by=order_by, powerformids=powerformids, search_text=search_text, start_position=start_position, status=status, to_date=to_date, transaction_ids=transaction_ids, user_filter=user_filter, user_id=user_id, user_name=user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_status_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **ac_status** | **str**| Specifies the Authoritative Copy Status for the envelopes. The possible values are: Unknown, Original, Transferred, AuthoritativeCopy, AuthoritativeCopyExportPending, AuthoritativeCopyExported, DepositPending, Deposited, DepositedEO, or DepositFailed. | [optional] 
 **block** | **str**|  | [optional] 
 **count** | **str**|  | [optional] 
 **custom_field** | **str**| This specifies the envelope custom field name and value searched for in the envelope information. The value portion of the query can use partial strings by adding &#39;%&#39; (percent sign) around the custom field query value.   Example 1: If you have an envelope custom field called \&quot;Region\&quot; and you want to search for all envelopes where the value is \&quot;West\&quot; you would use the query: &#x60;?custom_field&#x3D;Region&#x3D;West&#x60;.   Example 2: To search for envelopes where the &#x60;ApplicationID&#x60; custom field has the value or partial value of \&quot;DocuSign\&quot; in field, the query would be: &#x60;?custom_field&#x3D;ApplicationId&#x3D;%DocuSign%&#x60; This would find envelopes where the custom field value is \&quot;DocuSign for Salesforce\&quot; or \&quot;DocuSign envelope.\&quot;   | [optional] 
 **email** | **str**|  | [optional] 
 **envelope_ids** | **str**|  | [optional] 
 **exclude** | **str**|  | [optional] 
 **folder_ids** | **str**|  | [optional] 
 **folder_types** | **str**|  | [optional] 
 **from_date** | **str**| The date/time setting that specifies the date/time when the request begins checking for status changes for envelopes in the account.  This is required unless &#39;envelopeId&#39;s are used. | [optional] 
 **from_to_status** | **str**| This is the status type checked for in the &#x60;from_date&#x60;/&#x60;to_date&#x60; period. If &#x60;changed&#x60; is specified, then envelopes that changed status during the period are found. If for example, &#x60;created&#x60; is specified, then envelopes created during the period are found. Default is &#x60;changed&#x60;.   Possible values are: Voided, Changed, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut and Processing. | [optional] 
 **include** | **str**|  | [optional] 
 **include_purge_information** | **str**|  | [optional] 
 **intersecting_folder_ids** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **powerformids** | **str**|  | [optional] 
 **search_text** | **str**|  | [optional] 
 **start_position** | **str**|  | [optional] 
 **status** | **str**| The list of current statuses to include in the response. By default, all envelopes found are returned. If values are specified, then of the envelopes found, only those with the current status specified are returned in the results.   Possible values are: Voided, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut and Processing. | [optional] 
 **to_date** | **str**| Optional date/time setting that specifies the date/time when the request stops for status changes for envelopes in the account. If no entry, the system uses the time of the call as the &#x60;to_date&#x60;.  | [optional] 
 **transaction_ids** | **str**| If included in the query string, this is a comma separated list of envelope &#x60;transactionId&#x60;s.   If included in the &#x60;request_body&#x60;, this is a list of envelope &#x60;transactionId&#x60;s.   ###### Note: &#x60;transactionId&#x60;s are only valid in the DocuSign system for seven days.  | [optional] 
 **user_filter** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **user_name** | **str**|  | [optional] 

### Return type

[**EnvelopesInformation**](EnvelopesInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tabs**
> Tabs list_tabs(account_id, envelope_id, recipient_id, include_anchor_tab_locations=include_anchor_tab_locations, include_metadata=include_metadata)

Gets the tabs information for a signer or sign-in-person recipient in an envelope.

Retrieves information about the tabs associated with a recipient in a draft envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
include_anchor_tab_locations = 'include_anchor_tab_locations_example' # str | When set to **true**, all tabs with anchor tab properties are included in the response.  (optional)
include_metadata = 'include_metadata_example' # str |  (optional)

try: 
    # Gets the tabs information for a signer or sign-in-person recipient in an envelope.
    api_response = api_instance.list_tabs(account_id, envelope_id, recipient_id, include_anchor_tab_locations=include_anchor_tab_locations, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
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
> TemplateInformation list_templates(account_id, envelope_id, include=include)

Get List of Templates used in an Envelope

This returns a list of the server-side templates, their name and ID, used in an envelope. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
include = 'include_example' # str | The possible values are:  matching_applied – This returns template matching information for the template. (optional)

try: 
    # Get List of Templates used in an Envelope
    api_response = api_instance.list_templates(account_id, envelope_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **include** | **str**| The possible values are:  matching_applied – This returns template matching information for the template. | [optional] 

### Return type

[**TemplateInformation**](TemplateInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates_for_document**
> TemplateInformation list_templates_for_document(account_id, document_id, envelope_id, include=include)

Gets the templates associated with a document in an existing envelope.

Retrieves the templates associated with a document in the specified envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
include = 'include_example' # str |  (optional)

try: 
    # Gets the templates associated with a document in an existing envelope.
    api_response = api_instance.list_templates_for_document(account_id, document_id, envelope_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->list_templates_for_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **include** | **str**|  | [optional] 

### Return type

[**TemplateInformation**](TemplateInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attachment**
> EnvelopeAttachmentsResult put_attachment(account_id, attachment_id, envelope_id, attachment=attachment)

Add an attachment to a DRAFT or IN-PROCESS envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
attachment_id = 'attachment_id_example' # str | 
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
attachment = docusign.Attachment() # Attachment |  (optional)

try: 
    # Add an attachment to a DRAFT or IN-PROCESS envelope.
    api_response = api_instance.put_attachment(account_id, attachment_id, envelope_id, attachment=attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->put_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **attachment_id** | **str**|  | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **attachment** | [**Attachment**](Attachment.md)|  | [optional] 

### Return type

[**EnvelopeAttachmentsResult**](EnvelopeAttachmentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attachments**
> EnvelopeAttachmentsResult put_attachments(account_id, envelope_id, envelope_attachments_request=envelope_attachments_request)

Add one or more attachments to a DRAFT or IN-PROCESS envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
envelope_attachments_request = docusign.EnvelopeAttachmentsRequest() # EnvelopeAttachmentsRequest |  (optional)

try: 
    # Add one or more attachments to a DRAFT or IN-PROCESS envelope.
    api_response = api_instance.put_attachments(account_id, envelope_id, envelope_attachments_request=envelope_attachments_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->put_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **envelope_attachments_request** | [**EnvelopeAttachmentsRequest**](EnvelopeAttachmentsRequest.md)|  | [optional] 

### Return type

[**EnvelopeAttachmentsResult**](EnvelopeAttachmentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_document_page**
> rotate_document_page(account_id, document_id, envelope_id, page_number, page_request=page_request)

Rotates page image from an envelope for display.

Rotates page image from an envelope for display. The page image can be rotated to the left or right.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
page_number = 'page_number_example' # str | The page number being accessed.
page_request = docusign.PageRequest() # PageRequest |  (optional)

try: 
    # Rotates page image from an envelope for display.
    api_instance.rotate_document_page(account_id, document_id, envelope_id, page_number, page_request=page_request)
except ApiException as e:
    print("Exception when calling EnvelopesApi->rotate_document_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **page_number** | **str**| The page number being accessed. | 
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
> EnvelopeUpdateSummary update(account_id, envelope_id, advanced_update=advanced_update, resend_envelope=resend_envelope, envelope=envelope)

Send Draft Envelope/Void Envelope/Move/Purge Envelope/Modify draft

The Put Envelopes endpoint provides the following functionality:  * Sends the specified single draft envelope. Add {\"status\":\"sent\"} to the request body to send the envelope.  * Voids the specified in-process envelope. Add {\"status\":\"voided\", \"voidedReason\":\"The reason for voiding the envelope\"} to the request body to void the envelope.  * Replaces the current email subject and message for a draft envelope. Add {\"emailSubject\":\"subject\",  \"emailBlurb\":\"message\"}  to the request body to modify the subject and message.  * Place the envelope documents and envelope metadata in a purge queue so that this information is removed from the DocuSign system. Add {\"purgeState\":\"purge type\"} to the request body.  *Additional information on purging documents*  The purge request can only be used for completed envelopes that are not marked as the authoritative copy. The requesting user must have permission to purge documents and must be the sender (the requesting user can act as the sender using Send On Behalf Of).  ###### Note: If you have set the Document Retention policy on your account, envelope documents are automatically placed in the purge queue and the warning emails are sent at the end of the retention period.  ###### Note: You can set the Document Retention policy in the Classic DocuSign Experience by specifying the number of days to retain documents.  ###### Note: Setting a Document Retention policy is the same as setting a schedule for purging documents.  When the purge request is initiated the envelope documents, or documents and envelope metadata, are placed in a purge queue for deletion in 14 days. A warning email notification is sent to the sender and recipients associated with the envelope, notifying them that the envelope documents will be deleted in 14 days and providing a link to the documents. A second email is sent 7 days later with the same message. At the end of the 14-day period, the envelope documents are deleted from the system.  If `purgeState=\"documents_queued\"` is used in the request, then only the documents are deleted and any corresponding attachments and tabs remain in the DocuSign system. If `purgeState= \"documents_and_metadata_queued\"` is used in the request, then the documents, attachments, and tabs are deleted.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
advanced_update = 'advanced_update_example' # str | When set to **true**, allows the caller to update recipients, tabs, custom fields, notification, email settings and other envelope attributes. (optional)
resend_envelope = 'resend_envelope_example' # str | When set to **true**, sends the specified envelope again. (optional)
envelope = docusign.Envelope() # Envelope |  (optional)

try: 
    # Send Draft Envelope/Void Envelope/Move/Purge Envelope/Modify draft
    api_response = api_instance.update(account_id, envelope_id, advanced_update=advanced_update, resend_envelope=resend_envelope, envelope=envelope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **advanced_update** | **str**| When set to **true**, allows the caller to update recipients, tabs, custom fields, notification, email settings and other envelope attributes. | [optional] 
 **resend_envelope** | **str**| When set to **true**, sends the specified envelope again. | [optional] 
 **envelope** | [**Envelope**](Envelope.md)|  | [optional] 

### Return type

[**EnvelopeUpdateSummary**](EnvelopeUpdateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunked_upload**
> ChunkedUploadResponse update_chunked_upload(account_id, chunked_upload_id, action=action)

Integrity-Check and Commit a ChunkedUpload, readying it for use elsewhere.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
chunked_upload_id = 'chunked_upload_id_example' # str | 
action = 'action_example' # str |  (optional)

try: 
    # Integrity-Check and Commit a ChunkedUpload, readying it for use elsewhere.
    api_response = api_instance.update_chunked_upload(account_id, chunked_upload_id, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_chunked_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **chunked_upload_id** | **str**|  | 
 **action** | **str**|  | [optional] 

### Return type

[**ChunkedUploadResponse**](ChunkedUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunked_upload_part**
> ChunkedUploadResponse update_chunked_upload_part(account_id, chunked_upload_id, chunked_upload_part_seq, chunked_upload_request=chunked_upload_request)

Add a chunk, a chunk 'part', to an existing ChunkedUpload.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
chunked_upload_id = 'chunked_upload_id_example' # str | 
chunked_upload_part_seq = 'chunked_upload_part_seq_example' # str | 
chunked_upload_request = docusign.ChunkedUploadRequest() # ChunkedUploadRequest |  (optional)

try: 
    # Add a chunk, a chunk 'part', to an existing ChunkedUpload.
    api_response = api_instance.update_chunked_upload_part(account_id, chunked_upload_id, chunked_upload_part_seq, chunked_upload_request=chunked_upload_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_chunked_upload_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **chunked_upload_id** | **str**|  | 
 **chunked_upload_part_seq** | **str**|  | 
 **chunked_upload_request** | [**ChunkedUploadRequest**](ChunkedUploadRequest.md)|  | [optional] 

### Return type

[**ChunkedUploadResponse**](ChunkedUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_fields**
> CustomFields update_custom_fields(account_id, envelope_id, custom_fields=custom_fields)

Updates envelope custom fields in an envelope.

Updates the envelope custom fields in draft and in-process envelopes.  Each custom field used in an envelope must have a unique name. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
custom_fields = docusign.CustomFields() # CustomFields |  (optional)

try: 
    # Updates envelope custom fields in an envelope.
    api_response = api_instance.update_custom_fields(account_id, envelope_id, custom_fields=custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **custom_fields** | [**CustomFields**](CustomFields.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> update_document(account_id, document_id, envelope_id, apply_document_fields=apply_document_fields)

Adds a document to an existing draft envelope.

Adds a document to an existing draft envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
apply_document_fields = 'apply_document_fields_example' # str |  (optional)

try: 
    # Adds a document to an existing draft envelope.
    api_instance.update_document(account_id, document_id, envelope_id, apply_document_fields=apply_document_fields)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **apply_document_fields** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_fields**
> DocumentFieldsInformation update_document_fields(account_id, document_id, envelope_id, document_fields_information=document_fields_information)

Updates existing custom document fields in an existing envelope document.

Updates existing custom document fields in an existing envelope document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
document_id = 'document_id_example' # str | The ID of the document being accessed.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
document_fields_information = docusign.DocumentFieldsInformation() # DocumentFieldsInformation |  (optional)

try: 
    # Updates existing custom document fields in an existing envelope document.
    api_response = api_instance.update_document_fields(account_id, document_id, envelope_id, document_fields_information=document_fields_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **document_id** | **str**| The ID of the document being accessed. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
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
> EnvelopeDocumentsResult update_documents(account_id, envelope_id, apply_document_fields=apply_document_fields, envelope_definition=envelope_definition)

Adds one or more documents to an existing envelope document.

Adds one or more documents to an existing envelope document.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
apply_document_fields = 'apply_document_fields_example' # str | When true, Document fields can be added or modified while adding or modifying envelope documents. (optional)
envelope_definition = docusign.EnvelopeDefinition() # EnvelopeDefinition |  (optional)

try: 
    # Adds one or more documents to an existing envelope document.
    api_response = api_instance.update_documents(account_id, envelope_id, apply_document_fields=apply_document_fields, envelope_definition=envelope_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **apply_document_fields** | **str**| When true, Document fields can be added or modified while adding or modifying envelope documents. | [optional] 
 **envelope_definition** | [**EnvelopeDefinition**](EnvelopeDefinition.md)|  | [optional] 

### Return type

[**EnvelopeDocumentsResult**](EnvelopeDocumentsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_settings**
> EmailSettings update_email_settings(account_id, envelope_id, email_settings=email_settings)

Updates the email setting overrides for an envelope.

Updates the existing email override settings for the specified envelope. Note that modifying email settings will only affect email communications that occur after the modification was made.  This can also be used to delete an individual email override setting by using an empty string for the value to be deleted.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
email_settings = docusign.EmailSettings() # EmailSettings |  (optional)

try: 
    # Updates the email setting overrides for an envelope.
    api_response = api_instance.update_email_settings(account_id, envelope_id, email_settings=email_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **email_settings** | [**EmailSettings**](EmailSettings.md)|  | [optional] 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lock**
> LockInformation update_lock(account_id, envelope_id, lock_request=lock_request)

Updates an envelope lock.

Updates the lock duration time or update the `lockedByApp` property information for the specified envelope. The user and integrator key must match the user specified by the `lockByUser` property and integrator key information and the `X-DocuSign-Edit` header must be included or an error will be generated.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
lock_request = docusign.LockRequest() # LockRequest |  (optional)

try: 
    # Updates an envelope lock.
    api_response = api_instance.update_lock(account_id, envelope_id, lock_request=lock_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
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
> Notification update_notification_settings(account_id, envelope_id, envelope_notification_request=envelope_notification_request)

Sets envelope notification (Reminders/Expirations) structure for an existing envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
envelope_notification_request = docusign.EnvelopeNotificationRequest() # EnvelopeNotificationRequest |  (optional)

try: 
    # Sets envelope notification (Reminders/Expirations) structure for an existing envelope.
    api_response = api_instance.update_notification_settings(account_id, envelope_id, envelope_notification_request=envelope_notification_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **envelope_notification_request** | [**EnvelopeNotificationRequest**](EnvelopeNotificationRequest.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipient_document_visibility**
> DocumentVisibilityList update_recipient_document_visibility(account_id, envelope_id, recipient_id, document_visibility_list=document_visibility_list)

Updates document visibility for the recipients

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
document_visibility_list = docusign.DocumentVisibilityList() # DocumentVisibilityList |  (optional)

try: 
    # Updates document visibility for the recipients
    api_response = api_instance.update_recipient_document_visibility(account_id, envelope_id, recipient_id, document_visibility_list=document_visibility_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_recipient_document_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **document_visibility_list** | [**DocumentVisibilityList**](DocumentVisibilityList.md)|  | [optional] 

### Return type

[**DocumentVisibilityList**](DocumentVisibilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipient_initials_image**
> update_recipient_initials_image(account_id, envelope_id, recipient_id)

Sets the initials image for an accountless signer.

Updates the initials image for a signer that does not have a DocuSign account. The supported image formats for this file are: gif, png, jpeg, and bmp. The file size must be less than 200K.  For the Authentication/Authorization for this call, the credentials must match the sender of the envelope, the recipient must be an accountless signer or in person signer. The account must have the `CanSendEnvelope` property set to **true** and the `ExpressSendOnly` property in `SendingUser` structure must be set to **false**.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.

try: 
    # Sets the initials image for an accountless signer.
    api_instance.update_recipient_initials_image(account_id, envelope_id, recipient_id)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_recipient_initials_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipient_signature_image**
> update_recipient_signature_image(account_id, envelope_id, recipient_id)

Sets the signature image for an accountless signer.

Updates the signature image for an accountless signer. The supported image formats for this file are: gif, png, jpeg, and bmp. The file size must be less than 200K.  For the Authentication/Authorization for this call, the credentials must match the sender of the envelope, the recipient must be an accountless signer or in person signer. The account must have the `CanSendEnvelope` property set to **true** and the `ExpressSendOnly` property in `SendingUser` structure must be set to **false**.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.

try: 
    # Sets the signature image for an accountless signer.
    api_instance.update_recipient_signature_image(account_id, envelope_id, recipient_id)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_recipient_signature_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipients**
> RecipientsUpdateSummary update_recipients(account_id, envelope_id, resend_envelope=resend_envelope, recipients=recipients)

Updates recipients in a draft envelope or corrects recipient information for an in process envelope.

Updates recipients in a draft envelope or corrects recipient information for an in process envelope.   For draft envelopes, you can edit the following properties: `email`, `userName`, `routingOrder`, `faxNumber`, `deliveryMethod`, `accessCode`, and `requireIdLookup`.  Once an envelope has been sent, you can only edit: `email`, `userName`, `signerName`, `routingOrder`, `faxNumber`, and `deliveryMethod`. You can also select to resend an envelope by using the `resend_envelope` option.  If you send information for a recipient that does not already exist in a draft envelope, the recipient is added to the envelope (similar to the POST).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
resend_envelope = 'resend_envelope_example' # str | When set to **true**, resends the   envelope if the new recipient's routing order is before or the same as the envelope’s next recipient. (optional)
recipients = docusign.Recipients() # Recipients |  (optional)

try: 
    # Updates recipients in a draft envelope or corrects recipient information for an in process envelope.
    api_response = api_instance.update_recipients(account_id, envelope_id, resend_envelope=resend_envelope, recipients=recipients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **resend_envelope** | **str**| When set to **true**, resends the   envelope if the new recipient&#39;s routing order is before or the same as the envelope’s next recipient. | [optional] 
 **recipients** | [**Recipients**](Recipients.md)|  | [optional] 

### Return type

[**RecipientsUpdateSummary**](RecipientsUpdateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipients_document_visibility**
> DocumentVisibilityList update_recipients_document_visibility(account_id, envelope_id, document_visibility_list=document_visibility_list)

Updates document visibility for the recipients

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
document_visibility_list = docusign.DocumentVisibilityList() # DocumentVisibilityList |  (optional)

try: 
    # Updates document visibility for the recipients
    api_response = api_instance.update_recipients_document_visibility(account_id, envelope_id, document_visibility_list=document_visibility_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_recipients_document_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **document_visibility_list** | [**DocumentVisibilityList**](DocumentVisibilityList.md)|  | [optional] 

### Return type

[**DocumentVisibilityList**](DocumentVisibilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tabs**
> Tabs update_tabs(account_id, envelope_id, recipient_id, tabs=tabs)

Updates the tabs for a recipient.  

Updates one or more tabs for a recipient in a draft envelope.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
envelope_id = 'envelope_id_example' # str | The envelopeId Guid of the envelope being accessed.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
tabs = docusign.Tabs() # Tabs |  (optional)

try: 
    # Updates the tabs for a recipient.  
    api_response = api_instance.update_tabs(account_id, envelope_id, recipient_id, tabs=tabs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_tabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **envelope_id** | **str**| The envelopeId Guid of the envelope being accessed. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **tabs** | [**Tabs**](Tabs.md)|  | [optional] 

### Return type

[**Tabs**](Tabs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_recipient_document_visibility**
> TemplateDocumentVisibilityList update_template_recipient_document_visibility(account_id, recipient_id, template_id, template_document_visibility_list=template_document_visibility_list)

Updates document visibility for the recipients

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_id = 'recipient_id_example' # str | The ID of the recipient being accessed.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_document_visibility_list = docusign.TemplateDocumentVisibilityList() # TemplateDocumentVisibilityList |  (optional)

try: 
    # Updates document visibility for the recipients
    api_response = api_instance.update_template_recipient_document_visibility(account_id, recipient_id, template_id, template_document_visibility_list=template_document_visibility_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_template_recipient_document_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_id** | **str**| The ID of the recipient being accessed. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_document_visibility_list** | [**TemplateDocumentVisibilityList**](TemplateDocumentVisibilityList.md)|  | [optional] 

### Return type

[**TemplateDocumentVisibilityList**](TemplateDocumentVisibilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_recipients_document_visibility**
> TemplateDocumentVisibilityList update_template_recipients_document_visibility(account_id, template_id, template_document_visibility_list=template_document_visibility_list)

Updates document visibility for the recipients

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.EnvelopesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
template_id = 'template_id_example' # str | The ID of the template being accessed.
template_document_visibility_list = docusign.TemplateDocumentVisibilityList() # TemplateDocumentVisibilityList |  (optional)

try: 
    # Updates document visibility for the recipients
    api_response = api_instance.update_template_recipients_document_visibility(account_id, template_id, template_document_visibility_list=template_document_visibility_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvelopesApi->update_template_recipients_document_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **template_id** | **str**| The ID of the template being accessed. | 
 **template_document_visibility_list** | [**TemplateDocumentVisibilityList**](TemplateDocumentVisibilityList.md)|  | [optional] 

### Return type

[**TemplateDocumentVisibilityList**](TemplateDocumentVisibilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

