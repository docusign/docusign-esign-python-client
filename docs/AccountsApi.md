# docusign.AccountsApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AccountsApi.md#create) | **POST** /v2/accounts | Creates new accounts.
[**create_brand**](AccountsApi.md#create_brand) | **POST** /v2/accounts/{accountId}/brands | Creates one or more brand profile files for the account.
[**create_custom_field**](AccountsApi.md#create_custom_field) | **POST** /v2/accounts/{accountId}/custom_fields | Creates an acount custom field.
[**create_e_mortgage_transaction**](AccountsApi.md#create_e_mortgage_transaction) | **POST** /v2/accounts/{accountId}/eMortgage/transactions | Starts a new eMortgage Transaction
[**create_permission_profile**](AccountsApi.md#create_permission_profile) | **POST** /v2/accounts/{accountId}/permission_profiles | Creates a new permission profile in the specified account.
[**delete**](AccountsApi.md#delete) | **DELETE** /v2/accounts/{accountId} | Deletes the specified account.
[**delete_brand**](AccountsApi.md#delete_brand) | **DELETE** /v2/accounts/{accountId}/brands/{brandId} | Removes a brand.
[**delete_brand_logo_by_type**](AccountsApi.md#delete_brand_logo_by_type) | **DELETE** /v2/accounts/{accountId}/brands/{brandId}/logos/{logoType} | Delete one branding logo.
[**delete_brands**](AccountsApi.md#delete_brands) | **DELETE** /v2/accounts/{accountId}/brands | Deletes one or more brand profiles.
[**delete_captive_recipient**](AccountsApi.md#delete_captive_recipient) | **DELETE** /v2/accounts/{accountId}/captive_recipients/{recipientPart} | Deletes the signature for one or more captive recipient records.
[**delete_custom_field**](AccountsApi.md#delete_custom_field) | **DELETE** /v2/accounts/{accountId}/custom_fields/{customFieldId} | Delete an existing account custom field.
[**delete_e_note_configuration**](AccountsApi.md#delete_e_note_configuration) | **DELETE** /v2/accounts/{accountId}/settings/enote_configuration | Deletes configuration information for the eNote eOriginal integration.
[**delete_permission_profile**](AccountsApi.md#delete_permission_profile) | **DELETE** /v2/accounts/{accountId}/permission_profiles/{permissionProfileId} | Deletes a permissions profile within the specified account.
[**get_account_information**](AccountsApi.md#get_account_information) | **GET** /v2/accounts/{accountId} | Retrieves the account information for the specified account.
[**get_account_tab_settings**](AccountsApi.md#get_account_tab_settings) | **GET** /v2/accounts/{accountId}/settings/tabs | Returns tab settings list for specified account
[**get_all_payment_gateway_accounts**](AccountsApi.md#get_all_payment_gateway_accounts) | **GET** /v2/accounts/{accountId}/payment_gateway_accounts | Get all payment gateway account for the provided accountId
[**get_billing_charges**](AccountsApi.md#get_billing_charges) | **GET** /v2/accounts/{accountId}/billing_charges | Gets list of recurring and usage charges for the account.
[**get_brand**](AccountsApi.md#get_brand) | **GET** /v2/accounts/{accountId}/brands/{brandId} | Get information for a specific brand.
[**get_brand_export_file**](AccountsApi.md#get_brand_export_file) | **GET** /v2/accounts/{accountId}/brands/{brandId}/file | Export a specific brand.
[**get_brand_logo_by_type**](AccountsApi.md#get_brand_logo_by_type) | **GET** /v2/accounts/{accountId}/brands/{brandId}/logos/{logoType} | Obtains the specified image for a brand.
[**get_brand_resources**](AccountsApi.md#get_brand_resources) | **GET** /v2/accounts/{accountId}/brands/{brandId}/resources | Returns the specified account&#39;s list of branding resources (metadata).
[**get_brand_resources_by_content_type**](AccountsApi.md#get_brand_resources_by_content_type) | **GET** /v2/accounts/{accountId}/brands/{brandId}/resources/{resourceContentType} | Returns the specified branding resource file.
[**get_consumer_disclosure**](AccountsApi.md#get_consumer_disclosure) | **GET** /v2/accounts/{accountId}/consumer_disclosure/{langCode} | Gets the Electronic Record and Signature Disclosure.
[**get_consumer_disclosure_default**](AccountsApi.md#get_consumer_disclosure_default) | **GET** /v2/accounts/{accountId}/consumer_disclosure | Gets the Electronic Record and Signature Disclosure for the account.
[**get_e_note_configuration**](AccountsApi.md#get_e_note_configuration) | **GET** /v2/accounts/{accountId}/settings/enote_configuration | Returns the configuration information for the eNote eOriginal integration.
[**get_password_rules**](AccountsApi.md#get_password_rules) | **GET** /v2/accounts/{accountId}/settings/password_rules | Get the password rules
[**get_password_rules_0**](AccountsApi.md#get_password_rules_0) | **GET** /v2/current_user/password_rules | Get membership account password rules
[**get_permission_profile**](AccountsApi.md#get_permission_profile) | **GET** /v2/accounts/{accountId}/permission_profiles/{permissionProfileId} | Returns a permissions profile in the specified account.
[**get_provisioning**](AccountsApi.md#get_provisioning) | **GET** /v2/accounts/provisioning | Retrieves the account provisioning information for the account.
[**get_supported_languages**](AccountsApi.md#get_supported_languages) | **GET** /v2/accounts/{accountId}/supported_languages | Gets list of supported languages for recipient language setting.
[**get_watermark**](AccountsApi.md#get_watermark) | **GET** /v2/accounts/{accountId}/watermark | Get watermark information.
[**get_watermark_preview**](AccountsApi.md#get_watermark_preview) | **PUT** /v2/accounts/{accountId}/watermark/preview | Get watermark preview.
[**list_brands**](AccountsApi.md#list_brands) | **GET** /v2/accounts/{accountId}/brands | Gets a list of brand profiles.
[**list_custom_fields**](AccountsApi.md#list_custom_fields) | **GET** /v2/accounts/{accountId}/custom_fields | Gets a list of custom fields associated with the account.
[**list_permissions**](AccountsApi.md#list_permissions) | **GET** /v2/accounts/{accountId}/permission_profiles | Gets a list of permission profiles.
[**list_recipient_names_by_email**](AccountsApi.md#list_recipient_names_by_email) | **GET** /v2/accounts/{accountId}/recipient_names | Gets recipient names associated with an email address.
[**list_settings**](AccountsApi.md#list_settings) | **GET** /v2/accounts/{accountId}/settings | Gets account settings information.
[**list_shared_access**](AccountsApi.md#list_shared_access) | **GET** /v2/accounts/{accountId}/shared_access | Reserved: Gets the shared item status for one or more users.
[**list_signature_providers**](AccountsApi.md#list_signature_providers) | **GET** /v2/accounts/{accountId}/signatureProviders | Returns Account available signature providers for specified account.
[**list_unsupported_file_types**](AccountsApi.md#list_unsupported_file_types) | **GET** /v2/accounts/{accountId}/unsupported_file_types | Gets a list of unsupported file types.
[**update_account_tab_settings**](AccountsApi.md#update_account_tab_settings) | **PUT** /v2/accounts/{accountId}/settings/tabs | Modifies tab settings for specified account
[**update_brand**](AccountsApi.md#update_brand) | **PUT** /v2/accounts/{accountId}/brands/{brandId} | Updates an existing brand.
[**update_brand_logo_by_type**](AccountsApi.md#update_brand_logo_by_type) | **PUT** /v2/accounts/{accountId}/brands/{brandId}/logos/{logoType} | Put one branding logo.
[**update_brand_resources_by_content_type**](AccountsApi.md#update_brand_resources_by_content_type) | **PUT** /v2/accounts/{accountId}/brands/{brandId}/resources/{resourceContentType} | Uploads a branding resource file.
[**update_consumer_disclosure**](AccountsApi.md#update_consumer_disclosure) | **PUT** /v2/accounts/{accountId}/consumer_disclosure/{langCode} | Update Consumer Disclosure.
[**update_custom_field**](AccountsApi.md#update_custom_field) | **PUT** /v2/accounts/{accountId}/custom_fields/{customFieldId} | Updates an existing account custom field.
[**update_e_note_configuration**](AccountsApi.md#update_e_note_configuration) | **PUT** /v2/accounts/{accountId}/settings/enote_configuration | Updates configuration information for the eNote eOriginal integration.
[**update_password_rules**](AccountsApi.md#update_password_rules) | **PUT** /v2/accounts/{accountId}/settings/password_rules | Update the password rules
[**update_permission_profile**](AccountsApi.md#update_permission_profile) | **PUT** /v2/accounts/{accountId}/permission_profiles/{permissionProfileId} | Updates a permission profile within the specified account.
[**update_settings**](AccountsApi.md#update_settings) | **PUT** /v2/accounts/{accountId}/settings | Updates the account settings for an account.
[**update_shared_access**](AccountsApi.md#update_shared_access) | **PUT** /v2/accounts/{accountId}/shared_access | Reserved: Sets the shared access information for users.
[**update_watermark**](AccountsApi.md#update_watermark) | **PUT** /v2/accounts/{accountId}/watermark | Update watermark information.


# **create**
> NewAccountSummary create(preview_billing_plan=preview_billing_plan, new_account_definition=new_account_definition)

Creates new accounts.

Creates new DocuSign service accounts.  This is used to create multiple DocuSign accounts with one call. It uses the same information and formats as the normal a  [Accounts:create](accounts_create) call with the information included within a `newAccountRequests` element. A maximum of 100 new accounts can be created at one time.  Note that the structure of the XML request is slightly different than the JSON request, in that the new account information is included in a `newAccountDefinition` property inside the `newAccountRequests` element. Response  The response returns the new account ID, password and the default user information for each newly created account.  A 201 code is returned if the call succeeded.  While the call may have succeed, some of the individual account requests may have failed. In the case of failures to create the account,  an `errorDetails` node is added in the response to each specific request that failed.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
preview_billing_plan = 'preview_billing_plan_example' # str | When set to **true**, creates the account using a preview billing plan. (optional)
new_account_definition = docusign.NewAccountDefinition() # NewAccountDefinition |  (optional)

try: 
    # Creates new accounts.
    api_response = api_instance.create(preview_billing_plan=preview_billing_plan, new_account_definition=new_account_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_billing_plan** | **str**| When set to **true**, creates the account using a preview billing plan. | [optional] 
 **new_account_definition** | [**NewAccountDefinition**](NewAccountDefinition.md)|  | [optional] 

### Return type

[**NewAccountSummary**](NewAccountSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_brand**
> BrandsResponse create_brand(account_id, brand=brand)

Creates one or more brand profile files for the account.

Creates one or more brand profile files for the account. The Account Branding feature (accountSettings properties `canSelfBrandSend` and `canSelfBrandSig`) must be set to **true** for the account to use this call.  An error is returned if `brandId` property for a brand profile is already set for the account. To upload a new version of an existing brand profile, you must delete the profile and then upload the newer version.  When brand profile files are being uploaded, they must be combined into one zip file and the `Content-Type` must be `application/zip`.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand = docusign.Brand() # Brand |  (optional)

try: 
    # Creates one or more brand profile files for the account.
    api_response = api_instance.create_brand(account_id, brand=brand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_brand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand** | [**Brand**](Brand.md)|  | [optional] 

### Return type

[**BrandsResponse**](BrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_field**
> CustomFields create_custom_field(account_id, apply_to_templates=apply_to_templates, custom_field=custom_field)

Creates an acount custom field.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
apply_to_templates = 'apply_to_templates_example' # str |  (optional)
custom_field = docusign.CustomField() # CustomField |  (optional)

try: 
    # Creates an acount custom field.
    api_response = api_instance.create_custom_field(account_id, apply_to_templates=apply_to_templates, custom_field=custom_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **apply_to_templates** | **str**|  | [optional] 
 **custom_field** | [**CustomField**](CustomField.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_e_mortgage_transaction**
> PostTransactionsResponse create_e_mortgage_transaction(account_id, post_transactions_request=post_transactions_request)

Starts a new eMortgage Transaction

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
post_transactions_request = docusign.PostTransactionsRequest() # PostTransactionsRequest |  (optional)

try: 
    # Starts a new eMortgage Transaction
    api_response = api_instance.create_e_mortgage_transaction(account_id, post_transactions_request=post_transactions_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_e_mortgage_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **post_transactions_request** | [**PostTransactionsRequest**](PostTransactionsRequest.md)|  | [optional] 

### Return type

[**PostTransactionsResponse**](PostTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_permission_profile**
> PermissionProfile create_permission_profile(account_id, include=include, permission_profile=permission_profile)

Creates a new permission profile in the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
include = 'include_example' # str |  (optional)
permission_profile = docusign.PermissionProfile() # PermissionProfile |  (optional)

try: 
    # Creates a new permission profile in the specified account.
    api_response = api_instance.create_permission_profile(account_id, include=include, permission_profile=permission_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_permission_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **include** | **str**|  | [optional] 
 **permission_profile** | [**PermissionProfile**](PermissionProfile.md)|  | [optional] 

### Return type

[**PermissionProfile**](PermissionProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(account_id)

Deletes the specified account.

This closes the specified account. You must be an account admin to close your account. Once closed, an account must be reopened by DocuSign.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Deletes the specified account.
    api_instance.delete(account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand**
> delete_brand(account_id, brand_id)

Removes a brand.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.

try: 
    # Removes a brand.
    api_instance.delete_brand(account_id, brand_id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_brand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand_logo_by_type**
> delete_brand_logo_by_type(account_id, brand_id, logo_type)

Delete one branding logo.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
logo_type = 'logo_type_example' # str | One of **Primary**, **Secondary** or **Email**.

try: 
    # Delete one branding logo.
    api_instance.delete_brand_logo_by_type(account_id, brand_id, logo_type)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_brand_logo_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **logo_type** | **str**| One of **Primary**, **Secondary** or **Email**. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brands**
> BrandsResponse delete_brands(account_id, brands_request=brands_request)

Deletes one or more brand profiles.

Deletes one or more brand profiles from an account. The Account Branding feature (accountSettings properties `canSelfBrandSend` and `canSelfBrandSend`) must be set to **true** to use this call.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brands_request = docusign.BrandsRequest() # BrandsRequest |  (optional)

try: 
    # Deletes one or more brand profiles.
    api_response = api_instance.delete_brands(account_id, brands_request=brands_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_brands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brands_request** | [**BrandsRequest**](BrandsRequest.md)|  | [optional] 

### Return type

[**BrandsResponse**](BrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_captive_recipient**
> CaptiveRecipientInformation delete_captive_recipient(account_id, recipient_part, captive_recipient_information=captive_recipient_information)

Deletes the signature for one or more captive recipient records.

Deletes the signature for one or more captive recipient records; it is primarily used for testing. This provides a way to reset the signature associated with a client user ID so that a new signature can be created the next time the client user ID is used.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
recipient_part = 'recipient_part_example' # str | 
captive_recipient_information = docusign.CaptiveRecipientInformation() # CaptiveRecipientInformation |  (optional)

try: 
    # Deletes the signature for one or more captive recipient records.
    api_response = api_instance.delete_captive_recipient(account_id, recipient_part, captive_recipient_information=captive_recipient_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_captive_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **recipient_part** | **str**|  | 
 **captive_recipient_information** | [**CaptiveRecipientInformation**](CaptiveRecipientInformation.md)|  | [optional] 

### Return type

[**CaptiveRecipientInformation**](CaptiveRecipientInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> delete_custom_field(account_id, custom_field_id, apply_to_templates=apply_to_templates)

Delete an existing account custom field.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
custom_field_id = 'custom_field_id_example' # str | 
apply_to_templates = 'apply_to_templates_example' # str |  (optional)

try: 
    # Delete an existing account custom field.
    api_instance.delete_custom_field(account_id, custom_field_id, apply_to_templates=apply_to_templates)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **custom_field_id** | **str**|  | 
 **apply_to_templates** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_e_note_configuration**
> delete_e_note_configuration(account_id)

Deletes configuration information for the eNote eOriginal integration.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Deletes configuration information for the eNote eOriginal integration.
    api_instance.delete_e_note_configuration(account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_e_note_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_profile**
> delete_permission_profile(account_id, permission_profile_id)

Deletes a permissions profile within the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
permission_profile_id = 'permission_profile_id_example' # str | 

try: 
    # Deletes a permissions profile within the specified account.
    api_instance.delete_permission_profile(account_id, permission_profile_id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_permission_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **permission_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_information**
> AccountInformation get_account_information(account_id, include_account_settings=include_account_settings)

Retrieves the account information for the specified account.

Retrieves the account information for the specified account.  **Response** The `canUpgrade` property contains is a Boolean that indicates whether the account can be upgraded through the API. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
include_account_settings = 'include_account_settings_example' # str | When set to **true**, includes the account settings for the account in the response. (optional)

try: 
    # Retrieves the account information for the specified account.
    api_response = api_instance.get_account_information(account_id, include_account_settings=include_account_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **include_account_settings** | **str**| When set to **true**, includes the account settings for the account in the response. | [optional] 

### Return type

[**AccountInformation**](AccountInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_tab_settings**
> TabAccountSettings get_account_tab_settings(account_id)

Returns tab settings list for specified account

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Returns tab settings list for specified account
    api_response = api_instance.get_account_tab_settings(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_tab_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**TabAccountSettings**](TabAccountSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_gateway_accounts**
> PaymentGatewayAccountsInfo get_all_payment_gateway_accounts(account_id)

Get all payment gateway account for the provided accountId

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Get all payment gateway account for the provided accountId
    api_response = api_instance.get_all_payment_gateway_accounts(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_all_payment_gateway_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**PaymentGatewayAccountsInfo**](PaymentGatewayAccountsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_charges**
> BillingChargeResponse get_billing_charges(account_id, include_charges=include_charges)

Gets list of recurring and usage charges for the account.

Retrieves the list of recurring and usage charges for the account. This can be used to determine the charge structure and usage of charge plan items.   Privileges required: account administrator 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
include_charges = 'include_charges_example' # str | Specifies which billing charges to return. Valid values are:  * envelopes * seats  (optional)

try: 
    # Gets list of recurring and usage charges for the account.
    api_response = api_instance.get_billing_charges(account_id, include_charges=include_charges)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_billing_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **include_charges** | **str**| Specifies which billing charges to return. Valid values are:  * envelopes * seats  | [optional] 

### Return type

[**BillingChargeResponse**](BillingChargeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand**
> Brand get_brand(account_id, brand_id, include_external_references=include_external_references, include_logos=include_logos)

Get information for a specific brand.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
include_external_references = 'include_external_references_example' # str |  (optional)
include_logos = 'include_logos_example' # str |  (optional)

try: 
    # Get information for a specific brand.
    api_response = api_instance.get_brand(account_id, brand_id, include_external_references=include_external_references, include_logos=include_logos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_brand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **include_external_references** | **str**|  | [optional] 
 **include_logos** | **str**|  | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_export_file**
> get_brand_export_file(account_id, brand_id)

Export a specific brand.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.

try: 
    # Export a specific brand.
    api_instance.get_brand_export_file(account_id, brand_id)
except ApiException as e:
    print("Exception when calling AccountsApi->get_brand_export_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_logo_by_type**
> get_brand_logo_by_type(account_id, brand_id, logo_type)

Obtains the specified image for a brand.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
logo_type = 'logo_type_example' # str | One of **Primary**, **Secondary** or **Email**.

try: 
    # Obtains the specified image for a brand.
    api_instance.get_brand_logo_by_type(account_id, brand_id, logo_type)
except ApiException as e:
    print("Exception when calling AccountsApi->get_brand_logo_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **logo_type** | **str**| One of **Primary**, **Secondary** or **Email**. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_resources**
> BrandResourcesList get_brand_resources(account_id, brand_id)

Returns the specified account's list of branding resources (metadata).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.

try: 
    # Returns the specified account's list of branding resources (metadata).
    api_response = api_instance.get_brand_resources(account_id, brand_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_brand_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 

### Return type

[**BrandResourcesList**](BrandResourcesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_resources_by_content_type**
> get_brand_resources_by_content_type(account_id, brand_id, resource_content_type, langcode=langcode, return_master=return_master)

Returns the specified branding resource file.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
resource_content_type = 'resource_content_type_example' # str | 
langcode = 'langcode_example' # str |  (optional)
return_master = 'return_master_example' # str |  (optional)

try: 
    # Returns the specified branding resource file.
    api_instance.get_brand_resources_by_content_type(account_id, brand_id, resource_content_type, langcode=langcode, return_master=return_master)
except ApiException as e:
    print("Exception when calling AccountsApi->get_brand_resources_by_content_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **resource_content_type** | **str**|  | 
 **langcode** | **str**|  | [optional] 
 **return_master** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_disclosure**
> ConsumerDisclosure get_consumer_disclosure(account_id, lang_code)

Gets the Electronic Record and Signature Disclosure.

Retrieves the Electronic Record and Signature Disclosure, with HTML formatting, for the requested envelope recipient. This might be different than the current account disclosure depending on account settings, such as branding, and when the account disclosure was last updated. An optional query string can be included to return the language for the disclosure.  

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
lang_code = 'lang_code_example' # str | The simple type enumeration the language used in the response. The supported languages, with the language value shown in parenthesis, are:Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi). Additionally, the value can be set to �browser� to automatically detect the browser language being used by the viewer and display the disclosure in that language.

try: 
    # Gets the Electronic Record and Signature Disclosure.
    api_response = api_instance.get_consumer_disclosure(account_id, lang_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_consumer_disclosure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **lang_code** | **str**| The simple type enumeration the language used in the response. The supported languages, with the language value shown in parenthesis, are:Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi). Additionally, the value can be set to �browser� to automatically detect the browser language being used by the viewer and display the disclosure in that language. | 

### Return type

[**ConsumerDisclosure**](ConsumerDisclosure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_disclosure_default**
> ConsumerDisclosure get_consumer_disclosure_default(account_id, lang_code=lang_code)

Gets the Electronic Record and Signature Disclosure for the account.

Retrieves the Electronic Record and Signature Disclosure, with HTML formatting, associated with the account. You can use an optional query string to set the language for the disclosure.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
lang_code = 'lang_code_example' # str | Specifies the language used in the response. The supported languages, with the language value shown in parenthesis, are: Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk), and Vietnamese (vi).  Additionally, the value can be set to `browser` to automatically detect the browser language being used by the viewer and display the disclosure in that language.  (optional)

try: 
    # Gets the Electronic Record and Signature Disclosure for the account.
    api_response = api_instance.get_consumer_disclosure_default(account_id, lang_code=lang_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_consumer_disclosure_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **lang_code** | **str**| Specifies the language used in the response. The supported languages, with the language value shown in parenthesis, are: Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk), and Vietnamese (vi).  Additionally, the value can be set to &#x60;browser&#x60; to automatically detect the browser language being used by the viewer and display the disclosure in that language.  | [optional] 

### Return type

[**ConsumerDisclosure**](ConsumerDisclosure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_e_note_configuration**
> ENoteConfiguration get_e_note_configuration(account_id)

Returns the configuration information for the eNote eOriginal integration.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Returns the configuration information for the eNote eOriginal integration.
    api_response = api_instance.get_e_note_configuration(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_e_note_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**ENoteConfiguration**](ENoteConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_rules**
> AccountPasswordRules get_password_rules(account_id)

Get the password rules

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Get the password rules
    api_response = api_instance.get_password_rules(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_password_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**AccountPasswordRules**](AccountPasswordRules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_rules_0**
> UserPasswordRules get_password_rules_0()

Get membership account password rules

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()

try: 
    # Get membership account password rules
    api_response = api_instance.get_password_rules_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_password_rules_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserPasswordRules**](UserPasswordRules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_profile**
> PermissionProfile get_permission_profile(account_id, permission_profile_id, include=include)

Returns a permissions profile in the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
permission_profile_id = 'permission_profile_id_example' # str | 
include = 'include_example' # str |  (optional)

try: 
    # Returns a permissions profile in the specified account.
    api_response = api_instance.get_permission_profile(account_id, permission_profile_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_permission_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **permission_profile_id** | **str**|  | 
 **include** | **str**|  | [optional] 

### Return type

[**PermissionProfile**](PermissionProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provisioning**
> ProvisioningInformation get_provisioning()

Retrieves the account provisioning information for the account.

Retrieves the account provisioning information for the account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()

try: 
    # Retrieves the account provisioning information for the account.
    api_response = api_instance.get_provisioning()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_provisioning: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProvisioningInformation**](ProvisioningInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_languages**
> SupportedLanguages get_supported_languages(account_id)

Gets list of supported languages for recipient language setting.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Gets list of supported languages for recipient language setting.
    api_response = api_instance.get_supported_languages(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_supported_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**SupportedLanguages**](SupportedLanguages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watermark**
> Watermark get_watermark(account_id)

Get watermark information.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Get watermark information.
    api_response = api_instance.get_watermark(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_watermark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**Watermark**](Watermark.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watermark_preview**
> Watermark get_watermark_preview(account_id, watermark=watermark)

Get watermark preview.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
watermark = docusign.Watermark() # Watermark |  (optional)

try: 
    # Get watermark preview.
    api_response = api_instance.get_watermark_preview(account_id, watermark=watermark)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_watermark_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **watermark** | [**Watermark**](Watermark.md)|  | [optional] 

### Return type

[**Watermark**](Watermark.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_brands**
> BrandsResponse list_brands(account_id, exclude_distributor_brand=exclude_distributor_brand, include_logos=include_logos)

Gets a list of brand profiles.

Retrieves the list of brand profiles associated with the account and the default brand profiles. The Account Branding feature (accountSettings properties `canSelfBrandSend` and `canSelfBrandSend`)  must be set to **true** for the account to use this call.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
exclude_distributor_brand = 'exclude_distributor_brand_example' # str | When set to **true**, excludes distributor brand information from the response set. (optional)
include_logos = 'include_logos_example' # str | When set to **true**, returns the logos associated with the brand. (optional)

try: 
    # Gets a list of brand profiles.
    api_response = api_instance.list_brands(account_id, exclude_distributor_brand=exclude_distributor_brand, include_logos=include_logos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_brands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **exclude_distributor_brand** | **str**| When set to **true**, excludes distributor brand information from the response set. | [optional] 
 **include_logos** | **str**| When set to **true**, returns the logos associated with the brand. | [optional] 

### Return type

[**BrandsResponse**](BrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_fields**
> CustomFields list_custom_fields(account_id)

Gets a list of custom fields associated with the account.

Retrieves a list of envelope custom fields associated with the account. You can use these fields in the envelopes for your account to record information about the envelope, help search for envelopes and track information. The envelope custom fields are shown in the Envelope Settings section when a user is creating an envelope in the DocuSign member console. The envelope custom fields are not seen by the envelope recipients.  There are two types of envelope custom fields, text, and list. A text custom field lets the sender enter the value for the field. The list custom field lets the sender select the value of the field from a list you provide.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Gets a list of custom fields associated with the account.
    api_response = api_instance.list_custom_fields(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_permissions**
> PermissionProfileInformation list_permissions(account_id, include=include)

Gets a list of permission profiles.

Retrieves a list of Permission Profiles. Permission Profiles are a standard set of user permissions that you can apply to individual users or users in a Group. This makes it easier to manage user permissions for a large number of users, without having to change permissions on a user-by-user basis.  Currently, Permission Profiles can only be created and modified in the DocuSign console.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
include = 'include_example' # str |  (optional)

try: 
    # Gets a list of permission profiles.
    api_response = api_instance.list_permissions(account_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **include** | **str**|  | [optional] 

### Return type

[**PermissionProfileInformation**](PermissionProfileInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recipient_names_by_email**
> RecipientNamesResponse list_recipient_names_by_email(account_id, email=email)

Gets recipient names associated with an email address.

Retrieves a list of recipients in the specified account that are associated with a email address supplied in the query string.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
email = 'email_example' # str | The email address for the user (optional)

try: 
    # Gets recipient names associated with an email address.
    api_response = api_instance.list_recipient_names_by_email(account_id, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_recipient_names_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **email** | **str**| The email address for the user | [optional] 

### Return type

[**RecipientNamesResponse**](RecipientNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings**
> AccountSettingsInformation list_settings(account_id)

Gets account settings information.

Retrieves the account settings information for the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Gets account settings information.
    api_response = api_instance.list_settings(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**AccountSettingsInformation**](AccountSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_access**
> AccountSharedAccess list_shared_access(account_id, count=count, envelopes_not_shared_user_status=envelopes_not_shared_user_status, folder_ids=folder_ids, item_type=item_type, search_text=search_text, shared=shared, start_position=start_position, user_ids=user_ids)

Reserved: Gets the shared item status for one or more users.

Reserved: Retrieves shared item status for one or more users and types of items.  Users with account administration privileges can retrieve shared access information for all account users. Users without account administrator privileges can only retrieve shared access information for themselves and the returned information is limited to the retrieving the status of all members of the account that are sharing their folders to the user. This is equivalent to setting the shared=shared_from.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
count = 'count_example' # str | Specifies maximum number of results included in the response. If no value is specified, this defaults to 1000. (optional)
envelopes_not_shared_user_status = 'envelopes_not_shared_user_status_example' # str |  (optional)
folder_ids = 'folder_ids_example' # str |  (optional)
item_type = 'item_type_example' # str | Specifies the type of shared item being requested. The accepted values are: -envelopes: returns information about envelope sharing between users. (optional)
search_text = 'search_text_example' # str | This can be used to filter user names in the response. The wild-card ‘*’ (asterisk) can be used around the string. (optional)
shared = 'shared_example' # str | Specifies which users should be included in the response. Multiple values can be used in the query by using a comma separated list of shared values. If the requestor does not have account administrator privileges, the shared_to value is used. Requestors that do not have account administrator privileges can only use the shared_to, any other setting will result in an error. The accepted values are:  -not_shared: Returns account users that the specified item type is not being shared with and that are not sharing the specified item type with the user.  User X (Share) X Account user  -shared_to: Returns account users that the specified item type is not being shared with and who are sharing the specified item type with the user (only shared to the user).  User X (Share) Account user  -shared_from: Returns account users that the specified item type is being shared with and who are not sharing the specified item type with the user (only shared from the user).  User (Share) >> Account user  -shared_to_and_from: Returns account users that the specified item type is being shared with and who are sharing the specified item type with the user.  User << (Share) >> Account user (optional)
start_position = 'start_position_example' # str | If the response set exceeds Count, this can be used to specify that the method should return users starting at the specified index. The first index is 0, and should be used in the first GET call. Typically this number is a multiple of Count. If no value is specified, this defaults to be 0.  (optional)
user_ids = 'user_ids_example' # str | A comma separated list of userIds for whom the shared item information is being requested.  (optional)

try: 
    # Reserved: Gets the shared item status for one or more users.
    api_response = api_instance.list_shared_access(account_id, count=count, envelopes_not_shared_user_status=envelopes_not_shared_user_status, folder_ids=folder_ids, item_type=item_type, search_text=search_text, shared=shared, start_position=start_position, user_ids=user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_shared_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **count** | **str**| Specifies maximum number of results included in the response. If no value is specified, this defaults to 1000. | [optional] 
 **envelopes_not_shared_user_status** | **str**|  | [optional] 
 **folder_ids** | **str**|  | [optional] 
 **item_type** | **str**| Specifies the type of shared item being requested. The accepted values are: -envelopes: returns information about envelope sharing between users. | [optional] 
 **search_text** | **str**| This can be used to filter user names in the response. The wild-card ‘*’ (asterisk) can be used around the string. | [optional] 
 **shared** | **str**| Specifies which users should be included in the response. Multiple values can be used in the query by using a comma separated list of shared values. If the requestor does not have account administrator privileges, the shared_to value is used. Requestors that do not have account administrator privileges can only use the shared_to, any other setting will result in an error. The accepted values are:  -not_shared: Returns account users that the specified item type is not being shared with and that are not sharing the specified item type with the user.  User X (Share) X Account user  -shared_to: Returns account users that the specified item type is not being shared with and who are sharing the specified item type with the user (only shared to the user).  User X (Share) Account user  -shared_from: Returns account users that the specified item type is being shared with and who are not sharing the specified item type with the user (only shared from the user).  User (Share) &gt;&gt; Account user  -shared_to_and_from: Returns account users that the specified item type is being shared with and who are sharing the specified item type with the user.  User &lt;&lt; (Share) &gt;&gt; Account user | [optional] 
 **start_position** | **str**| If the response set exceeds Count, this can be used to specify that the method should return users starting at the specified index. The first index is 0, and should be used in the first GET call. Typically this number is a multiple of Count. If no value is specified, this defaults to be 0.  | [optional] 
 **user_ids** | **str**| A comma separated list of userIds for whom the shared item information is being requested.  | [optional] 

### Return type

[**AccountSharedAccess**](AccountSharedAccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signature_providers**
> AccountSignatureProviders list_signature_providers(account_id)

Returns Account available signature providers for specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Returns Account available signature providers for specified account.
    api_response = api_instance.list_signature_providers(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_signature_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**AccountSignatureProviders**](AccountSignatureProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unsupported_file_types**
> FileTypeList list_unsupported_file_types(account_id)

Gets a list of unsupported file types.

Retrieves a list of file types (mime-types and file-extensions) that are not supported for upload through the DocuSign system.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Gets a list of unsupported file types.
    api_response = api_instance.list_unsupported_file_types(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_unsupported_file_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**FileTypeList**](FileTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_tab_settings**
> TabAccountSettings update_account_tab_settings(account_id, tab_account_settings=tab_account_settings)

Modifies tab settings for specified account

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
tab_account_settings = docusign.TabAccountSettings() # TabAccountSettings |  (optional)

try: 
    # Modifies tab settings for specified account
    api_response = api_instance.update_account_tab_settings(account_id, tab_account_settings=tab_account_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account_tab_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **tab_account_settings** | [**TabAccountSettings**](TabAccountSettings.md)|  | [optional] 

### Return type

[**TabAccountSettings**](TabAccountSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brand**
> Brand update_brand(account_id, brand_id, brand=brand)

Updates an existing brand.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
brand = docusign.Brand() # Brand |  (optional)

try: 
    # Updates an existing brand.
    api_response = api_instance.update_brand(account_id, brand_id, brand=brand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_brand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **brand** | [**Brand**](Brand.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brand_logo_by_type**
> update_brand_logo_by_type(account_id, brand_id, logo_type)

Put one branding logo.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
logo_type = 'logo_type_example' # str | One of **Primary**, **Secondary** or **Email**.

try: 
    # Put one branding logo.
    api_instance.update_brand_logo_by_type(account_id, brand_id, logo_type)
except ApiException as e:
    print("Exception when calling AccountsApi->update_brand_logo_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **logo_type** | **str**| One of **Primary**, **Secondary** or **Email**. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brand_resources_by_content_type**
> BrandResources update_brand_resources_by_content_type(account_id, brand_id, resource_content_type)

Uploads a branding resource file.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
brand_id = 'brand_id_example' # str | The unique identifier of a brand.
resource_content_type = 'resource_content_type_example' # str | 

try: 
    # Uploads a branding resource file.
    api_response = api_instance.update_brand_resources_by_content_type(account_id, brand_id, resource_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_brand_resources_by_content_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **brand_id** | **str**| The unique identifier of a brand. | 
 **resource_content_type** | **str**|  | 

### Return type

[**BrandResources**](BrandResources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_consumer_disclosure**
> ConsumerDisclosure update_consumer_disclosure(account_id, lang_code, include_metadata=include_metadata, consumer_disclosure=consumer_disclosure)

Update Consumer Disclosure.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
lang_code = 'lang_code_example' # str | The simple type enumeration the language used in the response. The supported languages, with the language value shown in parenthesis, are:Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi). Additionally, the value can be set to �browser� to automatically detect the browser language being used by the viewer and display the disclosure in that language.
include_metadata = 'include_metadata_example' # str |  (optional)
consumer_disclosure = docusign.ConsumerDisclosure() # ConsumerDisclosure |  (optional)

try: 
    # Update Consumer Disclosure.
    api_response = api_instance.update_consumer_disclosure(account_id, lang_code, include_metadata=include_metadata, consumer_disclosure=consumer_disclosure)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_consumer_disclosure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **lang_code** | **str**| The simple type enumeration the language used in the response. The supported languages, with the language value shown in parenthesis, are:Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Bahasa Indonesia (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Bahasa Melayu (ms), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi). Additionally, the value can be set to �browser� to automatically detect the browser language being used by the viewer and display the disclosure in that language. | 
 **include_metadata** | **str**|  | [optional] 
 **consumer_disclosure** | [**ConsumerDisclosure**](ConsumerDisclosure.md)|  | [optional] 

### Return type

[**ConsumerDisclosure**](ConsumerDisclosure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> CustomFields update_custom_field(account_id, custom_field_id, apply_to_templates=apply_to_templates, custom_field=custom_field)

Updates an existing account custom field.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
custom_field_id = 'custom_field_id_example' # str | 
apply_to_templates = 'apply_to_templates_example' # str |  (optional)
custom_field = docusign.CustomField() # CustomField |  (optional)

try: 
    # Updates an existing account custom field.
    api_response = api_instance.update_custom_field(account_id, custom_field_id, apply_to_templates=apply_to_templates, custom_field=custom_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **custom_field_id** | **str**|  | 
 **apply_to_templates** | **str**|  | [optional] 
 **custom_field** | [**CustomField**](CustomField.md)|  | [optional] 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_e_note_configuration**
> ENoteConfiguration update_e_note_configuration(account_id, e_note_configuration=e_note_configuration)

Updates configuration information for the eNote eOriginal integration.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
e_note_configuration = docusign.ENoteConfiguration() # ENoteConfiguration |  (optional)

try: 
    # Updates configuration information for the eNote eOriginal integration.
    api_response = api_instance.update_e_note_configuration(account_id, e_note_configuration=e_note_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_e_note_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **e_note_configuration** | [**ENoteConfiguration**](ENoteConfiguration.md)|  | [optional] 

### Return type

[**ENoteConfiguration**](ENoteConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_rules**
> AccountPasswordRules update_password_rules(account_id, account_password_rules=account_password_rules)

Update the password rules

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
account_password_rules = docusign.AccountPasswordRules() # AccountPasswordRules |  (optional)

try: 
    # Update the password rules
    api_response = api_instance.update_password_rules(account_id, account_password_rules=account_password_rules)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_password_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **account_password_rules** | [**AccountPasswordRules**](AccountPasswordRules.md)|  | [optional] 

### Return type

[**AccountPasswordRules**](AccountPasswordRules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_profile**
> PermissionProfile update_permission_profile(account_id, permission_profile_id, include=include, permission_profile=permission_profile)

Updates a permission profile within the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
permission_profile_id = 'permission_profile_id_example' # str | 
include = 'include_example' # str |  (optional)
permission_profile = docusign.PermissionProfile() # PermissionProfile |  (optional)

try: 
    # Updates a permission profile within the specified account.
    api_response = api_instance.update_permission_profile(account_id, permission_profile_id, include=include, permission_profile=permission_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_permission_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **permission_profile_id** | **str**|  | 
 **include** | **str**|  | [optional] 
 **permission_profile** | [**PermissionProfile**](PermissionProfile.md)|  | [optional] 

### Return type

[**PermissionProfile**](PermissionProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> update_settings(account_id, account_settings_information=account_settings_information)

Updates the account settings for an account.

Updates the account settings for the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
account_settings_information = docusign.AccountSettingsInformation() # AccountSettingsInformation |  (optional)

try: 
    # Updates the account settings for an account.
    api_instance.update_settings(account_id, account_settings_information=account_settings_information)
except ApiException as e:
    print("Exception when calling AccountsApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **account_settings_information** | [**AccountSettingsInformation**](AccountSettingsInformation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shared_access**
> AccountSharedAccess update_shared_access(account_id, item_type=item_type, user_ids=user_ids, account_shared_access=account_shared_access)

Reserved: Sets the shared access information for users.

Reserved: Sets the shared access information for one or more users.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
item_type = 'item_type_example' # str |  (optional)
user_ids = 'user_ids_example' # str |  (optional)
account_shared_access = docusign.AccountSharedAccess() # AccountSharedAccess |  (optional)

try: 
    # Reserved: Sets the shared access information for users.
    api_response = api_instance.update_shared_access(account_id, item_type=item_type, user_ids=user_ids, account_shared_access=account_shared_access)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_shared_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **item_type** | **str**|  | [optional] 
 **user_ids** | **str**|  | [optional] 
 **account_shared_access** | [**AccountSharedAccess**](AccountSharedAccess.md)|  | [optional] 

### Return type

[**AccountSharedAccess**](AccountSharedAccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_watermark**
> Watermark update_watermark(account_id, watermark=watermark)

Update watermark information.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.AccountsApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
watermark = docusign.Watermark() # Watermark |  (optional)

try: 
    # Update watermark information.
    api_response = api_instance.update_watermark(account_id, watermark=watermark)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_watermark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **watermark** | [**Watermark**](Watermark.md)|  | [optional] 

### Return type

[**Watermark**](Watermark.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

