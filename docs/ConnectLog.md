# ConnectLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account ID associated with the envelope. | [optional] 
**config_url** | **str** | The web address of the listener or Retrieving Service end point for Connect. | [optional] 
**connect_debug_log** | [**list[ConnectDebugLog]**](ConnectDebugLog.md) | A complex element containing information about the Connect configuration, error details, date/time, description and payload.  This is only included in the response if the query additional_info&#x3D;true is used. | [optional] 
**connect_id** | **str** | The identifier for the Connect configuration that failed. If an account has multiple Connect configurations, this value is used to look up the Connect configuration for the failed post. | [optional] 
**created** | **str** | The date and time the entry was created. | [optional] 
**email** | **str** | The email that sent the envelope. | [optional] 
**envelope_id** | **str** | The envelope ID of the envelope status that failed to post. | [optional] 
**error** | **str** | The error that caused the Connect post to fail. | [optional] 
**failure_id** | **str** | The failure log ID for the failure. | [optional] 
**failure_uri** | **str** | The URI for the failure. | [optional] 
**last_try** | **str** | The date and time the last attempt to post. | [optional] 
**log_id** | **str** | The Connect log ID for the entry. | [optional] 
**log_uri** | **str** | The URI for the log item. | [optional] 
**retry_count** | **str** | The number of times the Connect post has been retried. | [optional] 
**retry_uri** | **str** | The UEI to retry to publish the Connect failure. | [optional] 
**status** | **str** | The new envelope status for the failed Connect post. The possible values are: Any, Voided, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut, Template, or Processing. | [optional] 
**subject** | **str** | The envelope subject. | [optional] 
**user_name** | **str** | The name of the envelope sender. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


