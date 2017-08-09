# BillingPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_store_products** | [**list[AppStoreProduct]**](AppStoreProduct.md) | Reserved: TBD | [optional] 
**currency_plan_prices** | [**list[CurrencyPlanPrice]**](CurrencyPlanPrice.md) | Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, and seatFee that are configured for this plan feature set. | [optional] 
**enable_support** | **str** | When set to **true**, then customer support is provided as part of the account plan. | [optional] 
**included_seats** | **str** | The number of seats (users) included. | [optional] 
**other_discount_percent** | **str** |  | [optional] 
**payment_cycle** | **str** |  The payment cycle associated with the plan. The possible values are: Monthly or Annually.  | [optional] 
**payment_method** | **str** |  | [optional] 
**per_seat_price** | **str** | The per seat price for the plan. | [optional] 
**plan_classification** | **str** | Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free. | [optional] 
**plan_feature_sets** | [**list[FeatureSet]**](FeatureSet.md) |  | [optional] 
**plan_id** | **str** |  | [optional] 
**plan_name** | **str** | The name of the Billing Plan. | [optional] 
**seat_discounts** | [**list[SeatDiscount]**](SeatDiscount.md) |  | [optional] 
**support_incident_fee** | **str** | The support incident fee charged for each support incident. | [optional] 
**support_plan_fee** | **str** | The support plan fee charged for this plan. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


