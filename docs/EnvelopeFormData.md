# EnvelopeFormData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_subject** | **str** | Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject. | [optional] 
**envelope_id** | **str** | The envelope ID of the envelope status that failed to post. | [optional] 
**form_data** | [**list[NameValue]**](NameValue.md) |  | [optional] 
**recipient_form_data** | [**list[RecipientFormData]**](RecipientFormData.md) |  | [optional] 
**sent_date_time** | **str** | The date and time the envelope was sent. | [optional] 
**status** | **str** | Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


