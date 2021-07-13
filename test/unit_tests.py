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
            email_subject = 'Please Sign my Python SDK Envelope'
            email_blurb = 'Hello, Please sign my Python SDK Envelope.'
            template_id = TemplateId

            role_name = 'Needs to sign'
            name = 'Pat Developer'
            email = Username
            t_role = docusign.TemplateRole(role_name=role_name,
                                           name=name,
                                           email=email)
            # send the envelope by setting |status| to "sent". To save as a draft set to "created"
            status = 'sent'
            # create an envelope definition
            envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                              email_blurb=email_blurb,
                                                              template_id=template_id,
                                                              template_roles=[t_role],
                                                              status=status)

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
        except Exception as e:
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

            # parse first account's baseUrl
            base_url, _ = login_accounts[0].base_url.split('/v2')

            # below code required for production, no effect in demo (same domain)
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testRequestASignature(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # Set properties and create an envelope later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        documents = [doc]

        # Create a SignHere tab somewhere on the document for the signer to sign
        document_id = '1'
        page_number = '1'
        recipient_id = '1'
        x_position = '100'
        y_position = '100'
        scale_value = '0.5'
        sign_here = docusign.SignHere(document_id=document_id,
                                      page_number=page_number,
                                      recipient_id=recipient_id,
                                      x_position=x_position,
                                      y_position=y_position,
                                      scale_value=scale_value)
        sign_here_tabs = [sign_here]
        tabs = docusign.Tabs(sign_here_tabs=sign_here_tabs)

        # Add a recipient to sign the document
        email = Username
        name = 'Pat Developer'
        recipient_id = '1'
        signer = docusign.Signer(email=email,
                                 name=name,
                                 recipient_id=recipient_id,
                                 tabs=tabs)
        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        status = 'sent'

        # create the envelope definition with the properties set
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          documents=documents,
                                                          recipients=recipients,
                                                          status=status)

        envelopes_api = EnvelopesApi()

        try:
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testRequestSignatureFromTemplate(self):
        template_role_name = 'Needs to sign'

        # Set properties and create an envelope later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # assign template information including ID and role(s)
        template_id = TemplateId

        # create a template role with a valid templateId and roleName and assign signer info
        role_name = template_role_name
        name = 'Pat Developer'
        email = Username
        t_role = docusign.TemplateRole(role_name=role_name,
                                       name=name,
                                       email=email)

        # create a list of template roles and add our newly created role
        # assign template role(s) to the envelope
        template_roles = [t_role]

        # send the envelope by setting |status| to "sent". To save as a draft set to "created"
        status = 'sent'

        # create the envelope definition with the properties set
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          template_id=template_id,
                                                          template_roles=template_roles,
                                                          status=status)

        envelopes_api = EnvelopesApi()

        try:
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testEmbeddedSigning(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # Set properties and create an envelope later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        name = 'TestFile.pdf'
        document_id = '1'
        doc = docusign.Document(document_base64=base64_doc,
                                name=name,
                                document_id=document_id)
        documents = [doc]

        # Add a recipient to sign the document
        email = Username
        name = 'Pat Developer'
        recipient_id_for_doc = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'

        # Create a SignHere tab somewhere on the document for the signer to sign
        document_id = '1'
        page_number = '1'
        recipient_id = '1'
        x_position = '100'
        y_position = '100'
        scale_value = '0.5'

        # create sign here object with the properties
        sign_here = docusign.SignHere(document_id=document_id,
                                      page_number=page_number,
                                      recipient_id=recipient_id,
                                      x_position=x_position,
                                      y_position=y_position,
                                      scale_value=scale_value)

        sign_here_tabs = [sign_here]
        tabs = docusign.Tabs(sign_here_tabs=sign_here_tabs)

        signer = docusign.Signer(email=email,
                                 name=name,
                                 recipient_id=recipient_id_for_doc,
                                 client_user_id=client_user_id,
                                 tabs=tabs)

        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        status = 'sent'
        # create the envelope definition with the properties set
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          documents=documents,
                                                          recipients=recipients,
                                                          status=status)

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

            # This Url should work in an Iframe or browser to allow signing
            assert view_url is not None
            assert view_url.url is not None

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testCreateTemplate(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()
        # Set properties
        email_subject = 'Please Sign my Python SDK Envelope (Embedded Signer)'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the template
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        name = 'TestFile.pdf'
        document_id = '1'
        doc = docusign.Document(document_base64=base64_doc,
                                name=name,
                                document_id=document_id)
        documents = [doc]

        # Add a recipient to sign the document
        email = Username
        name = 'Pat Developer'
        recipient_id = '1'

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_document_id = '1'
        sign_page_number = '1'
        sign_recipient_id = '1'
        sign_x_position = '100'
        sign_y_position = '100'
        sign_scale_value = '0.5'
        sign_here = docusign.SignHere(document_id=sign_document_id,
                                      page_number=sign_page_number,
                                      recipient_id=sign_recipient_id,
                                      x_position=sign_x_position,
                                      y_position=sign_y_position,
                                      scale_value=sign_scale_value)

        sign_here_tabs = [sign_here]
        tabs = docusign.Tabs(sign_here_tabs=sign_here_tabs)
        signer = docusign.Signer(email=email,
                                 name=name,
                                 recipient_id=recipient_id,
                                 tabs=tabs)

        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        template_name = 'myTemplate'
        env_template_definition = docusign.EnvelopeTemplateDefinition(name=template_name)

        # Create the Envelope template
        envelope_template = docusign.EnvelopeTemplate(email_subject=email_subject,
                                                      email_blurb=email_blurb,
                                                      documents=documents,
                                                      recipients=recipients,
                                                      envelope_template_definition=env_template_definition)

        templates_api = TemplatesApi()

        try:

            template_summary = templates_api.create_template(self.user_info.accounts[0].account_id,
                                                             envelope_template=envelope_template)
            assert template_summary is not None
            assert template_summary.template_id is not None

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testDownLoadEnvelopeDocuments(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # Set properties and create an envelope to be signed
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        document_name = 'TestFile.pdf'
        document_id = '1'
        doc = docusign.Document(document_base64=base64_doc,
                                name=document_name,
                                document_id=document_id)
        documents = [doc]

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'

        # Create a Text tab somewhere on the document for the signer to sign
        text_document_id = '1'
        page_number = '1'
        recipient_id = '1'
        x_position = '100'
        y_position = '100'
        text = docusign.Text(document_id=text_document_id,
                             page_number=page_number,
                             recipient_id=recipient_id,
                             x_position=x_position,
                             y_position=y_position)

        text_tabs = [text]
        tabs = docusign.Tabs(text_tabs=text_tabs)

        # Add a recipient to sign the document
        email = Username
        name = 'Pat Developer'
        recipient_id = '1'
        signer = docusign.Signer(email=email,
                                 name=name,
                                 recipient_id=recipient_id,
                                 client_user_id=client_user_id,
                                 tabs=tabs)

        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        # send the envelope (otherwise it will be "created" in the Draft folder)
        status = 'sent'

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          documents=documents,
                                                          recipients=recipients,
                                                          status=status)

        envelopes_api = EnvelopesApi()
        try:
            docusign.configuration.api_client = self.api_client

            file1 = envelopes_api.get_document(self.user_info.accounts[0].account_id, 'combined', self.envelope_id)

            assert len(file1) > 0
            subprocess.call('open ' + file1, shell=True)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
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

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testResendEnvelope(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # Set properties and create an envelope to be signed later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        name = 'TestFile.pdf'
        document_id = '1'
        doc = docusign.Document(document_base64=base64_doc,
                                name=name,
                                document_id=document_id)
        documents = [doc]

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'

        # Create a SignHere tab somewhere on the document for the signer to sign
        document_id = '1'
        page_number = '1'
        recipient_id = '1'
        x_position = '100'
        y_position = '100'
        scale_value = '0.5'

        sign_here = docusign.SignHere(document_id=document_id,
                                      page_number=page_number,
                                      recipient_id=recipient_id,
                                      x_position=x_position,
                                      y_position=y_position,
                                      scale_value=scale_value)
        sign_here_tabs = [sign_here]
        tabs = docusign.Tabs(sign_here_tabs=sign_here_tabs)

        # Add a recipient to sign the document
        email = Username
        name = 'Pat Developer'
        signer_recipient_id = '1'
        # Create the signer with the information created previous
        signer = docusign.Signer(tabs=tabs,
                                 email=email,
                                 name=name,
                                 recipient_id=signer_recipient_id,
                                 client_user_id=client_user_id)
        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        # send the envelope (otherwise it will be "created" in the Draft folder)
        status = 'sent'

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          documents=documents,
                                                          recipients=recipients,
                                                          status=status)

        envelopes_api = EnvelopesApi()

        try:
            docusign.configuration.api_client = self.api_client

            recipients_update_summary = envelopes_api.update_recipients(self.user_info.accounts[0].account_id,
                                                                        self.envelope_id, recipients=recipients,
                                                                        resend_envelope='true')
            assert recipients_update_summary is not None
            assert len(recipients_update_summary.recipient_update_results) > 0
            assert ("SUCCESS" == recipients_update_summary.recipient_update_results[0].error_details.error_code)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testGetDiagnosticLogs(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # Set properties for envelope and create an envelope to be signed later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        name = 'TestFile.pdf'
        document_id = '1'
        doc = docusign.Document(document_base64=base64_doc,
                                name=name,
                                document_id=document_id)
        documents = [doc]

        # Create a SignHere tab somewhere on the document for the signer to sign
        document_id = '1'
        page_number = '1'
        recipient_id = '1'
        x_position = '100'
        y_position = '100'
        scale_value = '0.5'

        sign_here = docusign.SignHere(document_id=document_id,
                                      page_number=page_number,
                                      recipient_id=recipient_id,
                                      x_position=x_position,
                                      y_position=y_position,
                                      scale_value=scale_value)
        sign_here_tabs = [sign_here]
        tabs = docusign.Tabs(sign_here_tabs=sign_here_tabs)

        # Add a recipient to sign the document
        signer_email = Username
        signer_name = 'Pat Developer'
        signer_recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        signer_client_user_id = '2939'
        signer_tabs = tabs

        signer = docusign.Signer(email=signer_email,
                                 name=signer_name,
                                 recipient_id=signer_recipient_id,
                                 client_user_id=signer_client_user_id,
                                 tabs=signer_tabs)
        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        # send the envelope (otherwise it will be "created" in the Draft folder)
        status = 'sent'

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          documents=documents,
                                                          recipients=recipients,
                                                          status=status)

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
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testGetFormData(self):
        try:
            envelopes_api = EnvelopesApi()

            form_data = envelopes_api.get_form_data(account_id=self.user_info.accounts[0].account_id,
                                                    envelope_id=self.envelope_id)
            assert form_data is not None
            assert form_data.prefill_form_data is not None
            assert form_data.prefill_form_data.form_data[0] is not None
            assert form_data.prefill_form_data.form_data[0].name is not None

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testListTabs(self):
        # For this the template Role should be manager
        template_role_name = 'Manager'

        # Set properties and create an envelope later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # assign template information including ID and role(s)
        template_id = TemplateId

        # create a template role with a valid templateId and roleName and assign signer info
        role_name = template_role_name
        name = 'Pat Developer'
        email = Username
        t_role = docusign.TemplateRole(role_name=role_name,
                                       name=name,
                                       email=email)

        # create a list of template roles and add our newly created role
        # assign template role(s) to the envelope
        template_roles = [t_role]

        # send the envelope by setting |status| to "sent". To save as a draft set to "created"
        status = 'sent'

        # create the envelope definition with the properties set
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          template_id=template_id,
                                                          template_roles=template_roles,
                                                          status=status)
        try:
            envelopes_api = EnvelopesApi()

            # Create Envelope with the new role
            envelope_summary = envelopes_api.create_envelope(self.user_info.accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            # Read the new Envelope
            created_envelope = envelopes_api.get_envelope(account_id=self.user_info.accounts[0].account_id,
                                                          envelope_id=envelope_summary.envelope_id)

            recipients = envelopes_api.list_recipients(account_id=self.user_info.accounts[0].account_id,
                                                       envelope_id=created_envelope.envelope_id)

            tabs = envelopes_api.list_tabs(account_id=self.user_info.accounts[0].account_id,
                                           envelope_id=created_envelope.envelope_id,
                                           recipient_id=recipients.signers[0].recipient_id)
            list_tabs = tabs.list_tabs

            assert list_tabs is not None

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testMoveEnvelopes(self):
        with open(SignTest1File, 'rb') as sign_file:
            file_contents = sign_file.read()

        # Set properties for envelope and create an envelope to be signed later on
        email_subject = 'Please Sign my Python SDK Envelope'
        email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        name = 'TestFile.pdf'
        document_id = '1'
        doc = docusign.Document(document_base64=base64_doc,
                                name=name,
                                document_id=document_id)
        documents = [doc]

        # Add a recipient to sign the document
        email = Username
        name = 'Pat Developer'
        recipient_id = '1'
        signer = docusign.Signer(email=email,
                                 name=name,
                                 recipient_id=recipient_id)

        # Create a SignHere tab somewhere on the document for the signer to sign
        document_id = '1'
        page_number = '1'
        recipient_id = '1'
        x_position = '100'
        y_position = '100'
        scale_value = '0.5'
        sign_here = docusign.SignHere(document_id=document_id,
                                      page_number=page_number,
                                      recipient_id=recipient_id,
                                      x_position=x_position,
                                      y_position=y_position,
                                      scale_value=scale_value)

        sign_here_tabs = [sign_here]
        tabs = docusign.Tabs(sign_here_tabs=sign_here_tabs)
        signer.tabs = tabs

        signers = [signer]
        recipients = docusign.Recipients(signers=signers)

        status = 'sent'
        # Now setting all the properties in previous steps create the envelope now
        envelope_definition = docusign.EnvelopeDefinition(email_subject=email_subject,
                                                          email_blurb=email_blurb,
                                                          documents=documents,
                                                          recipients=recipients,
                                                          status=status)

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

            # Wait for 5 second to make sure the newly created envelope was moved to the 'sentitems' folder
            # Note: It's discouraged to use sleep statement or to poll DocuSign for envelope status or folder id
            # In production, use DocuSign Connect to get notified when the status of the envelope have changed.
            sleep(5)
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
        except Exception as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception


if __name__ == '__main__':
    unittest.main()
