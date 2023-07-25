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
    "eventhubs eventhub update",
)
class Update(AAZCommand):
    """Update a new Event Hub as a nested resource within a Namespace.
    """

    _aaz_info = {
        "version": "2023-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}/eventhubs/{}", "2023-01-01-preview"],
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
        _args_schema.event_hub_name = AAZStrArg(
            options=["-n", "--name", "--event-hub-name"],
            help="The Event Hub name",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                max_length=256,
                min_length=1,
            ),
        )
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The Namespace name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9-]{6,50}[a-zA-Z0-9]$",
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "CaptureDescription"

        _args_schema = cls._args_schema
        _args_schema.enable_capture = AAZBoolArg(
            options=["--enable-capture"],
            arg_group="CaptureDescription",
            help="A value that indicates whether capture description is enabled.",
            nullable=True,
        )
        _args_schema.encoding = AAZStrArg(
            options=["--encoding"],
            arg_group="CaptureDescription",
            help="Enumerates the possible values for the encoding format of capture description. Note: 'AvroDeflate' will be deprecated in New API Version",
            nullable=True,
            enum={"Avro": "Avro", "AvroDeflate": "AvroDeflate"},
        )
        _args_schema.capture_interval = AAZIntArg(
            options=["--capture-interval"],
            arg_group="CaptureDescription",
            help="The time window allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds",
            nullable=True,
        )
        _args_schema.capture_size_limit = AAZIntArg(
            options=["--capture-size-limit"],
            arg_group="CaptureDescription",
            help="The size window defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 to 524288000 bytes",
            nullable=True,
        )
        _args_schema.skip_empty_archives = AAZBoolArg(
            options=["--skip-empty-archives"],
            arg_group="CaptureDescription",
            help="A value that indicates whether to Skip Empty Archives",
            nullable=True,
        )

        # define Arg Group "Destination"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Destination",
            help="A value that indicates whether capture description is enabled. ",
            nullable=True,
        )
        _args_schema.destination_name = AAZStrArg(
            options=["--destination-name"],
            arg_group="Destination",
            help="Name for capture destination",
            nullable=True,
        )
        _args_schema.archive_name_format = AAZStrArg(
            options=["--archive-name-format"],
            arg_group="Destination",
            help="Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order",
            nullable=True,
        )
        _args_schema.blob_container = AAZStrArg(
            options=["--blob-container"],
            arg_group="Destination",
            help="Blob container Name",
            nullable=True,
        )
        _args_schema.storage_account = AAZStrArg(
            options=["--storage-account"],
            arg_group="Destination",
            help="Resource id of the storage account to be used to create the blobs",
            nullable=True,
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of Azure Active Directory Managed Identity.",
            nullable=True,
            enum={"SystemAssigned": "SystemAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identity = AAZStrArg(
            options=["user-assigned-identity"],
            help="ARM ID of Managed User Identity. This property is required is the type is UserAssignedIdentity. If type is SystemAssigned, then the System Assigned Identity Associated with the namespace will be used.",
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.partition_count = AAZIntArg(
            options=["--partition-count"],
            arg_group="Properties",
            help="Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="Enumerates the possible values for the status of the Event Hub.",
            nullable=True,
            enum={"Active": "Active", "Creating": "Creating", "Deleting": "Deleting", "Disabled": "Disabled", "ReceiveDisabled": "ReceiveDisabled", "Renaming": "Renaming", "Restoring": "Restoring", "SendDisabled": "SendDisabled", "Unknown": "Unknown"},
        )

        # define Arg Group "RetentionDescription"

        _args_schema = cls._args_schema
        _args_schema.cleanup_policy = AAZStrArg(
            options=["--cleanup-policy"],
            arg_group="RetentionDescription",
            help="Enumerates the possible values for cleanup policy",
            nullable=True,
            enum={"Compact": "Compact", "Delete": "Delete"},
        )
        _args_schema.retention_time_in_hours = AAZIntArg(
            options=["--retention-time", "--retention-time-in-hours"],
            arg_group="RetentionDescription",
            help="Number of hours to retain the events for this Event Hub. This value is only used when cleanupPolicy is Delete. If cleanupPolicy is Compact the returned value of this property is Long.MaxValue",
            nullable=True,
        )
        _args_schema.tombstone_retention_time_in_hours = AAZIntArg(
            options=["-t", "--tombstone-retention-time-in-hours"],
            arg_group="RetentionDescription",
            help="Number of hours to retain the tombstone markers of a compacted Event Hub. This value is only used when cleanupPolicy is Compact. Consumer must complete reading the tombstone marker within this specified amount of time if consumer begins from starting offset to ensure they get a valid snapshot for the specific key described by the tombstone marker within the compacted Event Hub",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EventHubsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.EventHubsCreateOrUpdate(ctx=self.ctx)()
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

    class EventHubsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}",
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
                    "eventHubName", self.ctx.args.event_hub_name,
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
            _UpdateHelper._build_schema_eventhub_read(cls._schema_on_200)

            return cls._schema_on_200

    class EventHubsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "eventHubName", self.ctx.args.event_hub_name,
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
            _UpdateHelper._build_schema_eventhub_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("captureDescription", AAZObjectType)
                properties.set_prop("partitionCount", AAZIntType, ".partition_count")
                properties.set_prop("retentionDescription", AAZObjectType)
                properties.set_prop("status", AAZStrType, ".status")

            capture_description = _builder.get(".properties.captureDescription")
            if capture_description is not None:
                capture_description.set_prop("destination", AAZObjectType)
                capture_description.set_prop("enabled", AAZBoolType, ".enable_capture")
                capture_description.set_prop("encoding", AAZStrType, ".encoding")
                capture_description.set_prop("intervalInSeconds", AAZIntType, ".capture_interval")
                capture_description.set_prop("sizeLimitInBytes", AAZIntType, ".capture_size_limit")
                capture_description.set_prop("skipEmptyArchives", AAZBoolType, ".skip_empty_archives")

            destination = _builder.get(".properties.captureDescription.destination")
            if destination is not None:
                destination.set_prop("identity", AAZObjectType, ".identity")
                destination.set_prop("name", AAZStrType, ".destination_name")
                destination.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            identity = _builder.get(".properties.captureDescription.destination.identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type")
                identity.set_prop("userAssignedIdentity", AAZStrType, ".user_assigned_identity")

            properties = _builder.get(".properties.captureDescription.destination.properties")
            if properties is not None:
                properties.set_prop("archiveNameFormat", AAZStrType, ".archive_name_format")
                properties.set_prop("blobContainer", AAZStrType, ".blob_container")
                properties.set_prop("storageAccountResourceId", AAZStrType, ".storage_account")

            retention_description = _builder.get(".properties.retentionDescription")
            if retention_description is not None:
                retention_description.set_prop("cleanupPolicy", AAZStrType, ".cleanup_policy")
                retention_description.set_prop("retentionTimeInHours", AAZIntType, ".retention_time_in_hours")
                retention_description.set_prop("tombstoneRetentionTimeInHours", AAZIntType, ".tombstone_retention_time_in_hours")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_eventhub_read = None

    @classmethod
    def _build_schema_eventhub_read(cls, _schema):
        if cls._schema_eventhub_read is not None:
            _schema.id = cls._schema_eventhub_read.id
            _schema.location = cls._schema_eventhub_read.location
            _schema.name = cls._schema_eventhub_read.name
            _schema.properties = cls._schema_eventhub_read.properties
            _schema.system_data = cls._schema_eventhub_read.system_data
            _schema.type = cls._schema_eventhub_read.type
            return

        cls._schema_eventhub_read = _schema_eventhub_read = AAZObjectType()

        eventhub_read = _schema_eventhub_read
        eventhub_read.id = AAZStrType(
            flags={"read_only": True},
        )
        eventhub_read.location = AAZStrType(
            flags={"read_only": True},
        )
        eventhub_read.name = AAZStrType(
            flags={"read_only": True},
        )
        eventhub_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        eventhub_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        eventhub_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_eventhub_read.properties
        properties.capture_description = AAZObjectType(
            serialized_name="captureDescription",
        )
        properties.created_at = AAZStrType(
            serialized_name="createdAt",
            flags={"read_only": True},
        )
        properties.message_retention_in_days = AAZIntType(
            serialized_name="messageRetentionInDays",
        )
        properties.partition_count = AAZIntType(
            serialized_name="partitionCount",
        )
        properties.partition_ids = AAZListType(
            serialized_name="partitionIds",
            flags={"read_only": True},
        )
        properties.retention_description = AAZObjectType(
            serialized_name="retentionDescription",
        )
        properties.status = AAZStrType()
        properties.updated_at = AAZStrType(
            serialized_name="updatedAt",
            flags={"read_only": True},
        )

        capture_description = _schema_eventhub_read.properties.capture_description
        capture_description.destination = AAZObjectType()
        capture_description.enabled = AAZBoolType()
        capture_description.encoding = AAZStrType()
        capture_description.interval_in_seconds = AAZIntType(
            serialized_name="intervalInSeconds",
        )
        capture_description.size_limit_in_bytes = AAZIntType(
            serialized_name="sizeLimitInBytes",
        )
        capture_description.skip_empty_archives = AAZBoolType(
            serialized_name="skipEmptyArchives",
        )

        destination = _schema_eventhub_read.properties.capture_description.destination
        destination.identity = AAZObjectType()
        destination.name = AAZStrType()
        destination.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        identity = _schema_eventhub_read.properties.capture_description.destination.identity
        identity.type = AAZStrType()
        identity.user_assigned_identity = AAZStrType(
            serialized_name="userAssignedIdentity",
        )

        properties = _schema_eventhub_read.properties.capture_description.destination.properties
        properties.archive_name_format = AAZStrType(
            serialized_name="archiveNameFormat",
        )
        properties.blob_container = AAZStrType(
            serialized_name="blobContainer",
        )
        properties.data_lake_account_name = AAZStrType(
            serialized_name="dataLakeAccountName",
        )
        properties.data_lake_folder_path = AAZStrType(
            serialized_name="dataLakeFolderPath",
        )
        properties.data_lake_subscription_id = AAZStrType(
            serialized_name="dataLakeSubscriptionId",
        )
        properties.storage_account_resource_id = AAZStrType(
            serialized_name="storageAccountResourceId",
        )

        partition_ids = _schema_eventhub_read.properties.partition_ids
        partition_ids.Element = AAZStrType()

        retention_description = _schema_eventhub_read.properties.retention_description
        retention_description.cleanup_policy = AAZStrType(
            serialized_name="cleanupPolicy",
        )
        retention_description.retention_time_in_hours = AAZIntType(
            serialized_name="retentionTimeInHours",
        )
        retention_description.tombstone_retention_time_in_hours = AAZIntType(
            serialized_name="tombstoneRetentionTimeInHours",
        )

        system_data = _schema_eventhub_read.system_data
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

        _schema.id = cls._schema_eventhub_read.id
        _schema.location = cls._schema_eventhub_read.location
        _schema.name = cls._schema_eventhub_read.name
        _schema.properties = cls._schema_eventhub_read.properties
        _schema.system_data = cls._schema_eventhub_read.system_data
        _schema.type = cls._schema_eventhub_read.type


__all__ = ["Update"]
