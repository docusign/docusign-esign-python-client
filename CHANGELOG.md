# Change Log
All notable changes to this project will be documented in this file.

See [DocuSign Support Center](https://support.docusign.com/en/releasenotes/) for Product Release Notes.

## [Unreleased]
### Changed
- Updated the package with the latest API monthly release.

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