# UserInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_management_granular** | [**UserAccountManagementGranularInformation**](UserAccountManagementGranularInformation.md) |  | [optional] 
**activation_access_code** | **str** | The activation code the new user must enter when activating their account. | [optional] 
**created_date_time** | **str** | Indicates the date and time the item was created. | [optional] 
**custom_settings** | [**list[NameValue]**](NameValue.md) | The name/value pair information for the user custom setting. | [optional] 
**email** | **str** |  | [optional] 
**enable_connect_for_user** | **str** | Specifies whether the user is enabled for updates from DocuSign Connect. Valid values: true or false. | [optional] 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**first_name** | **str** | The user’s first name.  Maximum Length: 50 characters. | [optional] 
**forgotten_password_info** | [**ForgottenPasswordInformation**](ForgottenPasswordInformation.md) |  | [optional] 
**group_list** | [**list[Group]**](Group.md) | A list of the group information for groups to add the user to. Group information can be found by calling [ML:GET group information]. The only required parameter is groupId.   The parameters are:  * groupId – The DocuSign group ID for the group. * groupName – The name of the group * permissionProfileId – The ID of the permission profile associated with the group. * groupType – The group type.  | [optional] 
**home_address** | [**AddressInformationV2**](AddressInformationV2.md) |  | [optional] 
**initials_image_uri** | **str** | Contains the URI for an endpoint that you can use to retrieve the initials image. | [optional] 
**is_admin** | **str** | Determines if the feature set is actively set as part of the plan. | [optional] 
**last_login** | **str** | Shows the date-time when the user last logged on to the system. | [optional] 
**last_name** | **str** | The user’s last name.  Maximum Length: 50 characters. | [optional] 
**login_status** | **str** | Shows the current status of the user’s password. Possible values are:   * password_reset * password_active * password_expired * password_locked * password_reset_failed   | [optional] 
**middle_name** | **str** | The user’s middle name.  Maximum Length: 50 characters. | [optional] 
**password** | **str** |  | [optional] 
**password_expiration** | **str** |  | [optional] 
**permission_profile_id** | **str** |  | [optional] 
**permission_profile_name** | **str** |  | [optional] 
**profile_image_uri** | **str** |  | [optional] 
**send_activation_on_invalid_login** | **str** | When set to **true**, specifies that an additional activation email is sent to the user if they fail a log on before activating their account.  | [optional] 
**signature_image_uri** | **str** | Contains the URI for an endpoint that you can use to retrieve the signature image. | [optional] 
**suffix_name** | **str** | The suffix for the user&#39;s name.   Maximum Length: 50 characters.  | [optional] 
**title** | **str** | The title of the user. | [optional] 
**uri** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_profile_last_modified_date** | **str** |  | [optional] 
**user_settings** | [**list[NameValue]**](NameValue.md) |  The name/value pair information for user settings. These determine the actions that a user can take in the account. The &#x60;[ML:userSettings]&#x60; are listed and described below. | [optional] 
**user_status** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 
**work_address** | [**AddressInformationV2**](AddressInformationV2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


