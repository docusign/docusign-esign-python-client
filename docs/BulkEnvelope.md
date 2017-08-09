# BulkEnvelope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_recipient_row** | **str** | Reserved: TBD | [optional] 
**bulk_status** | **str** | Indicates the status of the bulk send operation. Returned values can be: * queued * processing * sent * failed | [optional] 
**email** | **str** |  | [optional] 
**envelope_id** | **str** | The envelope ID of the envelope status that failed to post. | [optional] 
**envelope_uri** | **str** | Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes. | [optional] 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**name** | **str** |  | [optional] 
**submitted_date_time** | **str** |  | [optional] 
**transaction_id** | **str** |  Used to identify an envelope. The id is a sender-generated value and is valid in the DocuSign system for 7 days. It is recommended that a transaction ID is used for offline signing to ensure that an envelope is not sent multiple times. The &#x60;transactionId&#x60; property can be used determine an envelope&#39;s status (i.e. was it created or not) in cases where the internet connection was lost before the envelope status was returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


