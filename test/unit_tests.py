# coding: utf-8

from __future__ import absolute_import, print_function

import base64
import os
import subprocess
import unittest
from pprint import pprint
from time import sleep

import docusign_esign as docusign
from docusign_esign import AuthenticationApi, EnvelopesApi, TemplatesApi, DiagnosticsApi, FoldersApi, ApiException

Username = os.environ.get("USER_NAME")
IntegratorKey = os.environ.get("INTEGRATOR_KEY_JWT")
BaseUrl = "https://demo.docusign.net/restapi"
OauthHostName = "account-d.docusign.com"
SignTest1File = "{}/docs/SignTest1.pdf".format(os.path.dirname(os.path.abspath(__file__)))
TemplateId = os.environ.get("TEMPLATE_ID")
UserId = os.environ.get("USER_ID")
PrivateKeyBytes = base64.b64decode(os.environ.get("PRIVATE_KEY"))


class SdkUnitTests(unittest.TestCase):

    def setUp(self):
        self.api_client = docusign.ApiClient(base_path=BaseUrl, oauth_host_name=OauthHostName)
        self.api_client.rest_client.pool_manager.clear()

        docusign.configuration.api_client = self.api_client
        try:
            envelope_definition = docusign.EnvelopeDefinition()
            envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
            envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'
            envelope_definition.template_id = TemplateId
            t_role = docusign.TemplateRole()
            t_role.role_name = 'Needs to sign'
            t_role.name = 'Pat Developer'
            t_role.email = Username
            envelope_definition.template_roles = [t_role]

            # send the envelope by setting |status| to "sent". To save as a draft set to "created"
            envelope_definition.status = 'sent'
            envelopes_api = EnvelopesApi()

            self.api_client.host = BaseUrl
            token = (self.api_client.request_jwt_user_token(client_id=IntegratorKey,
                                                            user_id=UserId,
                                                            oauth_host_name=OauthHostName,
                                                            private_key_bytes=PrivateKeyBytes,
                                                            expires_in=3600))
            self.user_info = self.api_client.get_user_info(token.access_token)
            self.api_client.rest_client.pool_manager.clear()
            docusign.configuration.api_client = self.api_client
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            self.api_client.rest_client.pool_manager.clear()
            self.envelope_id = envelope_summary.envelope_id

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
        self.api_client.rest_client.pool_manager.clear()

    def tearDown(self):
        self.api_client.rest_client.pool_manager.clear()

    def testLogin(self):
        auth_api = AuthenticationApi()

        try:
            login_info = auth_api.login(api_password='true', include_account_id_guid='true')
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None
            print("LoginInformation: ", end="")
            pprint(login_info)

            # parse first account's baseUrl
            base_url, _ = login_accounts[0].base_url.split('/v2')

            # below code required for production, no effect in demo (same domain)
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testRequestASignature(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position = '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()

        try:
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testRequestSignatureFromTemplate(self):
        template_role_name = 'Needs to sign'

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # assign template information including ID and role(s)
        envelope_definition.template_id = TemplateId

        # create a template role with a valid templateId and roleName and assign signer info
        t_role = docusign.TemplateRole()
        t_role.role_name = template_role_name
        t_role.name = 'Pat Developer'
        t_role.email = Username

        # create a list of template roles and add our newly created role
        # assign template role(s) to the envelope
        envelope_definition.template_roles = [t_role]

        # send the envelope by setting |status| to "sent". To save as a draft set to "created"
        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()

        try:
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testEmbeddedSigning(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position = '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()

        try:
        
            return_url = 'http://www.docusign.com/developer-center'
            recipient_view_request = docusign.RecipientViewRequest()
            recipient_view_request.return_url = return_url
            recipient_view_request.client_user_id = client_user_id
            recipient_view_request.authentication_method = 'email'
            recipient_view_request.user_name = 'Pat Developer'
            recipient_view_request.email = Username

            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            envelope_id = envelope_summary.envelope_id

            view_url = envelopes_api.create_recipient_view(self.user_info.accounts[0].account_id, envelope_id,
                                                           recipient_view_request=recipient_view_request)

            assert view_url is not None
            assert view_url.url is not None

            # This Url should work in an Iframe or browser to allow signing
            print("ViewUrl is ", end="")
            pprint(view_url)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testCreateTemplate(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()
        # create an envelope to be signed

        envelope_template = docusign.EnvelopeTemplate()
        envelope_template.email_subject = 'Please Sign my Python SDK Envelope (Embedded Signer)'
        envelope_template.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the template
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_template.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position = '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_template.recipients = recipients

        env_template_definition = docusign.EnvelopeTemplateDefinition()
        env_template_definition.name = 'myTemplate'
        envelope_template.envelope_template_definition = env_template_definition

        templates_api = TemplatesApi()

        try:

            template_summary = templates_api.create_template(self.user_info.accounts[0].account_id,
                                                             envelope_template=envelope_template)
            assert template_summary is not None
            assert template_summary.template_id is not None

            print("TemplateSummary: ", end="")
            pprint(template_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testDownLoadEnvelopeDocuments(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a Text tab somewhere on the document for the signer to sign
        text = docusign.Text()
        text.document_id = '1'
        text.page_number = '1'
        text.recipient_id = '1'
        text.x_position = '100'
        text.y_position = '100'
        text.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.text_tabs = [text]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        # send the envelope (otherwise it will be "created" in the Draft folder)
        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()
        try:
            docusign.configuration.api_client = self.api_client

            file1 = envelopes_api.get_document(self.user_info.accounts[0].account_id, 'combined', self.envelope_id)

            assert len(file1) > 0
            subprocess.call('open ' + file1, shell=True)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testListDocuments(self):
        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            docs_list = envelopes_api.list_documents(login_accounts[0].account_id, self.envelope_id)
            assert docs_list is not None
            assert (docs_list.envelope_id == self.envelope_id)

            print("EnvelopeDocumentsResult: ", end="")
            pprint(docs_list)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testResendEnvelope(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position = '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        # send the envelope (otherwise it will be "created" in the Draft folder)
        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()

        try:
            docusign.configuration.api_client = self.api_client

            recipients_update_summary = envelopes_api.update_recipients(self.user_info.accounts[0].account_id,
                                                                        self.envelope_id, recipients=recipients,
                                                                        resend_envelope='true')
            assert recipients_update_summary is not None
            assert len(recipients_update_summary.recipient_update_results) > 0
            assert ("SUCCESS" == recipients_update_summary.recipient_update_results[0].error_details.error_code)
            print("RecipientsUpdateSummary: ", end="")
            pprint(recipients_update_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testGetDiagnosticLogs(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position = '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        # send the envelope (otherwise it will be "created" in the Draft folder)
        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()
        diag_api = DiagnosticsApi()

        try:
            docusign.configuration.api_client = self.api_client

            diagnostics_settings_information = docusign.DiagnosticsSettingsInformation()
            diagnostics_settings_information.api_request_logging = 'true'
            diag_api.update_request_log_settings(diagnostics_settings_information=diagnostics_settings_information)
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            envelope_id = envelope_summary.envelope_id

            file1 = envelopes_api.get_document(self.user_info.accounts[0].account_id, 'combined', envelope_id)
            assert len(file1) > 0
            subprocess.call('open ' + file1, shell=True)

            logs_list = diag_api.list_request_logs()
            request_log_id = logs_list.api_request_logs[0].request_log_id
            file2 = diag_api.get_request_log(request_log_id)
            assert len(file2) > 0
            subprocess.call('open ' + file2, shell=True)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testMoveEnvelopes(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = Username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position = '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        envelope_definition.status = 'sent'

        envelopes_api = EnvelopesApi()

        try:
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

            folders_api = FoldersApi()
            folders_request = docusign.FoldersRequest(envelope_ids=[envelope_summary.envelope_id], from_folder_id="sentitems")

            to_folder_id = "draft"

            folders_api.move_envelopes(self.user_info.accounts[0].account_id, to_folder_id,
                                       folders_request=folders_request)

            # Wait for 1 second to make sure the newly created envelope was moved to the 'sentitems' folder
            # Note: It's discouraged to use sleep statement or to poll DocuSign for envelope status or folder id
            # In production, use DocuSign Connect to get notified when the status of the envelope have changed.
            sleep(1)
            # Test if we moved the envelope to the correct folder
            list_from_drafts_folder = folders_api.list_items(self.user_info.accounts[0].account_id, to_folder_id)

            assert list_from_drafts_folder is not None

            for item in list_from_drafts_folder.folder_items:
                if item.envelope_id == envelope_summary.envelope_id:
                    return

            assert False

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception


if __name__ == '__main__':
    unittest.main()
