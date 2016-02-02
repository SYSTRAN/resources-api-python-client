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

# import models into sdk package
from .models.lookup_supported_language_response import LookupSupportedLanguageResponse
from .models.supported_languages_response import SupportedLanguagesResponse
from .models.lookup_language_pair import LookupLanguagePair
from .models.lookup_response import LookupResponse
from .models.lookup_results import LookupResults
from .models.lookup_output_object import LookupOutputObject
from .models.lookup_match_object import LookupMatchObject
from .models.lookup_source_object import LookupSourceObject
from .models.lookup_target_object import LookupTargetObject
from .models.lookup_expression_object import LookupExpressionObject
from .models.lookup_other_expression import LookupOtherExpression
from .models.dictionary_add_body import DictionaryAddBody
from .models.dictionary_add_input import DictionaryAddInput
from .models.dictionary_add_response import DictionaryAddResponse
from .models.dictionary_add_output import DictionaryAddOutput
from .models.dictionary_update_body import DictionaryUpdateBody
from .models.dictionary_update_input import DictionaryUpdateInput
from .models.dictionary_update_response import DictionaryUpdateResponse
from .models.dictionary_update_output import DictionaryUpdateOutput
from .models.dictionaries_list_filters import DictionariesListFilters
from .models.dictionaries_list_sort_filter import DictionariesListSortFilter
from .models.dictionaries_list_match_filter import DictionariesListMatchFilter
from .models.dictionaries_list_response import DictionariesListResponse
from .models.dictionary_output import DictionaryOutput
from .models.dictionaries_import_response import DictionariesImportResponse
from .models.entry_add_body import EntryAddBody
from .models.entry_add_input import EntryAddInput
from .models.entry_add_response import EntryAddResponse
from .models.entry_add_output import EntryAddOutput
from .models.entry_delete_body import EntryDeleteBody
from .models.entry_delete_input import EntryDeleteInput
from .models.entry_delete_response import EntryDeleteResponse
from .models.entry_update_body import EntryUpdateBody
from .models.entry_update_input import EntryUpdateInput
from .models.entry_update_response import EntryUpdateResponse
from .models.entries_list_filters import EntriesListFilters
from .models.entries_list_sort_filter import EntriesListSortFilter
from .models.entries_list_match_filter import EntriesListMatchFilter
from .models.entries_list_response import EntriesListResponse
from .models.entry_output import EntryOutput
from .models.corpus import Corpus
from .models.corpus_list_response import CorpusListResponse
from .models.corpus_detail_response import CorpusDetailResponse
from .models.corpus_update_response import CorpusUpdateResponse
from .models.lite_corpus import LiteCorpus
from .models.corpus_add_response import CorpusAddResponse
from .models.corpus_exists_response import CorpusExistsResponse
from .models.corpus_delete_response import CorpusDeleteResponse
from .models.corpus_import_response import CorpusImportResponse
from .models.corpus_match import CorpusMatch
from .models.corpus_matches import CorpusMatches
from .models.corpus_match_response import CorpusMatchResponse
from .models.corpus_segment_target import CorpusSegmentTarget
from .models.corpus_segment import CorpusSegment
from .models.corpus_segment_list_response import CorpusSegmentListResponse
from .models.corpus_add_segment_target import CorpusAddSegmentTarget
from .models.corpus_add_segment import CorpusAddSegment
from .models.corpus_segment_add_request import CorpusSegmentAddRequest
from .models.corpus_segment_add_response import CorpusSegmentAddResponse
from .models.corpus_segment_delete_response import CorpusSegmentDeleteResponse
from .models.corpus_segment_update_response import CorpusSegmentUpdateResponse
from .models.corpus_segment_add_target_request import CorpusSegmentAddTargetRequest
from .models.corpus_segment_add_target_response import CorpusSegmentAddTargetResponse
from .models.corpus_segment_delete_target_response import CorpusSegmentDeleteTargetResponse

# import apis into sdk package
from .apis.corpus_api import CorpusApi
from .apis.dictionary_api import DictionaryApi

# import ApiClient
from .api_client import ApiClient
