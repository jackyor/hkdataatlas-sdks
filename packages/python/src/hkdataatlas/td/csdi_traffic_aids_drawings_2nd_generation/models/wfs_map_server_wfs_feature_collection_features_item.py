from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_dtadcrossingline_attributes import (
        WfsMapServerWfsDTADCROSSINGLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadcycpt_attributes import (
        WfsMapServerWfsDTADCYCPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddropkerbline_attributes import (
        WfsMapServerWfsDTADDROPKERBLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddsfilled_attributes import (
        WfsMapServerWfsDTADDSFILLEDAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddsmiscline_attributes import (
        WfsMapServerWfsDTADDSMISCLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddsplateline_attributes import (
        WfsMapServerWfsDTADDSPLATELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddspoleline_attributes import (
        WfsMapServerWfsDTADDSPOLELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddspolelinec_attributes import (
        WfsMapServerWfsDTADDSPOLELINECAttributes,
    )
    from ..models.wfs_map_server_wfs_dtaddspolept_attributes import (
        WfsMapServerWfsDTADDSPOLEPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadgipolept_attributes import (
        WfsMapServerWfsDTADGIPOLEPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv21line_attributes import (
        WfsMapServerWfsDTADLV21LINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv22filled_attributes import (
        WfsMapServerWfsDTADLV22FILLEDAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv22line_attributes import (
        WfsMapServerWfsDTADLV22LINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv23line_attributes import (
        WfsMapServerWfsDTADLV23LINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv24line_attributes import (
        WfsMapServerWfsDTADLV24LINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv30line_attributes import (
        WfsMapServerWfsDTADLV30LINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadlv38line_attributes import (
        WfsMapServerWfsDTADLV38LINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadmiscpt_attributes import (
        WfsMapServerWfsDTADMISCPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpedrefugeline_attributes import (
        WfsMapServerWfsDTADPEDREFUGELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpsanno_attributes import (
        WfsMapServerWfsDTADPSANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpsfilled_attributes import (
        WfsMapServerWfsDTADPSFILLEDAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpsmiscline_attributes import (
        WfsMapServerWfsDTADPSMISCLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpsplateline_attributes import (
        WfsMapServerWfsDTADPSPLATELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpspoleline_attributes import (
        WfsMapServerWfsDTADPSPOLELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadpspolept_attributes import (
        WfsMapServerWfsDTADPSPOLEPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrailingline_attributes import (
        WfsMapServerWfsDTADRAILINGLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrdalline_attributes import (
        WfsMapServerWfsDTADRDALLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrdmarkanno_attributes import (
        WfsMapServerWfsDTADRDMARKANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrdmarkline_attributes import (
        WfsMapServerWfsDTADRDMARKLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrdmarklinec_attributes import (
        WfsMapServerWfsDTADRDMARKLINECAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrdmarksymline_attributes import (
        WfsMapServerWfsDTADRDMARKSYMLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrdmarksympt_attributes import (
        WfsMapServerWfsDTADRDMARKSYMPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadrstzoneline_attributes import (
        WfsMapServerWfsDTADRSTZONELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadruninoutline_attributes import (
        WfsMapServerWfsDTADRUNINOUTLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtgpathline_attributes import (
        WfsMapServerWfsDTADTGPATHLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtrafficlightfilled_attributes import (
        WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtrafficlightline_attributes import (
        WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtrafficlightpt_attributes import (
        WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtsabvanno_attributes import (
        WfsMapServerWfsDTADTSABVANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtsabvline_attributes import (
        WfsMapServerWfsDTADTSABVLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtsabvpt_attributes import (
        WfsMapServerWfsDTADTSABVPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtsfilled_attributes import (
        WfsMapServerWfsDTADTSFILLEDAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtsmiscline_attributes import (
        WfsMapServerWfsDTADTSMISCLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtsplateline_attributes import (
        WfsMapServerWfsDTADTSPLATELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtspoleline_attributes import (
        WfsMapServerWfsDTADTSPOLELINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtspolept_attributes import (
        WfsMapServerWfsDTADTSPOLEPTAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtwstripline_attributes import (
        WfsMapServerWfsDTADTWSTRIPLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadtybarline_attributes import (
        WfsMapServerWfsDTADTYBARLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadylboxline_attributes import (
        WfsMapServerWfsDTADYLBOXLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_dtadylboxpoly_attributes import (
        WfsMapServerWfsDTADYLBOXPOLYAttributes,
    )
    from ..models.wfs_map_server_wfs_unknownline_attributes import (
        WfsMapServerWfsUNKNOWNLINEAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsDTADCROSSINGLINEAttributes | WfsMapServerWfsDTADCYCPTAttributes |
            WfsMapServerWfsDTADDROPKERBLINEAttributes | WfsMapServerWfsDTADDSFILLEDAttributes |
            WfsMapServerWfsDTADDSMISCLINEAttributes | WfsMapServerWfsDTADDSPLATELINEAttributes |
            WfsMapServerWfsDTADDSPOLELINEAttributes | WfsMapServerWfsDTADDSPOLELINECAttributes |
            WfsMapServerWfsDTADDSPOLEPTAttributes | WfsMapServerWfsDTADGIPOLEPTAttributes |
            WfsMapServerWfsDTADLV21LINEAttributes | WfsMapServerWfsDTADLV22FILLEDAttributes |
            WfsMapServerWfsDTADLV22LINEAttributes | WfsMapServerWfsDTADLV23LINEAttributes |
            WfsMapServerWfsDTADLV24LINEAttributes | WfsMapServerWfsDTADLV30LINEAttributes |
            WfsMapServerWfsDTADLV38LINEAttributes | WfsMapServerWfsDTADMISCPTAttributes |
            WfsMapServerWfsDTADPEDREFUGELINEAttributes | WfsMapServerWfsDTADPSANNOAttributes |
            WfsMapServerWfsDTADPSFILLEDAttributes | WfsMapServerWfsDTADPSMISCLINEAttributes |
            WfsMapServerWfsDTADPSPLATELINEAttributes | WfsMapServerWfsDTADPSPOLELINEAttributes |
            WfsMapServerWfsDTADPSPOLEPTAttributes | WfsMapServerWfsDTADRAILINGLINEAttributes |
            WfsMapServerWfsDTADRDALLINEAttributes | WfsMapServerWfsDTADRDMARKANNOAttributes |
            WfsMapServerWfsDTADRDMARKLINEAttributes | WfsMapServerWfsDTADRDMARKLINECAttributes |
            WfsMapServerWfsDTADRDMARKSYMLINEAttributes | WfsMapServerWfsDTADRDMARKSYMPTAttributes |
            WfsMapServerWfsDTADRSTZONELINEAttributes | WfsMapServerWfsDTADRUNINOUTLINEAttributes |
            WfsMapServerWfsDTADTGPATHLINEAttributes | WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes |
            WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes | WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes |
            WfsMapServerWfsDTADTSABVANNOAttributes | WfsMapServerWfsDTADTSABVLINEAttributes |
            WfsMapServerWfsDTADTSABVPTAttributes | WfsMapServerWfsDTADTSFILLEDAttributes |
            WfsMapServerWfsDTADTSMISCLINEAttributes | WfsMapServerWfsDTADTSPLATELINEAttributes |
            WfsMapServerWfsDTADTSPOLELINEAttributes | WfsMapServerWfsDTADTSPOLEPTAttributes |
            WfsMapServerWfsDTADTWSTRIPLINEAttributes | WfsMapServerWfsDTADTYBARLINEAttributes |
            WfsMapServerWfsDTADYLBOXLINEAttributes | WfsMapServerWfsDTADYLBOXPOLYAttributes |
            WfsMapServerWfsUNKNOWNLINEAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsDTADCROSSINGLINEAttributes
        | WfsMapServerWfsDTADCYCPTAttributes
        | WfsMapServerWfsDTADDROPKERBLINEAttributes
        | WfsMapServerWfsDTADDSFILLEDAttributes
        | WfsMapServerWfsDTADDSMISCLINEAttributes
        | WfsMapServerWfsDTADDSPLATELINEAttributes
        | WfsMapServerWfsDTADDSPOLELINEAttributes
        | WfsMapServerWfsDTADDSPOLELINECAttributes
        | WfsMapServerWfsDTADDSPOLEPTAttributes
        | WfsMapServerWfsDTADGIPOLEPTAttributes
        | WfsMapServerWfsDTADLV21LINEAttributes
        | WfsMapServerWfsDTADLV22FILLEDAttributes
        | WfsMapServerWfsDTADLV22LINEAttributes
        | WfsMapServerWfsDTADLV23LINEAttributes
        | WfsMapServerWfsDTADLV24LINEAttributes
        | WfsMapServerWfsDTADLV30LINEAttributes
        | WfsMapServerWfsDTADLV38LINEAttributes
        | WfsMapServerWfsDTADMISCPTAttributes
        | WfsMapServerWfsDTADPEDREFUGELINEAttributes
        | WfsMapServerWfsDTADPSANNOAttributes
        | WfsMapServerWfsDTADPSFILLEDAttributes
        | WfsMapServerWfsDTADPSMISCLINEAttributes
        | WfsMapServerWfsDTADPSPLATELINEAttributes
        | WfsMapServerWfsDTADPSPOLELINEAttributes
        | WfsMapServerWfsDTADPSPOLEPTAttributes
        | WfsMapServerWfsDTADRAILINGLINEAttributes
        | WfsMapServerWfsDTADRDALLINEAttributes
        | WfsMapServerWfsDTADRDMARKANNOAttributes
        | WfsMapServerWfsDTADRDMARKLINEAttributes
        | WfsMapServerWfsDTADRDMARKLINECAttributes
        | WfsMapServerWfsDTADRDMARKSYMLINEAttributes
        | WfsMapServerWfsDTADRDMARKSYMPTAttributes
        | WfsMapServerWfsDTADRSTZONELINEAttributes
        | WfsMapServerWfsDTADRUNINOUTLINEAttributes
        | WfsMapServerWfsDTADTGPATHLINEAttributes
        | WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes
        | WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes
        | WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes
        | WfsMapServerWfsDTADTSABVANNOAttributes
        | WfsMapServerWfsDTADTSABVLINEAttributes
        | WfsMapServerWfsDTADTSABVPTAttributes
        | WfsMapServerWfsDTADTSFILLEDAttributes
        | WfsMapServerWfsDTADTSMISCLINEAttributes
        | WfsMapServerWfsDTADTSPLATELINEAttributes
        | WfsMapServerWfsDTADTSPOLELINEAttributes
        | WfsMapServerWfsDTADTSPOLEPTAttributes
        | WfsMapServerWfsDTADTWSTRIPLINEAttributes
        | WfsMapServerWfsDTADTYBARLINEAttributes
        | WfsMapServerWfsDTADYLBOXLINEAttributes
        | WfsMapServerWfsDTADYLBOXPOLYAttributes
        | WfsMapServerWfsUNKNOWNLINEAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_dtadcrossingline_attributes import (
            WfsMapServerWfsDTADCROSSINGLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadcycpt_attributes import (
            WfsMapServerWfsDTADCYCPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddropkerbline_attributes import (
            WfsMapServerWfsDTADDROPKERBLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddsfilled_attributes import (
            WfsMapServerWfsDTADDSFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddsmiscline_attributes import (
            WfsMapServerWfsDTADDSMISCLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddsplateline_attributes import (
            WfsMapServerWfsDTADDSPLATELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddspoleline_attributes import (
            WfsMapServerWfsDTADDSPOLELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddspolelinec_attributes import (
            WfsMapServerWfsDTADDSPOLELINECAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddspolept_attributes import (
            WfsMapServerWfsDTADDSPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadgipolept_attributes import (
            WfsMapServerWfsDTADGIPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv21line_attributes import (
            WfsMapServerWfsDTADLV21LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv22filled_attributes import (
            WfsMapServerWfsDTADLV22FILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv22line_attributes import (
            WfsMapServerWfsDTADLV22LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv23line_attributes import (
            WfsMapServerWfsDTADLV23LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv24line_attributes import (
            WfsMapServerWfsDTADLV24LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv30line_attributes import (
            WfsMapServerWfsDTADLV30LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv38line_attributes import (
            WfsMapServerWfsDTADLV38LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadmiscpt_attributes import (
            WfsMapServerWfsDTADMISCPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpedrefugeline_attributes import (
            WfsMapServerWfsDTADPEDREFUGELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsanno_attributes import (
            WfsMapServerWfsDTADPSANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsfilled_attributes import (
            WfsMapServerWfsDTADPSFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsmiscline_attributes import (
            WfsMapServerWfsDTADPSMISCLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsplateline_attributes import (
            WfsMapServerWfsDTADPSPLATELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpspoleline_attributes import (
            WfsMapServerWfsDTADPSPOLELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpspolept_attributes import (
            WfsMapServerWfsDTADPSPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrailingline_attributes import (
            WfsMapServerWfsDTADRAILINGLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdalline_attributes import (
            WfsMapServerWfsDTADRDALLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarkanno_attributes import (
            WfsMapServerWfsDTADRDMARKANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarkline_attributes import (
            WfsMapServerWfsDTADRDMARKLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarklinec_attributes import (
            WfsMapServerWfsDTADRDMARKLINECAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarksymline_attributes import (
            WfsMapServerWfsDTADRDMARKSYMLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarksympt_attributes import (
            WfsMapServerWfsDTADRDMARKSYMPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrstzoneline_attributes import (
            WfsMapServerWfsDTADRSTZONELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadruninoutline_attributes import (
            WfsMapServerWfsDTADRUNINOUTLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtgpathline_attributes import (
            WfsMapServerWfsDTADTGPATHLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtrafficlightfilled_attributes import (
            WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtrafficlightline_attributes import (
            WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtrafficlightpt_attributes import (
            WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsabvanno_attributes import (
            WfsMapServerWfsDTADTSABVANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsabvline_attributes import (
            WfsMapServerWfsDTADTSABVLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsabvpt_attributes import (
            WfsMapServerWfsDTADTSABVPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsmiscline_attributes import (
            WfsMapServerWfsDTADTSMISCLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsplateline_attributes import (
            WfsMapServerWfsDTADTSPLATELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtspoleline_attributes import (
            WfsMapServerWfsDTADTSPOLELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtspolept_attributes import (
            WfsMapServerWfsDTADTSPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtwstripline_attributes import (
            WfsMapServerWfsDTADTWSTRIPLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtybarline_attributes import (
            WfsMapServerWfsDTADTYBARLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadylboxline_attributes import (
            WfsMapServerWfsDTADYLBOXLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadylboxpoly_attributes import (
            WfsMapServerWfsDTADYLBOXPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_unknownline_attributes import (
            WfsMapServerWfsUNKNOWNLINEAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsDTADPSANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSABVANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRDMARKANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDSPOLEPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADPSPOLEPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRDMARKSYMPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSABVPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSPOLEPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADGIPOLEPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADMISCPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADCYCPTAttributes)
            or isinstance(self.properties, WfsMapServerWfsUNKNOWNLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDSPOLELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADLV38LINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDSPLATELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDSMISCLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDSPOLELINECAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADPSPOLELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADLV30LINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADPSPLATELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADPSMISCLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADLV24LINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRSTZONELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADLV23LINEAttributes)
            or isinstance(
                self.properties, WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes
            )
            or isinstance(self.properties, WfsMapServerWfsDTADLV22LINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRDMARKSYMLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRDMARKLINECAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRDMARKLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADCROSSINGLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADYLBOXLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRAILINGLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTGPATHLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSPLATELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSMISCLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSABVLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTSPOLELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTWSTRIPLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADTYBARLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADLV21LINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADPEDREFUGELINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRUNINOUTLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDROPKERBLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADRDALLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADDSFILLEDAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADPSFILLEDAttributes)
            or isinstance(
                self.properties, WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes
            )
            or isinstance(self.properties, WfsMapServerWfsDTADLV22FILLEDAttributes)
            or isinstance(self.properties, WfsMapServerWfsDTADYLBOXPOLYAttributes)
        ):
            properties = self.properties.to_dict()
        else:
            properties = self.properties.to_dict()

        geometry = self.geometry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties
        if geometry is not UNSET:
            field_dict["geometry"] = geometry

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wfs_map_server_wfs_dtadcrossingline_attributes import (
            WfsMapServerWfsDTADCROSSINGLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadcycpt_attributes import (
            WfsMapServerWfsDTADCYCPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddropkerbline_attributes import (
            WfsMapServerWfsDTADDROPKERBLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddsfilled_attributes import (
            WfsMapServerWfsDTADDSFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddsmiscline_attributes import (
            WfsMapServerWfsDTADDSMISCLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddsplateline_attributes import (
            WfsMapServerWfsDTADDSPLATELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddspoleline_attributes import (
            WfsMapServerWfsDTADDSPOLELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddspolelinec_attributes import (
            WfsMapServerWfsDTADDSPOLELINECAttributes,
        )
        from ..models.wfs_map_server_wfs_dtaddspolept_attributes import (
            WfsMapServerWfsDTADDSPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadgipolept_attributes import (
            WfsMapServerWfsDTADGIPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv21line_attributes import (
            WfsMapServerWfsDTADLV21LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv22filled_attributes import (
            WfsMapServerWfsDTADLV22FILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv22line_attributes import (
            WfsMapServerWfsDTADLV22LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv23line_attributes import (
            WfsMapServerWfsDTADLV23LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv24line_attributes import (
            WfsMapServerWfsDTADLV24LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv30line_attributes import (
            WfsMapServerWfsDTADLV30LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadlv38line_attributes import (
            WfsMapServerWfsDTADLV38LINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadmiscpt_attributes import (
            WfsMapServerWfsDTADMISCPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpedrefugeline_attributes import (
            WfsMapServerWfsDTADPEDREFUGELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsanno_attributes import (
            WfsMapServerWfsDTADPSANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsfilled_attributes import (
            WfsMapServerWfsDTADPSFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsmiscline_attributes import (
            WfsMapServerWfsDTADPSMISCLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpsplateline_attributes import (
            WfsMapServerWfsDTADPSPLATELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpspoleline_attributes import (
            WfsMapServerWfsDTADPSPOLELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadpspolept_attributes import (
            WfsMapServerWfsDTADPSPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrailingline_attributes import (
            WfsMapServerWfsDTADRAILINGLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdalline_attributes import (
            WfsMapServerWfsDTADRDALLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarkanno_attributes import (
            WfsMapServerWfsDTADRDMARKANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarkline_attributes import (
            WfsMapServerWfsDTADRDMARKLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarklinec_attributes import (
            WfsMapServerWfsDTADRDMARKLINECAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarksymline_attributes import (
            WfsMapServerWfsDTADRDMARKSYMLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrdmarksympt_attributes import (
            WfsMapServerWfsDTADRDMARKSYMPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadrstzoneline_attributes import (
            WfsMapServerWfsDTADRSTZONELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadruninoutline_attributes import (
            WfsMapServerWfsDTADRUNINOUTLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtgpathline_attributes import (
            WfsMapServerWfsDTADTGPATHLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtrafficlightfilled_attributes import (
            WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtrafficlightline_attributes import (
            WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtrafficlightpt_attributes import (
            WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsabvanno_attributes import (
            WfsMapServerWfsDTADTSABVANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsabvline_attributes import (
            WfsMapServerWfsDTADTSABVLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsabvpt_attributes import (
            WfsMapServerWfsDTADTSABVPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsfilled_attributes import (
            WfsMapServerWfsDTADTSFILLEDAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsmiscline_attributes import (
            WfsMapServerWfsDTADTSMISCLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtsplateline_attributes import (
            WfsMapServerWfsDTADTSPLATELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtspoleline_attributes import (
            WfsMapServerWfsDTADTSPOLELINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtspolept_attributes import (
            WfsMapServerWfsDTADTSPOLEPTAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtwstripline_attributes import (
            WfsMapServerWfsDTADTWSTRIPLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadtybarline_attributes import (
            WfsMapServerWfsDTADTYBARLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadylboxline_attributes import (
            WfsMapServerWfsDTADYLBOXLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_dtadylboxpoly_attributes import (
            WfsMapServerWfsDTADYLBOXPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_unknownline_attributes import (
            WfsMapServerWfsUNKNOWNLINEAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsDTADCROSSINGLINEAttributes
            | WfsMapServerWfsDTADCYCPTAttributes
            | WfsMapServerWfsDTADDROPKERBLINEAttributes
            | WfsMapServerWfsDTADDSFILLEDAttributes
            | WfsMapServerWfsDTADDSMISCLINEAttributes
            | WfsMapServerWfsDTADDSPLATELINEAttributes
            | WfsMapServerWfsDTADDSPOLELINEAttributes
            | WfsMapServerWfsDTADDSPOLELINECAttributes
            | WfsMapServerWfsDTADDSPOLEPTAttributes
            | WfsMapServerWfsDTADGIPOLEPTAttributes
            | WfsMapServerWfsDTADLV21LINEAttributes
            | WfsMapServerWfsDTADLV22FILLEDAttributes
            | WfsMapServerWfsDTADLV22LINEAttributes
            | WfsMapServerWfsDTADLV23LINEAttributes
            | WfsMapServerWfsDTADLV24LINEAttributes
            | WfsMapServerWfsDTADLV30LINEAttributes
            | WfsMapServerWfsDTADLV38LINEAttributes
            | WfsMapServerWfsDTADMISCPTAttributes
            | WfsMapServerWfsDTADPEDREFUGELINEAttributes
            | WfsMapServerWfsDTADPSANNOAttributes
            | WfsMapServerWfsDTADPSFILLEDAttributes
            | WfsMapServerWfsDTADPSMISCLINEAttributes
            | WfsMapServerWfsDTADPSPLATELINEAttributes
            | WfsMapServerWfsDTADPSPOLELINEAttributes
            | WfsMapServerWfsDTADPSPOLEPTAttributes
            | WfsMapServerWfsDTADRAILINGLINEAttributes
            | WfsMapServerWfsDTADRDALLINEAttributes
            | WfsMapServerWfsDTADRDMARKANNOAttributes
            | WfsMapServerWfsDTADRDMARKLINEAttributes
            | WfsMapServerWfsDTADRDMARKLINECAttributes
            | WfsMapServerWfsDTADRDMARKSYMLINEAttributes
            | WfsMapServerWfsDTADRDMARKSYMPTAttributes
            | WfsMapServerWfsDTADRSTZONELINEAttributes
            | WfsMapServerWfsDTADRUNINOUTLINEAttributes
            | WfsMapServerWfsDTADTGPATHLINEAttributes
            | WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes
            | WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes
            | WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes
            | WfsMapServerWfsDTADTSABVANNOAttributes
            | WfsMapServerWfsDTADTSABVLINEAttributes
            | WfsMapServerWfsDTADTSABVPTAttributes
            | WfsMapServerWfsDTADTSFILLEDAttributes
            | WfsMapServerWfsDTADTSMISCLINEAttributes
            | WfsMapServerWfsDTADTSPLATELINEAttributes
            | WfsMapServerWfsDTADTSPOLELINEAttributes
            | WfsMapServerWfsDTADTSPOLEPTAttributes
            | WfsMapServerWfsDTADTWSTRIPLINEAttributes
            | WfsMapServerWfsDTADTYBARLINEAttributes
            | WfsMapServerWfsDTADYLBOXLINEAttributes
            | WfsMapServerWfsDTADYLBOXPOLYAttributes
            | WfsMapServerWfsUNKNOWNLINEAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsDTADPSANNOAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsDTADTSABVANNOAttributes.from_dict(
                    data
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsDTADRDMARKANNOAttributes.from_dict(
                    data
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsDTADDSPOLEPTAttributes.from_dict(
                    data
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsDTADPSPOLEPTAttributes.from_dict(
                    data
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = (
                    WfsMapServerWfsDTADTRAFFICLIGHTPTAttributes.from_dict(data)
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsDTADRDMARKSYMPTAttributes.from_dict(
                    data
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = WfsMapServerWfsDTADTSABVPTAttributes.from_dict(data)

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = WfsMapServerWfsDTADTSPOLEPTAttributes.from_dict(
                    data
                )

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = WfsMapServerWfsDTADGIPOLEPTAttributes.from_dict(
                    data
                )

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = WfsMapServerWfsDTADMISCPTAttributes.from_dict(data)

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = WfsMapServerWfsDTADCYCPTAttributes.from_dict(data)

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = WfsMapServerWfsUNKNOWNLINEAttributes.from_dict(
                    data
                )

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_13 = WfsMapServerWfsDTADDSPOLELINEAttributes.from_dict(
                    data
                )

                return properties_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_14 = WfsMapServerWfsDTADLV38LINEAttributes.from_dict(
                    data
                )

                return properties_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_15 = WfsMapServerWfsDTADDSPLATELINEAttributes.from_dict(
                    data
                )

                return properties_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_16 = WfsMapServerWfsDTADDSMISCLINEAttributes.from_dict(
                    data
                )

                return properties_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_17 = WfsMapServerWfsDTADDSPOLELINECAttributes.from_dict(
                    data
                )

                return properties_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_18 = WfsMapServerWfsDTADPSPOLELINEAttributes.from_dict(
                    data
                )

                return properties_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_19 = WfsMapServerWfsDTADLV30LINEAttributes.from_dict(
                    data
                )

                return properties_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_20 = WfsMapServerWfsDTADPSPLATELINEAttributes.from_dict(
                    data
                )

                return properties_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_21 = WfsMapServerWfsDTADPSMISCLINEAttributes.from_dict(
                    data
                )

                return properties_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_22 = WfsMapServerWfsDTADLV24LINEAttributes.from_dict(
                    data
                )

                return properties_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_23 = WfsMapServerWfsDTADRSTZONELINEAttributes.from_dict(
                    data
                )

                return properties_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_24 = WfsMapServerWfsDTADLV23LINEAttributes.from_dict(
                    data
                )

                return properties_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_25 = (
                    WfsMapServerWfsDTADTRAFFICLIGHTLINEAttributes.from_dict(data)
                )

                return properties_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_26 = WfsMapServerWfsDTADLV22LINEAttributes.from_dict(
                    data
                )

                return properties_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_27 = (
                    WfsMapServerWfsDTADRDMARKSYMLINEAttributes.from_dict(data)
                )

                return properties_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_28 = WfsMapServerWfsDTADRDMARKLINECAttributes.from_dict(
                    data
                )

                return properties_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_29 = WfsMapServerWfsDTADRDMARKLINEAttributes.from_dict(
                    data
                )

                return properties_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_30 = (
                    WfsMapServerWfsDTADCROSSINGLINEAttributes.from_dict(data)
                )

                return properties_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_31 = WfsMapServerWfsDTADYLBOXLINEAttributes.from_dict(
                    data
                )

                return properties_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_32 = WfsMapServerWfsDTADRAILINGLINEAttributes.from_dict(
                    data
                )

                return properties_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_33 = WfsMapServerWfsDTADTGPATHLINEAttributes.from_dict(
                    data
                )

                return properties_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_34 = WfsMapServerWfsDTADTSPLATELINEAttributes.from_dict(
                    data
                )

                return properties_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_35 = WfsMapServerWfsDTADTSMISCLINEAttributes.from_dict(
                    data
                )

                return properties_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_36 = WfsMapServerWfsDTADTSABVLINEAttributes.from_dict(
                    data
                )

                return properties_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_37 = WfsMapServerWfsDTADTSPOLELINEAttributes.from_dict(
                    data
                )

                return properties_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_38 = WfsMapServerWfsDTADTWSTRIPLINEAttributes.from_dict(
                    data
                )

                return properties_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_39 = WfsMapServerWfsDTADTYBARLINEAttributes.from_dict(
                    data
                )

                return properties_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_40 = WfsMapServerWfsDTADLV21LINEAttributes.from_dict(
                    data
                )

                return properties_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_41 = (
                    WfsMapServerWfsDTADPEDREFUGELINEAttributes.from_dict(data)
                )

                return properties_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_42 = (
                    WfsMapServerWfsDTADRUNINOUTLINEAttributes.from_dict(data)
                )

                return properties_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_43 = (
                    WfsMapServerWfsDTADDROPKERBLINEAttributes.from_dict(data)
                )

                return properties_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_44 = WfsMapServerWfsDTADRDALLINEAttributes.from_dict(
                    data
                )

                return properties_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_45 = WfsMapServerWfsDTADDSFILLEDAttributes.from_dict(
                    data
                )

                return properties_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_46 = WfsMapServerWfsDTADPSFILLEDAttributes.from_dict(
                    data
                )

                return properties_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_47 = (
                    WfsMapServerWfsDTADTRAFFICLIGHTFILLEDAttributes.from_dict(data)
                )

                return properties_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_48 = WfsMapServerWfsDTADLV22FILLEDAttributes.from_dict(
                    data
                )

                return properties_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_49 = WfsMapServerWfsDTADYLBOXPOLYAttributes.from_dict(
                    data
                )

                return properties_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_50 = WfsMapServerWfsDTADTSFILLEDAttributes.from_dict(data)

            return properties_type_50

        properties = _parse_properties(d.pop("properties", UNSET))

        geometry = d.pop("geometry", UNSET)

        wfs_map_server_wfs_feature_collection_features_item = cls(
            type_=type_,
            properties=properties,
            geometry=geometry,
        )

        wfs_map_server_wfs_feature_collection_features_item.additional_properties = d
        return wfs_map_server_wfs_feature_collection_features_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
