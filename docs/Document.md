# Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_anchor_tabs** | **str** | Reserved: TBD | [optional] 
**display** | **str** |  | [optional] 
**document_base64** | **str** | The document’s bytes. This field can be used to include a base64 version of the document bytes within an envelope definition instead of sending the document using a multi-part HTTP request. The maximum document size is smaller if this field is used due to the overhead of the base64 encoding. | [optional] 
**document_fields** | [**list[NameValue]**](NameValue.md) |  | [optional] 
**document_group** | **str** |  | [optional] 
**document_id** | **str** | Specifies the document ID number that the tab is placed on. This must refer to an existing Document&#39;s ID attribute. | [optional] 
**encrypted_with_key_manager** | **str** | When set to **true**, the document is been already encrypted by the sender for use with the DocuSign Key Manager Security Appliance.   | [optional] 
**file_extension** | **str** | The file extension type of the document. If the document is not a PDF it is converted to a PDF.   | [optional] 
**file_format_hint** | **str** |  | [optional] 
**include_in_download** | **str** |  | [optional] 
**match_boxes** | [**list[MatchBox]**](MatchBox.md) | Matchboxes define areas in a document for document matching when you are creating envelopes. They are only used when you upload and edit a template.   A matchbox consists of 5 elements:  * pageNumber - The document page number  on which the matchbox will appear.  * xPosition - The x position of the matchbox on a page.  * yPosition - The y position of the matchbox on a page. * width - The width of the matchbox.  * height - The height of the matchbox.   | [optional] 
**name** | **str** |  | [optional] 
**order** | **str** |  | [optional] 
**pages** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**remote_url** | **str** | The file id from the cloud storage service where the document is located. This information is returned using [ML:GET /folders] or [ML:/folders/{folderid}].  | [optional] 
**signer_must_acknowledge** | **str** |  | [optional] 
**template_locked** | **str** | When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.  | [optional] 
**template_required** | **str** | When set to **true**, the sender may not remove the recipient. Used only when working with template recipients. | [optional] 
**transform_pdf_fields** | **str** | When set to **true**, PDF form field data is transformed into document tab values when the PDF form field name matches the DocuSign custom tab tabLabel. The resulting PDF form data is also returned in the PDF meta data when requesting the document PDF. See the [ML:Transform PDF Fields] section for more information about how fields are transformed into DocuSign tabs.  | [optional] 
**uri** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


