"""Offline regressions for the access-token header helper."""

import json
import unittest
from unittest.mock import Mock

from docusign_esign.client.api_client import ApiClient
from docusign_esign.client.auth.oauth import OAuthToken


class TestAccessTokenHeader(unittest.TestCase):
    """Exercise token models through actual request construction."""

    def test_token_object_sets_bearer_header(self):
        client = ApiClient()
        token = OAuthToken(access_token='test-token', token_type='Bearer')
        client.set_access_token(token)
        self.assertEqual(client.default_headers['Authorization'], 'Bearer test-token')
        self.assertEqual(token.access_token, 'test-token')

    def test_deserialized_token_reaches_http_request(self):
        client = ApiClient()
        response = Mock(data=json.dumps({'access_token': 'new-token', 'token_type': 'Bearer'}))
        token = client.deserialize(response, OAuthToken)
        client.set_access_token(token)
        client.rest_client.GET = Mock(return_value=Mock())
        client.call_api('/accounts', 'GET', _preload_content=False, _return_http_data_only=True)
        headers = client.rest_client.GET.call_args.kwargs['headers']
        self.assertEqual(headers['Authorization'], 'Bearer new-token')
        self.assertEqual(headers['X-DocuSign-SDK'], 'Python')

    def test_setting_new_token_replaces_old_header(self):
        client = ApiClient(header_name='Authorization', header_value='Bearer old-token')
        client.set_access_token(OAuthToken(access_token='replacement-token'))
        self.assertEqual(client.default_headers['Authorization'], 'Bearer replacement-token')


if __name__ == '__main__':
    unittest.main()
