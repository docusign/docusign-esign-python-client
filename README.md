# The Official DocuSign Python Client

[![PyPI version][pypi-image]][pypi-url]
<!--[![PyPI downloads][downloads-image]][downloads-url]-->
[![Build status][travis-image]][travis-url]

[PyPI module](https://pypi.python.org/pypi/docusign_esign) that wraps the <a href="https://www.docusign.com">DocuSign</a> API

[Documentation about the DocuSign API](https://developers.docusign.com/)

You can sign up for a free [developer sandbox](https://developers.docusign.com/).

Requirements
============

Python 2.7 and 3.6+.

## PYTHONPATH set up
### *nix
- Find the path to site-packages folders, for your python version. Usually it's under "/usr/lib/python2.7" (Unix) or "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7" (Mac)
- export PYTHONPATH = ${PYTHONPATH}:.:/path/to/site-packages

Ideally you want this last line to be executed each time python command is launched. So you have to add it to ~/.bash_profile, ~/.bashrc or ~/.profile.

### Windows
- Find the path to site-packages folders, for your python version. Usually it's under "C:\Python27".
- Go to your Windows "Control Panel"
- Open "System Settings"
- Under "Advanced" tab, click on the "Environment Variables" button.
- Check if "PYTHONPATH" variable is defined under the "System Variables" section.
- If not defined yet, click on the "New" button and add it. The value of the varibale should be the path to site-packages (something like "C:\Python27").


Now that you've added the site-packages folder, to the list of modules python command scans, when it starts, it time to verify it's working:
- open python command prompt and type "help('modules')". Your should now see the list of modules installed under site-packages.

Installation
============

### PyPI Package Index

Install the client locally:  `pip install docusign_esign` (note you may have to use `sudo` based on your permissions)

Alternatively you can just copy the source code directly into your project.

#### Dependencies

This client has the following external dependencies:

* certifi >= 14.05.14
* six == 1.8.0
* python_dateutil >= 2.5.3
* setuptools >= 21.0.0
* urllib3 >= 1.15.1
* jwcrypto >= 0.4.2
* py-oauth2 >= 0.0.10

Usage
=====

To initialize the client, make the Login API Call and send a template for signature:

Run this script using python command
```python
from __future__ import absolute_import, print_function
from pprint import pprint
import unittest
import webbrowser

import docusign_esign as docusign
from docusign_esign import AuthenticationApi, TemplatesApi, EnvelopesApi
from docusign_esign.rest import ApiException

user_name = "[USERNAME]"
integrator_key = "[INTEGRATOR_KEY]"
base_url = "https://demo.docusign.net/restapi"
oauth_base_url = "account-d.docusign.com" # use account.docusign.com for Live/Production
redirect_uri = "https://www.docusign.com/api"
private_key_filename = "keys/docusign_private_key.txt"
user_id = "[USER_ID]"
template_id = "[TEMPLATE_ID]"

api_client = docusign.ApiClient(base_url)

# IMPORTANT NOTE:
# the first time you ask for a JWT access token, you should grant access by making the following call
# get DocuSign OAuth authorization url:
oauth_login_url = api_client.get_jwt_uri(integrator_key, redirect_uri, oauth_base_url)
# open DocuSign OAuth authorization url in the browser, login and grant access
# webbrowser.open_new_tab(oauth_login_url)
print(oauth_login_url)

# END OF NOTE

# configure the ApiClient to asynchronously get an access token and store it
api_client.configure_jwt_authorization_flow(private_key_filename, oauth_base_url, integrator_key, user_id, 3600)

docusign.configuration.api_client = api_client

template_role_name = 'Needs to sign'

# create an envelope to be signed
envelope_definition = docusign.EnvelopeDefinition()
envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

# assign template information including ID and role(s)
envelope_definition.template_id = template_id

# create a template role with a valid template_id and role_name and assign signer info
t_role = docusign.TemplateRole()
t_role.role_name = template_role_name
t_role.name ='Pat Developer'
t_role.email = user_name

# create a list of template roles and add our newly created role
# assign template role(s) to the envelope
envelope_definition.template_roles = [t_role]

# send the envelope by setting |status| to "sent". To save as a draft set to "created"
envelope_definition.status = 'sent'

auth_api = AuthenticationApi()
envelopes_api = EnvelopesApi()

try:
    login_info = auth_api.login(api_password='true', include_account_id_guid='true')
    assert login_info is not None
    assert len(login_info.login_accounts) > 0
    login_accounts = login_info.login_accounts
    assert login_accounts[0].account_id is not None

    base_url, _ = login_accounts[0].base_url.split('/v2')
    api_client.host = base_url
    docusign.configuration.api_client = api_client

    envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
    assert envelope_summary is not None
    assert envelope_summary.envelope_id is not None
    assert envelope_summary.status == 'sent'

    print("EnvelopeSummary: ", end="")
    pprint(envelope_summary)

except ApiException as e:
    print("\nException when calling DocuSign API: %s" % e)
    assert e is None # make the test case fail in case of an API exception
```

See [unit_tests.py](./test/unit_tests.py) for more examples.

# Authentication

## Service Integrations that use Legacy Header Authentication

([Legacy Header Authentication](https://docs.docusign.com/esign/guide/authentication/legacy_auth.html) uses the X-DocuSign-Authentication header.)

1. Use the [Authentication: login method](https://docs.docusign.com/esign/restapi/Authentication/Authentication/login/) to retrieve the account number **and the baseUrl** for the account.
The url for the login method is www.docusign.net for production and demo.docusign.net for the developer sandbox.
The `base_url` field is part of the `login_account` object. See the [docs and the login_account object](https://docs.docusign.com/esign/restapi/Authentication/Authentication/login/#/definitions/loginAccount)
2. The base_url for the selected account, in production, will start with na1, na2, na3, eu1, or something else. Use the base_url that is returned to create the *host* (see the next step.) Use the host for all of your subsequent API calls.
3. As returned by login method, the base_url includes the API version and account id. Split the string to obtain the *host*, just the server name and api name. Eg, you will receive `https://na1.docusign.net/restapi/v2/accounts/123123123`. You want just `https://na1.docusign.net/restapi` 
4. Instantiate the SDK using the basePath. Eg `api_client = docusign.ApiClient(host)`
5. Set the authentication header as shown in the examples by using `api_client.set_default_header`

## User Applications that use OAuth Authentication
1. After obtaining a Bearer token, call the [OAuth: Userinfo method](https://docs.docusign.com/esign/guide/authentication/userinfo.html). Obtain the selected account's `base_uri` (server name) field.
The url for the Userinfo method is account-d.docusign.com for the demo/developer environment, and account.docusign.com for the production environment.
1. Combine the base_uri with "/restapi" to create the host. The base_uri will start with na1, na2, na3, eu1, or something else. Use the host for your subsequent API calls.
4. Instantiate the SDK using the basePath. Eg `api_client = docusign.ApiClient(host)`
5. Create the `authentication_value` by combining the `token_type` and `access_token` fields you receive from either an [Authorization Code Grant](https://docs.docusign.com/esign/guide/authentication/oa2_auth_code.html) or [Implicit Grant](https://docs.docusign.com/esign/guide/authentication/oa2_implicit.html) OAuth flow. 
5. Set the authentication header by using `api_client.set_default_header('Authorization', authentication_value)`

Testing
=======

Unit tests are available in the [Test](https://github.com/docusign/docusign-python-client/tree/master/test/unit_tests.py) folder.

Contributing
============

**This SDK is auto-generated from OpenAPI specification file. For that reason, we actually do NOT accept pull requests. If you find a bug or have an idea that you want to see in the SDK, please open a new [issue](https://github.com/docusign/docusign-python-client/issues/new).**

Support
=======

Feel free to log issues against this client through GitHub.  We also have an active developer community on Stack Overflow, search the [DocuSignAPI](http://stackoverflow.com/questions/tagged/docusignapi) tag.

License
=======

The DocuSign Node Client is licensed under the following [License](LICENSE).


[pypi-image]: https://img.shields.io/pypi/v/docusign_esign.svg?style=flat
[pypi-url]: https://pypi.python.org/pypi/docusign_esign
[downloads-image]: https://img.shields.io/pypi/dm/docusign_esign.svg?style=flat
[downloads-url]: https://pypi.python.org/pypi/docusign_esign
[travis-image]: https://img.shields.io/travis/docusign/docusign-python-client.svg?style=flat
[travis-url]: https://travis-ci.org/docusign/docusign-python-client
