from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.benchmark import Benchmark
    from ..models.matured import Matured
    from ..models.outstanding import Outstanding


T = TypeVar("T", bound="Result")


@_attrs_define
class Result:
    """
    Attributes:
        datasize (int | Unset):
        records (list[Benchmark | Matured | Outstanding] | Unset):
    """

    datasize: int | Unset = UNSET
    records: list[Benchmark | Matured | Outstanding] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.benchmark import Benchmark
        from ..models.outstanding import Outstanding

        datasize = self.datasize

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item: dict[str, Any]
                if isinstance(records_item_data, Benchmark) or isinstance(
                    records_item_data, Outstanding
                ):
                    records_item = records_item_data.to_dict()
                else:
                    records_item = records_item_data.to_dict()

                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datasize is not UNSET:
            field_dict["datasize"] = datasize
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.benchmark import Benchmark
        from ..models.matured import Matured
        from ..models.outstanding import Outstanding

        d = dict(src_dict)
        datasize = d.pop("datasize", UNSET)

        _records = d.pop("records", UNSET)
        records: list[Benchmark | Matured | Outstanding] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:

                def _parse_records_item(
                    data: object,
                ) -> Benchmark | Matured | Outstanding:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        records_item_type_0 = Benchmark.from_dict(data)

                        return records_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        records_item_type_1 = Outstanding.from_dict(data)

                        return records_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    records_item_type_2 = Matured.from_dict(data)

                    return records_item_type_2

                records_item = _parse_records_item(records_item_data)

                records.append(records_item)

        result = cls(
            datasize=datasize,
            records=records,
        )

        result.additional_properties = d
        return result

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
