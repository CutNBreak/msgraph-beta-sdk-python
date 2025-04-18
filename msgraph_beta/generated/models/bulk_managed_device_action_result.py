from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BulkManagedDeviceActionResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Failed devices
    failed_device_ids: Optional[list[str]] = None
    # Not found devices
    not_found_device_ids: Optional[list[str]] = None
    # Not supported devices
    not_supported_device_ids: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Successful devices
    successful_device_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BulkManagedDeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BulkManagedDeviceActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BulkManagedDeviceActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "failedDeviceIds": lambda n : setattr(self, 'failed_device_ids', n.get_collection_of_primitive_values(str)),
            "notFoundDeviceIds": lambda n : setattr(self, 'not_found_device_ids', n.get_collection_of_primitive_values(str)),
            "notSupportedDeviceIds": lambda n : setattr(self, 'not_supported_device_ids', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulDeviceIds": lambda n : setattr(self, 'successful_device_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("failedDeviceIds", self.failed_device_ids)
        writer.write_collection_of_primitive_values("notFoundDeviceIds", self.not_found_device_ids)
        writer.write_collection_of_primitive_values("notSupportedDeviceIds", self.not_supported_device_ids)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("successfulDeviceIds", self.successful_device_ids)
        writer.write_additional_data_value(self.additional_data)
    

