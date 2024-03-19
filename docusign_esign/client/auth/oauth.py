# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import json
from pprint import pformat
from six import iteritems


class OAuth(object):
    """
        NOTE: This class is auto generated by the swagger code generator program.
        Do not edit the class manually.
        """
    #  create and send envelopes, and obtain links for starting signing sessions.
    SCOPE_SIGNATURE = "signature"
    #  obtain a refresh token with an extended lifetime.
    SCOPE_EXTENDED = "extended"
    #  obtain access to the user’s account when the user is not present.
    SCOPE_IMPERSONATION = "impersonation"

    #  OAuth Base path constants
    #  Demo server base path
    DEMO_OAUTH_BASE_PATH = "account-d.docusign.com"
    #  Production server base path
    PRODUCTION_OAUTH_BASE_PATH = "account.docusign.com"
    #  Stage server base path
    STAGE_OAUTH_BASE_PATH = "account-s.docusign.com"
    #   JWT Grant Type
    GRANT_TYPE_JWT = "urn:ietf:params:oauth:grant-type:jwt-bearer"


class OAuthUserInfo(object):

    def __init__(self, sub=None, email=None, accounts=None, name=None, given_name=None, family_name=None,
                 created=None):

        self.swagger_types = {
            'sub': 'str',
            'email': 'str',
            'accounts': 'list[Account]',
            'name': 'str',
            'given_name': 'str',
            'family_name': 'str',
            'created': 'str'
        }

        self.attribute_map = {
            'sub': 'sub',
            'email': 'email',
            'accounts': 'accounts',
            'name': 'name',
            'given_name': 'given_name',
            'family_name': 'family_name',
            'created': 'created'
        }
        self._sub = sub
        self._email = email
        self._accounts = accounts
        self._name = name
        self._given_name = given_name
        self._family_name = family_name
        self._created = created

    @property
    def sub(self):
        return self._sub

    @sub.setter
    def sub(self, sub):
        self._sub = sub

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created):
        self._created = created

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        self._given_name = given_name

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        self._family_name = family_name

    def list(self):
        return self._accounts

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    def add_account(self, account):
        if not self.accounts:
            self._accounts = list()
        self._accounts.append(account)

    def get_accounts(self):
        if not self.accounts:
            self._accounts = list()
        return self._accounts

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def __str__(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def to_indented_string(self, obj):
        """
         Convert the given object to string with each line indented by 4
         spaces (except the first line).
        :param obj:
        :return:
        """
        if obj:
            return str(obj).replace("\n", "\n    ")
        return ""


class Account(object):
    def __init__(self, account_id=None, is_default=None, account_name=None, base_uri=None, organization=None):
        self.swagger_types = {
            'account_id': 'str',
            'is_default': 'str',
            'account_name': 'str',
            'base_uri': 'str',
            'organization': 'str',
        }

        self.attribute_map =  {
            'account_id': 'account_id',
            'is_default': 'is_default',
            'account_name': 'account_name',
            'base_uri': 'base_uri',
            'organization': 'organization',
        }
        self._account_id = account_id
        self.is_default = is_default
        self._account_name = account_name
        self._base_uri = base_uri
        self._organization = organization

    def get_is_default(self):
        return self.get_is_default

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def is_default(self):
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        self._is_default = is_default

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

    @property
    def base_uri(self):
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri):
        self._base_uri = base_uri

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, organization):
        self._organization = organization


class Link(object):
    def __init__(self, rel=None, href=None):
        self._rel = rel
        self._href = href

    @property
    def rel(self):
        return self._rel

    @rel.setter
    def rel(self, rel):
        self._rel = rel

    @property
    def href(self):
        return self._href

    @href.setter
    def organization(self, href):
        self._href = href

    def __str__(self):
        return "class Link {\n    rel: {}\n    href: {}".format(self.to_indented_string(self.rel),
                                                                self.to_indented_string(self.href))

    def to_indented_string(self, obj):
        """
         Convert the given object to string with each line indented by 4
         spaces (except the first line).
        :param obj: 
        :return: 
        """
        if obj:
            return str(obj).replace("\n", "\n    ")
        return None

    def __eq__(self, other):
        if not other:
            return False
        return (self.rel == other.rel or self.rel and self.rel == other.rel) and \
                (self.href == other.href or self.href and self.href == other.href)

    def to_json(self):
        pass


class Organization(object):
    def __init__(self, organization_id=None, links=None):
        self._organization_id = organization_id
        self._links = links

    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        self._organization_id = organization_id

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    def list(self):
        if not self._links:
            self._links = list()
        return self._links

    def add_links(self, link):
        if not self.links:
            self.links = list()
        self._links.append(link)

    def __str__(self):
        return "class Organization {\n    organization_id: {}\n    links: {}".format(
            self.to_indented_string(self._organization_id),
            self.to_indented_string(self._links)
        )

    def to_indented_string(self, obj):

        if obj:
            return str(obj).replace("\n", "\n    ")
        return None

    def __eq__(self, other):
        if not other:
            return False
        return (self.organization_id == other.organization_id or self.organization_id
                and self.organization_id == other.organization_id) and\
               (self.links == other.links or self.links and self.links == other.links)


class OAuthToken(object):

    def __init__(self, access_token=None, data=None, expires_in=None, refresh_token=None, scope=None, token_type=None):
        """
        OAuthToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_token': 'str',
            'data': 'list[NameValue]',
            'expires_in': 'str',
            'refresh_token': 'str',
            'scope': 'str',
            'token_type': 'str'
        }

        self.attribute_map = {
            'access_token': 'access_token',
            'data': 'data',
            'expires_in': 'expires_in',
            'refresh_token': 'refresh_token',
            'scope': 'scope',
            'token_type': 'token_type'
        }

        self._access_token = access_token
        self._data = data
        self._expires_in = expires_in
        self._refresh_token = refresh_token
        self._scope = scope
        self._token_type = token_type

    @property
    def access_token(self):
        """
        Gets the access_token of this OAuthToken.
        Access token information.

        :return: The access_token of this OAuthToken.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this OAuthToken.
        Access token information.

        :param access_token: The access_token of this OAuthToken.
        :type: str
        """

        self._access_token = access_token

    @property
    def data(self):
        """
        Gets the data of this OAuthToken.
        

        :return: The data of this OAuthToken.
        :rtype: list[NameValue]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this OAuthToken.
        

        :param data: The data of this OAuthToken.
        :type: list[NameValue]
        """

        self._data = data

    @property
    def expires_in(self):
        """
        Gets the expires_in of this OAuthToken.
        

        :return: The expires_in of this OAuthToken.
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this OAuthToken.
        

        :param expires_in: The expires_in of this OAuthToken.
        :type: str
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this OAuthToken.
        

        :return: The refresh_token of this OAuthToken.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this OAuthToken.
        

        :param refresh_token: The refresh_token of this OAuthToken.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """
        Gets the scope of this OAuthToken.
        Must be set to \"api\".

        :return: The scope of this OAuthToken.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this OAuthToken.
        Must be set to \"api\".

        :param scope: The scope of this OAuthToken.
        :type: str
        """

        self._scope = scope

    @property
    def token_type(self):
        """
        Gets the token_type of this OAuthToken.
        

        :return: The token_type of this OAuthToken.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this OAuthToken.
        

        :param token_type: The token_type of this OAuthToken.
        :type: str
        """

        self._token_type = token_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other