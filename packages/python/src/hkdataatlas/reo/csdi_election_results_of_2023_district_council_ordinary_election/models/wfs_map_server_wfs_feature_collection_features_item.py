from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_result2023dcoea1_attributes import (
        WfsMapServerWfsRESULT2023DCOEA1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoea2_attributes import (
        WfsMapServerWfsRESULT2023DCOEA2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeb1_attributes import (
        WfsMapServerWfsRESULT2023DCOEB1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoec1_attributes import (
        WfsMapServerWfsRESULT2023DCOEC1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoec2_attributes import (
        WfsMapServerWfsRESULT2023DCOEC2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoec3_attributes import (
        WfsMapServerWfsRESULT2023DCOEC3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoed1_attributes import (
        WfsMapServerWfsRESULT2023DCOED1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoed2_attributes import (
        WfsMapServerWfsRESULT2023DCOED2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoee1_attributes import (
        WfsMapServerWfsRESULT2023DCOEE1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoee2_attributes import (
        WfsMapServerWfsRESULT2023DCOEE2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoef1_attributes import (
        WfsMapServerWfsRESULT2023DCOEF1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoef2_attributes import (
        WfsMapServerWfsRESULT2023DCOEF2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeg1_attributes import (
        WfsMapServerWfsRESULT2023DCOEG1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeg2_attributes import (
        WfsMapServerWfsRESULT2023DCOEG2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeh1_attributes import (
        WfsMapServerWfsRESULT2023DCOEH1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeh2_attributes import (
        WfsMapServerWfsRESULT2023DCOEH2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoej1_attributes import (
        WfsMapServerWfsRESULT2023DCOEJ1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoej2_attributes import (
        WfsMapServerWfsRESULT2023DCOEJ2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoej3_attributes import (
        WfsMapServerWfsRESULT2023DCOEJ3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoej4_attributes import (
        WfsMapServerWfsRESULT2023DCOEJ4Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoek1_attributes import (
        WfsMapServerWfsRESULT2023DCOEK1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoek2_attributes import (
        WfsMapServerWfsRESULT2023DCOEK2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoel1_attributes import (
        WfsMapServerWfsRESULT2023DCOEL1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoel2_attributes import (
        WfsMapServerWfsRESULT2023DCOEL2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoel3_attributes import (
        WfsMapServerWfsRESULT2023DCOEL3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoem1_attributes import (
        WfsMapServerWfsRESULT2023DCOEM1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoem2_attributes import (
        WfsMapServerWfsRESULT2023DCOEM2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoem3_attributes import (
        WfsMapServerWfsRESULT2023DCOEM3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoem4_attributes import (
        WfsMapServerWfsRESULT2023DCOEM4Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoen1_attributes import (
        WfsMapServerWfsRESULT2023DCOEN1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoen2_attributes import (
        WfsMapServerWfsRESULT2023DCOEN2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoep1_attributes import (
        WfsMapServerWfsRESULT2023DCOEP1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoep2_attributes import (
        WfsMapServerWfsRESULT2023DCOEP2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeq1_attributes import (
        WfsMapServerWfsRESULT2023DCOEQ1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeq2_attributes import (
        WfsMapServerWfsRESULT2023DCOEQ2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoeq3_attributes import (
        WfsMapServerWfsRESULT2023DCOEQ3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoer1_attributes import (
        WfsMapServerWfsRESULT2023DCOER1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoer2_attributes import (
        WfsMapServerWfsRESULT2023DCOER2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoer3_attributes import (
        WfsMapServerWfsRESULT2023DCOER3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoer4_attributes import (
        WfsMapServerWfsRESULT2023DCOER4Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoes1_attributes import (
        WfsMapServerWfsRESULT2023DCOES1Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoes2_attributes import (
        WfsMapServerWfsRESULT2023DCOES2Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoes3_attributes import (
        WfsMapServerWfsRESULT2023DCOES3Attributes,
    )
    from ..models.wfs_map_server_wfs_result2023dcoet1_attributes import (
        WfsMapServerWfsRESULT2023DCOET1Attributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsRESULT2023DCOEA1Attributes | WfsMapServerWfsRESULT2023DCOEA2Attributes |
            WfsMapServerWfsRESULT2023DCOEB1Attributes | WfsMapServerWfsRESULT2023DCOEC1Attributes |
            WfsMapServerWfsRESULT2023DCOEC2Attributes | WfsMapServerWfsRESULT2023DCOEC3Attributes |
            WfsMapServerWfsRESULT2023DCOED1Attributes | WfsMapServerWfsRESULT2023DCOED2Attributes |
            WfsMapServerWfsRESULT2023DCOEE1Attributes | WfsMapServerWfsRESULT2023DCOEE2Attributes |
            WfsMapServerWfsRESULT2023DCOEF1Attributes | WfsMapServerWfsRESULT2023DCOEF2Attributes |
            WfsMapServerWfsRESULT2023DCOEG1Attributes | WfsMapServerWfsRESULT2023DCOEG2Attributes |
            WfsMapServerWfsRESULT2023DCOEH1Attributes | WfsMapServerWfsRESULT2023DCOEH2Attributes |
            WfsMapServerWfsRESULT2023DCOEJ1Attributes | WfsMapServerWfsRESULT2023DCOEJ2Attributes |
            WfsMapServerWfsRESULT2023DCOEJ3Attributes | WfsMapServerWfsRESULT2023DCOEJ4Attributes |
            WfsMapServerWfsRESULT2023DCOEK1Attributes | WfsMapServerWfsRESULT2023DCOEK2Attributes |
            WfsMapServerWfsRESULT2023DCOEL1Attributes | WfsMapServerWfsRESULT2023DCOEL2Attributes |
            WfsMapServerWfsRESULT2023DCOEL3Attributes | WfsMapServerWfsRESULT2023DCOEM1Attributes |
            WfsMapServerWfsRESULT2023DCOEM2Attributes | WfsMapServerWfsRESULT2023DCOEM3Attributes |
            WfsMapServerWfsRESULT2023DCOEM4Attributes | WfsMapServerWfsRESULT2023DCOEN1Attributes |
            WfsMapServerWfsRESULT2023DCOEN2Attributes | WfsMapServerWfsRESULT2023DCOEP1Attributes |
            WfsMapServerWfsRESULT2023DCOEP2Attributes | WfsMapServerWfsRESULT2023DCOEQ1Attributes |
            WfsMapServerWfsRESULT2023DCOEQ2Attributes | WfsMapServerWfsRESULT2023DCOEQ3Attributes |
            WfsMapServerWfsRESULT2023DCOER1Attributes | WfsMapServerWfsRESULT2023DCOER2Attributes |
            WfsMapServerWfsRESULT2023DCOER3Attributes | WfsMapServerWfsRESULT2023DCOER4Attributes |
            WfsMapServerWfsRESULT2023DCOES1Attributes | WfsMapServerWfsRESULT2023DCOES2Attributes |
            WfsMapServerWfsRESULT2023DCOES3Attributes | WfsMapServerWfsRESULT2023DCOET1Attributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsRESULT2023DCOEA1Attributes
        | WfsMapServerWfsRESULT2023DCOEA2Attributes
        | WfsMapServerWfsRESULT2023DCOEB1Attributes
        | WfsMapServerWfsRESULT2023DCOEC1Attributes
        | WfsMapServerWfsRESULT2023DCOEC2Attributes
        | WfsMapServerWfsRESULT2023DCOEC3Attributes
        | WfsMapServerWfsRESULT2023DCOED1Attributes
        | WfsMapServerWfsRESULT2023DCOED2Attributes
        | WfsMapServerWfsRESULT2023DCOEE1Attributes
        | WfsMapServerWfsRESULT2023DCOEE2Attributes
        | WfsMapServerWfsRESULT2023DCOEF1Attributes
        | WfsMapServerWfsRESULT2023DCOEF2Attributes
        | WfsMapServerWfsRESULT2023DCOEG1Attributes
        | WfsMapServerWfsRESULT2023DCOEG2Attributes
        | WfsMapServerWfsRESULT2023DCOEH1Attributes
        | WfsMapServerWfsRESULT2023DCOEH2Attributes
        | WfsMapServerWfsRESULT2023DCOEJ1Attributes
        | WfsMapServerWfsRESULT2023DCOEJ2Attributes
        | WfsMapServerWfsRESULT2023DCOEJ3Attributes
        | WfsMapServerWfsRESULT2023DCOEJ4Attributes
        | WfsMapServerWfsRESULT2023DCOEK1Attributes
        | WfsMapServerWfsRESULT2023DCOEK2Attributes
        | WfsMapServerWfsRESULT2023DCOEL1Attributes
        | WfsMapServerWfsRESULT2023DCOEL2Attributes
        | WfsMapServerWfsRESULT2023DCOEL3Attributes
        | WfsMapServerWfsRESULT2023DCOEM1Attributes
        | WfsMapServerWfsRESULT2023DCOEM2Attributes
        | WfsMapServerWfsRESULT2023DCOEM3Attributes
        | WfsMapServerWfsRESULT2023DCOEM4Attributes
        | WfsMapServerWfsRESULT2023DCOEN1Attributes
        | WfsMapServerWfsRESULT2023DCOEN2Attributes
        | WfsMapServerWfsRESULT2023DCOEP1Attributes
        | WfsMapServerWfsRESULT2023DCOEP2Attributes
        | WfsMapServerWfsRESULT2023DCOEQ1Attributes
        | WfsMapServerWfsRESULT2023DCOEQ2Attributes
        | WfsMapServerWfsRESULT2023DCOEQ3Attributes
        | WfsMapServerWfsRESULT2023DCOER1Attributes
        | WfsMapServerWfsRESULT2023DCOER2Attributes
        | WfsMapServerWfsRESULT2023DCOER3Attributes
        | WfsMapServerWfsRESULT2023DCOER4Attributes
        | WfsMapServerWfsRESULT2023DCOES1Attributes
        | WfsMapServerWfsRESULT2023DCOES2Attributes
        | WfsMapServerWfsRESULT2023DCOES3Attributes
        | WfsMapServerWfsRESULT2023DCOET1Attributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_result2023dcoea2_attributes import (
            WfsMapServerWfsRESULT2023DCOEA2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeb1_attributes import (
            WfsMapServerWfsRESULT2023DCOEB1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoec1_attributes import (
            WfsMapServerWfsRESULT2023DCOEC1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoec2_attributes import (
            WfsMapServerWfsRESULT2023DCOEC2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoec3_attributes import (
            WfsMapServerWfsRESULT2023DCOEC3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoed1_attributes import (
            WfsMapServerWfsRESULT2023DCOED1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoed2_attributes import (
            WfsMapServerWfsRESULT2023DCOED2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoee1_attributes import (
            WfsMapServerWfsRESULT2023DCOEE1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoee2_attributes import (
            WfsMapServerWfsRESULT2023DCOEE2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoef1_attributes import (
            WfsMapServerWfsRESULT2023DCOEF1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoef2_attributes import (
            WfsMapServerWfsRESULT2023DCOEF2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeg1_attributes import (
            WfsMapServerWfsRESULT2023DCOEG1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeg2_attributes import (
            WfsMapServerWfsRESULT2023DCOEG2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeh1_attributes import (
            WfsMapServerWfsRESULT2023DCOEH1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeh2_attributes import (
            WfsMapServerWfsRESULT2023DCOEH2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej1_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej2_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej3_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej4_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ4Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoek1_attributes import (
            WfsMapServerWfsRESULT2023DCOEK1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoek2_attributes import (
            WfsMapServerWfsRESULT2023DCOEK2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoel1_attributes import (
            WfsMapServerWfsRESULT2023DCOEL1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoel2_attributes import (
            WfsMapServerWfsRESULT2023DCOEL2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoel3_attributes import (
            WfsMapServerWfsRESULT2023DCOEL3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem1_attributes import (
            WfsMapServerWfsRESULT2023DCOEM1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem2_attributes import (
            WfsMapServerWfsRESULT2023DCOEM2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem3_attributes import (
            WfsMapServerWfsRESULT2023DCOEM3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem4_attributes import (
            WfsMapServerWfsRESULT2023DCOEM4Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoen1_attributes import (
            WfsMapServerWfsRESULT2023DCOEN1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoen2_attributes import (
            WfsMapServerWfsRESULT2023DCOEN2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoep1_attributes import (
            WfsMapServerWfsRESULT2023DCOEP1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoep2_attributes import (
            WfsMapServerWfsRESULT2023DCOEP2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeq1_attributes import (
            WfsMapServerWfsRESULT2023DCOEQ1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeq2_attributes import (
            WfsMapServerWfsRESULT2023DCOEQ2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeq3_attributes import (
            WfsMapServerWfsRESULT2023DCOEQ3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer1_attributes import (
            WfsMapServerWfsRESULT2023DCOER1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer2_attributes import (
            WfsMapServerWfsRESULT2023DCOER2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer3_attributes import (
            WfsMapServerWfsRESULT2023DCOER3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer4_attributes import (
            WfsMapServerWfsRESULT2023DCOER4Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoes1_attributes import (
            WfsMapServerWfsRESULT2023DCOES1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoes2_attributes import (
            WfsMapServerWfsRESULT2023DCOES2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoes3_attributes import (
            WfsMapServerWfsRESULT2023DCOES3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoet1_attributes import (
            WfsMapServerWfsRESULT2023DCOET1Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsRESULT2023DCOET1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOES3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOES2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOES1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOER4Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOER3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOER2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOER1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEQ3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEQ2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEQ1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEP2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEP1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEN2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEN1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEM4Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEM3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEM2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEM1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEL3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEL2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEL1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEK2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEK1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEJ4Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEJ3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEJ2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEJ1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEH2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEH1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEG2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEG1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEF2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEF1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEE2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEE1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOED2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOED1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEC3Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEC2Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEC1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEB1Attributes)
            or isinstance(self.properties, WfsMapServerWfsRESULT2023DCOEA2Attributes)
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
        from ..models.wfs_map_server_wfs_result2023dcoea1_attributes import (
            WfsMapServerWfsRESULT2023DCOEA1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoea2_attributes import (
            WfsMapServerWfsRESULT2023DCOEA2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeb1_attributes import (
            WfsMapServerWfsRESULT2023DCOEB1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoec1_attributes import (
            WfsMapServerWfsRESULT2023DCOEC1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoec2_attributes import (
            WfsMapServerWfsRESULT2023DCOEC2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoec3_attributes import (
            WfsMapServerWfsRESULT2023DCOEC3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoed1_attributes import (
            WfsMapServerWfsRESULT2023DCOED1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoed2_attributes import (
            WfsMapServerWfsRESULT2023DCOED2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoee1_attributes import (
            WfsMapServerWfsRESULT2023DCOEE1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoee2_attributes import (
            WfsMapServerWfsRESULT2023DCOEE2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoef1_attributes import (
            WfsMapServerWfsRESULT2023DCOEF1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoef2_attributes import (
            WfsMapServerWfsRESULT2023DCOEF2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeg1_attributes import (
            WfsMapServerWfsRESULT2023DCOEG1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeg2_attributes import (
            WfsMapServerWfsRESULT2023DCOEG2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeh1_attributes import (
            WfsMapServerWfsRESULT2023DCOEH1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeh2_attributes import (
            WfsMapServerWfsRESULT2023DCOEH2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej1_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej2_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej3_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoej4_attributes import (
            WfsMapServerWfsRESULT2023DCOEJ4Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoek1_attributes import (
            WfsMapServerWfsRESULT2023DCOEK1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoek2_attributes import (
            WfsMapServerWfsRESULT2023DCOEK2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoel1_attributes import (
            WfsMapServerWfsRESULT2023DCOEL1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoel2_attributes import (
            WfsMapServerWfsRESULT2023DCOEL2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoel3_attributes import (
            WfsMapServerWfsRESULT2023DCOEL3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem1_attributes import (
            WfsMapServerWfsRESULT2023DCOEM1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem2_attributes import (
            WfsMapServerWfsRESULT2023DCOEM2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem3_attributes import (
            WfsMapServerWfsRESULT2023DCOEM3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoem4_attributes import (
            WfsMapServerWfsRESULT2023DCOEM4Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoen1_attributes import (
            WfsMapServerWfsRESULT2023DCOEN1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoen2_attributes import (
            WfsMapServerWfsRESULT2023DCOEN2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoep1_attributes import (
            WfsMapServerWfsRESULT2023DCOEP1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoep2_attributes import (
            WfsMapServerWfsRESULT2023DCOEP2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeq1_attributes import (
            WfsMapServerWfsRESULT2023DCOEQ1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeq2_attributes import (
            WfsMapServerWfsRESULT2023DCOEQ2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoeq3_attributes import (
            WfsMapServerWfsRESULT2023DCOEQ3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer1_attributes import (
            WfsMapServerWfsRESULT2023DCOER1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer2_attributes import (
            WfsMapServerWfsRESULT2023DCOER2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer3_attributes import (
            WfsMapServerWfsRESULT2023DCOER3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoer4_attributes import (
            WfsMapServerWfsRESULT2023DCOER4Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoes1_attributes import (
            WfsMapServerWfsRESULT2023DCOES1Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoes2_attributes import (
            WfsMapServerWfsRESULT2023DCOES2Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoes3_attributes import (
            WfsMapServerWfsRESULT2023DCOES3Attributes,
        )
        from ..models.wfs_map_server_wfs_result2023dcoet1_attributes import (
            WfsMapServerWfsRESULT2023DCOET1Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsRESULT2023DCOEA1Attributes
            | WfsMapServerWfsRESULT2023DCOEA2Attributes
            | WfsMapServerWfsRESULT2023DCOEB1Attributes
            | WfsMapServerWfsRESULT2023DCOEC1Attributes
            | WfsMapServerWfsRESULT2023DCOEC2Attributes
            | WfsMapServerWfsRESULT2023DCOEC3Attributes
            | WfsMapServerWfsRESULT2023DCOED1Attributes
            | WfsMapServerWfsRESULT2023DCOED2Attributes
            | WfsMapServerWfsRESULT2023DCOEE1Attributes
            | WfsMapServerWfsRESULT2023DCOEE2Attributes
            | WfsMapServerWfsRESULT2023DCOEF1Attributes
            | WfsMapServerWfsRESULT2023DCOEF2Attributes
            | WfsMapServerWfsRESULT2023DCOEG1Attributes
            | WfsMapServerWfsRESULT2023DCOEG2Attributes
            | WfsMapServerWfsRESULT2023DCOEH1Attributes
            | WfsMapServerWfsRESULT2023DCOEH2Attributes
            | WfsMapServerWfsRESULT2023DCOEJ1Attributes
            | WfsMapServerWfsRESULT2023DCOEJ2Attributes
            | WfsMapServerWfsRESULT2023DCOEJ3Attributes
            | WfsMapServerWfsRESULT2023DCOEJ4Attributes
            | WfsMapServerWfsRESULT2023DCOEK1Attributes
            | WfsMapServerWfsRESULT2023DCOEK2Attributes
            | WfsMapServerWfsRESULT2023DCOEL1Attributes
            | WfsMapServerWfsRESULT2023DCOEL2Attributes
            | WfsMapServerWfsRESULT2023DCOEL3Attributes
            | WfsMapServerWfsRESULT2023DCOEM1Attributes
            | WfsMapServerWfsRESULT2023DCOEM2Attributes
            | WfsMapServerWfsRESULT2023DCOEM3Attributes
            | WfsMapServerWfsRESULT2023DCOEM4Attributes
            | WfsMapServerWfsRESULT2023DCOEN1Attributes
            | WfsMapServerWfsRESULT2023DCOEN2Attributes
            | WfsMapServerWfsRESULT2023DCOEP1Attributes
            | WfsMapServerWfsRESULT2023DCOEP2Attributes
            | WfsMapServerWfsRESULT2023DCOEQ1Attributes
            | WfsMapServerWfsRESULT2023DCOEQ2Attributes
            | WfsMapServerWfsRESULT2023DCOEQ3Attributes
            | WfsMapServerWfsRESULT2023DCOER1Attributes
            | WfsMapServerWfsRESULT2023DCOER2Attributes
            | WfsMapServerWfsRESULT2023DCOER3Attributes
            | WfsMapServerWfsRESULT2023DCOER4Attributes
            | WfsMapServerWfsRESULT2023DCOES1Attributes
            | WfsMapServerWfsRESULT2023DCOES2Attributes
            | WfsMapServerWfsRESULT2023DCOES3Attributes
            | WfsMapServerWfsRESULT2023DCOET1Attributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsRESULT2023DCOET1Attributes.from_dict(
                    data
                )

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsRESULT2023DCOES3Attributes.from_dict(
                    data
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsRESULT2023DCOES2Attributes.from_dict(
                    data
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsRESULT2023DCOES1Attributes.from_dict(
                    data
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsRESULT2023DCOER4Attributes.from_dict(
                    data
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsRESULT2023DCOER3Attributes.from_dict(
                    data
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsRESULT2023DCOER2Attributes.from_dict(
                    data
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = WfsMapServerWfsRESULT2023DCOER1Attributes.from_dict(
                    data
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = WfsMapServerWfsRESULT2023DCOEQ3Attributes.from_dict(
                    data
                )

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = WfsMapServerWfsRESULT2023DCOEQ2Attributes.from_dict(
                    data
                )

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = (
                    WfsMapServerWfsRESULT2023DCOEQ1Attributes.from_dict(data)
                )

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = (
                    WfsMapServerWfsRESULT2023DCOEP2Attributes.from_dict(data)
                )

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = (
                    WfsMapServerWfsRESULT2023DCOEP1Attributes.from_dict(data)
                )

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_13 = (
                    WfsMapServerWfsRESULT2023DCOEN2Attributes.from_dict(data)
                )

                return properties_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_14 = (
                    WfsMapServerWfsRESULT2023DCOEN1Attributes.from_dict(data)
                )

                return properties_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_15 = (
                    WfsMapServerWfsRESULT2023DCOEM4Attributes.from_dict(data)
                )

                return properties_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_16 = (
                    WfsMapServerWfsRESULT2023DCOEM3Attributes.from_dict(data)
                )

                return properties_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_17 = (
                    WfsMapServerWfsRESULT2023DCOEM2Attributes.from_dict(data)
                )

                return properties_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_18 = (
                    WfsMapServerWfsRESULT2023DCOEM1Attributes.from_dict(data)
                )

                return properties_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_19 = (
                    WfsMapServerWfsRESULT2023DCOEL3Attributes.from_dict(data)
                )

                return properties_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_20 = (
                    WfsMapServerWfsRESULT2023DCOEL2Attributes.from_dict(data)
                )

                return properties_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_21 = (
                    WfsMapServerWfsRESULT2023DCOEL1Attributes.from_dict(data)
                )

                return properties_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_22 = (
                    WfsMapServerWfsRESULT2023DCOEK2Attributes.from_dict(data)
                )

                return properties_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_23 = (
                    WfsMapServerWfsRESULT2023DCOEK1Attributes.from_dict(data)
                )

                return properties_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_24 = (
                    WfsMapServerWfsRESULT2023DCOEJ4Attributes.from_dict(data)
                )

                return properties_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_25 = (
                    WfsMapServerWfsRESULT2023DCOEJ3Attributes.from_dict(data)
                )

                return properties_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_26 = (
                    WfsMapServerWfsRESULT2023DCOEJ2Attributes.from_dict(data)
                )

                return properties_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_27 = (
                    WfsMapServerWfsRESULT2023DCOEJ1Attributes.from_dict(data)
                )

                return properties_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_28 = (
                    WfsMapServerWfsRESULT2023DCOEH2Attributes.from_dict(data)
                )

                return properties_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_29 = (
                    WfsMapServerWfsRESULT2023DCOEH1Attributes.from_dict(data)
                )

                return properties_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_30 = (
                    WfsMapServerWfsRESULT2023DCOEG2Attributes.from_dict(data)
                )

                return properties_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_31 = (
                    WfsMapServerWfsRESULT2023DCOEG1Attributes.from_dict(data)
                )

                return properties_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_32 = (
                    WfsMapServerWfsRESULT2023DCOEF2Attributes.from_dict(data)
                )

                return properties_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_33 = (
                    WfsMapServerWfsRESULT2023DCOEF1Attributes.from_dict(data)
                )

                return properties_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_34 = (
                    WfsMapServerWfsRESULT2023DCOEE2Attributes.from_dict(data)
                )

                return properties_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_35 = (
                    WfsMapServerWfsRESULT2023DCOEE1Attributes.from_dict(data)
                )

                return properties_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_36 = (
                    WfsMapServerWfsRESULT2023DCOED2Attributes.from_dict(data)
                )

                return properties_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_37 = (
                    WfsMapServerWfsRESULT2023DCOED1Attributes.from_dict(data)
                )

                return properties_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_38 = (
                    WfsMapServerWfsRESULT2023DCOEC3Attributes.from_dict(data)
                )

                return properties_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_39 = (
                    WfsMapServerWfsRESULT2023DCOEC2Attributes.from_dict(data)
                )

                return properties_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_40 = (
                    WfsMapServerWfsRESULT2023DCOEC1Attributes.from_dict(data)
                )

                return properties_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_41 = (
                    WfsMapServerWfsRESULT2023DCOEB1Attributes.from_dict(data)
                )

                return properties_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_42 = (
                    WfsMapServerWfsRESULT2023DCOEA2Attributes.from_dict(data)
                )

                return properties_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_43 = WfsMapServerWfsRESULT2023DCOEA1Attributes.from_dict(
                data
            )

            return properties_type_43

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
