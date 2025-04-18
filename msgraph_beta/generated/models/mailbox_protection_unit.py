from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mailbox_type import MailboxType
    from .protection_unit_base import ProtectionUnitBase

from .protection_unit_base import ProtectionUnitBase

@dataclass
class MailboxProtectionUnit(ProtectionUnitBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mailboxProtectionUnit"
    # The ID of the directory object.
    directory_object_id: Optional[str] = None
    # Display name of the directory object.
    display_name: Optional[str] = None
    # Email address associated with the directory object.
    email: Optional[str] = None
    # The type of mailbox which is assigned to the user with id: directoryObjectId.The possible values are: unknown, user, shared, unknownFutureValue.
    mailbox_type: Optional[MailboxType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailboxProtectionUnit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxProtectionUnit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailboxProtectionUnit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mailbox_type import MailboxType
        from .protection_unit_base import ProtectionUnitBase

        from .mailbox_type import MailboxType
        from .protection_unit_base import ProtectionUnitBase

        fields: dict[str, Callable[[Any], None]] = {
            "directoryObjectId": lambda n : setattr(self, 'directory_object_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "mailboxType": lambda n : setattr(self, 'mailbox_type', n.get_enum_value(MailboxType)),
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
        writer.write_str_value("directoryObjectId", self.directory_object_id)
        writer.write_enum_value("mailboxType", self.mailbox_type)
    

