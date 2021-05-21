# The Official DocuSign eSignature Python Client SDK

[![PyPI version][pypi-image]][pypi-url]
<!--[![PyPI downloads][downloads-image]][downloads-url]-->
[![Build status][travis-image]][travis-url]

[PyPI module](https://pypi.python.org/pypi/docusign_esign)

[Documentation about DocuSign APIs](https://developers.docusign.com/)

## Requirements

- Python 2.7 (3.7+ recommended)
- Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16531)

## Compatibility

- Python 2.7+

## Installation
This SDK is provided as open source, which enables you to customize its functionality to suit your particular use case. To do so, download or clone the repository. If the SDK’s given functionality meets your integration needs, or if you’re working through our [code examples](https://developers.docusign.com/docs/esign-rest-api/how-to/) from the [DocuSign Developer Center](https://developers.docusign.com/), you merely need to install it by following the instructions below.

### Path setup:
1. Locate your Python installation, also referred to as a **site-packages** folder. This folder is usually labeled in a format of **Python{VersionNumber}**.  
    **Examples:**
    *   Unix/Linux: **/usr/lib/python2.7**
    *   Mac: **/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7**
    *   Windows: **C:\Users{username}\AppData\Local\Programs\Python\Python37**
2. Add your Python folder’s path to your system as an environment variable.  
    **Unix/Linux:**
    1. Type the following command into your console: \
        **export PYTHONPATH = "${PYTHONPATH}:.:/_path_/_to_/_site-packages_"**
    2. Optionally, you can add this command to your system profile, which will run the command each time Python is launched.  

    **Windows:**
    <ol>
      <li>Open the Windows <strong>Control Panel.</strong></li>
      <li>Under the System and Security category, open the <strong>System</strong> information panel.</li>
      <li>Select <strong>Advanced System Settings</strong> to open the <strong>System Properties</strong> dialog box.</li>
      <li>On the <strong>Advanced</strong> tab, select the <strong>Environment Variables</strong> button at the lower-right corner.
          <ol style="list-style-type: lower-alpha">
              <li>Check to see whether <strong>PYTHONPATH</strong> has been added as a <strong>system variable.</strong></li>
              <li>If it has not, select <strong>New</strong> to add it. The variable you add is the path to the <strong>site-packages</strong> folder.</li>
          </ol>
      </li>
    </ol>

**Note:** If you are still unable to reference Python or pip via your command console, you can also add the path to the **site-packages** folder to the built-in environment variable labeled **Path**, which will take effect the next time you start your machine.

### Install via PIP:
In your command console, type: **pip install docusign-esign**  
    **Note:** This may require the command console to be elevated. You can accomplish this via sudo in Unix/Linux, or by running the command console as an administrator in Windows.

## Dependencies
This client has the following external dependencies:

- certifi v14.05.14+
- six v1.8.0+
- python\_dateutil v2.5.3+
- setuptools v21.0.0+
- urllib3 v1.15.1+
- jwcrypto v0.4.2+
- py-oauth2 v0.0.10+

## Code examples
You can find on our GitHub a self-executing package of code examples for the eSignature Python SDK, called a [Launcher](https://github.com/docusign/code-examples-python/blob/master/README.md), that demonstrates common use cases. You can also download a version preconfigured for your DocuSign developer account from [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/). These examples can use either the [Authorization Code Grant](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-code-grant) or [JSON Web Token (JWT)](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-jsonwebtoken) authentication workflows.

## OAuth implementations
For details regarding which type of OAuth grant will work best for your DocuSign integration, see [Choose OAuth Type](https://developers.docusign.com/platform/auth/choose/) in the [DocuSign Developer Center](https://developers.docusign.com/).

For security purposes, DocuSign recommends using the [Authorization Code Grant](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-code-grant) flow.

## Support
Log issues against this client through GitHub. We also have an [active developer community on Stack Overflow](https://stackoverflow.com/questions/tagged/docusignapi).

## License
The DocuSign eSignature Python Client SDK is licensed under the [MIT License](https://github.com/docusign/docusign-python-client/blob/master/LICENSE).

### Additional resources
*   [DocuSign Developer Center](https://developers.docusign.com/)
*   [DocuSign API on Twitter](https://twitter.com/docusignapi)
*   [DocuSign For Developers on LinkedIn](https://www.linkedin.com/showcase/docusign-for-developers/)
*   [DocuSign For Developers on YouTube](https://www.youtube.com/channel/UCJSJ2kMs_qeQotmw4-lX2

[pypi-image]: https://img.shields.io/pypi/v/docusign_esign.svg?style=flat
[pypi-url]: https://pypi.python.org/pypi/docusign_esign
[downloads-image]: https://img.shields.io/pypi/dm/docusign_esign.svg?style=flat
[downloads-url]: https://pypi.python.org/pypi/docusign_esign
[travis-image]: https://img.shields.io/travis/docusign/docusign-python-client.svg?style=flat
[travis-url]: https://travis-ci.org/docusign/docusign-python-client