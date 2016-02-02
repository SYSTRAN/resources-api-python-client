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

class CorpusApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def resources_corpus_add_post(self, name, lang, **kwargs):
        """
        Add a new corpus
        Add a new empty corpus.\n

        :param str name: Corpus name. The name also contains the directories (ex: \"/myproject/firstPass/PersonalCorpus\") (required)
        :param str lang: Language code ([details](#description_langage_code_values)) (required)
        :param list[str] tag: Tag for the the corpus (this parameter can be repeated) 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusAddResponse
        """
        
        # verify the required parameter 'name' is set
        if name is None:
            raise ValueError("Missing the required parameter `name` when calling `resources_corpus_add_post`")
        
        # verify the required parameter 'lang' is set
        if lang is None:
            raise ValueError("Missing the required parameter `lang` when calling `resources_corpus_add_post`")
        
        all_params = ['name', 'lang', 'tag', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_add_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/add'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'name' in params:
            query_params['name'] = params['name']
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'tag' in params:
            query_params['tag'] = params['tag']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusAddResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_delete_post(self, corpus_id, **kwargs):
        """
        Delete corpus
        Delete a corpus.\n

        :param list[str] corpus_id: Corpus identifier (this parameter can be repeated) (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusDeleteResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_delete_post`")
        
        all_params = ['corpus_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_delete_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/delete'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusDeleteResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_details_get(self, corpus_id, **kwargs):
        """
        Detail corpus
        Get detailed information about a corpus.\n

        :param str corpus_id: Corpus identifier (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusDetailResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_details_get`")
        
        all_params = ['corpus_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_details_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/details'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusDetailResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_exists_get(self, name, **kwargs):
        """
        Corpus Exists
        Check if a corpus exists\n

        :param str name: Corpus name. The name also contains the directories (ex: \"/myproject/firstPass/PersonalCorpus\") (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusExistsResponse
        """
        
        # verify the required parameter 'name' is set
        if name is None:
            raise ValueError("Missing the required parameter `name` when calling `resources_corpus_exists_get`")
        
        all_params = ['name', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_exists_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/exists'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'name' in params:
            query_params['name'] = params['name']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusExistsResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_export_get(self, corpus_id, **kwargs):
        """
        Export corpus
        Download a corpus in an expected format.\n

        :param str corpus_id: Corpus identifier (required)
        :param str format: The expected corpus format\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: File
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_export_get`")
        
        all_params = ['corpus_id', 'format', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_export_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/export'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'format' in params:
            query_params['format'] = params['format']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/x-tmx+xml', 'text/bitext'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='File', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_import_post(self, name, **kwargs):
        """
        Import corpus
        Add a new corpus from an existing corpus.\n

        :param str name: Corpus name. The name also contains the directories (ex: \"/myproject/firstPass/PersonalCorpus\") (required)
        :param str input: Content of the existing corpus\n\n**Either `input` or `inputFile` is required**\n 
        :param File input_file: Content of the existing corpus\n\n**Either `input` or `inputFile` is required**\n 
        :param str format: Format of the input corpus.\n 
        :param list[str] tag: Tag for the the corpus (this parameter can be repeated) 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusImportResponse
        """
        
        # verify the required parameter 'name' is set
        if name is None:
            raise ValueError("Missing the required parameter `name` when calling `resources_corpus_import_post`")
        
        all_params = ['name', 'input', 'input_file', 'format', 'tag', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_import_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/import'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'name' in params:
            query_params['name'] = params['name']
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'format' in params:
            query_params['format'] = params['format']
        
        if 'tag' in params:
            query_params['tag'] = params['tag']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
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
                                            response='CorpusImportResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_list_get(self, **kwargs):
        """
        List corpora
        List available corpora. Parameters can be used to restrict the list of returned corpora.\n

        :param str source_lang: Source language code ([details](#description_langage_code_values)) 
        :param str target_lang: Target language code ([details](#description_langage_code_values)) 
        :param bool without_pending: Filter out corpora in \"pending\" status\n 
        :param bool without_error: Filter out corpora in \"error\" status\n 
        :param str prefix: Prefix of the corpus name\n 
        :param str directory: If specified, response will return the content of this directory, including corpora and directories. This list can can also be filtered by the prefix parameter.\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusListResponse
        """
        
        all_params = ['source_lang', 'target_lang', 'without_pending', 'without_error', 'prefix', 'directory', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'source_lang' in params:
            query_params['sourceLang'] = params['source_lang']
        
        if 'target_lang' in params:
            query_params['targetLang'] = params['target_lang']
        
        if 'without_pending' in params:
            query_params['withoutPending'] = params['without_pending']
        
        if 'without_error' in params:
            query_params['withoutError'] = params['without_error']
        
        if 'prefix' in params:
            query_params['prefix'] = params['prefix']
        
        if 'directory' in params:
            query_params['directory'] = params['directory']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusListResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_match_get(self, corpus_id, input, source_lang, target_lang, **kwargs):
        """
        Corpus Match
        Find sentences in the corpus that match the input text from a given threshold.\n

        :param list[str] corpus_id: Corpus identifier (this parameter can be repeated) (required)
        :param list[str] input: Text is used to perform the match operation (this parameter can be repeated)\n (required)
        :param str source_lang: Source language code ([details](#description_langage_code_values)) (required)
        :param str target_lang: Target language code ([details](#description_langage_code_values)) (required)
        :param float threshold: The fuzzy match threshold from which a sentence will be considered as a match result\n 
        :param int limit: Limit the number of returned matches. Only first matches within the \"limit\" will be returned\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusMatchResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_match_get`")
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `resources_corpus_match_get`")
        
        # verify the required parameter 'source_lang' is set
        if source_lang is None:
            raise ValueError("Missing the required parameter `source_lang` when calling `resources_corpus_match_get`")
        
        # verify the required parameter 'target_lang' is set
        if target_lang is None:
            raise ValueError("Missing the required parameter `target_lang` when calling `resources_corpus_match_get`")
        
        all_params = ['corpus_id', 'input', 'source_lang', 'target_lang', 'threshold', 'limit', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_match_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/match'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'source_lang' in params:
            query_params['sourceLang'] = params['source_lang']
        
        if 'target_lang' in params:
            query_params['targetLang'] = params['target_lang']
        
        if 'threshold' in params:
            query_params['threshold'] = params['threshold']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusMatchResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_segment_add_post(self, body, **kwargs):
        """
        Add corpus segments
        Add segments in a corpus.\n

        :param CorpusSegmentAddRequest body: List of segments to add (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusSegmentAddResponse
        """
        
        # verify the required parameter 'body' is set
        if body is None:
            raise ValueError("Missing the required parameter `body` when calling `resources_corpus_segment_add_post`")
        
        all_params = ['body', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_segment_add_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/segment/add'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'body' in params:
            body_params = params['body']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusSegmentAddResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_segment_delete_post(self, corpus_id, seg_id, **kwargs):
        """
        Delete corpus segments
        Delete segments in a corpus.\n

        :param str corpus_id: Corpus identifier (required)
        :param list[str] seg_id: Segment Id (this parameter can be repeated) (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusSegmentDeleteResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_segment_delete_post`")
        
        # verify the required parameter 'seg_id' is set
        if seg_id is None:
            raise ValueError("Missing the required parameter `seg_id` when calling `resources_corpus_segment_delete_post`")
        
        all_params = ['corpus_id', 'seg_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_segment_delete_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/segment/delete'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'seg_id' in params:
            query_params['segId'] = params['seg_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusSegmentDeleteResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_segment_list_get(self, corpus_id, **kwargs):
        """
        List corpus segments
        List segments in a corpus.\n

        :param str corpus_id: Corpus identifier (required)
        :param int skip: Skip first found segments in the response\n 
        :param int limit: Limit the number of returned segments\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusSegmentListResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_segment_list_get`")
        
        all_params = ['corpus_id', 'skip', 'limit', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_segment_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/segment/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'skip' in params:
            query_params['skip'] = params['skip']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusSegmentListResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_segment_target_add_post(self, body, **kwargs):
        """
        Add corpus segment targets
        Add targets to a segment in a corpus.\n

        :param CorpusSegmentAddTargetRequest body: List of targets to add (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusSegmentAddTargetResponse
        """
        
        # verify the required parameter 'body' is set
        if body is None:
            raise ValueError("Missing the required parameter `body` when calling `resources_corpus_segment_target_add_post`")
        
        all_params = ['body', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_segment_target_add_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/segment/target/add'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'body' in params:
            body_params = params['body']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusSegmentAddTargetResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_segment_target_delete_post(self, corpus_id, seg_id, target_id, **kwargs):
        """
        Delete corpus segment targets
        Delete segment targets in a corpus.\n

        :param str corpus_id: Corpus identifier (required)
        :param str seg_id: Segment Id (required)
        :param list[str] target_id: Target id (this parameter can be repeated) (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusSegmentDeleteTargetResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_segment_target_delete_post`")
        
        # verify the required parameter 'seg_id' is set
        if seg_id is None:
            raise ValueError("Missing the required parameter `seg_id` when calling `resources_corpus_segment_target_delete_post`")
        
        # verify the required parameter 'target_id' is set
        if target_id is None:
            raise ValueError("Missing the required parameter `target_id` when calling `resources_corpus_segment_target_delete_post`")
        
        all_params = ['corpus_id', 'seg_id', 'target_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_segment_target_delete_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/segment/target/delete'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'seg_id' in params:
            query_params['segId'] = params['seg_id']
        
        if 'target_id' in params:
            query_params['targetId'] = params['target_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusSegmentDeleteTargetResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_segment_update_post(self, corpus_id, seg_id, **kwargs):
        """
        Update corpus segment
        Update a segment in a corpus.\n

        :param str corpus_id: Corpus identifier (required)
        :param str seg_id: Segment Id (required)
        :param str source: Source text 
        :param str target_id: Target id 
        :param str target: Target text. `targetId` is required if `target` is specified. 
        :param str target_lang: Target language. `targetId` is required if `targetLang` is specified. 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusSegmentUpdateResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_segment_update_post`")
        
        # verify the required parameter 'seg_id' is set
        if seg_id is None:
            raise ValueError("Missing the required parameter `seg_id` when calling `resources_corpus_segment_update_post`")
        
        all_params = ['corpus_id', 'seg_id', 'source', 'target_id', 'target', 'target_lang', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_segment_update_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/segment/update'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'seg_id' in params:
            query_params['segId'] = params['seg_id']
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target_id' in params:
            query_params['targetId'] = params['target_id']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'target_lang' in params:
            query_params['targetLang'] = params['target_lang']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusSegmentUpdateResponse', auth_settings=auth_settings)
        
        return response
        
    def resources_corpus_update_post(self, corpus_id, **kwargs):
        """
        Update corpus properties
        Update properties of a corpus.\n

        :param str corpus_id: Corpus identifier (required)
        :param str name: Corpus name. The name also contains the directories (ex: \"/myproject/firstPass/PersonalCorpus\") 
        :param list[str] tag: Tag for the the corpus (this parameter can be repeated) 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: CorpusUpdateResponse
        """
        
        # verify the required parameter 'corpus_id' is set
        if corpus_id is None:
            raise ValueError("Missing the required parameter `corpus_id` when calling `resources_corpus_update_post`")
        
        all_params = ['corpus_id', 'name', 'tag', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method resources_corpus_update_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/resources/corpus/update'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        if 'corpus_id' in params:
            query_params['corpusId'] = params['corpus_id']
        
        if 'name' in params:
            query_params['name'] = params['name']
        
        if 'tag' in params:
            query_params['tag'] = params['tag']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='CorpusUpdateResponse', auth_settings=auth_settings)
        
        return response
        









