#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systran_resources_api
import systran_resources_api.configuration

class DictionaryApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systran_resources_api.configuration.load_api_key(api_key_file)
        self.api_client = systran_resources_api.ApiClient()
        self.dictionary_api = systran_resources_api.DictionaryApi(self.api_client)

    def test_resources_lookup_supported_languages_get(self):
        result = self.dictionary_api.resources_dictionary_lookup_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_lookup_get(self):
        source = "en"
        target = "fr"
        inputs = ["test", "work"]
        result = self.dictionary_api.resources_dictionary_lookup_get(source=source, target=target, input=inputs)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_lookup_get_with_auto_complete(self):
        source = "en"
        target = "fr"
        inputs = ["workaroun"]
        result = self.dictionary_api.resources_dictionary_lookup_get(source=source, target=target, input=inputs, autocomplete=True)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_dictionary_list_post(self):
        result = self.dictionary_api.resources_dictionary_list_post()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_dictionary_add_post(self):
        dict_add_input = systran_resources_api.DictionaryAddInput()
        dict_add_input.name = "testPythonClient"
        dict_add_input.source_lang = "en"
        dict_add_input.target_langs = "fr"
        dict_add_input.type = "UD"
        dict_add_input.comments = "This is a dictionary created for client java test"

        dict_add_body = systran_resources_api.DictionaryAddBody()
        dict_add_body.dictionary = dict_add_input

        result = self.dictionary_api.resources_dictionary_add_post(input=dict_add_body)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_dictionary_list_post_with_match_filter(self):
        match_filter = systran_resources_api.DictionariesListMatchFilter()
        match_filter.regex_name = "test"

        list_filters = systran_resources_api.DictionariesListFilters()
        list_filters.match = match_filter

        result = self.dictionary_api.resources_dictionary_list_post(filters=list_filters)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_dictionary_list_post_with_sort_filter(self):
        sort_filter = systran_resources_api.DictionariesListSortFilter()
        sort_filter.name = 1    # sort by dictionary name in "ascending" order

        list_filters = systran_resources_api.DictionariesListFilters()
        list_filters.sort = sort_filter

        result = self.dictionary_api.resources_dictionary_list_post(filters=list_filters)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_dictionary_update_post(self):
        dictionary_id = "55c0a88275314374575ae4d4"
        dict_update_input = systran_resources_api.DictionaryUpdateInput()
        dict_update_input.name = "testPythonClient"
        dict_update_input.source_lang = "en"
        dict_update_input.target_langs = "fr"
        dict_update_input.comments = "This dictionary has been updated by python client test"

        dict_update_body = systran_resources_api.DictionaryUpdateBody()
        dict_update_body.dictionary = dict_update_input

        print 'Use a valid "dictionary_id" and uncomment below codes to test'
        # result = self.dictionary_api.resources_dictionary_update_post(dictionary_id=dictionary_id, input=dict_update_body)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_dictionary_delete_post(self):
        dictionary_id = "55db168775314374575ae630"
        print 'Use a valid "dictionary_id" and uncomment below codes to test'
        # result = self.dictionary_api.resources_dictionary_delete_post(dictionary_id=dictionary_id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_dictionary_entry_add_post(self):
        dictionary_id = "5603ba796b5e3fa187e83604"
        entry_add_input = systran_resources_api.EntryAddInput()
        entry_add_input.source_lang = "en"
        entry_add_input.target_lang = "fr"
        entry_add_input.source = "house"
        entry_add_input.target = "maison"

        entry_add_body = systran_resources_api.EntryAddBody()
        entry_add_body.entry = entry_add_input

        print 'Use a valid "dictionary_id" and correspond "source lang", "target lang" then uncomment below codes to test'
        # result = self.dictionary_api.resources_dictionary_entry_add_post(dictionary_id=dictionary_id, input=entry_add_body)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_dictionary_entry_list_post(self):
        dictionary_id = "55c0a88275314374575ae4d4"
        print 'Use a valid "dictionary_id" and uncomment below codes to test'
        # result = self.dictionary_api.resources_dictionary_entry_list_post(dictionary_id=dictionary_id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

if __name__ == '__main__':
    unittest.main()