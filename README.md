# The Official DocuSign Python Client

[![PyPI version][pypi-image]][pypi-url]
<!--[![PyPI downloads][downloads-image]][downloads-url]-->
[![Build status][travis-image]][travis-url]

[PyPI module](https://pypi.python.org/pypi/docusign_esign) that wraps the <a href="https://www.docusign.com">DocuSign</a> API

[Documentation about the DocuSign API](https://developers.docusign.com/)

## Requirements

- Python 2.7 (3.6+ recommended)
- Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16531)

## Compatibility

- Python 2.7+

## Note

This open-source SDK is provided for cases where you would like to make additional changes that the SDK does not provide out-of-the-box. If you simply want to use the SDK with any of the examples shown in the [Developer Center](https://developers.docusign.com/esign-rest-api/code-examples), follow the installation instructions below.

## Installation

### Path Setup:

1. Locate your Python installation, also referred to as a **site-packages** folder. This folder is usually labeled in a format of Python{VersionNumber}.

**Examples:**

- **Unix/Linux:** /usr/lib/python2.7
- **Mac:** /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7
- **Windows:** C:\Users\{username}\AppData\Local\Programs\Python\Python37

1. Add the path to your Python folder as an environment variable.

**Unix/Linux:**

- Type the following command into your console:  
   **export PYTHONPATH = "${PYTHONPATH}:.:/path/to/site-packages"**
- Optionally, you can add this command to your system profile, which will run the command each time Python is launched.

**Windows:**

<ol>
   <li>Open the Windows <b>Control Panel.</b></li>
   <li>Under the System and Security category, open the <b>System</b></li>
   <li>Select <b>Advanced System Settings</b> to open the <b>System Properties</b> dialog box.</li>
   <li>On the <b>Advanced</b> tab, select the <b>Environmental Variables</b> button at the lower-right corner.
       <ol style="list-style-type: lower-alpha">
           <li>Check if <b>PYTHONPATH</b> has been added as a <b>system variable.</b></li>
           <li>If it has not, select <b>New</b> to add it. The variable you add is the path to the <b>site-packages</b></li>
       </ol>
   </li>
</ol>

**Note:** If you are still unable to reference python or pip via your command console,you can also add the path to the site-packages folder to the built-in environment variable labeled **Path** , which will take effect the next time you start your machine.

### Install via PIP:

1. In your command console, type:
pip install docusign-esign

Note: This may require the command console be elevated. You can accomplish this via sudoin Unix/Linux, or by running the command console as an administrator in Windows.

## Dependencies

This client has the following external dependencies:

- certifi v14.05.14+
- six v1.8.0
- python\_dateutil v2.5.3+
- setuptools v21.0.0+
- urllib3 v1.15.1+
- jwcrypto v0.4.2+
- py-oauth2 v0.0.10+

## Code Examples

### Launchers

DocuSign provides a sample application referred to as a [Launcher](https://github.com/docusign/eg-03-python-auth-code-grant). The Launcher contains a set of 14 common use cases and associated source files. These examples use DocuSign&#39;s [Authorization Code Grant](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-code-grant) flow.

## Proof-of-concept applications

If your goal is to create a proof of concept application, DocuSign provides a set of [Quick Start](https://github.com/docusign/qs-python) examples. The Quick Start examples are meant to be used with DocuSign&#39;s [OAuth Token Generator](https://developers.docusign.com/oauth-token-generator), which will allow you to generate tokens for the Demo/Sandbox environment only. These tokens last for eight hours and will enable you to build your proof-of-concept application without the need to fully implement an OAuth solution.

## OAuth Implementations

For details regarding which type of OAuth grant will work best for your DocuSign integration, see the [REST API Authentication Overview](https://developers.docusign.com/esign-rest-api/guides/authentication) guide located on the [DocuSign Developer Center](https://developers.docusign.com/esign-rest-api/guides/authentication).

For security purposes, DocuSign recommends using the [Authorization Code Grant](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-code-grant) flow.

There are other use-case scenarios, such as **single-page applications** (SPA) that use **Cross-Origin Resource Sharing** (CORS), or where there may not be a user to interact with your Service Account. For these use cases, DocuSign also supports [JWT](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-jsonwebtoken) and [Implicit](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-implicit) grants. For code examples, see the links below:

- [JWT (JSON Web Token)](https://github.com/docusign/eg-01-python-jwt)
- Implicit Grant (coming soon)

## Support

Log issues against this client through GitHub. We also have an [active developer community on Stack Overflow](https://stackoverflow.com/questions/tagged/docusignapi).

## License

The DocuSign Python Client is licensed under the [MIT License](https://github.com/docusign/docusign-python-client/blob/master/LICENSE).


[pypi-image]: https://img.shields.io/pypi/v/docusign_esign.svg?style=flat
[pypi-url]: https://pypi.python.org/pypi/docusign_esign
[downloads-image]: https://img.shields.io/pypi/dm/docusign_esign.svg?style=flat
[downloads-url]: https://pypi.python.org/pypi/docusign_esign
[travis-image]: https://img.shields.io/travis/docusign/docusign-python-client.svg?style=flat
[travis-url]: https://travis-ci.org/docusign/docusign-python-client
