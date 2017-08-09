# PaymentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_id** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**gateway_account_id** | **str** |  | [optional] 
**gateway_name** | **str** |  | [optional] 
**line_items** | [**list[PaymentLineItem]**](PaymentLineItem.md) |  | [optional] 
**status** | **str** | Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later. | [optional] 
**total** | [**Money**](Money.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


