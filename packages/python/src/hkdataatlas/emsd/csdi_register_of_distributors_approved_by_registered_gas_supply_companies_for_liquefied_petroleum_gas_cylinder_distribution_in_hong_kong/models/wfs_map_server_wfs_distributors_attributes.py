from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDistributorsAttributes")


@_attrs_define
class WfsMapServerWfsDistributorsAttributes:
    """
    Attributes:
        address_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        area_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        area_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        concord (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        distributor_name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        distributor_name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        district_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        esso (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        mobil (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        new_ocean (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        peninsula (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        rgc_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        rating_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        rating_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        shell_gas (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sinopec (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        street_name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        street_name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        telephone_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    area_chinese: None | str | Unset = UNSET
    area_english: None | str | Unset = UNSET
    concord: None | str | Unset = UNSET
    distributor_name_chinese: None | str | Unset = UNSET
    distributor_name_english: None | str | Unset = UNSET
    district_chinese: None | str | Unset = UNSET
    district_english: None | str | Unset = UNSET
    esso: None | str | Unset = UNSET
    mobil: None | str | Unset = UNSET
    new_ocean: None | str | Unset = UNSET
    peninsula: None | str | Unset = UNSET
    rgc_no: None | str | Unset = UNSET
    rating_chinese: None | str | Unset = UNSET
    rating_english: None | str | Unset = UNSET
    shell_gas: None | str | Unset = UNSET
    sinopec: None | str | Unset = UNSET
    street_name_chinese: None | str | Unset = UNSET
    street_name_english: None | str | Unset = UNSET
    telephone_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        address_english: None | str | Unset
        if isinstance(self.address_english, Unset):
            address_english = UNSET
        else:
            address_english = self.address_english

        area_chinese: None | str | Unset
        if isinstance(self.area_chinese, Unset):
            area_chinese = UNSET
        else:
            area_chinese = self.area_chinese

        area_english: None | str | Unset
        if isinstance(self.area_english, Unset):
            area_english = UNSET
        else:
            area_english = self.area_english

        concord: None | str | Unset
        if isinstance(self.concord, Unset):
            concord = UNSET
        else:
            concord = self.concord

        distributor_name_chinese: None | str | Unset
        if isinstance(self.distributor_name_chinese, Unset):
            distributor_name_chinese = UNSET
        else:
            distributor_name_chinese = self.distributor_name_chinese

        distributor_name_english: None | str | Unset
        if isinstance(self.distributor_name_english, Unset):
            distributor_name_english = UNSET
        else:
            distributor_name_english = self.distributor_name_english

        district_chinese: None | str | Unset
        if isinstance(self.district_chinese, Unset):
            district_chinese = UNSET
        else:
            district_chinese = self.district_chinese

        district_english: None | str | Unset
        if isinstance(self.district_english, Unset):
            district_english = UNSET
        else:
            district_english = self.district_english

        esso: None | str | Unset
        if isinstance(self.esso, Unset):
            esso = UNSET
        else:
            esso = self.esso

        mobil: None | str | Unset
        if isinstance(self.mobil, Unset):
            mobil = UNSET
        else:
            mobil = self.mobil

        new_ocean: None | str | Unset
        if isinstance(self.new_ocean, Unset):
            new_ocean = UNSET
        else:
            new_ocean = self.new_ocean

        peninsula: None | str | Unset
        if isinstance(self.peninsula, Unset):
            peninsula = UNSET
        else:
            peninsula = self.peninsula

        rgc_no: None | str | Unset
        if isinstance(self.rgc_no, Unset):
            rgc_no = UNSET
        else:
            rgc_no = self.rgc_no

        rating_chinese: None | str | Unset
        if isinstance(self.rating_chinese, Unset):
            rating_chinese = UNSET
        else:
            rating_chinese = self.rating_chinese

        rating_english: None | str | Unset
        if isinstance(self.rating_english, Unset):
            rating_english = UNSET
        else:
            rating_english = self.rating_english

        shell_gas: None | str | Unset
        if isinstance(self.shell_gas, Unset):
            shell_gas = UNSET
        else:
            shell_gas = self.shell_gas

        sinopec: None | str | Unset
        if isinstance(self.sinopec, Unset):
            sinopec = UNSET
        else:
            sinopec = self.sinopec

        street_name_chinese: None | str | Unset
        if isinstance(self.street_name_chinese, Unset):
            street_name_chinese = UNSET
        else:
            street_name_chinese = self.street_name_chinese

        street_name_english: None | str | Unset
        if isinstance(self.street_name_english, Unset):
            street_name_english = UNSET
        else:
            street_name_english = self.street_name_english

        telephone_no: None | str | Unset
        if isinstance(self.telephone_no, Unset):
            telephone_no = UNSET
        else:
            telephone_no = self.telephone_no

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if area_chinese is not UNSET:
            field_dict["Area_Chinese"] = area_chinese
        if area_english is not UNSET:
            field_dict["Area_English"] = area_english
        if concord is not UNSET:
            field_dict["Concord"] = concord
        if distributor_name_chinese is not UNSET:
            field_dict["Distributor_Name_Chinese"] = distributor_name_chinese
        if distributor_name_english is not UNSET:
            field_dict["Distributor_Name_English"] = distributor_name_english
        if district_chinese is not UNSET:
            field_dict["District_Chinese"] = district_chinese
        if district_english is not UNSET:
            field_dict["District_English"] = district_english
        if esso is not UNSET:
            field_dict["Esso"] = esso
        if mobil is not UNSET:
            field_dict["Mobil"] = mobil
        if new_ocean is not UNSET:
            field_dict["New_Ocean"] = new_ocean
        if peninsula is not UNSET:
            field_dict["Peninsula"] = peninsula
        if rgc_no is not UNSET:
            field_dict["RGC_No"] = rgc_no
        if rating_chinese is not UNSET:
            field_dict["Rating_Chinese"] = rating_chinese
        if rating_english is not UNSET:
            field_dict["Rating_English"] = rating_english
        if shell_gas is not UNSET:
            field_dict["Shell_Gas"] = shell_gas
        if sinopec is not UNSET:
            field_dict["Sinopec"] = sinopec
        if street_name_chinese is not UNSET:
            field_dict["Street_Name_Chinese"] = street_name_chinese
        if street_name_english is not UNSET:
            field_dict["Street_Name_English"] = street_name_english
        if telephone_no is not UNSET:
            field_dict["Telephone_No"] = telephone_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("Address_Chinese", UNSET))

        def _parse_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english = _parse_address_english(d.pop("Address_English", UNSET))

        def _parse_area_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_chinese = _parse_area_chinese(d.pop("Area_Chinese", UNSET))

        def _parse_area_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_english = _parse_area_english(d.pop("Area_English", UNSET))

        def _parse_concord(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        concord = _parse_concord(d.pop("Concord", UNSET))

        def _parse_distributor_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distributor_name_chinese = _parse_distributor_name_chinese(
            d.pop("Distributor_Name_Chinese", UNSET)
        )

        def _parse_distributor_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distributor_name_english = _parse_distributor_name_english(
            d.pop("Distributor_Name_English", UNSET)
        )

        def _parse_district_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chinese = _parse_district_chinese(d.pop("District_Chinese", UNSET))

        def _parse_district_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english = _parse_district_english(d.pop("District_English", UNSET))

        def _parse_esso(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        esso = _parse_esso(d.pop("Esso", UNSET))

        def _parse_mobil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mobil = _parse_mobil(d.pop("Mobil", UNSET))

        def _parse_new_ocean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_ocean = _parse_new_ocean(d.pop("New_Ocean", UNSET))

        def _parse_peninsula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        peninsula = _parse_peninsula(d.pop("Peninsula", UNSET))

        def _parse_rgc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rgc_no = _parse_rgc_no(d.pop("RGC_No", UNSET))

        def _parse_rating_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating_chinese = _parse_rating_chinese(d.pop("Rating_Chinese", UNSET))

        def _parse_rating_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating_english = _parse_rating_english(d.pop("Rating_English", UNSET))

        def _parse_shell_gas(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shell_gas = _parse_shell_gas(d.pop("Shell_Gas", UNSET))

        def _parse_sinopec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sinopec = _parse_sinopec(d.pop("Sinopec", UNSET))

        def _parse_street_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name_chinese = _parse_street_name_chinese(
            d.pop("Street_Name_Chinese", UNSET)
        )

        def _parse_street_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name_english = _parse_street_name_english(
            d.pop("Street_Name_English", UNSET)
        )

        def _parse_telephone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_no = _parse_telephone_no(d.pop("Telephone_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_distributors_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            area_chinese=area_chinese,
            area_english=area_english,
            concord=concord,
            distributor_name_chinese=distributor_name_chinese,
            distributor_name_english=distributor_name_english,
            district_chinese=district_chinese,
            district_english=district_english,
            esso=esso,
            mobil=mobil,
            new_ocean=new_ocean,
            peninsula=peninsula,
            rgc_no=rgc_no,
            rating_chinese=rating_chinese,
            rating_english=rating_english,
            shell_gas=shell_gas,
            sinopec=sinopec,
            street_name_chinese=street_name_chinese,
            street_name_english=street_name_english,
            telephone_no=telephone_no,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_distributors_attributes.additional_properties = d
        return wfs_map_server_wfs_distributors_attributes

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
