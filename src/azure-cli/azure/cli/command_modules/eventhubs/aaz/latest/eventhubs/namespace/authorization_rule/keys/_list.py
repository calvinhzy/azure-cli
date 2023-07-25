# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "eventhubs namespace authorization-rule keys list",
)
class List(AAZCommand):
    """Gets the primary and secondary connection strings for the Namespace.

    :example: Shows the connection strings of Authorizationrule for the namespace.
        az eventhubs namespace authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
    """

    _aaz_info = {
        "version": "2023-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}/authorizationrules/{}/listkeys", "2023-01-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.authorization_rule_name = AAZStrArg(
            options=["--name", "--authorization-rule-name"],
            help="The authorization rule name.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The Namespace name",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NamespacesListKeys(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NamespacesListKeys(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/authorizationRules/{authorizationRuleName}/listKeys",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "authorizationRuleName", self.ctx.args.authorization_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.alias_primary_connection_string = AAZStrType(
                serialized_name="aliasPrimaryConnectionString",
                flags={"read_only": True},
            )
            _schema_on_200.alias_secondary_connection_string = AAZStrType(
                serialized_name="aliasSecondaryConnectionString",
                flags={"read_only": True},
            )
            _schema_on_200.key_name = AAZStrType(
                serialized_name="keyName",
                flags={"read_only": True},
            )
            _schema_on_200.primary_connection_string = AAZStrType(
                serialized_name="primaryConnectionString",
                flags={"read_only": True},
            )
            _schema_on_200.primary_key = AAZStrType(
                serialized_name="primaryKey",
                flags={"read_only": True},
            )
            _schema_on_200.secondary_connection_string = AAZStrType(
                serialized_name="secondaryConnectionString",
                flags={"read_only": True},
            )
            _schema_on_200.secondary_key = AAZStrType(
                serialized_name="secondaryKey",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
