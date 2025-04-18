from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .rule_destination import RuleDestination

from .rule_destination import RuleDestination

@dataclass
class WebCategory(RuleDestination, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.webCategory"
    # The display name for the web category.
    display_name: Optional[str] = None
    # The group or category to which the web category belongs.
    group: Optional[str] = None
    # The unique name that is associated with the web category.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .rule_destination import RuleDestination

        from .rule_destination import RuleDestination

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group": lambda n : setattr(self, 'group', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("group", self.group)
        writer.write_str_value("name", self.name)
    

