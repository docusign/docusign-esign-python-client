# WorkspaceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_authorization** | [**WorkspaceUserAuthorization**](WorkspaceUserAuthorization.md) |  | [optional] 
**content_type** | **str** |  | [optional] 
**created** | **str** | The UTC DateTime when the workspace item was created. | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_information** | [**WorkspaceUser**](WorkspaceUser.md) |  | [optional] 
**extension** | **str** |  | [optional] 
**file_size** | **str** |  | [optional] 
**file_uri** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_public** | **str** |  If true, this supersedes need for bit mask permission with workspaceUserAuthorization | [optional] 
**last_modified** | **str** |  | [optional] 
**last_modified_by_id** | **str** | Utc date and time the comment was last updated (can only be done by creator) | [optional] 
**last_modified_by_information** | [**WorkspaceUser**](WorkspaceUser.md) |  | [optional] 
**name** | **str** | A simple string description of the item, such as a file name or a folder name. | [optional] 
**page_count** | **str** |  | [optional] 
**parent_folder_id** | **str** | The ID of the parent folder. This is the GUID of the parent folder, or the special value &#39;root&#39; for the root folder. | [optional] 
**parent_folder_uri** | **str** |  | [optional] 
**type** | **str** | The type of the workspace item. Valid values are file, folder. | [optional] 
**uri** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


