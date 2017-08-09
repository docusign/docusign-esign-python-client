# EventNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envelope_events** | [**list[EnvelopeEvent]**](EnvelopeEvent.md) | A list of envelope-level event statuses that will trigger Connect to send updates to the endpoint specified in the &#x60;url&#x60; property.   To receive notifications, you must include either an &#x60;envelopeEvents&#x60; node or a &#x60;recipientEvents&#x60; node. You do not need to specify both. | [optional] 
**include_certificate_of_completion** | **str** | When set to **true**, the Connect Service includes the Certificate of Completion with completed envelopes.  | [optional] 
**include_certificate_with_soap** | **str** | When set to **true**, this tells the Connect service to send the DocuSign signedby certificate as part of the outgoing SOAP xml. This appears in the XML as wsse:BinarySecurityToken. | [optional] 
**include_document_fields** | **str** | When set to **true**, the Document Fields associated with envelope documents are included in the data. Document Fields are optional custom name-value pairs added to documents using the API.  | [optional] 
**include_documents** | **str** | When set to **true**, the PDF documents are included in the message along with the updated XML.  | [optional] 
**include_envelope_void_reason** | **str** | When set to **true**, this tells the Connect Service to include the void reason, as entered by the person that voided the envelope, in the message.  | [optional] 
**include_sender_account_as_custom_field** | **str** | When set to **true**, the sender account ID is included as a envelope custom field in the data.  | [optional] 
**include_time_zone** | **str** | When set to **true**, the envelope time zone information is included in the message.  | [optional] 
**logging_enabled** | **str** | When set to **true**, logging is turned on for envelope events on the Web Console Connect page.  | [optional] 
**recipient_events** | [**list[RecipientEvent]**](RecipientEvent.md) | A list of recipient event statuses that will trigger Connect to send updates to   the endpoint specified in the url property.  To receive notifications, you must include either an &#x60;envelopeEvents&#x60; node or a &#x60;recipientEvents&#x60; node. You do not need to specify both. | [optional] 
**require_acknowledgment** | **str** | When set to **true**, the DocuSign Connect service checks that the message was received and retries on failures.  | [optional] 
**sign_message_with_x509_cert** | **str** | When set to **true**, messages are signed with an X509 certificate. This provides support for 2-way SSL in the envelope.  | [optional] 
**soap_name_space** | **str** | This lists the namespace in the SOAP listener provided. | [optional] 
**url** | **str** | Specifies the endpoint to which envelope updates are sent. Udpates are sent as XML unless &#x60;useSoapInterface&#x60; property is set to **true**. | [optional] 
**use_soap_interface** | **str** | When set to **true**, this tells the Connect service that the user&#39;s endpoint has implemented a SOAP interface.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


