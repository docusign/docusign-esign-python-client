# UserSignature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adopted_date_time** | **str** | The date and time the user adopted their signature. | [optional] 
**created_date_time** | **str** | Indicates the date and time the item was created. | [optional] 
**date_stamp_properties** | [**DateStampProperties**](DateStampProperties.md) |  | [optional] 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**external_id** | **str** |  | [optional] 
**image_type** | **str** |  | [optional] 
**initials150_image_id** | **str** |  | [optional] 
**initials_image_uri** | **str** | Contains the URI for an endpoint that you can use to retrieve the initials image. | [optional] 
**is_default** | **str** |  | [optional] 
**phonetic_name** | **str** |  | [optional] 
**signature150_image_id** | **str** |  | [optional] 
**signature_font** | **str** | The font type for the signature, if the signature is not drawn. The supported font types are:  \&quot;7_DocuSign\&quot;, \&quot;1_DocuSign\&quot;, \&quot;6_DocuSign\&quot;, \&quot;8_DocuSign\&quot;, \&quot;3_DocuSign\&quot;, \&quot;Mistral\&quot;, \&quot;4_DocuSign\&quot;, \&quot;2_DocuSign\&quot;, \&quot;5_DocuSign\&quot;, \&quot;Rage Italic\&quot;  | [optional] 
**signature_id** | **str** | Specifies the signature ID associated with the signature name. You can use the signature ID in the URI in place of the signature name, and the value stored in the &#x60;signatureName&#x60; property in the body is used. This allows the use of special characters (such as \&quot;&amp;\&quot;, \&quot;&lt;\&quot;, \&quot;&gt;\&quot;) in a the signature name. Note that with each update to signatures, the returned signature ID might change, so the caller will need to trigger off the signature name to get the new signature ID. | [optional] 
**signature_image_uri** | **str** | Contains the URI for an endpoint that you can use to retrieve the signature image. | [optional] 
**signature_initials** | **str** |  The initials associated with the signature. | [optional] 
**signature_name** | **str** | Specifies the user signature name. | [optional] 
**signature_type** | **str** |  | [optional] 
**stamp_format** | **str** |  | [optional] 
**stamp_image_uri** | **str** |  | [optional] 
**stamp_size_mm** | **str** |  | [optional] 
**stamp_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


