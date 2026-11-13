import unittest
from urllib.parse import parse_qs, urlsplit

from docusign_esign.client.api_client import ApiClient


class TestAuthorizationUri(unittest.TestCase):
    def test_query_values_round_trip(self):
        client = ApiClient(oauth_host_name="account-d.docusign.com")
        redirect_uri = "https://example.com/callback?tenant=one&next=%2Fhome"
        state = "a+b&return=/home#fragment"
        try:
            uri = client.get_authorization_uri(
                "client-id", ["signature", "impersonation"],
                redirect_uri, "code", state=state,
            )
            parsed = urlsplit(uri)
            self.assertEqual(parsed.fragment, "")
            self.assertEqual(parse_qs(parsed.query), {
                "response_type": ["code"],
                "scope": ["signature impersonation"],
                "client_id": ["client-id"],
                "redirect_uri": [redirect_uri],
                "state": [state],
            })
        finally:
            client.rest_client.pool_manager.clear()

    def test_optional_state_is_omitted(self):
        client = ApiClient(oauth_host_name="account-d.docusign.com")
        try:
            uri = client.get_authorization_uri(
                "client-id", ["signature"], "https://example.com/callback", "code",
            )
            self.assertNotIn("state", parse_qs(urlsplit(uri).query))
        finally:
            client.rest_client.pool_manager.clear()
