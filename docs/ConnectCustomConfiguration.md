# ConnectCustomConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_envelope_publish** | **str** | When set to **true**, data is sent to the urlToPublishTo web address. This option can be set to false to stop sending data while maintaining the Connect configuration information. | [optional] 
**all_users** | **str** | When set to **true**, the tracked envelope and recipient events for all users, including users that are added a later time, are sent through Connect. | [optional] 
**configuration_type** | **str** | If merge field&#39;s are being used, specifies the type of the merge field. The only  supported value is **salesforce**. | [optional] 
**connect_id** | **str** |  Specifies the DocuSign generated ID for the Connect configuration.   | [optional] 
**enable_log** | **str** | This turns Connect logging on or off. When set to **true**, logging is turned on. | [optional] 
**envelope_events** | **str** | A comma separated list of �Envelope� related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, and Voided. | [optional] 
**include_certificate_of_completion** | **str** | When set to **true**, the Connect Service includes the Certificate of Completion with completed envelopes.  | [optional] 
**include_cert_soap_header** | **str** |  | [optional] 
**include_document_fields** | **str** | When set to **true**, the Document Fields associated with envelope documents are included in the data. Document Fields are optional custom name-value pairs added to documents using the API.  | [optional] 
**include_documents** | **str** | When set to **true**, Connect will send the PDF document along with the update XML. | [optional] 
**include_envelope_void_reason** | **str** | When set to **true**, Connect will include the voidedReason for voided envelopes. | [optional] 
**include_sender_accountas_custom_field** | **str** | When set to **true**, Connect will include the sender account as Custom Field in the data. | [optional] 
**include_time_zone_information** | **str** | When set to **true**, Connect will include the envelope time zone information. | [optional] 
**name** | **str** | The name of the Connect configuration. The name helps identify the configuration in the list. | [optional] 
**recipient_events** | **str** | A comma separated list of �Recipient� related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded. | [optional] 
**requires_acknowledgement** | **str** | When set to **true**, and a publication message fails to be acknowledged, the message goes back into the queue and the system will retry delivery after a successful acknowledgement is received. If the delivery fails a second time, the message is not returned to the queue for sending until Connect receives a successful acknowledgement and it has been at least 24 hours since the previous retry. There is a maximum of ten retries Alternately, you can use Republish Connect Information to manually republish the envelope information. | [optional] 
**sign_message_with_x509_certificate** | **str** | When set to **true**, Connect messages are signed with an X509 certificate. This provides support for 2-way SSL. | [optional] 
**soap_namespace** | **str** | The namespace of the SOAP interface.  The namespace value must be set if useSoapInterface is set to true. | [optional] 
**url_to_publish_to** | **str** | This is the web address and name of your listener or Retrieving Service endpoint. You need to include HTTPS:// in the web address. | [optional] 
**user_ids** | **str** | A comma separated list of userIds. This sets the users associated with the tracked envelope and recipient events. When one of the event occurs for a set user, the information is sent through Connect.   ###### Note: If allUsers is set to �false� then you must provide a list of user id�s. | [optional] 
**use_soap_interface** | **str** | When set to **true**, indicates that the &#x60;urlToPublishTo&#x60; property contains a SOAP endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


