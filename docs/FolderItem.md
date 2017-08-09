# FolderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_date_time** | **str** | Specifies the date and time this item was completed. | [optional] 
**created_date_time** | **str** | Indicates the date and time the item was created. | [optional] 
**custom_fields** | [**list[CustomFieldV2]**](CustomFieldV2.md) | An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters. | [optional] 
**description** | **str** |  | [optional] 
**envelope_id** | **str** | The envelope ID of the envelope status that failed to post. | [optional] 
**envelope_uri** | **str** | Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes. | [optional] 
**is21_cfr_part11** | **str** | When set to **true**, indicates that this module is enabled on the account. | [optional] 
**is_signature_provider_envelope** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_name** | **str** | Name of the envelope owner. | [optional] 
**page_count** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**sender_email** | **str** |  | [optional] 
**sender_name** | **str** | Name of the envelope sender. | [optional] 
**sent_date_time** | **str** | The date and time the envelope was sent. | [optional] 
**shared** | **str** | When set to **true**, this custom tab is shared. | [optional] 
**status** | **str** | Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later. | [optional] 
**subject** | **str** |  | [optional] 
**template_id** | **str** | The unique identifier of the template. If this is not provided, DocuSign will generate a value.  | [optional] 
**uri** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


