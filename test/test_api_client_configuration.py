# coding: utf-8

from __future__ import absolute_import

import unittest

import urllib3

from docusign_esign.client.api_client import ApiClient
from docusign_esign.client.configuration import Configuration


class TestApiClientConfiguration(unittest.TestCase):

    def test_default_configuration_when_none_provided(self):
        client = ApiClient()
        assert isinstance(client.rest_client.pool_manager, urllib3.PoolManager)

    def test_custom_configuration_is_used(self):
        config = Configuration()
        config.proxy = "http://127.0.0.1:3129"

        client = ApiClient(configuration=config)
        assert isinstance(client.rest_client.pool_manager, urllib3.ProxyManager)

    def test_proxy_url_is_applied(self):
        config = Configuration()
        config.proxy = "http://myproxy.corp:8080"

        client = ApiClient(configuration=config)
        pool_manager = client.rest_client.pool_manager
        assert isinstance(pool_manager, urllib3.ProxyManager)
        assert pool_manager.proxy.scheme == "http"
        assert pool_manager.proxy.host == "myproxy.corp"
        assert pool_manager.proxy.port == 8080

    def test_no_proxy_uses_pool_manager(self):
        config = Configuration()
        config.proxy = None

        client = ApiClient(configuration=config)
        assert isinstance(client.rest_client.pool_manager, urllib3.PoolManager)

    def test_custom_host_with_configuration(self):
        config = Configuration()
        config.proxy = "http://127.0.0.1:3129"

        client = ApiClient(host="https://custom.docusign.net/restapi", configuration=config)
        assert client.host == "https://custom.docusign.net/restapi"
        assert isinstance(client.rest_client.pool_manager, urllib3.ProxyManager)

    def test_configuration_host_used_when_host_param_is_none(self):
        config = Configuration()
        config.host = "https://from-config.docusign.net/restapi"

        client = ApiClient(configuration=config)
        assert client.host == "https://from-config.docusign.net/restapi"


if __name__ == '__main__':
    unittest.main()
