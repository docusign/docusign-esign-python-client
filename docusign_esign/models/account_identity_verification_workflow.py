# coding: utf-8

"""
    Docusign eSignature REST API

    The Docusign eSignature REST API provides you with a powerful, convenient, and simple Web services API for interacting with Docusign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class AccountIdentityVerificationWorkflow(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_description': 'str',
        'default_name': 'str',
        'input_options': 'list[AccountIdentityInputOption]',
        'is_disabled': 'str',
        'owner_type': 'str',
        'signature_provider': 'AccountSignatureProvider',
        'steps': 'list[AccountIdentityVerificationStep]',
        'workflow_id': 'str',
        'workflow_label': 'str',
        'workflow_resource_key': 'str'
    }

    attribute_map = {
        'default_description': 'defaultDescription',
        'default_name': 'defaultName',
        'input_options': 'inputOptions',
        'is_disabled': 'isDisabled',
        'owner_type': 'ownerType',
        'signature_provider': 'signatureProvider',
        'steps': 'steps',
        'workflow_id': 'workflowId',
        'workflow_label': 'workflowLabel',
        'workflow_resource_key': 'workflowResourceKey'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AccountIdentityVerificationWorkflow - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default_description = None
        self._default_name = None
        self._input_options = None
        self._is_disabled = None
        self._owner_type = None
        self._signature_provider = None
        self._steps = None
        self._workflow_id = None
        self._workflow_label = None
        self._workflow_resource_key = None
        self.discriminator = None

        setattr(self, "_{}".format('default_description'), kwargs.get('default_description', None))
        setattr(self, "_{}".format('default_name'), kwargs.get('default_name', None))
        setattr(self, "_{}".format('input_options'), kwargs.get('input_options', None))
        setattr(self, "_{}".format('is_disabled'), kwargs.get('is_disabled', None))
        setattr(self, "_{}".format('owner_type'), kwargs.get('owner_type', None))
        setattr(self, "_{}".format('signature_provider'), kwargs.get('signature_provider', None))
        setattr(self, "_{}".format('steps'), kwargs.get('steps', None))
        setattr(self, "_{}".format('workflow_id'), kwargs.get('workflow_id', None))
        setattr(self, "_{}".format('workflow_label'), kwargs.get('workflow_label', None))
        setattr(self, "_{}".format('workflow_resource_key'), kwargs.get('workflow_resource_key', None))

    @property
    def default_description(self):
        """Gets the default_description of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The default_description of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._default_description

    @default_description.setter
    def default_description(self, default_description):
        """Sets the default_description of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param default_description: The default_description of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._default_description = default_description

    @property
    def default_name(self):
        """Gets the default_name of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The default_name of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._default_name

    @default_name.setter
    def default_name(self, default_name):
        """Sets the default_name of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param default_name: The default_name of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._default_name = default_name

    @property
    def input_options(self):
        """Gets the input_options of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The input_options of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: list[AccountIdentityInputOption]
        """
        return self._input_options

    @input_options.setter
    def input_options(self, input_options):
        """Sets the input_options of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param input_options: The input_options of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: list[AccountIdentityInputOption]
        """

        self._input_options = input_options

    @property
    def is_disabled(self):
        """Gets the is_disabled of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The is_disabled of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param is_disabled: The is_disabled of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._is_disabled = is_disabled

    @property
    def owner_type(self):
        """Gets the owner_type of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The owner_type of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param owner_type: The owner_type of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._owner_type = owner_type

    @property
    def signature_provider(self):
        """Gets the signature_provider of this AccountIdentityVerificationWorkflow.  # noqa: E501

        The signature provider associated with the Identity Verification workflow.  # noqa: E501

        :return: The signature_provider of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: AccountSignatureProvider
        """
        return self._signature_provider

    @signature_provider.setter
    def signature_provider(self, signature_provider):
        """Sets the signature_provider of this AccountIdentityVerificationWorkflow.

        The signature provider associated with the Identity Verification workflow.  # noqa: E501

        :param signature_provider: The signature_provider of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: AccountSignatureProvider
        """

        self._signature_provider = signature_provider

    @property
    def steps(self):
        """Gets the steps of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The steps of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: list[AccountIdentityVerificationStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param steps: The steps of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: list[AccountIdentityVerificationStep]
        """

        self._steps = steps

    @property
    def workflow_id(self):
        """Gets the workflow_id of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The workflow_id of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param workflow_id: The workflow_id of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def workflow_label(self):
        """Gets the workflow_label of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The workflow_label of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_label

    @workflow_label.setter
    def workflow_label(self, workflow_label):
        """Sets the workflow_label of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param workflow_label: The workflow_label of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._workflow_label = workflow_label

    @property
    def workflow_resource_key(self):
        """Gets the workflow_resource_key of this AccountIdentityVerificationWorkflow.  # noqa: E501

          # noqa: E501

        :return: The workflow_resource_key of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_resource_key

    @workflow_resource_key.setter
    def workflow_resource_key(self, workflow_resource_key):
        """Sets the workflow_resource_key of this AccountIdentityVerificationWorkflow.

          # noqa: E501

        :param workflow_resource_key: The workflow_resource_key of this AccountIdentityVerificationWorkflow.  # noqa: E501
        :type: str
        """

        self._workflow_resource_key = workflow_resource_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AccountIdentityVerificationWorkflow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountIdentityVerificationWorkflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountIdentityVerificationWorkflow):
            return True

        return self.to_dict() != other.to_dict()
