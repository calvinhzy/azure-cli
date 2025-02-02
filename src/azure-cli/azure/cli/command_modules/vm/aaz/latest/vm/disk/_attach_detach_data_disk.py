# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class AttachDetachDataDisk(AAZCommand):
    """Attach and detach data disks to/from the virtual machine.
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/virtualmachines/{}/attachdetachdatadisks", "2024-03-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vm_name = AAZStrArg(
            options=["--vm-name"],
            help="The name of the virtual machine.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.data_disks_to_attach = AAZListArg(
            options=["--data-disks-to-attach"],
            arg_group="Parameters",
            help="The list of managed data disks to be attached.",
        )
        _args_schema.data_disks_to_detach = AAZListArg(
            options=["--data-disks-to-detach"],
            arg_group="Parameters",
            help="The list of managed data disks to be detached.",
        )

        data_disks_to_attach = cls._args_schema.data_disks_to_attach
        data_disks_to_attach.Element = AAZObjectArg()

        _element = cls._args_schema.data_disks_to_attach.Element
        _element.caching = AAZStrArg(
            options=["caching"],
            help="Specify the caching requirements. Possible values are: **None,** **ReadOnly,** **ReadWrite.** The defaulting behavior is: **None for Standard storage. ReadOnly for Premium storage.**",
            enum={"None": "None", "ReadOnly": "ReadOnly", "ReadWrite": "ReadWrite"},
        )
        _element.delete_option = AAZStrArg(
            options=["delete-option"],
            help="Specify whether data disk should be deleted or detached upon VM deletion. Possible values are: **Delete.** If this value is used, the data disk is deleted when VM is deleted. **Detach.** If this value is used, the data disk is retained after VM is deleted. The default value is set to **Detach**.",
            enum={"Delete": "Delete", "Detach": "Detach"},
        )
        _element.disk_encryption_set = AAZObjectArg(
            options=["disk-encryption-set"],
            help="Specify the customer managed disk encryption set resource id for the managed disk.",
        )
        _element.disk_id = AAZStrArg(
            options=["disk-id"],
            help="ID of the managed data disk.",
            required=True,
        )
        _element.lun = AAZIntArg(
            options=["lun"],
            help="The logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. If not specified, lun would be auto assigned.",
        )
        _element.write_accelerator_enabled = AAZBoolArg(
            options=["write-accelerator-enabled"],
            help="Specify whether writeAccelerator should be enabled or disabled on the disk.",
        )

        disk_encryption_set = cls._args_schema.data_disks_to_attach.Element.disk_encryption_set
        disk_encryption_set.id = AAZStrArg(
            options=["id"],
            help="Resource Id",
        )

        data_disks_to_detach = cls._args_schema.data_disks_to_detach
        data_disks_to_detach.Element = AAZObjectArg()

        _element = cls._args_schema.data_disks_to_detach.Element
        _element.detach_option = AAZStrArg(
            options=["detach-option"],
            help="Supported options available for Detach of a disk from a VM. Refer to DetachOption object reference for more details.",
            enum={"ForceDetach": "ForceDetach"},
        )
        _element.disk_id = AAZStrArg(
            options=["disk-id"],
            help="ID of the managed data disk.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualMachinesAttachDetachDataDisks(ctx=self.ctx)()
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

    class VirtualMachinesAttachDetachDataDisks(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/attachDetachDataDisks",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "vmName", self.ctx.args.vm_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("dataDisksToAttach", AAZListType, ".data_disks_to_attach")
            _builder.set_prop("dataDisksToDetach", AAZListType, ".data_disks_to_detach")

            data_disks_to_attach = _builder.get(".dataDisksToAttach")
            if data_disks_to_attach is not None:
                data_disks_to_attach.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".dataDisksToAttach[]")
            if _elements is not None:
                _elements.set_prop("caching", AAZStrType, ".caching")
                _elements.set_prop("deleteOption", AAZStrType, ".delete_option")
                _elements.set_prop("diskEncryptionSet", AAZObjectType, ".disk_encryption_set")
                _elements.set_prop("diskId", AAZStrType, ".disk_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("lun", AAZIntType, ".lun")
                _elements.set_prop("writeAcceleratorEnabled", AAZBoolType, ".write_accelerator_enabled")

            disk_encryption_set = _builder.get(".dataDisksToAttach[].diskEncryptionSet")
            if disk_encryption_set is not None:
                disk_encryption_set.set_prop("id", AAZStrType, ".id")

            data_disks_to_detach = _builder.get(".dataDisksToDetach")
            if data_disks_to_detach is not None:
                data_disks_to_detach.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".dataDisksToDetach[]")
            if _elements is not None:
                _elements.set_prop("detachOption", AAZStrType, ".detach_option")
                _elements.set_prop("diskId", AAZStrType, ".disk_id", typ_kwargs={"flags": {"required": True}})

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.data_disks = AAZListType(
                serialized_name="dataDisks",
            )
            _schema_on_200.disk_controller_type = AAZStrType(
                serialized_name="diskControllerType",
            )
            _schema_on_200.image_reference = AAZObjectType(
                serialized_name="imageReference",
            )
            _schema_on_200.os_disk = AAZObjectType(
                serialized_name="osDisk",
            )

            data_disks = cls._schema_on_200.data_disks
            data_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.data_disks.Element
            _element.caching = AAZStrType()
            _element.create_option = AAZStrType(
                serialized_name="createOption",
                flags={"required": True},
            )
            _element.delete_option = AAZStrType(
                serialized_name="deleteOption",
            )
            _element.detach_option = AAZStrType(
                serialized_name="detachOption",
            )
            _element.disk_iops_read_write = AAZIntType(
                serialized_name="diskIOPSReadWrite",
                flags={"read_only": True},
            )
            _element.disk_m_bps_read_write = AAZIntType(
                serialized_name="diskMBpsReadWrite",
                flags={"read_only": True},
            )
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            _element.image = AAZObjectType()
            _AttachDetachDataDiskHelper._build_schema_virtual_hard_disk_read(_element.image)
            _element.lun = AAZIntType(
                flags={"required": True},
            )
            _element.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _AttachDetachDataDiskHelper._build_schema_managed_disk_parameters_read(_element.managed_disk)
            _element.name = AAZStrType()
            _element.source_resource = AAZObjectType(
                serialized_name="sourceResource",
            )
            _element.to_be_detached = AAZBoolType(
                serialized_name="toBeDetached",
            )
            _element.vhd = AAZObjectType()
            _AttachDetachDataDiskHelper._build_schema_virtual_hard_disk_read(_element.vhd)
            _element.write_accelerator_enabled = AAZBoolType(
                serialized_name="writeAcceleratorEnabled",
            )

            source_resource = cls._schema_on_200.data_disks.Element.source_resource
            source_resource.id = AAZStrType()

            image_reference = cls._schema_on_200.image_reference
            image_reference.community_gallery_image_id = AAZStrType(
                serialized_name="communityGalleryImageId",
            )
            image_reference.exact_version = AAZStrType(
                serialized_name="exactVersion",
                flags={"read_only": True},
            )
            image_reference.id = AAZStrType()
            image_reference.offer = AAZStrType()
            image_reference.publisher = AAZStrType()
            image_reference.shared_gallery_image_id = AAZStrType(
                serialized_name="sharedGalleryImageId",
            )
            image_reference.sku = AAZStrType()
            image_reference.version = AAZStrType()

            os_disk = cls._schema_on_200.os_disk
            os_disk.caching = AAZStrType()
            os_disk.create_option = AAZStrType(
                serialized_name="createOption",
                flags={"required": True},
            )
            os_disk.delete_option = AAZStrType(
                serialized_name="deleteOption",
            )
            os_disk.diff_disk_settings = AAZObjectType(
                serialized_name="diffDiskSettings",
            )
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            os_disk.encryption_settings = AAZObjectType(
                serialized_name="encryptionSettings",
            )
            os_disk.image = AAZObjectType()
            _AttachDetachDataDiskHelper._build_schema_virtual_hard_disk_read(os_disk.image)
            os_disk.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _AttachDetachDataDiskHelper._build_schema_managed_disk_parameters_read(os_disk.managed_disk)
            os_disk.name = AAZStrType()
            os_disk.os_type = AAZStrType(
                serialized_name="osType",
            )
            os_disk.vhd = AAZObjectType()
            _AttachDetachDataDiskHelper._build_schema_virtual_hard_disk_read(os_disk.vhd)
            os_disk.write_accelerator_enabled = AAZBoolType(
                serialized_name="writeAcceleratorEnabled",
            )

            diff_disk_settings = cls._schema_on_200.os_disk.diff_disk_settings
            diff_disk_settings.option = AAZStrType()
            diff_disk_settings.placement = AAZStrType()

            encryption_settings = cls._schema_on_200.os_disk.encryption_settings
            encryption_settings.disk_encryption_key = AAZObjectType(
                serialized_name="diskEncryptionKey",
            )
            encryption_settings.enabled = AAZBoolType()
            encryption_settings.key_encryption_key = AAZObjectType(
                serialized_name="keyEncryptionKey",
            )

            disk_encryption_key = cls._schema_on_200.os_disk.encryption_settings.disk_encryption_key
            disk_encryption_key.secret_url = AAZStrType(
                serialized_name="secretUrl",
                flags={"required": True},
            )
            disk_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _AttachDetachDataDiskHelper._build_schema_sub_resource_read(disk_encryption_key.source_vault)

            key_encryption_key = cls._schema_on_200.os_disk.encryption_settings.key_encryption_key
            key_encryption_key.key_url = AAZStrType(
                serialized_name="keyUrl",
                flags={"required": True},
            )
            key_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _AttachDetachDataDiskHelper._build_schema_sub_resource_read(key_encryption_key.source_vault)

            return cls._schema_on_200


class _AttachDetachDataDiskHelper:
    """Helper class for AttachDetachDataDisk"""

    _schema_disk_encryption_set_parameters_read = None

    @classmethod
    def _build_schema_disk_encryption_set_parameters_read(cls, _schema):
        if cls._schema_disk_encryption_set_parameters_read is not None:
            _schema.id = cls._schema_disk_encryption_set_parameters_read.id
            return

        cls._schema_disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read = AAZObjectType()

        disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read
        disk_encryption_set_parameters_read.id = AAZStrType()

        _schema.id = cls._schema_disk_encryption_set_parameters_read.id

    _schema_managed_disk_parameters_read = None

    @classmethod
    def _build_schema_managed_disk_parameters_read(cls, _schema):
        if cls._schema_managed_disk_parameters_read is not None:
            _schema.disk_encryption_set = cls._schema_managed_disk_parameters_read.disk_encryption_set
            _schema.id = cls._schema_managed_disk_parameters_read.id
            _schema.security_profile = cls._schema_managed_disk_parameters_read.security_profile
            _schema.storage_account_type = cls._schema_managed_disk_parameters_read.storage_account_type
            return

        cls._schema_managed_disk_parameters_read = _schema_managed_disk_parameters_read = AAZObjectType()

        managed_disk_parameters_read = _schema_managed_disk_parameters_read
        managed_disk_parameters_read.disk_encryption_set = AAZObjectType(
            serialized_name="diskEncryptionSet",
        )
        cls._build_schema_disk_encryption_set_parameters_read(managed_disk_parameters_read.disk_encryption_set)
        managed_disk_parameters_read.id = AAZStrType()
        managed_disk_parameters_read.security_profile = AAZObjectType(
            serialized_name="securityProfile",
        )
        managed_disk_parameters_read.storage_account_type = AAZStrType(
            serialized_name="storageAccountType",
        )

        security_profile = _schema_managed_disk_parameters_read.security_profile
        security_profile.disk_encryption_set = AAZObjectType(
            serialized_name="diskEncryptionSet",
        )
        cls._build_schema_disk_encryption_set_parameters_read(security_profile.disk_encryption_set)
        security_profile.security_encryption_type = AAZStrType(
            serialized_name="securityEncryptionType",
        )

        _schema.disk_encryption_set = cls._schema_managed_disk_parameters_read.disk_encryption_set
        _schema.id = cls._schema_managed_disk_parameters_read.id
        _schema.security_profile = cls._schema_managed_disk_parameters_read.security_profile
        _schema.storage_account_type = cls._schema_managed_disk_parameters_read.storage_account_type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_virtual_hard_disk_read = None

    @classmethod
    def _build_schema_virtual_hard_disk_read(cls, _schema):
        if cls._schema_virtual_hard_disk_read is not None:
            _schema.uri = cls._schema_virtual_hard_disk_read.uri
            return

        cls._schema_virtual_hard_disk_read = _schema_virtual_hard_disk_read = AAZObjectType()

        virtual_hard_disk_read = _schema_virtual_hard_disk_read
        virtual_hard_disk_read.uri = AAZStrType()

        _schema.uri = cls._schema_virtual_hard_disk_read.uri


__all__ = ["AttachDetachDataDisk"]
