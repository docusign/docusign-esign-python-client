# Change Log
All notable changes to this project will be documented in this file.

See [DocuSign Support Center](https://support.docusign.com/en/releasenotes/) for Product Release Notes.

## [v5.1.0] - eSignature API v2.1-25.2.00.00 - 2025-05-21
### Changed
- Added support for version v2.1-25.2.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v5.0.0] - eSignature API v2.1-25.1.00.02 - 2025-04-24
### Changed
- Added support for version v2.1-25.1.00.02 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v5.0.0rc3] - eSignature API v2.1-25.1.00.02 - 2025-04-04
### Changed
- Added support for version v2.1-25.1.00.02 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v5.0.0rc2] - eSignature API v2.1-24.2.00.00 - 2024-08-22
### Breaking Changes
- Updated datatype for `get_document` method from `envelopes_api`.
### Changed
- Updated the SDK release version.

## [v5.0.0rc1] - eSignature API v2.1-24.2.00.00 - 2024-06-28
### Changed
- Added support for version v2.1-24.2.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v4.0.0] - eSignature API v2.1-24.1.01.00 - 2024-05-22
## Endpoint-Specific Changes

### Updated [EnvelopeRecipients: createRecipientProofFileResourceToken](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createrecipientprooffileresourcetoken/)
The `"token_scopes"` parameter has been moved from path parameters to query parameters for the above mentioned endpoint.

### Updated [EnvelopeView:CreateSender](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createsender/) and [EnvelopeView:CreateEdit](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createedit/)
The body parameter `returnUrlRequest` has been changed to `envelopeViewRequest`.
`envelopeViewRequest` has the same properties as the previous `returnUrlRequest` but now includes additional `viewAccess` and `settings` properties, where settings is a complex object with several UI controls for the view experience.

### Updated [TemplateViews: createEdit](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templateviews/createedit/)
The body parameter `returnUrlRequest` has been changed to `templateViewRequest`.
`templateViewRequest` has the same properties as the previous `returnUrlRequest` but now includes an additional `viewAccess` string.

## Model Changes

- Updated existing models

### `accountSettingsInformation`

- **Added fields:**
  - `allowConnectEnvelopeRemovedEvent`
  - `allowOrganizationBranding`
  - `allowOrganizationBrandingMetadata`
  - `allowPendingDestinationUrlEdition`
  - `allowPendingDestinationUrlEditionMetadata`
  - `disableBulkSendRecipientLimit`
  - `disableBulkSendRecipientLimitMetaData`
  - `enableAdvancedSearch`
  - `enableAdvancedSearchMetadata`
  - `enableContentSearch`
  - `enableContentSearchMetadata`
  - `enableMultiUserRepositoryFeatures`
  - `enableMultiUserRepositoryFeaturesMetadata`
  - `enablePremiumDataVerificationExtensions`
  - `enablePremiumDataVerificationExtensionsMetadata`
  - `enableSaveAsEnvelopeCustomFieldInWebForms`
  - `enableSaveAsEnvelopeCustomFieldInWebFormsMetadata`
  - `enableScheduledRelease`
  - `enableScheduledReleaseMetadata`
  - `isvOemEmbed`
  - `isvOemEmbedMetaData`

- **Removed fields:**
  - `enableInboxRelevanceSortForRecentAccounts`
  - `enableInboxRelevanceSortForRecentAccountsMetadata`
  - `enableScheduledRelease`
  - `enableScheduledReleaseMetadata`
  - `enableSearch`
  - `enableSearchMetadata`
  - `enableSearchUI`
  - `enableSearchUIMetadata`

### `accountUISettings`

- **Added fields:**
  - `enableEnvelopeTypes`
  - `enableEnvelopeTypesMetadata`

### `envelopDefinitions`

- **Added field:**
  - `uSigState`

### `envelopTemplate`

- **Added field:**
  - `uSigState`

### `group`

- **Added property:**
  - `lastModifiedOn`

### `receipientViewRequest`

- **Added property:**
  - `displayFormat`

### `userSettingsInformation`

- **Added properties:**
  - `accountAgreementsAccessType`
  - `accountAgreementsAccessTypeMetadata`
  - `canBulkUploadAgreements`
  - `canBulkUploadAgreementsMetadata`
  - `canManageAgreementParties`
  - `canManageAgreementPartiesMetadata`

### Newly added Models

- `envelopeViewDocumentSettings`
- `envelopeViewEnvelopeCustomFieldSettings`
- `envelopeViewRecipientSettings`
- `envelopeViewRequest`
- `envelopeViewSettings`
- `envelopeViewTaggerSettings`
- `envelopeViewTemplateSettings`
- `paletteItemSettings`
- `paletteSettings`
- `templateViewRequest`

### Removed Models
- `returnUrlRequest`

## [v4.0.0rc1] - eSignature API v2.1-24.1.01.00 - 2024-05-02
### Changed
- Added support for version v2.1-24.1.01.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.26.0] - eSignature API v2.1-23.4.02.00 - 2024-04-30
### Changed
- Revised the logic to determine the `oauth_host_name` based on the `base_path`.
- Adjusted the minimum required `PyJWT` package version to `2.0.0`.
- Added support for version v2.1-23.4.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.26.0rc1] - eSignature API v2.1-23.4.02.00 - 2024-03-12
### Changed
- Added support for version v2.1-23.4.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.26.0a2] - eSignature API v2.1-23.4.02.00 - 2024-03-07
### Changed
- Revised the logic to determine the `oauth_host_name` based on the `base_path`.
- Adjusted the minimum required `PyJWT` package version to `2.0.0`.
- Added support for version v2.1-23.4.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.25.1] - eSignature API v2.1-23.3.01.02 - 2023-12-14
### Changed
- Added support for version v2.1-23.3.01.02 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.25.0] - eSignature API v2.1-23.3.01.02 - 2023-10-25
### Changed
- Added support for version v2.1-23.3.01.02 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.24.0] - eSignature API v2.1-23.3.00.01 - 2023-08-30
### Changed
- Added support for version v2.1-23.3.00.01 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.23.0] - eSignature API v2.1-23.2.00.00 - 2023-05-18
### Changed
- Added support for version v2.1-23.2.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.22.0] - eSignature API v2.1-23.2.00.00 - 2023-05-17
### Changed
- Added support for version v2.1-23.2.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.21.0] - eSignature API v2.1-23.1.01.00 - 2023-03-17
### Changed
- Added support for version v2.1-23.1.01.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.20.0] - eSignature API v2.1-22.4.02.00 - 2023-02-10
### Changed
- Added support for version v2.1-22.4.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.19.0] - eSignature API v2.1-22.3.01.00 - 2022-11-22
### Changed
- Added support for version v2.1-22.3.01.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.18.1] - eSignature API v2.1-22.3.00.00 - 2022-10-25
### Changed
- Added support for version v2.1-22.3.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.
### Fixed
- Setup.py version limitation for PyJwt removed

## [v3.18.0] - eSignature API v2.1-22.3.00.00 - 2022-09-07
### Changed
- Added support for version v2.1-22.3.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.
### Fixed
- Date issue resolved in imports (DCM-7769)

## [v3.17.0] - eSignature API v2.1-22.2.00.00 - 2022-06-17
### Changed
- Added support for version v2.1-22.2.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.16.0] - eSignature API v2.1-22.1.02.00 - 2022-05-18
### Changed
- Added support for version v2.1-22.1.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.
- Added support for latest PyJwt versions of library.

## [v3.15.0] - eSignature API v2.1-22.1.01.00 - 2022-04-07
### Changed
- Added support for version v2.1-22.1.01.00 of the DocuSign ESignature API.
- Updated the SDK release version.

### Breaking
- Following models are renamed

    - `ScheduledSendingApiModel` is renamed to `ScheduledSending`
    - `DelayedRoutingApiModel` is renamed to `DelayedRouting`

## [v3.14.0] - eSignature API v2.1-21.4.02.00 - 2022-02-11
### Changed
- Added support for version v2.1-21.4.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [v3.14.0rc1] - eSignature API v2.1-21.4.01.00 - 2022-01-06
### Changed
- Added support for version v2.1-21.4.01.00 of the DocuSign ESignature API.
- Updated the SDK release version.

## [3.13.0] - ESignature API v2.1-21.4.00.00 - 2021-12-13
### Changed
- Added support for version v2.1-21.4.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.


## [3.13.0rc1] - ESignature API v2.1-21.3.02.00 - 2021-11-03
### Changed
- Added support for version v2.1-21.3.02.00 of the DocuSign ESignature API.
- Updated the SDK release version.


## [3.12.0] - ESignature API v2.1-21.3.00.00 - 2021-09-20
### Changed
- Added support for version v2.1-21.3.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.


## [3.12.0rc1] - eSignature API v2.1-21.2.02.00 - 2021-09-01
### Changed
- Added support for version v2.1-21.2.02.00 of the DocuSign eSignature API.
- Updated the SDK release version.
- The way all models take in init parameters using `kwargs`
- Updated to latest OpenAPI spec.

## [3.11.0] - eSignature API v2.1-21.2.00.00 - 2021-07-22
### Changed
- Added support for version v2.1-21.2.00.00 of the DocuSign eSignature API.
- Updated the SDK release version.

## [3.11.0rc1] - eSignature API v2.1-21.2.00.00 - 2021-07-13
### Changed
- Added support for version v2.1-21.2.00.00 of the DocuSign eSignature API.
- Updated the SDK release version.

## [3.10.0] - eSignature API v2.1-21.1.02.00 - 2021-06-08
### Breaking
- Removed methods `get_account_settings_export`,`get_seal_providers` from Accounts.
- Removed methods `create_connect_secret`,`delete_connect_secret`,`generate_connect_secret`,`get_connect_secrets` from Connect.
- Removed methods `get_dynamic_system_settings`,`get_template_info`,`get_appliance_info`,`get_account`,`get_custom_fields`,`delete_custom_fields_v2`,`get_document_pages`,`get_image`,`get_locale_policy`,`update_page_info`,`create_page_info`,`delete_page_info`,
`update_pdf`,`get_pdf`,`get_pdf_blob`,`update_pdf_blob`,`create_pdf_blob`,`update_recipient_denied_document_copy`,`delete_recipient_denied_document_copy`,`get_signer_attachment`,`delete_signer_attachment`, from Envelopes.
- Removed methods `complete_sign_hash`,`get_user_info`,`health_check`,`sign_hash_session_info`,`update_transaction` from Trust_Service_Providers.
- Removed methods `get_user_list_export` from Users.
### Added
- Added new methods `get_bulk_send_batch_envelopes` to BulkEnvelopes.
- Description in PyPi taken from Readme file.
- Test cases for tab_lists and Form pre-fill data.
### Changed
- Added support for version v2.1-21.1.02.00 of the DocuSign eSignature API.
- Updated the SDK release version.

## [3.10.0rc1] - eSignature API v2.1-21.1.02.00 - 2021-05-20
### Breaking
- Removed methods `get_account_settings_export`,`get_seal_providers` from Accounts.
- Removed methods `create_connect_secret`,`delete_connect_secret`,`generate_connect_secret`,`get_connect_secrets` from Connect.
- Removed methods `get_dynamic_system_settings`,`get_template_info`,`get_appliance_info`,`get_account`,`get_custom_fields`,`delete_custom_fields_v2`,`get_document_pages`,`get_image`,`get_locale_policy`,`update_page_info`,`create_page_info`,`delete_page_info`,
`update_pdf`,`get_pdf`,`get_pdf_blob`,`update_pdf_blob`,`create_pdf_blob`,`update_recipient_denied_document_copy`,`delete_recipient_denied_document_copy`,`get_signer_attachment`,`delete_signer_attachment`, from Envelopes.
- Removed methods `complete_sign_hash`,`get_user_info`,`health_check`,`sign_hash_session_info`,`update_transaction` from Trust_Service_Providers.
- Removed methods `get_user_list_export` from Users.
### Added
- Added new methods `get_bulk_send_batch_envelopes` to BulkEnvelopes.
- Description in PyPi taken from Readme file.
### Changed
- Added support for version v2.1-21.1.02.00 of the DocuSign eSignature API.
- Updated the SDK release version.

## [3.9.0] - eSignature API v2.1-21.1.01.03 - 2021-04-22
### Added
- Added support for version v2.1-21.1.01.03 of the DocuSign eSignature API.
### Updated
- Updated the SDK release version.
- Updated `user_agent` in configurations. Eg; `'Swagger-Codegen/v2.1/3.9.0rc1/python3'`
- Updated test cases to remove printing sensitive info

## [3.8.1] - eSignature API v2.1-20.4.01 - 2021-02-26
### Changed
- Added support for version v2.1-20.4.01 of the DocuSign eSignature API.
- Updated the SDK release version.
### Fixed
- Exposed BulkEnvelopeApi and other api files as public and accessible.
- Adding `Type` fix in envelope_document model.

## [3.7.1] - eSignature API v2.1-20.3.01 - 2020-10-30
### Changed
- Added support for version v2.1-20.3.01 of the DocuSign eSignature API.
- Updated the SDK release version.
### Fixed
- DCM-3866, Added support for updateBrandResourcesByContentType function to take in file to upload.
- DCM-3468, Template get working, added test case for catching regression in future.

## [3.6.0] - eSignature API v2.1-20.3.00 - 2020-09-24
### Changed
- Added support for version v2.1-20.3.00 of the DocuSign eSignature API.
- Updated the SDK release version.

## [3.5.0] - eSignature API v2.1-20.2.02.02 - 2020-08-21
### Changed
* Added support for version v2.1-20.2.02.02 of the DocuSign eSignature API.
* Updated the SDK release version.
* Updated/added properties for bulk send & advanced recipient routing.

## [3.4.0] - eSignature API v2.1-20.2.00 - 2020-07-09
### Changed
* Added support for version v2.1-20.2.00 of the DocuSign eSignature API.
* Updated the SDK release version.
* Updated/added properties for bulk update call

## [3.3.0] - eSignature API v2.1-20.1.02 - 2020-06-02
### Changed
*   Added support for version v2.1-20.1.02 of the DocuSign eSignature API.
*   Updated the SDK release version.
*   Changed the way the model takes in the parameters when more than 255 arguments, now works with python3 versions which were limiting it. Fix introduced again. (DCM-3701)

## [3.2.0] - eSignature API v2.1-20.1.00 - 2020-03-27
### Changed
*   Added support for version v2.1-20.1.00 of the DocuSign eSignature API.
*   Updated the SDK release version.
### Added
*   Added the new property `copy_recipient_data` to envelopes. When set to **true**, the information that recipients enter is retained when you clone an envelope. For example, if you resend an envelope that was declined or voided after one or more recipients entered data, that data is retained. Note that this functionality must be enabled for the account.
*   Added `RecipientIdentityInputOption` and `input_options` to support Identity Verification workflows: Reserved for DocuSign.
### Deleted
*   Deleted the GET methods for account seals providers, which returned the seals for an account.

## [3.2.0rc2] - eSignature API v2.1-20.1.00 - 2020-03-13
### Changed
* The SDK now supports version v20.1.00 of the DocuSign eSignature API.
* SDK Release Version updated.

## [3.1.0] - eSignature API v2.1-19.4.01 - 2020-02-10
### Changed
* Changed the way the model takes in the parameters where the size of the parameters exceeded 255 arguments, now works with python3 versions which were limiting it. (DCM-3701)
### Fixed
* A bug in deserialize file with the same name, if downloaded multiple times on different thread or during parallel processing, wrong files are overwritten or served. (DCM-3631)
* Unit test updated to handle delays in moving Envelopes.
* Changed the return type of model to `TemplateInformation` to fix deserialization.

## [3.1.0rc2] - eSignature API v2.1-19.4.01 - 2019-12-31
### Changed
* Changed the way the model takes in the parameters where the size of the parameters exceeded 255 arguments, now works with python3 versions which were limiting it. (DCM-3701)
### Fixed
* A bug in deserialize file with the same name, if downloaded multiple times on different thread or during parallel processing, wrong files are overwritten or served. (DCM-3631)
* Unit test updated to handle delays in moving Envelopes.
* Changed the return type of model to `TemplateInformation` to fix deserialization.

## [3.0.0] - eSignature API v2.1-19.2.02 - 2019-10-09
### Changed
* Updated the way the models and classes are initialized. Now using constructor parameters to initialize the classes. Updates to unit tests. (DCM-1788)
### Fixed
* A bug in model mapping where instead of mapping to custom DocuSign `Date` class, was mapping to python `date` class. Causing the functions such as `envelope_api.list_tabs()` to raise exception. (DCM-3102)
### BREAKING
* The SDK now supports API v2.1-19.2.02 of the DocuSign eSignature API.
* SDK Release Version updated.

## [3.0.0rc1] - eSignature API v2.1-19.2.02 - 2019-08-28
### Changed
* Updated the way the models and classes are initialized. Now using constructor parameters to initialize the classes. Updates to unit tests. (DCM-1788)
### Fixed
* A bug in model mapping where instead of mapping to custom DocuSign `Date` class, was mapping to python `date` class. Causing the functions such as `envelope_api.list_tabs()` to raise exception. (DCM-3102)
### BREAKING
* The SDK now supports API v2.1-19.2.02 of the DocuSign eSignature API.
* SDK Release Version updated.

## [2.0.1] - 2019-06-24
### Removed
* Removed harcoded test config values from the test cases. Now getting test config values from the environment variables.
### Changed
* Made dependencies versions broader (using '>=' to specify minimum supported versions).

## [2.0.0] - eSignature API v19.1.02 - 2019-05-24
### Removed
* configure_jwt_authorization_flow has been removed. Update to use either request_jwt_user_token or request_jwt_application_token
* empty test placeholder files
### Changed
* The SDK now supports version 19.1.02 of the DocuSign eSignature API.
* SDK Release Version updated.
* ApiException, ApiClient and Configuration classes have moved under client folder. New import statement was simplified. Example: from docusign_esign import ApiException
* Using PyJWT and cryptography libraries for OAuth, instead of jwcrypto and py-oauth2
### Added
* Added a new *tabGroupLabels* field to all Tabs models
* Added a new *Witnesses* field to all Recipients models
* Implemented models for Smart Sections feature
* Implemented initial support of HMAC for DocuSign Connect
### Fixed
* A bug with that could cause the *moveEnvelopes* method call to return a response without a *Content-Type* header. (DCM-2871)

## [2.0.0rc1] - eSignature API v19.1.02 - 2019-05-13
### Removed
* configure_jwt_authorization_flow has been removed. Update to use either request_jwt_user_token or request_jwt_application_token
* empty test placeholder files
### Changed
* The SDK now supports version 19.1.02 of the DocuSign eSignature API.
* SDK Release Version updated.
* ApiException, ApiClient and Configuration classes have moved under client folder. New import statement was simplified. Example: from docusign_esign import ApiException
* Using PyJWT and cryptography libraries for OAuth, instead of jwcrypto and py-oauth2
### Added
* Added a new *tabGroupLabels* field to all Tabs models
* Added a new *Witnesses* field to all Recipients models
* Implemented models for Smart Sections feature
* Implemented initial support of HMAC for DocuSign Connect
### Fixed
* A bug with that could cause the *moveEnvelopes* method call to return a response without a *Content-Type* header. (DCM-2871)

## [1.0.3] - 2018-03-22
### Fixed
- Issue [`#7`](https://github.com/docusign/docusign-python-client/issues/7): TypeError: the JSON object must be str, not 'bytes'.
- PR [`#8`](https://github.com/docusign/docusign-python-client/pull/8): Ensure closure of private key file to prevent open handles. Allow key bytes to be supplied to JWT configure method.
- PR [`#9`](https://github.com/docusign/docusign-python-client/pull/9): Support for cross-version json parsing of response.

## [1.0.2] - 2017-12-05
### Fixed
- PR [`#6`](https://github.com/docusign/docusign-python-client/pull/6): Invalid Grant URI at get_jwt_uri().

## [1.0.1] - 2017-09-05
### Added
- Added OAuth support.

## [1.0.0] - 2017-08-08
### Added
- Initial commit of the new Python SDK for DocuSign API, automatically generated from OpenAPI specification.
