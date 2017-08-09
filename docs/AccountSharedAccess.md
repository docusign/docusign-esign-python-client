# AccountSharedAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account ID associated with the envelope. | [optional] 
**end_position** | **str** | The last position in the result set.  | [optional] 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**next_uri** | **str** | The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.  | [optional] 
**previous_uri** | **str** | The postal code for the billing address. | [optional] 
**result_set_size** | **str** | The number of results returned in this response.  | [optional] 
**shared_access** | [**list[MemberSharedItems]**](MemberSharedItems.md) | A complex type containing the shared access information to an envelope for the users specified in the request. | [optional] 
**start_position** | **str** | Starting position of the current result set. | [optional] 
**total_set_size** | **str** | The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


