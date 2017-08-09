# RadioGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditional_parent_label** | **str** | For conditional fields this is the TabLabel of the parent tab that controls this tab&#39;s visibility. | [optional] 
**conditional_parent_value** | **str** | For conditional fields, this is the value of the parent tab that controls the tab&#39;s visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \&quot;on\&quot; as the value to show that the parent tab is active.  | [optional] 
**document_id** | **str** | Specifies the document ID number that the tab is placed on. This must refer to an existing Document&#39;s ID attribute. | [optional] 
**group_name** | **str** | The name of the group. | [optional] 
**radios** | [**list[Radio]**](Radio.md) | Specifies the locations and status for radio buttons that are grouped together. | [optional] 
**recipient_id** | **str** | Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document. | [optional] 
**require_all** | **str** | When set to **true** and shared is true, information must be entered in this field to complete the envelope.  | [optional] 
**require_initial_on_shared_change** | **str** | Optional element for field markup. When set to **true**, the signer is required to initial when they modify a shared field. | [optional] 
**shared** | **str** | When set to **true**, this custom tab is shared. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


