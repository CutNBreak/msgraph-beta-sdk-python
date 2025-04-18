from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_content_threat_submission import FileContentThreatSubmission
    from .file_url_threat_submission import FileUrlThreatSubmission
    from .threat_submission import ThreatSubmission

from .threat_submission import ThreatSubmission

@dataclass
class FileThreatSubmission(ThreatSubmission, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.fileThreatSubmission"
    # It specifies the file name to be submitted.
    file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileThreatSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileContentThreatSubmission".casefold():
            from .file_content_threat_submission import FileContentThreatSubmission

            return FileContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileUrlThreatSubmission".casefold():
            from .file_url_threat_submission import FileUrlThreatSubmission

            return FileUrlThreatSubmission()
        return FileThreatSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_content_threat_submission import FileContentThreatSubmission
        from .file_url_threat_submission import FileUrlThreatSubmission
        from .threat_submission import ThreatSubmission

        from .file_content_threat_submission import FileContentThreatSubmission
        from .file_url_threat_submission import FileUrlThreatSubmission
        from .threat_submission import ThreatSubmission

        fields: dict[str, Callable[[Any], None]] = {
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
        writer.write_str_value("fileName", self.file_name)
    

