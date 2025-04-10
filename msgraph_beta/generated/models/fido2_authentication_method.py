from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attestation_level import AttestationLevel
    from .authentication_method import AuthenticationMethod
    from .webauthn_public_key_credential import WebauthnPublicKeyCredential

from .authentication_method import AuthenticationMethod

@dataclass
class Fido2AuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.fido2AuthenticationMethod"
    # Authenticator Attestation GUID, an identifier that indicates the type (such as make and model) of the authenticator.
    aa_guid: Optional[str] = None
    # The attestation certificate or certificates attached to this security key.
    attestation_certificates: Optional[list[str]] = None
    # The attestation level of this FIDO2 security key. Possible values are: attested, notAttested, unknownFutureValue.
    attestation_level: Optional[AttestationLevel] = None
    # The display name of the key as given by the user.
    display_name: Optional[str] = None
    # The manufacturer-assigned model of the FIDO2 security key.
    model: Optional[str] = None
    # Contains the WebAuthn public key credential information being registered. Only used for write requests. This property isn't returned on read operations.
    public_key_credential: Optional[WebauthnPublicKeyCredential] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Fido2AuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Fido2AuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Fido2AuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attestation_level import AttestationLevel
        from .authentication_method import AuthenticationMethod
        from .webauthn_public_key_credential import WebauthnPublicKeyCredential

        from .attestation_level import AttestationLevel
        from .authentication_method import AuthenticationMethod
        from .webauthn_public_key_credential import WebauthnPublicKeyCredential

        fields: dict[str, Callable[[Any], None]] = {
            "aaGuid": lambda n : setattr(self, 'aa_guid', n.get_str_value()),
            "attestationCertificates": lambda n : setattr(self, 'attestation_certificates', n.get_collection_of_primitive_values(str)),
            "attestationLevel": lambda n : setattr(self, 'attestation_level', n.get_enum_value(AttestationLevel)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "publicKeyCredential": lambda n : setattr(self, 'public_key_credential', n.get_object_value(WebauthnPublicKeyCredential)),
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
        writer.write_str_value("aaGuid", self.aa_guid)
        writer.write_collection_of_primitive_values("attestationCertificates", self.attestation_certificates)
        writer.write_enum_value("attestationLevel", self.attestation_level)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("model", self.model)
        writer.write_object_value("publicKeyCredential", self.public_key_credential)
    

