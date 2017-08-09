# docusign.BillingApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_plan**](BillingApi.md#get_billing_plan) | **GET** /v2/billing_plans/{billingPlanId} | Get the billing plan details.
[**get_credit_card_info**](BillingApi.md#get_credit_card_info) | **GET** /v2/accounts/{accountId}/billing_plan/credit_card | Get metadata for a given credit card.
[**get_invoice**](BillingApi.md#get_invoice) | **GET** /v2/accounts/{accountId}/billing_invoices/{invoiceId} | Retrieves a billing invoice.
[**get_payment**](BillingApi.md#get_payment) | **GET** /v2/accounts/{accountId}/billing_payments/{paymentId} | Gets billing payment information for a specific payment.
[**get_plan**](BillingApi.md#get_plan) | **GET** /v2/accounts/{accountId}/billing_plan | Get Account Billing Plan
[**list_billing_plans**](BillingApi.md#list_billing_plans) | **GET** /v2/billing_plans | Gets the list of available billing plans.
[**list_invoices**](BillingApi.md#list_invoices) | **GET** /v2/accounts/{accountId}/billing_invoices | Get a List of Billing Invoices
[**list_invoices_past_due**](BillingApi.md#list_invoices_past_due) | **GET** /v2/accounts/{accountId}/billing_invoices_past_due | Get a list of past due invoices.
[**list_payments**](BillingApi.md#list_payments) | **GET** /v2/accounts/{accountId}/billing_payments | Gets payment information for one or more payments.
[**make_payment**](BillingApi.md#make_payment) | **POST** /v2/accounts/{accountId}/billing_payments | Posts a payment to a past due invoice.
[**purchase_envelopes**](BillingApi.md#purchase_envelopes) | **PUT** /v2/accounts/{accountId}/billing_plan/purchased_envelopes | Reserverd: Purchase additional envelopes.
[**update_plan**](BillingApi.md#update_plan) | **PUT** /v2/accounts/{accountId}/billing_plan | Updates the account billing plan.


# **get_billing_plan**
> BillingPlanResponse get_billing_plan(billing_plan_id)

Get the billing plan details.

Retrieves the billing plan details for the specified billing plan ID.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
billing_plan_id = 'billing_plan_id_example' # str | The ID of the billing plan being accessed.

try: 
    # Get the billing plan details.
    api_response = api_instance.get_billing_plan(billing_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_plan_id** | **str**| The ID of the billing plan being accessed. | 

### Return type

[**BillingPlanResponse**](BillingPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_card_info**
> CreditCardInformation get_credit_card_info(account_id)

Get metadata for a given credit card.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Get metadata for a given credit card.
    api_response = api_instance.get_credit_card_info(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_credit_card_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**CreditCardInformation**](CreditCardInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> BillingInvoice get_invoice(account_id, invoice_id)

Retrieves a billing invoice.

Retrieves the specified invoice.   ###### Note: If the `pdfAvailable` property in the response is set to *true*, you can download a PDF version of the invoice. To download the PDF, make the call again and change the value of the `Accept` property in the header to `Accept: application/pdf`.  Privileges required: account administrator  The response returns a list of charges and information about the charges. Quantities are usually shown as ‘unlimited’ or an integer. Amounts are shown in the currency set for the account.  **Response** The following table provides a description of the different `chargeName` property values. The information will grow as more chargeable items are added to the system.  | chargeName | Description | | --- | --- | | id_check | ID Check Charge | | in_person_signing | In Person Signing charge | | envelopes Included | Sent Envelopes for the account | | age_verify | Age verification check | | ofac | OFAC Check | | id_confirm | ID confirmation check | | student_authentication | STAN PIN authentication check | | wet_sign_fax | Pages for returning signed documents by fax | | attachment_fax | Pages for returning attachments by fax | | phone_authentication | Phone authentication charge | | powerforms | PowerForm envelopes sent | | signer_payments | Payment processing charge | | outbound_fax | Send by fax charge | | bulk_recipient_envelopes | Bulk Recipient Envelopes sent | | sms_authentications | SMS authentication charge | | saml_authentications | SAML authentication charge | | express_signer_certificate | DocuSign Express Certificate charge | | personal_signer_certificate | Personal Signer Certificate charge | | safe_certificate | SAFE BioPharma Signer Certificate charge | | seats | Included active seats charge | | open_trust_certificate | OpenTrust Signer Certificate charge | 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
invoice_id = 'invoice_id_example' # str | 

try: 
    # Retrieves a billing invoice.
    api_response = api_instance.get_invoice(account_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **invoice_id** | **str**|  | 

### Return type

[**BillingInvoice**](BillingInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> BillingPaymentItem get_payment(account_id, payment_id)

Gets billing payment information for a specific payment.

Retrieves the information for a specified payment.   Privileges required: account administrator 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
payment_id = 'payment_id_example' # str | 

try: 
    # Gets billing payment information for a specific payment.
    api_response = api_instance.get_payment(account_id, payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **payment_id** | **str**|  | 

### Return type

[**BillingPaymentItem**](BillingPaymentItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan**
> AccountBillingPlanResponse get_plan(account_id, include_credit_card_information=include_credit_card_information, include_metadata=include_metadata, include_successor_plans=include_successor_plans)

Get Account Billing Plan

Retrieves the billing plan information for the specified account, including the current billing plan, successor plans, billing address, and billing credit card.  By default the successor plan and credit card information is included in the response. This information can be excluded from the response by adding the appropriate optional query string with the `setting` set to **false**.   Response  The response returns the billing plan information, including the currency code, for the plan. The `billingPlan` and `succesorPlans` property values are the same as those shown in the [ML:Get Billing Plan Details] reference. the `billingAddress` and `creditCardInformation` property values are the same as those shown in the [ML:Update Billing Plan] reference.  ###### Note: When credit card number information is shown, a mask is applied to the response so that only the last 4 digits of the card number are visible. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
include_credit_card_information = 'include_credit_card_information_example' # str | When set to **true**, excludes credit card information from the response. (optional)
include_metadata = 'include_metadata_example' # str | When set to **true**, the `canUpgrade` and `renewalStatus` properities are included the response and an array of `supportedCountries` property is added to the `billingAddress` information.  (optional)
include_successor_plans = 'include_successor_plans_example' # str | When set to **true**, excludes successor information from the response. (optional)

try: 
    # Get Account Billing Plan
    api_response = api_instance.get_plan(account_id, include_credit_card_information=include_credit_card_information, include_metadata=include_metadata, include_successor_plans=include_successor_plans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **include_credit_card_information** | **str**| When set to **true**, excludes credit card information from the response. | [optional] 
 **include_metadata** | **str**| When set to **true**, the &#x60;canUpgrade&#x60; and &#x60;renewalStatus&#x60; properities are included the response and an array of &#x60;supportedCountries&#x60; property is added to the &#x60;billingAddress&#x60; information.  | [optional] 
 **include_successor_plans** | **str**| When set to **true**, excludes successor information from the response. | [optional] 

### Return type

[**AccountBillingPlanResponse**](AccountBillingPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_plans**
> BillingPlansResponse list_billing_plans()

Gets the list of available billing plans.

Retrieves a list of the billing plans associated with a distributor.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()

try: 
    # Gets the list of available billing plans.
    api_response = api_instance.list_billing_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_billing_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillingPlansResponse**](BillingPlansResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> BillingInvoicesResponse list_invoices(account_id, from_date=from_date, to_date=to_date)

Get a List of Billing Invoices

Retrieves a list of invoices for the account. If the from date or to date queries are not specified, the response returns invoices for the last 365 days.  Privileges required: account administrator 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
from_date = 'from_date_example' # str | Specifies the date/time of the earliest invoice in the account to retrieve. (optional)
to_date = 'to_date_example' # str | Specifies the date/time of the latest invoice in the account to retrieve. (optional)

try: 
    # Get a List of Billing Invoices
    api_response = api_instance.list_invoices(account_id, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **from_date** | **str**| Specifies the date/time of the earliest invoice in the account to retrieve. | [optional] 
 **to_date** | **str**| Specifies the date/time of the latest invoice in the account to retrieve. | [optional] 

### Return type

[**BillingInvoicesResponse**](BillingInvoicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices_past_due**
> BillingInvoicesSummary list_invoices_past_due(account_id)

Get a list of past due invoices.

Returns a list past due invoices for the account and notes if payment can be made through the REST API.   Privileges Required: account administrator

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # Get a list of past due invoices.
    api_response = api_instance.list_invoices_past_due(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_invoices_past_due: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**BillingInvoicesSummary**](BillingInvoicesSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments**
> BillingPaymentsResponse list_payments(account_id, from_date=from_date, to_date=to_date)

Gets payment information for one or more payments.

Retrieves a list containing information about one or more payments. If the from date or to date queries are not used, the response returns payment information for the last 365 days.   Privileges required: account administrator 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
from_date = 'from_date_example' # str | Specifies the date/time of the earliest payment in the account to retrieve. (optional)
to_date = 'to_date_example' # str | Specifies the date/time of the latest payment in the account to retrieve. (optional)

try: 
    # Gets payment information for one or more payments.
    api_response = api_instance.list_payments(account_id, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **from_date** | **str**| Specifies the date/time of the earliest payment in the account to retrieve. | [optional] 
 **to_date** | **str**| Specifies the date/time of the latest payment in the account to retrieve. | [optional] 

### Return type

[**BillingPaymentsResponse**](BillingPaymentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_payment**
> BillingPaymentResponse make_payment(account_id, billing_payment_request=billing_payment_request)

Posts a payment to a past due invoice.

Posts a payment to a past due invoice.   ###### Note: This can only be used if the `paymentAllowed` value for a past due invoice is true. This can be determined calling [ML:GetBillingInvoicesPastDue].  The response returns information for a single payment, if a payment ID was used in the endpoint, or a list of payments. If the from date or to date queries or payment ID are not used, the response returns payment information for the last 365 days. If the request was for a single payment ID, the `nextUri` and `previousUri` properties are not returned.  Privileges required: account administrator

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
billing_payment_request = docusign.BillingPaymentRequest() # BillingPaymentRequest |  (optional)

try: 
    # Posts a payment to a past due invoice.
    api_response = api_instance.make_payment(account_id, billing_payment_request=billing_payment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->make_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **billing_payment_request** | [**BillingPaymentRequest**](BillingPaymentRequest.md)|  | [optional] 

### Return type

[**BillingPaymentResponse**](BillingPaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_envelopes**
> purchase_envelopes(account_id, purchased_envelopes_information=purchased_envelopes_information)

Reserverd: Purchase additional envelopes.

Reserved: At this time, this endpoint is limited to DocuSign internal use only. Completes the purchase of envelopes for your account. The actual purchase is done as part of an internal workflow interaction with an envelope vendor.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
purchased_envelopes_information = docusign.PurchasedEnvelopesInformation() # PurchasedEnvelopesInformation |  (optional)

try: 
    # Reserverd: Purchase additional envelopes.
    api_instance.purchase_envelopes(account_id, purchased_envelopes_information=purchased_envelopes_information)
except ApiException as e:
    print("Exception when calling BillingApi->purchase_envelopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **purchased_envelopes_information** | [**PurchasedEnvelopesInformation**](PurchasedEnvelopesInformation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plan**
> BillingPlanUpdateResponse update_plan(account_id, preview_billing_plan=preview_billing_plan, billing_plan_information=billing_plan_information)

Updates the account billing plan.

Updates the billing plan information, billing address, and credit card information for the specified account.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.BillingApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
preview_billing_plan = 'preview_billing_plan_example' # str | When set to **true**, updates the account using a preview billing plan. (optional)
billing_plan_information = docusign.BillingPlanInformation() # BillingPlanInformation |  (optional)

try: 
    # Updates the account billing plan.
    api_response = api_instance.update_plan(account_id, preview_billing_plan=preview_billing_plan, billing_plan_information=billing_plan_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->update_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **preview_billing_plan** | **str**| When set to **true**, updates the account using a preview billing plan. | [optional] 
 **billing_plan_information** | [**BillingPlanInformation**](BillingPlanInformation.md)|  | [optional] 

### Return type

[**BillingPlanUpdateResponse**](BillingPlanUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

