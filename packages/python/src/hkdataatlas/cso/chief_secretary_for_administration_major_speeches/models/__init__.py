"""Contains all the data models used in inputs/outputs"""

from .major_speech import MajorSpeech
from .major_speech_xml_feed_record import MajorSpeechXmlFeedRecord
from .search_major_speeches_lang import SearchMajorSpeechesLang
from .search_major_speeches_response_200 import SearchMajorSpeechesResponse200

__all__ = (
    "MajorSpeech",
    "MajorSpeechXmlFeedRecord",
    "SearchMajorSpeechesLang",
    "SearchMajorSpeechesResponse200",
)
