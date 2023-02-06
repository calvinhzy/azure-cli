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
    "network traffic-manager profile update",
)
class Update(AAZCommand):
    """Update a traffic manager profile.

    :example: Update a traffic manager profile to change the TTL to 300.
        az network traffic-manager profile update -g MyResourceGroup -n MyTmProfile --ttl 300

    :example: Update a traffic manager profile. (autogenerated)
        az network traffic-manager profile update --name MyTmProfile --resource-group MyResourceGroup --status Enabled

    :example: Update a traffic manager profile.
        az network traffic-manager profile update -n MyTmProfile -g MyResourceGroup --status-code-ranges [{min:200,max:204}] --custom-headers  [{name:foo,value:doo},{name:test,value:best}]
    """

    _aaz_info = {
        "version": "2022-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/trafficmanagerprofiles/{}", "2022-04-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the Traffic Manager profile.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "DnsConfig"

        _args_schema = cls._args_schema
        _args_schema.ttl = AAZIntArg(
            options=["--ttl"],
            arg_group="DnsConfig",
            help="DNS config time-to-live in seconds.",
            nullable=True,
        )

        # define Arg Group "Monitor Configuration"

        _args_schema = cls._args_schema
        _args_schema.custom_headers = AAZListArg(
            options=["--custom-headers"],
            arg_group="Monitor Configuration",
            help="Space-separated list of names or values.",
            nullable=True,
        )
        _args_schema.status_code_ranges = AAZListArg(
            options=["--status-code-ranges"],
            arg_group="Monitor Configuration",
            help="Space-separated list of status codes in shorthand-syntax format.",
            nullable=True,
        )
        _args_schema.interval = AAZIntArg(
            options=["--interval"],
            arg_group="Monitor Configuration",
            help="The interval in seconds at which health checks are conducted.",
            nullable=True,
        )
        _args_schema.path = AAZStrArg(
            options=["--path"],
            arg_group="Monitor Configuration",
            help="Path to monitor. Use \"\"('\"\"' in PowerShell) for none.",
            nullable=True,
        )
        _args_schema.port = AAZIntArg(
            options=["--port"],
            arg_group="Monitor Configuration",
            help="Port to monitor.",
            nullable=True,
        )
        _args_schema.protocol = AAZStrArg(
            options=["--protocol"],
            arg_group="Monitor Configuration",
            help="Monitor protocol.  Allowed values: HTTP, HTTPS, TCP.",
            nullable=True,
            enum={"HTTP": "HTTP", "HTTPS": "HTTPS", "TCP": "TCP"},
        )
        _args_schema.timeout = AAZIntArg(
            options=["--timeout"],
            arg_group="Monitor Configuration",
            help="The time in seconds allowed for endpoints to respond to a health check.",
            nullable=True,
        )
        _args_schema.max_failures = AAZIntArg(
            options=["--max-failures"],
            arg_group="Monitor Configuration",
            help="The number of consecutive failed health checks tolerated before an endpoint is considered degraded.",
            nullable=True,
        )

        custom_headers = cls._args_schema.custom_headers
        custom_headers.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.custom_headers.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="Header name.",
            nullable=True,
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="Header value.",
            nullable=True,
        )

        status_code_ranges = cls._args_schema.status_code_ranges
        status_code_ranges.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.status_code_ranges.Element
        _element.max = AAZIntArg(
            options=["max"],
            help="Max status code.",
            nullable=True,
        )
        _element.min = AAZIntArg(
            options=["min"],
            help="Min status code.",
            nullable=True,
        )

        # define Arg Group "MonitorConfig"

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Space-separated tags: key[=value] [key[=value] ...].",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.max_return = AAZIntArg(
            options=["--max-return"],
            arg_group="Properties",
            help="Maximum number of endpoints to be returned for MultiValue routing type.",
            nullable=True,
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="Status of the Traffic Manager profile.  Allowed values: Disabled, Enabled.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.routing_method = AAZStrArg(
            options=["--routing-method"],
            arg_group="Properties",
            help="Routing method.",
            nullable=True,
            enum={"Geographic": "Geographic", "MultiValue": "MultiValue", "Performance": "Performance", "Priority": "Priority", "Subnet": "Subnet", "Weighted": "Weighted"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ProfilesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.ProfilesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ProfilesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "profileName", self.ctx.args.name,
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
                    "api-version", "2022-04-01-preview",
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
            _build_schema_profile_read(cls._schema_on_200)

            return cls._schema_on_200

    class ProfilesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "profileName", self.ctx.args.name,
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
                    "api-version", "2022-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_profile_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("dnsConfig", AAZObjectType)
                properties.set_prop("maxReturn", AAZIntType, ".max_return")
                properties.set_prop("monitorConfig", AAZObjectType)
                properties.set_prop("profileStatus", AAZStrType, ".status")
                properties.set_prop("trafficRoutingMethod", AAZStrType, ".routing_method")

            dns_config = _builder.get(".properties.dnsConfig")
            if dns_config is not None:
                dns_config.set_prop("ttl", AAZIntType, ".ttl")

            monitor_config = _builder.get(".properties.monitorConfig")
            if monitor_config is not None:
                monitor_config.set_prop("customHeaders", AAZListType, ".custom_headers")
                monitor_config.set_prop("expectedStatusCodeRanges", AAZListType, ".status_code_ranges")
                monitor_config.set_prop("intervalInSeconds", AAZIntType, ".interval")
                monitor_config.set_prop("path", AAZStrType, ".path")
                monitor_config.set_prop("port", AAZIntType, ".port")
                monitor_config.set_prop("protocol", AAZStrType, ".protocol")
                monitor_config.set_prop("timeoutInSeconds", AAZIntType, ".timeout")
                monitor_config.set_prop("toleratedNumberOfFailures", AAZIntType, ".max_failures")

            custom_headers = _builder.get(".properties.monitorConfig.customHeaders")
            if custom_headers is not None:
                custom_headers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.monitorConfig.customHeaders[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("value", AAZStrType, ".value")

            expected_status_code_ranges = _builder.get(".properties.monitorConfig.expectedStatusCodeRanges")
            if expected_status_code_ranges is not None:
                expected_status_code_ranges.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.monitorConfig.expectedStatusCodeRanges[]")
            if _elements is not None:
                _elements.set_prop("max", AAZIntType, ".max")
                _elements.set_prop("min", AAZIntType, ".min")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_profile_read = None


def _build_schema_profile_read(_schema):
    global _schema_profile_read
    if _schema_profile_read is not None:
        _schema.id = _schema_profile_read.id
        _schema.location = _schema_profile_read.location
        _schema.name = _schema_profile_read.name
        _schema.properties = _schema_profile_read.properties
        _schema.tags = _schema_profile_read.tags
        _schema.type = _schema_profile_read.type
        return

    _schema_profile_read = AAZObjectType()

    profile_read = _schema_profile_read
    profile_read.id = AAZStrType()
    profile_read.location = AAZStrType()
    profile_read.name = AAZStrType()
    profile_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    profile_read.tags = AAZDictType()
    profile_read.type = AAZStrType()

    properties = _schema_profile_read.properties
    properties.allowed_endpoint_record_types = AAZListType(
        serialized_name="allowedEndpointRecordTypes",
    )
    properties.dns_config = AAZObjectType(
        serialized_name="dnsConfig",
    )
    properties.endpoints = AAZListType()
    properties.max_return = AAZIntType(
        serialized_name="maxReturn",
    )
    properties.monitor_config = AAZObjectType(
        serialized_name="monitorConfig",
    )
    properties.profile_status = AAZStrType(
        serialized_name="profileStatus",
    )
    properties.traffic_routing_method = AAZStrType(
        serialized_name="trafficRoutingMethod",
    )
    properties.traffic_view_enrollment_status = AAZStrType(
        serialized_name="trafficViewEnrollmentStatus",
    )

    allowed_endpoint_record_types = _schema_profile_read.properties.allowed_endpoint_record_types
    allowed_endpoint_record_types.Element = AAZStrType()

    dns_config = _schema_profile_read.properties.dns_config
    dns_config.fqdn = AAZStrType(
        flags={"read_only": True},
    )
    dns_config.relative_name = AAZStrType(
        serialized_name="relativeName",
    )
    dns_config.ttl = AAZIntType()

    endpoints = _schema_profile_read.properties.endpoints
    endpoints.Element = AAZObjectType()

    _element = _schema_profile_read.properties.endpoints.Element
    _element.id = AAZStrType()
    _element.name = AAZStrType()
    _element.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    _element.type = AAZStrType()

    properties = _schema_profile_read.properties.endpoints.Element.properties
    properties.always_serve = AAZStrType(
        serialized_name="alwaysServe",
    )
    properties.custom_headers = AAZListType(
        serialized_name="customHeaders",
    )
    properties.endpoint_location = AAZStrType(
        serialized_name="endpointLocation",
    )
    properties.endpoint_monitor_status = AAZStrType(
        serialized_name="endpointMonitorStatus",
    )
    properties.endpoint_status = AAZStrType(
        serialized_name="endpointStatus",
    )
    properties.geo_mapping = AAZListType(
        serialized_name="geoMapping",
    )
    properties.min_child_endpoints = AAZIntType(
        serialized_name="minChildEndpoints",
    )
    properties.min_child_endpoints_i_pv4 = AAZIntType(
        serialized_name="minChildEndpointsIPv4",
    )
    properties.min_child_endpoints_i_pv6 = AAZIntType(
        serialized_name="minChildEndpointsIPv6",
    )
    properties.priority = AAZIntType()
    properties.subnets = AAZListType()
    properties.target = AAZStrType()
    properties.target_resource_id = AAZStrType(
        serialized_name="targetResourceId",
    )
    properties.weight = AAZIntType()

    custom_headers = _schema_profile_read.properties.endpoints.Element.properties.custom_headers
    custom_headers.Element = AAZObjectType()

    _element = _schema_profile_read.properties.endpoints.Element.properties.custom_headers.Element
    _element.name = AAZStrType()
    _element.value = AAZStrType()

    geo_mapping = _schema_profile_read.properties.endpoints.Element.properties.geo_mapping
    geo_mapping.Element = AAZStrType()

    subnets = _schema_profile_read.properties.endpoints.Element.properties.subnets
    subnets.Element = AAZObjectType()

    _element = _schema_profile_read.properties.endpoints.Element.properties.subnets.Element
    _element.first = AAZStrType()
    _element.last = AAZStrType()
    _element.scope = AAZIntType()

    monitor_config = _schema_profile_read.properties.monitor_config
    monitor_config.custom_headers = AAZListType(
        serialized_name="customHeaders",
    )
    monitor_config.expected_status_code_ranges = AAZListType(
        serialized_name="expectedStatusCodeRanges",
    )
    monitor_config.interval_in_seconds = AAZIntType(
        serialized_name="intervalInSeconds",
    )
    monitor_config.path = AAZStrType()
    monitor_config.port = AAZIntType()
    monitor_config.profile_monitor_status = AAZStrType(
        serialized_name="profileMonitorStatus",
    )
    monitor_config.protocol = AAZStrType()
    monitor_config.timeout_in_seconds = AAZIntType(
        serialized_name="timeoutInSeconds",
    )
    monitor_config.tolerated_number_of_failures = AAZIntType(
        serialized_name="toleratedNumberOfFailures",
    )

    custom_headers = _schema_profile_read.properties.monitor_config.custom_headers
    custom_headers.Element = AAZObjectType()

    _element = _schema_profile_read.properties.monitor_config.custom_headers.Element
    _element.name = AAZStrType()
    _element.value = AAZStrType()

    expected_status_code_ranges = _schema_profile_read.properties.monitor_config.expected_status_code_ranges
    expected_status_code_ranges.Element = AAZObjectType()

    _element = _schema_profile_read.properties.monitor_config.expected_status_code_ranges.Element
    _element.max = AAZIntType()
    _element.min = AAZIntType()

    tags = _schema_profile_read.tags
    tags.Element = AAZStrType()

    _schema.id = _schema_profile_read.id
    _schema.location = _schema_profile_read.location
    _schema.name = _schema_profile_read.name
    _schema.properties = _schema_profile_read.properties
    _schema.tags = _schema_profile_read.tags
    _schema.type = _schema_profile_read.type


__all__ = ["Update"]
