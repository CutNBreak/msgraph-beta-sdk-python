from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AlertFrequencyPoint(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The highSeverityCount property
    high_severity_count: Optional[int] = None
    # The informationalSeverityCount property
    informational_severity_count: Optional[int] = None
    # The lowSeverityCount property
    low_severity_count: Optional[int] = None
    # The mediumSeverityCount property
    medium_severity_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The timeStampDateTime property
    time_stamp_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertFrequencyPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertFrequencyPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlertFrequencyPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "highSeverityCount": lambda n : setattr(self, 'high_severity_count', n.get_int_value()),
            "informationalSeverityCount": lambda n : setattr(self, 'informational_severity_count', n.get_int_value()),
            "lowSeverityCount": lambda n : setattr(self, 'low_severity_count', n.get_int_value()),
            "mediumSeverityCount": lambda n : setattr(self, 'medium_severity_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeStampDateTime": lambda n : setattr(self, 'time_stamp_date_time', n.get_datetime_value()),
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
        writer.write_int_value("highSeverityCount", self.high_severity_count)
        writer.write_int_value("informationalSeverityCount", self.informational_severity_count)
        writer.write_int_value("lowSeverityCount", self.low_severity_count)
        writer.write_int_value("mediumSeverityCount", self.medium_severity_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("timeStampDateTime", self.time_stamp_date_time)
        writer.write_additional_data_value(self.additional_data)
    

