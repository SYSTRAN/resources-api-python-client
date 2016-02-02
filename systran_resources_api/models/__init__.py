"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into model package
from .lookup_supported_language_response import LookupSupportedLanguageResponse
from .supported_languages_response import SupportedLanguagesResponse
from .lookup_language_pair import LookupLanguagePair
from .lookup_response import LookupResponse
from .lookup_results import LookupResults
from .lookup_output_object import LookupOutputObject
from .lookup_match_object import LookupMatchObject
from .lookup_source_object import LookupSourceObject
from .lookup_target_object import LookupTargetObject
from .lookup_expression_object import LookupExpressionObject
from .lookup_other_expression import LookupOtherExpression
from .dictionary_add_body import DictionaryAddBody
from .dictionary_add_input import DictionaryAddInput
from .dictionary_add_response import DictionaryAddResponse
from .dictionary_add_output import DictionaryAddOutput
from .dictionary_update_body import DictionaryUpdateBody
from .dictionary_update_input import DictionaryUpdateInput
from .dictionary_update_response import DictionaryUpdateResponse
from .dictionary_update_output import DictionaryUpdateOutput
from .dictionaries_list_filters import DictionariesListFilters
from .dictionaries_list_sort_filter import DictionariesListSortFilter
from .dictionaries_list_match_filter import DictionariesListMatchFilter
from .dictionaries_list_response import DictionariesListResponse
from .dictionary_output import DictionaryOutput
from .dictionaries_import_response import DictionariesImportResponse
from .entry_add_body import EntryAddBody
from .entry_add_input import EntryAddInput
from .entry_add_response import EntryAddResponse
from .entry_add_output import EntryAddOutput
from .entry_delete_body import EntryDeleteBody
from .entry_delete_input import EntryDeleteInput
from .entry_delete_response import EntryDeleteResponse
from .entry_update_body import EntryUpdateBody
from .entry_update_input import EntryUpdateInput
from .entry_update_response import EntryUpdateResponse
from .entries_list_filters import EntriesListFilters
from .entries_list_sort_filter import EntriesListSortFilter
from .entries_list_match_filter import EntriesListMatchFilter
from .entries_list_response import EntriesListResponse
from .entry_output import EntryOutput
from .corpus import Corpus
from .corpus_list_response import CorpusListResponse
from .corpus_detail_response import CorpusDetailResponse
from .corpus_update_response import CorpusUpdateResponse
from .lite_corpus import LiteCorpus
from .corpus_add_response import CorpusAddResponse
from .corpus_exists_response import CorpusExistsResponse
from .corpus_delete_response import CorpusDeleteResponse
from .corpus_import_response import CorpusImportResponse
from .corpus_match import CorpusMatch
from .corpus_matches import CorpusMatches
from .corpus_match_response import CorpusMatchResponse
from .corpus_segment_target import CorpusSegmentTarget
from .corpus_segment import CorpusSegment
from .corpus_segment_list_response import CorpusSegmentListResponse
from .corpus_add_segment_target import CorpusAddSegmentTarget
from .corpus_add_segment import CorpusAddSegment
from .corpus_segment_add_request import CorpusSegmentAddRequest
from .corpus_segment_add_response import CorpusSegmentAddResponse
from .corpus_segment_delete_response import CorpusSegmentDeleteResponse
from .corpus_segment_update_response import CorpusSegmentUpdateResponse
from .corpus_segment_add_target_request import CorpusSegmentAddTargetRequest
from .corpus_segment_add_target_response import CorpusSegmentAddTargetResponse
from .corpus_segment_delete_target_response import CorpusSegmentDeleteTargetResponse

