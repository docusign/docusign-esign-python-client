# CompositeTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_template_id** | **str** | The identify of this composite template. It is used as a reference when adding document object information. If used, the document’s &#x60;content-disposition&#x60; must include the composite template ID to which the document should be added. If a composite template ID is not specified in the content-disposition, the document is applied based on the value of the &#x60;documentId&#x60; property only. If no document object is specified, the composite template inherits the first document. | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**inline_templates** | [**list[InlineTemplate]**](InlineTemplate.md) |  Zero or more inline templates and their position in the overlay. If supplied, they are overlaid into the envelope in the order of their Sequence value. | [optional] 
**pdf_meta_data_template_sequence** | **str** |  | [optional] 
**server_templates** | [**list[ServerTemplate]**](ServerTemplate.md) | 0 or more server-side templates and their position in the overlay. If supplied, they are overlaid into the envelope in the order of their Sequence value | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


