from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

@dataclass
class RedundantAssignmentAlertConfiguration(UnifiedRoleManagementAlertConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.redundantAssignmentAlertConfiguration"
    # The number of days without activation to look back on from current timestamp.
    duration: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedundantAssignmentAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedundantAssignmentAlertConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedundantAssignmentAlertConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
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
        writer.write_timedelta_value("duration", self.duration)
    

