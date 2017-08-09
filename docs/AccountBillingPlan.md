# AccountBillingPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_ons** | [**list[AddOn]**](AddOn.md) | Reserved: | [optional] 
**can_cancel_renewal** | **str** | Reserved: TBD | [optional] 
**can_upgrade** | **str** | When set to **true**, specifies that you can upgrade the account through the API. | [optional] 
**currency_code** | **str** | Specifies the ISO currency code for the account. | [optional] 
**enable_support** | **str** | When set to **true**, then customer support is provided as part of the account plan. | [optional] 
**included_seats** | **str** | The number of seats (users) included. | [optional] 
**incremental_seats** | **str** | Reserved: TBD | [optional] 
**is_downgrade** | **str** |  | [optional] 
**other_discount_percent** | **str** |  Any other percentage discount for the plan.  | [optional] 
**payment_cycle** | **str** |  | [optional] 
**payment_method** | **str** |  The payment method used with the plan. The possible values are: CreditCard, PurchaseOrder, Premium, or Freemium.  | [optional] 
**per_seat_price** | **str** |  | [optional] 
**plan_classification** | **str** | Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free. | [optional] 
**plan_feature_sets** | [**list[FeatureSet]**](FeatureSet.md) | A complex type that sets the feature sets for the account. It contains the following information (all string content):  * currencyFeatureSetPrices - Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, seatFee that are configured for this plan feature set. * envelopeFee - An incremental envelope cost for plans with envelope overages (when isEnabled&#x3D;true). * featureSetId - A unique ID for the feature set. * fixedFee - A one-time fee associated with the plan (when isEnabled&#x3D;true). * isActive - Specifies whether the feature set is actively set as part of the plan. * isEnabled - Specifies whether the feature set is actively enabled as part of the plan. * name - The name of the feature set. * seatFee - An incremental seat cost for seat-based plans (when isEnabled&#x3D;true).  | [optional] 
**plan_id** | **str** |  | [optional] 
**plan_name** | **str** | The name of the Billing Plan. | [optional] 
**renewal_status** | **str** | The renewal status for the account. The acceptable values are:  * auto: The account automatically renews. * queued_for_close: Account will be closed at the billingPeriodEndDate. * queued_for_downgrade: Account will be downgraded at the billingPeriodEndDate. | [optional] 
**seat_discounts** | [**list[SeatDiscount]**](SeatDiscount.md) |  A complex type that contains any seat discount information.  Values are: BeginSeatCount, EndSeatCount, and SeatDiscountPercent.   | [optional] 
**support_incident_fee** | **str** | The support incident fee charged for each support incident. | [optional] 
**support_plan_fee** | **str** | The support plan fee charged for this plan. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


