# Change Log
All notable changes to this project will be documented in this file.

See [DocuSign Support Center](https://support.docusign.com/en/releasenotes/) for Product Release Notes.

## [3.2.0] - eSignature API v2.1-20.1.00 - 2020-03-27
### Changed
*   Added support for version v2.1-20.1.00 of the DocuSign eSignature API.
*   Updated the SDK release version.
### Added
*   Added the new property `copy_recipient_data` to envelopes. When set to **true**, the information that recipients enter is retained when you clone an envelope. For example, if you resend an envelope that was declined or voided after one or more recipients entered data, that data is retained. Note that this functionality must be enabled for the account.
*   Added `RecipientIdentityInputOption` and `input_options` to support Identity Verification workflows: Reserved for DocuSign.

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
