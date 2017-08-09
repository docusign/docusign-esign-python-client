# PowerForm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date_time** | **str** | Indicates the date and time the item was created. | [optional] 
**email_body** | **str** | Specifies the email body of the message sent to the recipient.   Maximum length: 10000 characters.  | [optional] 
**email_subject** | **str** | Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject. | [optional] 
**envelopes** | [**list[Envelope]**](Envelope.md) |  | [optional] 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**instructions** | **str** |  | [optional] 
**is_active** | **str** |  | [optional] 
**last_used** | **str** |  | [optional] 
**limit_use_interval** | **str** |  | [optional] 
**limit_use_interval_enabled** | **str** |  | [optional] 
**limit_use_interval_units** | **str** |  | [optional] 
**max_use_enabled** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**power_form_id** | **str** |  | [optional] 
**power_form_url** | **str** |  | [optional] 
**recipients** | [**list[PowerFormRecipient]**](PowerFormRecipient.md) | An array of powerform recipients. | [optional] 
**sender_name** | **str** |  | [optional] 
**sender_user_id** | **str** |  | [optional] 
**signing_mode** | **str** |  | [optional] 
**template_id** | **str** | The unique identifier of the template. If this is not provided, DocuSign will generate a value.  | [optional] 
**template_name** | **str** |  | [optional] 
**times_used** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**uses_remaining** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


