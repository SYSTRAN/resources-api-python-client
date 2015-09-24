#!/usr/bin/env python
# coding: utf-8

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

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class DictionaryApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def resources_dictionary_add_post(self, input, **kwargs):
        """
        Add dictionary
        Add a new dictionary.

        :param DictionaryAddBody input: Input with dictionary information (required)
        
        :return: DictionaryAddResponse
        """
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_dictionary_add_post`")
        
        all_params = ['input']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_add_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/add'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'input' in params:
            body_params = params['input']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='DictionaryAddResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_delete_post(self, dictionary_id, **kwargs):
        """
        Delete a dictionary
        Delete an existing dictionary.

        :param str dictionary_id: Dictionary Id (required)
        
        :return: None
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_delete_post`")
        
        all_params = ['dictionary_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_delete_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/delete'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def resources_dictionary_entry_add_post(self, dictionary_id, input, **kwargs):
        """
        Add an entry
        Add a new entry to an existing dictionary.

        :param str dictionary_id: Dictionary Id (required)
        :param EntryAddBody input: Input with dictionary id and entries information (required)
        
        :return: EntryAddResponse
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_entry_add_post`")
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_dictionary_entry_add_post`")
        
        all_params = ['dictionary_id', 'input']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_entry_add_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/entry/add'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'input' in params:
            body_params = params['input']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='EntryAddResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_entry_delete_post(self, dictionary_id, input, **kwargs):
        """
        Delete an entry
        Delete an entry in an existing dictionary.

        :param str dictionary_id: Dictionary Id (required)
        :param EntryDeleteBody input: Input with dictionary id + entry id (src or tgt) to delete (required)
        
        :return: EntryDeleteResponse
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_entry_delete_post`")
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_dictionary_entry_delete_post`")
        
        all_params = ['dictionary_id', 'input']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_entry_delete_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/entry/delete'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'input' in params:
            body_params = params['input']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='EntryDeleteResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_entry_import_post(self, dictionary_id, source_lang, input_file, **kwargs):
        """
        Import entries
        Import entries to an existing dictionary.

        :param str dictionary_id: Id of the dictionary where to import entries (required)
        :param str source_lang: Source lang of the entries to import (required)
        :param File input_file: File with entries to import (required)
        
        :return: DictionariesImportResponse
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_entry_import_post`")
        
        # verify the required parameter 'source_lang' is set
        if source_lang is None:
            raise ValueError("Missing the required parameter `source_lang` when calling `resources_dictionary_entry_import_post`")
        
        # verify the required parameter 'input_file' is set
        if input_file is None:
            raise ValueError("Missing the required parameter `input_file` when calling `resources_dictionary_entry_import_post`")
        
        all_params = ['dictionary_id', 'source_lang', 'input_file']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_entry_import_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/entry/import'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        if 'source_lang' in params:
            query_params['sourceLang'] = params['source_lang']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='DictionariesImportResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_entry_list_post(self, dictionary_id, **kwargs):
        """
        List entries
        List entries for a specific dictionary.

        :param str dictionary_id: Dictionary Id (required)
        :param EntriesListFilters filters: Different filters that can be applied to the list functionality (skip/limit/sort/match) 
        
        :return: EntriesListResponse
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_entry_list_post`")
        
        all_params = ['dictionary_id', 'filters']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_entry_list_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/entry/list'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'filters' in params:
            body_params = params['filters']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='EntriesListResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_entry_update_post(self, dictionary_id, input, **kwargs):
        """
        Update an entry
        Update an entry in an existing dictionary.

        :param str dictionary_id: Dictionary Id (required)
        :param EntryUpdateBody input: Input with dictionary id + entry id (src or tgt) to delete (required)
        
        :return: EntryUpdateResponse
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_entry_update_post`")
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_dictionary_entry_update_post`")
        
        all_params = ['dictionary_id', 'input']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_entry_update_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/entry/update'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'input' in params:
            body_params = params['input']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='EntryUpdateResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_list_post(self, **kwargs):
        """
        List dictionaries
        List the dictionaries.

        :param DictionariesListFilters filters: Different filters that can be applied to the list functionality (skip/limit/sort/match) 
        
        :return: DictionariesListResponse
        """
        
        all_params = ['filters']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_list_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/list'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'filters' in params:
            body_params = params['filters']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='DictionariesListResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_lookup_get(self, source, target, input, **kwargs):
        """
        Lookup
        Lookup words from a source language to a target language.

        :param str source: Language code of the source text\n (required)
        :param str target: Language code in which to lookup the source text\n (required)
        :param list[str] input: Input word (the 'input' parameter can be repeated)\n (required)
        :param bool autocomplete: With this option, if the input word is not found in the source language, it will be filled in with autocompletion to perform the lookup\n\nDefault: false\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: LookupResponse
        """
        
        # verify the required parameter 'source' is set
        if source is None:
            raise ValueError("Missing the required parameter `source` when calling `resources_dictionary_lookup_get`")
        
        # verify the required parameter 'target' is set
        if target is None:
            raise ValueError("Missing the required parameter `target` when calling `resources_dictionary_lookup_get`")
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_dictionary_lookup_get`")
        
        all_params = ['source', 'target', 'input', 'autocomplete', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_lookup_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/lookup'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'autocomplete' in params:
            query_params['autocomplete'] = params['autocomplete']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='LookupResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_lookup_supported_languages_get(self, **kwargs):
        """
        Lookup Supported Languages
        List of language pairs in which lookup is supported. This list can be limited to a specific source language or target language.\n

        :param str source: Language code of the source text\n 
        :param str target: Language code into which to translate the source text\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: LookupSupportedLanguageResponse
        """
        
        all_params = ['source', 'target', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_lookup_supported_languages_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/lookup/supportedLanguages'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='LookupSupportedLanguageResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_supported_languages_get(self, **kwargs):
        """
        Supported Languages
        Get supported languages by dictionaries

        
        :return: SupportedLanguagesResponse
        """
        
        all_params = []

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_supported_languages_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/supportedLanguages'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SupportedLanguagesResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_dictionary_update_post(self, dictionary_id, input, **kwargs):
        """
        Update a dictionary
        Update an existing dictionary.

        :param str dictionary_id: Dictionary Id (required)
        :param DictionaryUpdateBody input: Input with dictionary id (required)
        
        :return: DictionaryUpdateResponse
        """
        
        # verify the required parameter 'dictionary_id' is set
        if dictionary_id is None:
            raise ValueError("Missing the required parameter `dictionary_id` when calling `resources_dictionary_update_post`")
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_dictionary_update_post`")
        
        all_params = ['dictionary_id', 'input']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_dictionary_update_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/dictionary/update'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'dictionary_id' in params:
            query_params['dictionaryId'] = params['dictionary_id']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'input' in params:
            body_params = params['input']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='DictionaryUpdateResponse', auth_settings=auth_settings)
        
        return response
        









