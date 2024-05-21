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
    "cdn origin-group show",
)
class Show(AAZCommand):
    """Get an existing origin group within an endpoint.
    """

    _aaz_info = {
        "version": "2024-02-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/endpoints/{}/origingroups/{}", "2024-02-01"],
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
        _args_schema.endpoint_name = AAZStrArg(
            options=["--endpoint-name"],
            help="Name of the endpoint under the profile which is unique globally.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.origin_group_name = AAZStrArg(
            options=["-n", "--name", "--origin-group-name"],
            help="Name of the origin group which is unique within the endpoint.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the CDN profile which is unique within the resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.OriginGroupsGet(ctx=self.ctx)()
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

    class OriginGroupsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "endpointName", self.ctx.args.endpoint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "originGroupName", self.ctx.args.origin_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2024-02-01",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.health_probe_settings = AAZObjectType(
                serialized_name="healthProbeSettings",
            )
            properties.origins = AAZListType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_state = AAZStrType(
                serialized_name="resourceState",
                flags={"read_only": True},
            )
            properties.response_based_origin_error_detection_settings = AAZObjectType(
                serialized_name="responseBasedOriginErrorDetectionSettings",
            )
            properties.traffic_restoration_time_to_healed_or_new_endpoints_in_minutes = AAZIntType(
                serialized_name="trafficRestorationTimeToHealedOrNewEndpointsInMinutes",
            )

            health_probe_settings = cls._schema_on_200.properties.health_probe_settings
            health_probe_settings.probe_interval_in_seconds = AAZIntType(
                serialized_name="probeIntervalInSeconds",
            )
            health_probe_settings.probe_path = AAZStrType(
                serialized_name="probePath",
            )
            health_probe_settings.probe_protocol = AAZStrType(
                serialized_name="probeProtocol",
            )
            health_probe_settings.probe_request_type = AAZStrType(
                serialized_name="probeRequestType",
            )

            origins = cls._schema_on_200.properties.origins
            origins.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.origins.Element
            _element.id = AAZStrType()

            response_based_origin_error_detection_settings = cls._schema_on_200.properties.response_based_origin_error_detection_settings
            response_based_origin_error_detection_settings.http_error_ranges = AAZListType(
                serialized_name="httpErrorRanges",
            )
            response_based_origin_error_detection_settings.response_based_detected_error_types = AAZStrType(
                serialized_name="responseBasedDetectedErrorTypes",
            )
            response_based_origin_error_detection_settings.response_based_failover_threshold_percentage = AAZIntType(
                serialized_name="responseBasedFailoverThresholdPercentage",
            )

            http_error_ranges = cls._schema_on_200.properties.response_based_origin_error_detection_settings.http_error_ranges
            http_error_ranges.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.response_based_origin_error_detection_settings.http_error_ranges.Element
            _element.begin = AAZIntType()
            _element.end = AAZIntType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
