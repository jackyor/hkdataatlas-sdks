from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        c_max_ed (None | str | Unset): Publisher field type: esriFieldTypeString
        sum_length (int | None | Unset): Publisher field type: esriFieldTypeInteger
        catch_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_relict (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_recent (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_relict_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_recent_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        max_trail (float | None | Unset): Publisher field type: esriFieldTypeDouble
        catch_no (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    c_max_ed: None | str | Unset = UNSET
    sum_length: int | None | Unset = UNSET
    catch_area: float | None | Unset = UNSET
    no_relict: float | None | Unset = UNSET
    no_recent: float | None | Unset = UNSET
    m_relict_l: float | None | Unset = UNSET
    m_recent_l: float | None | Unset = UNSET
    max_trail: float | None | Unset = UNSET
    catch_no: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        c_max_ed: None | str | Unset
        if isinstance(self.c_max_ed, Unset):
            c_max_ed = UNSET
        else:
            c_max_ed = self.c_max_ed

        sum_length: int | None | Unset
        if isinstance(self.sum_length, Unset):
            sum_length = UNSET
        else:
            sum_length = self.sum_length

        catch_area: float | None | Unset
        if isinstance(self.catch_area, Unset):
            catch_area = UNSET
        else:
            catch_area = self.catch_area

        no_relict: float | None | Unset
        if isinstance(self.no_relict, Unset):
            no_relict = UNSET
        else:
            no_relict = self.no_relict

        no_recent: float | None | Unset
        if isinstance(self.no_recent, Unset):
            no_recent = UNSET
        else:
            no_recent = self.no_recent

        m_relict_l: float | None | Unset
        if isinstance(self.m_relict_l, Unset):
            m_relict_l = UNSET
        else:
            m_relict_l = self.m_relict_l

        m_recent_l: float | None | Unset
        if isinstance(self.m_recent_l, Unset):
            m_recent_l = UNSET
        else:
            m_recent_l = self.m_recent_l

        max_trail: float | None | Unset
        if isinstance(self.max_trail, Unset):
            max_trail = UNSET
        else:
            max_trail = self.max_trail

        catch_no: None | str | Unset
        if isinstance(self.catch_no, Unset):
            catch_no = UNSET
        else:
            catch_no = self.catch_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if c_max_ed is not UNSET:
            field_dict["C_MAX_ED"] = c_max_ed
        if sum_length is not UNSET:
            field_dict["SUM_LENGTH"] = sum_length
        if catch_area is not UNSET:
            field_dict["CATCH_AREA"] = catch_area
        if no_relict is not UNSET:
            field_dict["NO_RELICT"] = no_relict
        if no_recent is not UNSET:
            field_dict["NO_RECENT"] = no_recent
        if m_relict_l is not UNSET:
            field_dict["M_RELICT_L"] = m_relict_l
        if m_recent_l is not UNSET:
            field_dict["M_RECENT_L"] = m_recent_l
        if max_trail is not UNSET:
            field_dict["MAX_TRAIL"] = max_trail
        if catch_no is not UNSET:
            field_dict["CATCH_NO"] = catch_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_c_max_ed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_max_ed = _parse_c_max_ed(d.pop("C_MAX_ED", UNSET))

        def _parse_sum_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sum_length = _parse_sum_length(d.pop("SUM_LENGTH", UNSET))

        def _parse_catch_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        catch_area = _parse_catch_area(d.pop("CATCH_AREA", UNSET))

        def _parse_no_relict(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_relict = _parse_no_relict(d.pop("NO_RELICT", UNSET))

        def _parse_no_recent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_recent = _parse_no_recent(d.pop("NO_RECENT", UNSET))

        def _parse_m_relict_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_relict_l = _parse_m_relict_l(d.pop("M_RELICT_L", UNSET))

        def _parse_m_recent_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_recent_l = _parse_m_recent_l(d.pop("M_RECENT_L", UNSET))

        def _parse_max_trail(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_trail = _parse_max_trail(d.pop("MAX_TRAIL", UNSET))

        def _parse_catch_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        catch_no = _parse_catch_no(d.pop("CATCH_NO", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            c_max_ed=c_max_ed,
            sum_length=sum_length,
            catch_area=catch_area,
            no_relict=no_relict,
            no_recent=no_recent,
            m_relict_l=m_relict_l,
            m_recent_l=m_recent_l,
            max_trail=max_trail,
            catch_no=catch_no,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
