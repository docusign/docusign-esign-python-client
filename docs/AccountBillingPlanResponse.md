# AccountBillingPlanResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**billing_address_is_credit_card_address** | **str** | When set to **true**, the credit card address information is the same as that returned as the billing address. If false, then the billing address is considered a billing contact address, and the credit card address can be different. | [optional] 
**billing_plan** | [**AccountBillingPlan**](AccountBillingPlan.md) |  | [optional] 
**credit_card_information** | [**CreditCardInformation**](CreditCardInformation.md) |  | [optional] 
**payment_processor_information** | [**PaymentProcessorInformation**](PaymentProcessorInformation.md) |  | [optional] 
**referral_information** | [**ReferralInformation**](ReferralInformation.md) |  | [optional] 
**successor_plans** | [**list[BillingPlan]**](BillingPlan.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


