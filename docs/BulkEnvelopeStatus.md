# BulkEnvelopeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | Specifies an identifier which can be used to retrieve a more detailed status of individual bulk recipient batches. | [optional] 
**batch_size** | **str** | The number of items returned in this response. | [optional] 
**bulk_envelopes** | [**list[BulkEnvelope]**](BulkEnvelope.md) | Reserved: TBD | [optional] 
**bulk_envelopes_batch_uri** | **str** | Reserved: TBD | [optional] 
**end_position** | **str** | The last position in the result set.  | [optional] 
**failed** | **str** | The number of entries with a status of failed.  | [optional] 
**next_uri** | **str** | The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.  | [optional] 
**previous_uri** | **str** | The postal code for the billing address. | [optional] 
**queued** | **str** | The number of entries with a status of queued.  | [optional] 
**result_set_size** | **str** | The number of results returned in this response.  | [optional] 
**sent** | **str** | The number of entries with a status of sent. | [optional] 
**start_position** | **str** | Starting position of the current result set. | [optional] 
**submitted_date** | **str** |  | [optional] 
**total_set_size** | **str** | The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


