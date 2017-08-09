# IntegratedUserInfoList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_users_selected** | **str** |  | [optional] 
**end_position** | **str** | The last position in the result set.  | [optional] 
**next_uri** | **str** | The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.  | [optional] 
**previous_uri** | **str** | The postal code for the billing address. | [optional] 
**result_set_size** | **str** | The number of results returned in this response.  | [optional] 
**start_position** | **str** | Starting position of the current result set. | [optional] 
**total_set_size** | **str** | The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response. | [optional] 
**users** | [**list[UserInfo]**](UserInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


