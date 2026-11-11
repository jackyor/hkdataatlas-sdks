from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voting_result_field_dictionary_constituency import (
    VotingResultFieldDictionaryConstituency,
    check_voting_result_field_dictionary_constituency,
)
from ..models.voting_result_field_dictionary_fc_result_type_1 import (
    VotingResultFieldDictionaryFcResultType1,
    check_voting_result_field_dictionary_fc_result_type_1,
)
from ..models.voting_result_field_dictionary_fc_result_type_2_type_1 import (
    VotingResultFieldDictionaryFcResultType2Type1,
    check_voting_result_field_dictionary_fc_result_type_2_type_1,
)
from ..models.voting_result_field_dictionary_fc_result_type_3_type_1 import (
    VotingResultFieldDictionaryFcResultType3Type1,
    check_voting_result_field_dictionary_fc_result_type_3_type_1,
)
from ..models.voting_result_field_dictionary_gc_result_type_1 import (
    VotingResultFieldDictionaryGcResultType1,
    check_voting_result_field_dictionary_gc_result_type_1,
)
from ..models.voting_result_field_dictionary_gc_result_type_2_type_1 import (
    VotingResultFieldDictionaryGcResultType2Type1,
    check_voting_result_field_dictionary_gc_result_type_2_type_1,
)
from ..models.voting_result_field_dictionary_gc_result_type_3_type_1 import (
    VotingResultFieldDictionaryGcResultType3Type1,
    check_voting_result_field_dictionary_gc_result_type_3_type_1,
)
from ..models.voting_result_field_dictionary_mover_type import (
    VotingResultFieldDictionaryMoverType,
    check_voting_result_field_dictionary_mover_type,
)
from ..models.voting_result_field_dictionary_overall_result import (
    VotingResultFieldDictionaryOverallResult,
    check_voting_result_field_dictionary_overall_result,
)
from ..models.voting_result_field_dictionary_type import (
    VotingResultFieldDictionaryType,
    check_voting_result_field_dictionary_type,
)
from ..models.voting_result_field_dictionary_vote import (
    VotingResultFieldDictionaryVote,
    check_voting_result_field_dictionary_vote,
)
from ..models.voting_result_field_dictionary_vote_separate_mechanism import (
    VotingResultFieldDictionaryVoteSeparateMechanism,
    check_voting_result_field_dictionary_vote_separate_mechanism,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingResultFieldDictionary")


@_attrs_define
class VotingResultFieldDictionary:
    """Dictionary of documented voting-result and Member-vote fields. This describes named fields, meanings, types and
    selected acceptable values, not a complete guarantee of a JSON response's shape or required properties.

        Attributes:
            constituency (VotingResultFieldDictionaryConstituency | Unset): Constituency of the Member. Data type: Text.
                Documented acceptable values: Geographical, Functional.
            display_order (int | Unset): Display order of the vote cast by the Member. Data type: Numeric. Example: 10.
            fc_abstain_count (int | Unset): Number of Members returned by functional constituencies who cast an Abstain
                vote. Numeric; example 0.
            fc_no_count (int | Unset): Number of Members returned by functional constituencies who cast a No vote. Numeric;
                example 13.
            fc_present_count (int | Unset): Number of Members returned by functional constituencies who were present.
                Numeric; example 35. Associated by the dictionary with vote_separate_mechanism.
            fc_result (None | Unset | VotingResultFieldDictionaryFcResultType1 |
                VotingResultFieldDictionaryFcResultType2Type1 | VotingResultFieldDictionaryFcResultType3Type1): Voting result in
                the group of Members returned by functional constituencies. Documented as Text when vote_separate_mechanism is
                Yes, or null when it is No. Acceptable text values: Passed, Negatived.
            fc_vote_count (int | Unset): Number of Members returned by functional constituencies who cast a vote. Numeric;
                example 35.
            fc_yes_count (int | Unset): Number of Members returned by functional constituencies who cast a Yes vote.
                Numeric; example 22.
            gc_abstain_count (int | Unset): Number of Members returned by geographical constituencies who cast an Abstain
                vote. Numeric; example 1.
            gc_no_count (int | Unset): Number of Members returned by geographical constituencies who cast a No vote.
                Numeric; example 13.
            gc_present_count (int | Unset): Number of Members returned by geographical constituencies who were present.
                Numeric; example 35. The dictionary associates this and the following gc vote-count fields with
                vote_separate_mechanism; its repeated table text does not precisely specify conditional presence.
            gc_result (None | Unset | VotingResultFieldDictionaryGcResultType1 |
                VotingResultFieldDictionaryGcResultType2Type1 | VotingResultFieldDictionaryGcResultType3Type1): Voting result in
                the group of Members returned by geographical constituencies. Documented as Text when vote_separate_mechanism is
                Yes, or null when it is No. Acceptable text values: Passed, Negatived.
            gc_vote_count (int | Unset): Number of Members returned by geographical constituencies who cast a vote. Numeric;
                example 34.
            gc_yes_count (int | Unset): Number of Members returned by geographical constituencies who cast a Yes vote.
                Numeric; example 20.
            id (int | Unset): Voting result identifier. Data type is Numeric. Example: 123456.
            motion_ch (str | Unset): Motion title in Chinese. Data type: Text. Example: 致謝議案.
            motion_en (str | Unset): Motion title in English. Data type: Text. Example: MOTION.
            mover_ch (str | Unset): Mover of the motion in Chinese. Data type: Text. Acceptable values described as Member
                or Chinese. Example: 財經事務及庫務局局長.
            mover_en (str | Unset): Mover of the motion in English. Data type: Text. Acceptable values described as Member
                or English. Example: Secretary the Treasury.
            mover_type (VotingResultFieldDictionaryMoverType | Unset): Type of the mover. Data type: Text. Documented
                acceptable values: Public Officer, Member.
            name_ch (str | Unset): Member's name in Chinese. Data type: Text. Example: 陳大文.
            name_en (str | Unset): Member's name in English. Data type: Text. Example: Dr Chan.
            overall_abstain_count (int | None | Unset): Overall number of Members who cast an Abstain vote. Documented as
                null if vote_separate_mechanism is Yes, otherwise Numeric; example 1.
            overall_no_count (int | None | Unset): Overall number of Members who cast a No vote. Documented as null if
                vote_separate_mechanism is Yes, otherwise Numeric; example 26.
            overall_present_count (int | None | Unset): Overall number of Members who were present. Documented as null if
                vote_separate_mechanism is Yes, otherwise Numeric; example 70.
            overall_result (VotingResultFieldDictionaryOverallResult | Unset): Overall voting result. Data type: Text.
                Documented acceptable values: Passed, Negatived, Tied.
            overall_vote_count (int | None | Unset): Overall number of Members who cast a vote. Documented as null if
                vote_separate_mechanism is Yes, otherwise Numeric; example 69.
            overall_yes_count (int | None | Unset): Overall number of Members who cast a Yes vote. Documented as null if
                vote_separate_mechanism is Yes, otherwise Numeric; example 42.
            start_date (str | Unset): Meeting date. Data type is Date. Example: 2012-10-15T11:00:00. The documentation's
                Date label and example do not establish an exact wire date-time format.
            term_no (int | Unset): The term of the Legislative Council. Data type is Numeric. Example: 5.
            type_ (VotingResultFieldDictionaryType | Unset): Meeting type. Documented acceptable values are Council Meeting,
                House Committee, Finance Committee, Public Works Subcommittee, and Establishment.
            vote (VotingResultFieldDictionaryVote | Unset): Vote cast by the Member. Data type: Text. Documented acceptable
                values: Present, Absent, Yes, No, Abstain.
            vote_date (str | Unset): Date of voting. Data type is Date. Example: 2012-10-15T00:00:00; exact wire format is
                not further specified.
            vote_number (int | Unset): Vote number in the meeting. Data type is Numeric. Example: 1.
            vote_separate_mechanism (VotingResultFieldDictionaryVoteSeparateMechanism | Unset): Indicates a motion requiring
                a majority vote of each of two groups of Members present: Members returned by functional constituencies and
                Members returned by geographical constituencies. Documented acceptable values: Yes, No.
            vote_time (str | Unset): Time of voting. The source labels the data type Date. Example: 2012-10-15T14:26:18; the
                example representation is retained without asserting a specific format.
    """

    constituency: VotingResultFieldDictionaryConstituency | Unset = UNSET
    display_order: int | Unset = UNSET
    fc_abstain_count: int | Unset = UNSET
    fc_no_count: int | Unset = UNSET
    fc_present_count: int | Unset = UNSET
    fc_result: (
        None
        | Unset
        | VotingResultFieldDictionaryFcResultType1
        | VotingResultFieldDictionaryFcResultType2Type1
        | VotingResultFieldDictionaryFcResultType3Type1
    ) = UNSET
    fc_vote_count: int | Unset = UNSET
    fc_yes_count: int | Unset = UNSET
    gc_abstain_count: int | Unset = UNSET
    gc_no_count: int | Unset = UNSET
    gc_present_count: int | Unset = UNSET
    gc_result: (
        None
        | Unset
        | VotingResultFieldDictionaryGcResultType1
        | VotingResultFieldDictionaryGcResultType2Type1
        | VotingResultFieldDictionaryGcResultType3Type1
    ) = UNSET
    gc_vote_count: int | Unset = UNSET
    gc_yes_count: int | Unset = UNSET
    id: int | Unset = UNSET
    motion_ch: str | Unset = UNSET
    motion_en: str | Unset = UNSET
    mover_ch: str | Unset = UNSET
    mover_en: str | Unset = UNSET
    mover_type: VotingResultFieldDictionaryMoverType | Unset = UNSET
    name_ch: str | Unset = UNSET
    name_en: str | Unset = UNSET
    overall_abstain_count: int | None | Unset = UNSET
    overall_no_count: int | None | Unset = UNSET
    overall_present_count: int | None | Unset = UNSET
    overall_result: VotingResultFieldDictionaryOverallResult | Unset = UNSET
    overall_vote_count: int | None | Unset = UNSET
    overall_yes_count: int | None | Unset = UNSET
    start_date: str | Unset = UNSET
    term_no: int | Unset = UNSET
    type_: VotingResultFieldDictionaryType | Unset = UNSET
    vote: VotingResultFieldDictionaryVote | Unset = UNSET
    vote_date: str | Unset = UNSET
    vote_number: int | Unset = UNSET
    vote_separate_mechanism: (
        VotingResultFieldDictionaryVoteSeparateMechanism | Unset
    ) = UNSET
    vote_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituency: str | Unset = UNSET
        if not isinstance(self.constituency, Unset):
            constituency = self.constituency

        display_order = self.display_order

        fc_abstain_count = self.fc_abstain_count

        fc_no_count = self.fc_no_count

        fc_present_count = self.fc_present_count

        fc_result: None | str | Unset
        if isinstance(self.fc_result, Unset):
            fc_result = UNSET
        elif (
            isinstance(self.fc_result, str)
            or isinstance(self.fc_result, str)
            or isinstance(self.fc_result, str)
        ):
            fc_result = self.fc_result
        else:
            fc_result = self.fc_result

        fc_vote_count = self.fc_vote_count

        fc_yes_count = self.fc_yes_count

        gc_abstain_count = self.gc_abstain_count

        gc_no_count = self.gc_no_count

        gc_present_count = self.gc_present_count

        gc_result: None | str | Unset
        if isinstance(self.gc_result, Unset):
            gc_result = UNSET
        elif (
            isinstance(self.gc_result, str)
            or isinstance(self.gc_result, str)
            or isinstance(self.gc_result, str)
        ):
            gc_result = self.gc_result
        else:
            gc_result = self.gc_result

        gc_vote_count = self.gc_vote_count

        gc_yes_count = self.gc_yes_count

        id = self.id

        motion_ch = self.motion_ch

        motion_en = self.motion_en

        mover_ch = self.mover_ch

        mover_en = self.mover_en

        mover_type: str | Unset = UNSET
        if not isinstance(self.mover_type, Unset):
            mover_type = self.mover_type

        name_ch = self.name_ch

        name_en = self.name_en

        overall_abstain_count: int | None | Unset
        if isinstance(self.overall_abstain_count, Unset):
            overall_abstain_count = UNSET
        else:
            overall_abstain_count = self.overall_abstain_count

        overall_no_count: int | None | Unset
        if isinstance(self.overall_no_count, Unset):
            overall_no_count = UNSET
        else:
            overall_no_count = self.overall_no_count

        overall_present_count: int | None | Unset
        if isinstance(self.overall_present_count, Unset):
            overall_present_count = UNSET
        else:
            overall_present_count = self.overall_present_count

        overall_result: str | Unset = UNSET
        if not isinstance(self.overall_result, Unset):
            overall_result = self.overall_result

        overall_vote_count: int | None | Unset
        if isinstance(self.overall_vote_count, Unset):
            overall_vote_count = UNSET
        else:
            overall_vote_count = self.overall_vote_count

        overall_yes_count: int | None | Unset
        if isinstance(self.overall_yes_count, Unset):
            overall_yes_count = UNSET
        else:
            overall_yes_count = self.overall_yes_count

        start_date = self.start_date

        term_no = self.term_no

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        vote: str | Unset = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote

        vote_date = self.vote_date

        vote_number = self.vote_number

        vote_separate_mechanism: str | Unset = UNSET
        if not isinstance(self.vote_separate_mechanism, Unset):
            vote_separate_mechanism = self.vote_separate_mechanism

        vote_time = self.vote_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituency is not UNSET:
            field_dict["constituency"] = constituency
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if fc_abstain_count is not UNSET:
            field_dict["fc_abstain_count"] = fc_abstain_count
        if fc_no_count is not UNSET:
            field_dict["fc_no_count"] = fc_no_count
        if fc_present_count is not UNSET:
            field_dict["fc_present_count"] = fc_present_count
        if fc_result is not UNSET:
            field_dict["fc_result"] = fc_result
        if fc_vote_count is not UNSET:
            field_dict["fc_vote_count"] = fc_vote_count
        if fc_yes_count is not UNSET:
            field_dict["fc_yes_count"] = fc_yes_count
        if gc_abstain_count is not UNSET:
            field_dict["gc_abstain_count"] = gc_abstain_count
        if gc_no_count is not UNSET:
            field_dict["gc_no_count"] = gc_no_count
        if gc_present_count is not UNSET:
            field_dict["gc_present_count"] = gc_present_count
        if gc_result is not UNSET:
            field_dict["gc_result"] = gc_result
        if gc_vote_count is not UNSET:
            field_dict["gc_vote_count"] = gc_vote_count
        if gc_yes_count is not UNSET:
            field_dict["gc_yes_count"] = gc_yes_count
        if id is not UNSET:
            field_dict["id"] = id
        if motion_ch is not UNSET:
            field_dict["motion_ch"] = motion_ch
        if motion_en is not UNSET:
            field_dict["motion_en"] = motion_en
        if mover_ch is not UNSET:
            field_dict["mover_ch"] = mover_ch
        if mover_en is not UNSET:
            field_dict["mover_en"] = mover_en
        if mover_type is not UNSET:
            field_dict["mover_type"] = mover_type
        if name_ch is not UNSET:
            field_dict["name_ch"] = name_ch
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if overall_abstain_count is not UNSET:
            field_dict["overall_abstain_count"] = overall_abstain_count
        if overall_no_count is not UNSET:
            field_dict["overall_no_count"] = overall_no_count
        if overall_present_count is not UNSET:
            field_dict["overall_present_count"] = overall_present_count
        if overall_result is not UNSET:
            field_dict["overall_result"] = overall_result
        if overall_vote_count is not UNSET:
            field_dict["overall_vote_count"] = overall_vote_count
        if overall_yes_count is not UNSET:
            field_dict["overall_yes_count"] = overall_yes_count
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if term_no is not UNSET:
            field_dict["term_no"] = term_no
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vote is not UNSET:
            field_dict["vote"] = vote
        if vote_date is not UNSET:
            field_dict["vote_date"] = vote_date
        if vote_number is not UNSET:
            field_dict["vote_number"] = vote_number
        if vote_separate_mechanism is not UNSET:
            field_dict["vote_separate_mechanism"] = vote_separate_mechanism
        if vote_time is not UNSET:
            field_dict["vote_time"] = vote_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _constituency = d.pop("constituency", UNSET)
        constituency: VotingResultFieldDictionaryConstituency | Unset
        if isinstance(_constituency, Unset):
            constituency = UNSET
        else:
            constituency = check_voting_result_field_dictionary_constituency(
                _constituency
            )

        display_order = d.pop("display_order", UNSET)

        fc_abstain_count = d.pop("fc_abstain_count", UNSET)

        fc_no_count = d.pop("fc_no_count", UNSET)

        fc_present_count = d.pop("fc_present_count", UNSET)

        def _parse_fc_result(
            data: object,
        ) -> (
            None
            | Unset
            | VotingResultFieldDictionaryFcResultType1
            | VotingResultFieldDictionaryFcResultType2Type1
            | VotingResultFieldDictionaryFcResultType3Type1
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fc_result_type_1 = (
                    check_voting_result_field_dictionary_fc_result_type_1(data)
                )

                return fc_result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fc_result_type_2_type_1 = (
                    check_voting_result_field_dictionary_fc_result_type_2_type_1(data)
                )

                return fc_result_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fc_result_type_3_type_1 = (
                    check_voting_result_field_dictionary_fc_result_type_3_type_1(data)
                )

                return fc_result_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | VotingResultFieldDictionaryFcResultType1
                | VotingResultFieldDictionaryFcResultType2Type1
                | VotingResultFieldDictionaryFcResultType3Type1,
                data,
            )

        fc_result = _parse_fc_result(d.pop("fc_result", UNSET))

        fc_vote_count = d.pop("fc_vote_count", UNSET)

        fc_yes_count = d.pop("fc_yes_count", UNSET)

        gc_abstain_count = d.pop("gc_abstain_count", UNSET)

        gc_no_count = d.pop("gc_no_count", UNSET)

        gc_present_count = d.pop("gc_present_count", UNSET)

        def _parse_gc_result(
            data: object,
        ) -> (
            None
            | Unset
            | VotingResultFieldDictionaryGcResultType1
            | VotingResultFieldDictionaryGcResultType2Type1
            | VotingResultFieldDictionaryGcResultType3Type1
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gc_result_type_1 = (
                    check_voting_result_field_dictionary_gc_result_type_1(data)
                )

                return gc_result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gc_result_type_2_type_1 = (
                    check_voting_result_field_dictionary_gc_result_type_2_type_1(data)
                )

                return gc_result_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gc_result_type_3_type_1 = (
                    check_voting_result_field_dictionary_gc_result_type_3_type_1(data)
                )

                return gc_result_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | VotingResultFieldDictionaryGcResultType1
                | VotingResultFieldDictionaryGcResultType2Type1
                | VotingResultFieldDictionaryGcResultType3Type1,
                data,
            )

        gc_result = _parse_gc_result(d.pop("gc_result", UNSET))

        gc_vote_count = d.pop("gc_vote_count", UNSET)

        gc_yes_count = d.pop("gc_yes_count", UNSET)

        id = d.pop("id", UNSET)

        motion_ch = d.pop("motion_ch", UNSET)

        motion_en = d.pop("motion_en", UNSET)

        mover_ch = d.pop("mover_ch", UNSET)

        mover_en = d.pop("mover_en", UNSET)

        _mover_type = d.pop("mover_type", UNSET)
        mover_type: VotingResultFieldDictionaryMoverType | Unset
        if isinstance(_mover_type, Unset):
            mover_type = UNSET
        else:
            mover_type = check_voting_result_field_dictionary_mover_type(_mover_type)

        name_ch = d.pop("name_ch", UNSET)

        name_en = d.pop("name_en", UNSET)

        def _parse_overall_abstain_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overall_abstain_count = _parse_overall_abstain_count(
            d.pop("overall_abstain_count", UNSET)
        )

        def _parse_overall_no_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overall_no_count = _parse_overall_no_count(d.pop("overall_no_count", UNSET))

        def _parse_overall_present_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overall_present_count = _parse_overall_present_count(
            d.pop("overall_present_count", UNSET)
        )

        _overall_result = d.pop("overall_result", UNSET)
        overall_result: VotingResultFieldDictionaryOverallResult | Unset
        if isinstance(_overall_result, Unset):
            overall_result = UNSET
        else:
            overall_result = check_voting_result_field_dictionary_overall_result(
                _overall_result
            )

        def _parse_overall_vote_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overall_vote_count = _parse_overall_vote_count(
            d.pop("overall_vote_count", UNSET)
        )

        def _parse_overall_yes_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overall_yes_count = _parse_overall_yes_count(d.pop("overall_yes_count", UNSET))

        start_date = d.pop("start_date", UNSET)

        term_no = d.pop("term_no", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: VotingResultFieldDictionaryType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_voting_result_field_dictionary_type(_type_)

        _vote = d.pop("vote", UNSET)
        vote: VotingResultFieldDictionaryVote | Unset
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = check_voting_result_field_dictionary_vote(_vote)

        vote_date = d.pop("vote_date", UNSET)

        vote_number = d.pop("vote_number", UNSET)

        _vote_separate_mechanism = d.pop("vote_separate_mechanism", UNSET)
        vote_separate_mechanism: (
            VotingResultFieldDictionaryVoteSeparateMechanism | Unset
        )
        if isinstance(_vote_separate_mechanism, Unset):
            vote_separate_mechanism = UNSET
        else:
            vote_separate_mechanism = (
                check_voting_result_field_dictionary_vote_separate_mechanism(
                    _vote_separate_mechanism
                )
            )

        vote_time = d.pop("vote_time", UNSET)

        voting_result_field_dictionary = cls(
            constituency=constituency,
            display_order=display_order,
            fc_abstain_count=fc_abstain_count,
            fc_no_count=fc_no_count,
            fc_present_count=fc_present_count,
            fc_result=fc_result,
            fc_vote_count=fc_vote_count,
            fc_yes_count=fc_yes_count,
            gc_abstain_count=gc_abstain_count,
            gc_no_count=gc_no_count,
            gc_present_count=gc_present_count,
            gc_result=gc_result,
            gc_vote_count=gc_vote_count,
            gc_yes_count=gc_yes_count,
            id=id,
            motion_ch=motion_ch,
            motion_en=motion_en,
            mover_ch=mover_ch,
            mover_en=mover_en,
            mover_type=mover_type,
            name_ch=name_ch,
            name_en=name_en,
            overall_abstain_count=overall_abstain_count,
            overall_no_count=overall_no_count,
            overall_present_count=overall_present_count,
            overall_result=overall_result,
            overall_vote_count=overall_vote_count,
            overall_yes_count=overall_yes_count,
            start_date=start_date,
            term_no=term_no,
            type_=type_,
            vote=vote,
            vote_date=vote_date,
            vote_number=vote_number,
            vote_separate_mechanism=vote_separate_mechanism,
            vote_time=vote_time,
        )

        voting_result_field_dictionary.additional_properties = d
        return voting_result_field_dictionary

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
