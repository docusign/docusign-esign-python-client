# InitialHere

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_case_sensitive** | **str** | When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**. | [optional] 
**anchor_horizontal_alignment** | **str** | Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**. | [optional] 
**anchor_ignore_if_not_present** | **str** | When set to **true**, this tab is ignored if anchorString is not found in the document. | [optional] 
**anchor_match_whole_word** | **str** | When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**. | [optional] 
**anchor_string** | **str** | Anchor text information for a radio button. | [optional] 
**anchor_units** | **str** | Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches. | [optional] 
**anchor_x_offset** | **str** | Specifies the X axis location of the tab, in achorUnits, relative to the anchorString. | [optional] 
**anchor_y_offset** | **str** | Specifies the Y axis location of the tab, in achorUnits, relative to the anchorString. | [optional] 
**conditional_parent_label** | **str** | For conditional fields this is the TabLabel of the parent tab that controls this tab&#39;s visibility. | [optional] 
**conditional_parent_value** | **str** | For conditional fields, this is the value of the parent tab that controls the tab&#39;s visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \&quot;on\&quot; as the value to show that the parent tab is active.  | [optional] 
**custom_tab_id** | **str** | The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties. | [optional] 
**document_id** | **str** | Specifies the document ID number that the tab is placed on. This must refer to an existing Document&#39;s ID attribute. | [optional] 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**merge_field** | [**MergeField**](MergeField.md) |  | [optional] 
**name** | **str** | Specifies the tool tip text for the tab. | [optional] 
**optional** | **str** |  | [optional] 
**page_number** | **str** | Specifies the page number on which the tab is located. | [optional] 
**recipient_id** | **str** | Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document. | [optional] 
**scale_value** | **float** |  Sets the size for the InitialHere tab. It can be value from 0.5 to 1.0, where 1.0 represents full size and 0.5 is 50% size. | [optional] 
**status** | **str** | Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later. | [optional] 
**tab_id** | **str** | The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].      | [optional] 
**tab_label** | **str** | The label string associated with the tab. | [optional] 
**tab_order** | **str** |  | [optional] 
**template_locked** | **str** | When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.  | [optional] 
**template_required** | **str** | When set to **true**, the sender may not remove the recipient. Used only when working with template recipients. | [optional] 
**x_position** | **str** | This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position. | [optional] 
**y_position** | **str** | This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


