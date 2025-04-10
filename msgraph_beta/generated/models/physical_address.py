from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .physical_address_type import PhysicalAddressType

@dataclass
class PhysicalAddress(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The city.
    city: Optional[str] = None
    # The country or region. It's a free-format string value, for example, 'United States'.
    country_or_region: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The post office box number.
    post_office_box: Optional[str] = None
    # The postal code.
    postal_code: Optional[str] = None
    # The state.
    state: Optional[str] = None
    # The street.
    street: Optional[str] = None
    # The type of address. Possible values are: unknown, home, business, other.
    type: Optional[PhysicalAddressType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhysicalAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhysicalAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhysicalAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .physical_address_type import PhysicalAddressType

        from .physical_address_type import PhysicalAddressType

        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postOfficeBox": lambda n : setattr(self, 'post_office_box', n.get_str_value()),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PhysicalAddressType)),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("postOfficeBox", self.post_office_box)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street", self.street)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

