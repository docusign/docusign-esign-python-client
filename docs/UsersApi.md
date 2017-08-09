# docusign.UsersApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UsersApi.md#create) | **POST** /v2/accounts/{accountId}/users | Adds news user to the specified account.
[**create_signatures**](UsersApi.md#create_signatures) | **POST** /v2/accounts/{accountId}/users/{userId}/signatures | Adds user Signature and initials images to a Signature.
[**delete**](UsersApi.md#delete) | **DELETE** /v2/accounts/{accountId}/users | Removes users account privileges.
[**delete_contact_with_id**](UsersApi.md#delete_contact_with_id) | **DELETE** /v2/accounts/{accountId}/contacts/{contactId} | Replaces a particular contact associated with an account for the DocuSign service.
[**delete_contacts**](UsersApi.md#delete_contacts) | **DELETE** /v2/accounts/{accountId}/contacts | Delete contacts associated with an account for the DocuSign service.
[**delete_custom_settings**](UsersApi.md#delete_custom_settings) | **DELETE** /v2/accounts/{accountId}/users/{userId}/custom_settings | Deletes custom user settings for a specified user.
[**delete_profile_image**](UsersApi.md#delete_profile_image) | **DELETE** /v2/accounts/{accountId}/users/{userId}/profile/image | Deletes the user profile image for the specified user.
[**delete_signature**](UsersApi.md#delete_signature) | **DELETE** /v2/accounts/{accountId}/users/{userId}/signatures/{signatureId} | Removes removes signature information for the specified user.
[**delete_signature_image**](UsersApi.md#delete_signature_image) | **DELETE** /v2/accounts/{accountId}/users/{userId}/signatures/{signatureId}/{imageType} | Deletes the user initials image or the  user signature image for the specified user.
[**get_contact_by_id**](UsersApi.md#get_contact_by_id) | **GET** /v2/accounts/{accountId}/contacts/{contactId} | Gets a particular contact associated with the user&#39;s account.
[**get_information**](UsersApi.md#get_information) | **GET** /v2/accounts/{accountId}/users/{userId} | Gets the user information for a specified user.
[**get_profile**](UsersApi.md#get_profile) | **GET** /v2/accounts/{accountId}/users/{userId}/profile | Retrieves the user profile for a specified user.
[**get_profile_image**](UsersApi.md#get_profile_image) | **GET** /v2/accounts/{accountId}/users/{userId}/profile/image | Retrieves the user profile image for the specified user.
[**get_settings**](UsersApi.md#get_settings) | **GET** /v2/accounts/{accountId}/users/{userId}/settings | Gets the user account settings for a specified user.
[**get_signature**](UsersApi.md#get_signature) | **GET** /v2/accounts/{accountId}/users/{userId}/signatures/{signatureId} | Gets the user signature information for the specified user.
[**get_signature_image**](UsersApi.md#get_signature_image) | **GET** /v2/accounts/{accountId}/users/{userId}/signatures/{signatureId}/{imageType} | Retrieves the user initials image or the  user signature image for the specified user.
[**list**](UsersApi.md#list) | **GET** /v2/accounts/{accountId}/users | Retrieves the list of users for the specified account.
[**list_custom_settings**](UsersApi.md#list_custom_settings) | **GET** /v2/accounts/{accountId}/users/{userId}/custom_settings | Retrieves the custom user settings for a specified user.
[**list_signatures**](UsersApi.md#list_signatures) | **GET** /v2/accounts/{accountId}/users/{userId}/signatures | Retrieves a list of user signature definitions for a specified user.
[**post_contacts**](UsersApi.md#post_contacts) | **POST** /v2/accounts/{accountId}/contacts | Imports multiple new contacts into the contacts collection from CSV, JSON, or XML (based on content type).
[**put_contacts**](UsersApi.md#put_contacts) | **PUT** /v2/accounts/{accountId}/contacts | Replaces contacts associated with an account for the DocuSign service.
[**update_custom_settings**](UsersApi.md#update_custom_settings) | **PUT** /v2/accounts/{accountId}/users/{userId}/custom_settings | Adds or updates custom user settings for the specified user.
[**update_profile**](UsersApi.md#update_profile) | **PUT** /v2/accounts/{accountId}/users/{userId}/profile | Updates the user profile information for the specified user.
[**update_profile_image**](UsersApi.md#update_profile_image) | **PUT** /v2/accounts/{accountId}/users/{userId}/profile/image | Updates the user profile image for a specified user.
[**update_settings**](UsersApi.md#update_settings) | **PUT** /v2/accounts/{accountId}/users/{userId}/settings | Updates the user account settings for a specified user.
[**update_signature**](UsersApi.md#update_signature) | **PUT** /v2/accounts/{accountId}/users/{userId}/signatures/{signatureId} | Updates the user signature for a specified user.
[**update_signature_image**](UsersApi.md#update_signature_image) | **PUT** /v2/accounts/{accountId}/users/{userId}/signatures/{signatureId}/{imageType} | Updates the user signature image or user initials image for the specified user.
[**update_signatures**](UsersApi.md#update_signatures) | **PUT** /v2/accounts/{accountId}/users/{userId}/signatures | Adds/updates a user signature.
[**update_user**](UsersApi.md#update_user) | **PUT** /v2/accounts/{accountId}/users/{userId} | Updates the specified user information.
[**update_users**](UsersApi.md#update_users) | **PUT** /v2/accounts/{accountId}/users | Change one or more user in the specified account.


# **create**
> NewUsersSummary create(account_id, new_users_definition=new_users_definition)

Adds news user to the specified account.

Adds new users to your account. Set the `userSettings` property in the request to specify the actions the users can perform on the account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
new_users_definition = docusign.NewUsersDefinition() # NewUsersDefinition |  (optional)

try: 
    # Adds news user to the specified account.
    api_response = api_instance.create(account_id, new_users_definition=new_users_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **new_users_definition** | [**NewUsersDefinition**](NewUsersDefinition.md)|  | [optional] 

### Return type

[**NewUsersSummary**](NewUsersSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_signatures**
> UserSignaturesInformation create_signatures(account_id, user_id, user_signatures_information=user_signatures_information)

Adds user Signature and initials images to a Signature.

Adds a user signature image and/or user initials image to the specified user.   The userId property specified in the endpoint must match the authenticated user's userId and the user must be a member of the account.  The rules and processes associated with this are:  * If Content-Type is set to application/json, then the default behavior for creating a default signature image, based on the name and a DocuSign font, is used. * If Content-Type is set to multipart/form-data, then the request must contain a first part with the user signature information, followed by parts that contain the images.  For each Image part, the Content-Disposition header has a \"filename\" value that is used to map to the `signatureName` and/or `signatureInitials` properties in the JSON to the image.   For example:  `Content-Disposition: file; filename=\"Ron Test20121127083900\"`  If no matching image (by filename value) is found, then the image is not set. One, both, or neither of the signature and initials images can be set with this call.  The Content-Transfer-Encoding: base64 header, set in the header for the part containing the image, can be set to indicate that the images are formatted as base64 instead of as binary.  If successful, 200-OK is returned, and a JSON structure containing the signature information is provided, note that the signatureId can change with each API POST, PUT, or DELETE since the changes to the signature structure cause the current signature to be closed, and a new signature record to be created.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
user_signatures_information = docusign.UserSignaturesInformation() # UserSignaturesInformation |  (optional)

try: 
    # Adds user Signature and initials images to a Signature.
    api_response = api_instance.create_signatures(account_id, user_id, user_signatures_information=user_signatures_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **user_signatures_information** | [**UserSignaturesInformation**](UserSignaturesInformation.md)|  | [optional] 

### Return type

[**UserSignaturesInformation**](UserSignaturesInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> UsersResponse delete(account_id, user_info_list=user_info_list)

Removes users account privileges.

This closes one or more user records in the account. Users are never deleted from an account, but closing a user prevents them from using account functions.  The response returns whether the API execution was successful (200 - OK) or  if it failed. The response contains a user structure similar to the request and includes the user changes. If an error occurred during the DELETE operation for any of the users, the response for that user contains an `errorDetails` node with `errorCode` and `message` properties.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_info_list = docusign.UserInfoList() # UserInfoList |  (optional)

try: 
    # Removes users account privileges.
    api_response = api_instance.delete(account_id, user_info_list=user_info_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_info_list** | [**UserInfoList**](UserInfoList.md)|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_with_id**
> ContactUpdateResponse delete_contact_with_id(account_id, contact_id)

Replaces a particular contact associated with an account for the DocuSign service.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
contact_id = 'contact_id_example' # str | The unique identifier of a person in the contacts address book.

try: 
    # Replaces a particular contact associated with an account for the DocuSign service.
    api_response = api_instance.delete_contact_with_id(account_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_contact_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **contact_id** | **str**| The unique identifier of a person in the contacts address book. | 

### Return type

[**ContactUpdateResponse**](ContactUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts**
> ContactUpdateResponse delete_contacts(account_id, contact_mod_request=contact_mod_request)

Delete contacts associated with an account for the DocuSign service.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
contact_mod_request = docusign.ContactModRequest() # ContactModRequest |  (optional)

try: 
    # Delete contacts associated with an account for the DocuSign service.
    api_response = api_instance.delete_contacts(account_id, contact_mod_request=contact_mod_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **contact_mod_request** | [**ContactModRequest**](ContactModRequest.md)|  | [optional] 

### Return type

[**ContactUpdateResponse**](ContactUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_settings**
> CustomSettingsInformation delete_custom_settings(account_id, user_id, custom_settings_information=custom_settings_information)

Deletes custom user settings for a specified user.

Deletes the specified custom user settings for a single user.  ###Deleting Grouped Custom User Settings###  If the custom user settings you want to delete are grouped, you must include the following information in the header, after Content-Type, in the request:  `X-DocuSign-User-Settings-Key:group_name`  Where the `group_name` is your designated name for the group of customer user settings.  If the extra header information is not included, only the custom user settings that were added without a group are deleted.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
custom_settings_information = docusign.CustomSettingsInformation() # CustomSettingsInformation |  (optional)

try: 
    # Deletes custom user settings for a specified user.
    api_response = api_instance.delete_custom_settings(account_id, user_id, custom_settings_information=custom_settings_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_custom_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **custom_settings_information** | [**CustomSettingsInformation**](CustomSettingsInformation.md)|  | [optional] 

### Return type

[**CustomSettingsInformation**](CustomSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile_image**
> delete_profile_image(account_id, user_id)

Deletes the user profile image for the specified user.

Deletes the user profile image from the  specified user's profile.  The userId parameter specified in the endpoint must match the authenticated user's user ID and the user must be a member of the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Deletes the user profile image for the specified user.
    api_instance.delete_profile_image(account_id, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_signature**
> delete_signature(account_id, signature_id, user_id)

Removes removes signature information for the specified user.

Removes the signature information for the user.  The userId parameter specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\".

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signature_id = 'signature_id_example' # str | The ID of the signature being accessed.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Removes removes signature information for the specified user.
    api_instance.delete_signature(account_id, signature_id, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signature_id** | **str**| The ID of the signature being accessed. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_signature_image**
> UserSignature delete_signature_image(account_id, image_type, signature_id, user_id)

Deletes the user initials image or the  user signature image for the specified user.

Deletes the specified initials image or signature image for the specified user.  The function deletes one or the other of the image types, to delete both the initials image and signature image you must call the endpoint twice.  The userId parameter specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` parameter accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\".

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
image_type = 'image_type_example' # str | One of **signature_image** or **initials_image**.
signature_id = 'signature_id_example' # str | The ID of the signature being accessed.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Deletes the user initials image or the  user signature image for the specified user.
    api_response = api_instance.delete_signature_image(account_id, image_type, signature_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_signature_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **image_type** | **str**| One of **signature_image** or **initials_image**. | 
 **signature_id** | **str**| The ID of the signature being accessed. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**UserSignature**](UserSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> ContactGetResponse get_contact_by_id(account_id, contact_id, cloud_provider=cloud_provider)

Gets a particular contact associated with the user's account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
contact_id = 'contact_id_example' # str | The unique identifier of a person in the contacts address book.
cloud_provider = 'cloud_provider_example' # str |  (optional)

try: 
    # Gets a particular contact associated with the user's account.
    api_response = api_instance.get_contact_by_id(account_id, contact_id, cloud_provider=cloud_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **contact_id** | **str**| The unique identifier of a person in the contacts address book. | 
 **cloud_provider** | **str**|  | [optional] 

### Return type

[**ContactGetResponse**](ContactGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_information**
> UserInformation get_information(account_id, user_id, additional_info=additional_info, email=email)

Gets the user information for a specified user.

Retrieves the user information for the specified user.   To return additional user information that details the last login date, login status, and the user's password expiration date, set the optional `additional_info` query string parameter to **true**.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
additional_info = 'additional_info_example' # str | When set to **true**, the full list of user information is returned for each user in the account. (optional)
email = 'email_example' # str |  (optional)

try: 
    # Gets the user information for a specified user.
    api_response = api_instance.get_information(account_id, user_id, additional_info=additional_info, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **additional_info** | **str**| When set to **true**, the full list of user information is returned for each user in the account. | [optional] 
 **email** | **str**|  | [optional] 

### Return type

[**UserInformation**](UserInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> UserProfile get_profile(account_id, user_id)

Retrieves the user profile for a specified user.

Retrieves the user profile information, the privacy settings and personal information (address, phone number, etc.) for the specified user.  The userId parameter specified in the endpoint must match the authenticated user's user ID and the user must be a member of the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Retrieves the user profile for a specified user.
    api_response = api_instance.get_profile(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_image**
> file get_profile_image(account_id, user_id, encoding=encoding)

Retrieves the user profile image for the specified user.

Retrieves the user profile picture for the specified user. The image is returned in the same format as uploaded.  The userId parameter specified in the endpoint must match the authenticated user's user ID and the user must be a member of the specified account.  If successful, the response returns a 200 - OK and the user profile image.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
encoding = 'encoding_example' # str |  (optional)

try: 
    # Retrieves the user profile image for the specified user.
    api_response = api_instance.get_profile_image(account_id, user_id, encoding=encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **encoding** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> UserSettingsInformation get_settings(account_id, user_id)

Gets the user account settings for a specified user.

Retrieves a list of the account settings and email notification information for the specified user.  The response returns the account setting name/value information and the email notification settings for the specified user. For more information about the different user settings, see the [ML:userSettings list].

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Gets the user account settings for a specified user.
    api_response = api_instance.get_settings(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**UserSettingsInformation**](UserSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature**
> UserSignature get_signature(account_id, signature_id, user_id)

Gets the user signature information for the specified user.

Retrieves the structure of a single signature with a known signature name.  The userId specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` parameter accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\".

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signature_id = 'signature_id_example' # str | The ID of the signature being accessed.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Gets the user signature information for the specified user.
    api_response = api_instance.get_signature(account_id, signature_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signature_id** | **str**| The ID of the signature being accessed. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**UserSignature**](UserSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_image**
> file get_signature_image(account_id, image_type, signature_id, user_id, include_chrome=include_chrome)

Retrieves the user initials image or the  user signature image for the specified user.

Retrieves the specified initials image or signature image for the specified user. The image is returned in the same format as uploaded. In the request you can specify if the chrome (the added line and identifier around the initial image) is returned with the image.  The userId property specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` parameter accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\".  ###### Note: Older envelopes might only have chromed images. If getting the non-chromed image fails, try getting the chromed image.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
image_type = 'image_type_example' # str | One of **signature_image** or **initials_image**.
signature_id = 'signature_id_example' # str | The ID of the signature being accessed.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
include_chrome = 'include_chrome_example' # str |  (optional)

try: 
    # Retrieves the user initials image or the  user signature image for the specified user.
    api_response = api_instance.get_signature_image(account_id, image_type, signature_id, user_id, include_chrome=include_chrome)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_signature_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **image_type** | **str**| One of **signature_image** or **initials_image**. | 
 **signature_id** | **str**| The ID of the signature being accessed. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **include_chrome** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> UserInformationList list(account_id, additional_info=additional_info, count=count, email=email, email_substring=email_substring, group_id=group_id, include_usersettings_for_csv=include_usersettings_for_csv, login_status=login_status, not_group_id=not_group_id, start_position=start_position, status=status, user_name_substring=user_name_substring)

Retrieves the list of users for the specified account.

Retrieves the list of users for the specified account.  The response returns the list of users for the account along with the information about the result set. If the `additional_info` query was added to the endpoint and set to **true**, the full user information is returned for each user

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
additional_info = 'additional_info_example' # str | When set to **true**, the full list of user information is returned for each user in the account. (optional)
count = 'count_example' # str | Number of records to return. The number must be greater than 0 and less than or equal to 100.  (optional)
email = 'email_example' # str |  (optional)
email_substring = 'email_substring_example' # str | Filters the returned user records by the email address or a sub-string of email address. (optional)
group_id = 'group_id_example' # str | Filters user records returned by one or more group Id's. (optional)
include_usersettings_for_csv = 'include_usersettings_for_csv_example' # str |  (optional)
login_status = 'login_status_example' # str |  (optional)
not_group_id = 'not_group_id_example' # str |  (optional)
start_position = 'start_position_example' # str | Starting value for the list.  (optional)
status = 'status_example' # str |  (optional)
user_name_substring = 'user_name_substring_example' # str | Filters the user records returned by the user name or a sub-string of user name. (optional)

try: 
    # Retrieves the list of users for the specified account.
    api_response = api_instance.list(account_id, additional_info=additional_info, count=count, email=email, email_substring=email_substring, group_id=group_id, include_usersettings_for_csv=include_usersettings_for_csv, login_status=login_status, not_group_id=not_group_id, start_position=start_position, status=status, user_name_substring=user_name_substring)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **additional_info** | **str**| When set to **true**, the full list of user information is returned for each user in the account. | [optional] 
 **count** | **str**| Number of records to return. The number must be greater than 0 and less than or equal to 100.  | [optional] 
 **email** | **str**|  | [optional] 
 **email_substring** | **str**| Filters the returned user records by the email address or a sub-string of email address. | [optional] 
 **group_id** | **str**| Filters user records returned by one or more group Id&#39;s. | [optional] 
 **include_usersettings_for_csv** | **str**|  | [optional] 
 **login_status** | **str**|  | [optional] 
 **not_group_id** | **str**|  | [optional] 
 **start_position** | **str**| Starting value for the list.  | [optional] 
 **status** | **str**|  | [optional] 
 **user_name_substring** | **str**| Filters the user records returned by the user name or a sub-string of user name. | [optional] 

### Return type

[**UserInformationList**](UserInformationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_settings**
> CustomSettingsInformation list_custom_settings(account_id, user_id)

Retrieves the custom user settings for a specified user.

Retrieves a list of custom user settings for a single user.  Custom settings provide a flexible way to store and retrieve custom user information that can be used in your own system.  ###### Note: Custom user settings are not the same as user account settings.  ###Getting Grouped Custom User Settings###  If the custom user settings you want to retrieve are grouped, you must include the following information in the header, after Content-Type, in the request:  `X-DocuSign-User-Settings-Key:group_name`  Where the `group_name` is your designated name for the group of customer user settings.  If the extra header information is not included, only the custom user settings that were added without a group are retrieved.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Retrieves the custom user settings for a specified user.
    api_response = api_instance.list_custom_settings(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_custom_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**CustomSettingsInformation**](CustomSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signatures**
> UserSignaturesInformation list_signatures(account_id, user_id, stamp_type=stamp_type)

Retrieves a list of user signature definitions for a specified user.

Retrieves the signature definitions for the specified user.  The userId parameter specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` parameter accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\".

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
stamp_type = 'stamp_type_example' # str |  (optional)

try: 
    # Retrieves a list of user signature definitions for a specified user.
    api_response = api_instance.list_signatures(account_id, user_id, stamp_type=stamp_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **stamp_type** | **str**|  | [optional] 

### Return type

[**UserSignaturesInformation**](UserSignaturesInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contacts**
> ContactUpdateResponse post_contacts(account_id, contact_mod_request=contact_mod_request)

Imports multiple new contacts into the contacts collection from CSV, JSON, or XML (based on content type).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
contact_mod_request = docusign.ContactModRequest() # ContactModRequest |  (optional)

try: 
    # Imports multiple new contacts into the contacts collection from CSV, JSON, or XML (based on content type).
    api_response = api_instance.post_contacts(account_id, contact_mod_request=contact_mod_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **contact_mod_request** | [**ContactModRequest**](ContactModRequest.md)|  | [optional] 

### Return type

[**ContactUpdateResponse**](ContactUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contacts**
> ContactUpdateResponse put_contacts(account_id, contact_mod_request=contact_mod_request)

Replaces contacts associated with an account for the DocuSign service.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
contact_mod_request = docusign.ContactModRequest() # ContactModRequest |  (optional)

try: 
    # Replaces contacts associated with an account for the DocuSign service.
    api_response = api_instance.put_contacts(account_id, contact_mod_request=contact_mod_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **contact_mod_request** | [**ContactModRequest**](ContactModRequest.md)|  | [optional] 

### Return type

[**ContactUpdateResponse**](ContactUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_settings**
> CustomSettingsInformation update_custom_settings(account_id, user_id, custom_settings_information=custom_settings_information)

Adds or updates custom user settings for the specified user.

Adds or updates custom user settings for the specified user.  ###### Note: Custom user settings are not the same as user account settings.  Custom settings provide a flexible way to store and retrieve custom user information that you can use in your own system.  **Important**: There is a limit on the size for all the custom user settings for a single user. The limit is 4,000 characters, which includes the XML and JSON structure for the settings.  ### Grouping Custom User Settings ###  You can group custom user settings when adding them. Grouping allows you to retrieve settings that are in a specific group, instead of retrieving all the user custom settings.  To group custom user settings, add the following information in the header, after Content-Type:  `X-DocuSign-User-Settings-Key:group_name`  Where the `group_name` is your designated name for the group of customer user settings. Grouping is shown in the Example Request Body below.  When getting or deleting grouped custom user settings, you must include the extra header information.  Grouping custom user settings is not required and if the extra header information is not included, the custom user settings are added normally and can be retrieved or deleted without including the additional header.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
custom_settings_information = docusign.CustomSettingsInformation() # CustomSettingsInformation |  (optional)

try: 
    # Adds or updates custom user settings for the specified user.
    api_response = api_instance.update_custom_settings(account_id, user_id, custom_settings_information=custom_settings_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_custom_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **custom_settings_information** | [**CustomSettingsInformation**](CustomSettingsInformation.md)|  | [optional] 

### Return type

[**CustomSettingsInformation**](CustomSettingsInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> update_profile(account_id, user_id, user_profile=user_profile)

Updates the user profile information for the specified user.

Updates the user's detail information, profile information, privacy settings, and personal information in the user ID card.  You can also change a user's name by changing the information in the `userDetails` property. When changing a user's name, you can either change the information in the `userName` property OR change the information in `firstName`, `middleName`, `lastName, suffixName`, and `title` properties. Changes to `firstName`, `middleName`, `lastName`, `suffixName`, and `title` properties take precedence over changes to the `userName` property.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
user_profile = docusign.UserProfile() # UserProfile |  (optional)

try: 
    # Updates the user profile information for the specified user.
    api_instance.update_profile(account_id, user_id, user_profile=user_profile)
except ApiException as e:
    print("Exception when calling UsersApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **user_profile** | [**UserProfile**](UserProfile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_image**
> update_profile_image(account_id, user_id)

Updates the user profile image for a specified user.

Updates the user profile image by uploading an image to the user profile.  The supported image formats are: gif, png, jpeg, and bmp. The file must be less than 200K. For best viewing results, DocuSign recommends that the image is no more than 79 pixels wide and high.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Updates the user profile image for a specified user.
    api_instance.update_profile_image(account_id, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->update_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> update_settings(account_id, user_id, user_settings_information=user_settings_information)

Updates the user account settings for a specified user.

Updates the account settings list and email notification types for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
user_settings_information = docusign.UserSettingsInformation() # UserSettingsInformation |  (optional)

try: 
    # Updates the user account settings for a specified user.
    api_instance.update_settings(account_id, user_id, user_settings_information=user_settings_information)
except ApiException as e:
    print("Exception when calling UsersApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **user_settings_information** | [**UserSettingsInformation**](UserSettingsInformation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signature**
> UserSignature update_signature(account_id, signature_id, user_id, close_existing_signature=close_existing_signature, user_signature_definition=user_signature_definition)

Updates the user signature for a specified user.

Creates, or updates, the signature font and initials for the specified user. When creating a signature, you use this resource to create the signature name and then add the signature and initials images into the signature.  ###### Note: This will also create a default signature for the user when one does not exist.  The userId property specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` parameter accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\".

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
signature_id = 'signature_id_example' # str | The ID of the signature being accessed.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
close_existing_signature = 'close_existing_signature_example' # str | When set to **true**, closes the current signature. (optional)
user_signature_definition = docusign.UserSignatureDefinition() # UserSignatureDefinition |  (optional)

try: 
    # Updates the user signature for a specified user.
    api_response = api_instance.update_signature(account_id, signature_id, user_id, close_existing_signature=close_existing_signature, user_signature_definition=user_signature_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **signature_id** | **str**| The ID of the signature being accessed. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **close_existing_signature** | **str**| When set to **true**, closes the current signature. | [optional] 
 **user_signature_definition** | [**UserSignatureDefinition**](UserSignatureDefinition.md)|  | [optional] 

### Return type

[**UserSignature**](UserSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signature_image**
> UserSignature update_signature_image(account_id, image_type, signature_id, user_id)

Updates the user signature image or user initials image for the specified user.

Updates the user signature image or user initials image for the specified user. The supported image formats for this file are: gif, png, jpeg, and bmp. The file must be less than 200K.  The userId property specified in the endpoint must match the authenticated user's user ID and the user must be a member of the account.  The `signatureId` parameter accepts a signature ID or a signature name. DocuSign recommends you use signature ID (`signatureId`), since some names contain characters that do not properly encode into a URL. If you use the user name, it is likely that the name includes spaces. In that case, URL encode the name before using it in the endpoint.   For example encode \"Bob Smith\" as \"Bob%20Smith\". 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
image_type = 'image_type_example' # str | One of **signature_image** or **initials_image**.
signature_id = 'signature_id_example' # str | The ID of the signature being accessed.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.

try: 
    # Updates the user signature image or user initials image for the specified user.
    api_response = api_instance.update_signature_image(account_id, image_type, signature_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_signature_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **image_type** | **str**| One of **signature_image** or **initials_image**. | 
 **signature_id** | **str**| The ID of the signature being accessed. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 

### Return type

[**UserSignature**](UserSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signatures**
> UserSignaturesInformation update_signatures(account_id, user_id, user_signatures_information=user_signatures_information)

Adds/updates a user signature.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
user_signatures_information = docusign.UserSignaturesInformation() # UserSignaturesInformation |  (optional)

try: 
    # Adds/updates a user signature.
    api_response = api_instance.update_signatures(account_id, user_id, user_signatures_information=user_signatures_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **user_signatures_information** | [**UserSignaturesInformation**](UserSignaturesInformation.md)|  | [optional] 

### Return type

[**UserSignaturesInformation**](UserSignaturesInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserInformation update_user(account_id, user_id, user_information=user_information)

Updates the specified user information.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_id = 'user_id_example' # str | The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing.
user_information = docusign.UserInformation() # UserInformation |  (optional)

try: 
    # Updates the specified user information.
    api_response = api_instance.update_user(account_id, user_id, user_information=user_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_id** | **str**| The user ID of the user being accessed. Generally this is the user ID of the authenticated user, but if the authenticated user is an Admin on the account, this may be another user the Admin user is accessing. | 
 **user_information** | [**UserInformation**](UserInformation.md)|  | [optional] 

### Return type

[**UserInformation**](UserInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users**
> UserInformationList update_users(account_id, user_information_list=user_information_list)

Change one or more user in the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.UsersApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
user_information_list = docusign.UserInformationList() # UserInformationList |  (optional)

try: 
    # Change one or more user in the specified account.
    api_response = api_instance.update_users(account_id, user_information_list=user_information_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **user_information_list** | [**UserInformationList**](UserInformationList.md)|  | [optional] 

### Return type

[**UserInformationList**](UserInformationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

