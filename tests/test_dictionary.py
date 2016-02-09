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

    def get_dictionary_id(self):
        match_filter = systran_resources_api.DictionariesListMatchFilter()
        match_filter.regex_name = "pythonClientTest"

        list_filters = systran_resources_api.DictionariesListFilters()
        list_filters.match = match_filter

        result = self.dictionary_api.resources_dictionary_list_post(filters=list_filters)
        if result.dictionaries is not None and result.dictionaries[0].id is not None:
            return result.dictionaries[0].id

    def test11_resources_lookup_supported_languages_get(self):
        result = self.dictionary_api.resources_dictionary_lookup_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test12_resources_lookup_get(self):
        source = "en"
        target = "fr"
        inputs = ["test", "work"]
        result = self.dictionary_api.resources_dictionary_lookup_get(source=source, target=target, input=inputs)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test13_resources_lookup_get_with_auto_complete(self):
        source = "en"
        target = "fr"
        inputs = ["workaroun"]
        result = self.dictionary_api.resources_dictionary_lookup_get(source=source, target=target, input=inputs, autocomplete=True)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test14_resources_dictionary_list_post(self):
        result = self.dictionary_api.resources_dictionary_list_post()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test15_resources_dictionary_add_post(self):
        dict_add_input = systran_resources_api.DictionaryAddInput()
        dict_add_input.name = "pythonClientTest"
        dict_add_input.source_lang = "en"
        dict_add_input.target_langs = "fr"
        dict_add_input.type = "UD"
        dict_add_input.comments = "This is a dictionary created for python client testing purposes"

        dict_add_body = systran_resources_api.DictionaryAddBody()
        dict_add_body.dictionary = dict_add_input

        result = self.dictionary_api.resources_dictionary_add_post(input=dict_add_body)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test16_resources_dictionary_list_post_with_match_filter(self):
        match_filter = systran_resources_api.DictionariesListMatchFilter()
        match_filter.regex_name = "pythonClientTest"

        list_filters = systran_resources_api.DictionariesListFilters()
        list_filters.match = match_filter

        result = self.dictionary_api.resources_dictionary_list_post(filters=list_filters)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test17_resources_dictionary_list_post_with_sort_filter(self):
        sort_filter = systran_resources_api.DictionariesListSortFilter()
        sort_filter.name = 1    # sort by dictionary name in "ascending" order

        list_filters = systran_resources_api.DictionariesListFilters()
        list_filters.sort = sort_filter

        result = self.dictionary_api.resources_dictionary_list_post(filters=list_filters)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test21_resources_dictionary_update_post(self):
        dictionary_id = self.get_dictionary_id()
        if dictionary_id is None:
            print "No dictionary found to update"
            return
        dict_update_input = systran_resources_api.DictionaryUpdateInput()
        dict_update_input.name = "pythonClientTestUpdatedName"
        dict_update_input.source_lang = "en"
        dict_update_input.target_langs = "fr"
        dict_update_input.comments = "This dictionary has been updated by python client"

        dict_update_body = systran_resources_api.DictionaryUpdateBody()
        dict_update_body.dictionary = dict_update_input

        result = self.dictionary_api.resources_dictionary_update_post(dictionary_id=dictionary_id, input=dict_update_body)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test22_resources_dictionary_entry_add_post(self):
        dictionary_id = self.get_dictionary_id()
        if dictionary_id is None:
            print "No dictionary found to add an entry"
            return
        entry_add_input = systran_resources_api.EntryAddInput()
        entry_add_input.source_lang = "en"
        entry_add_input.target_lang = "fr"
        entry_add_input.source = "house"
        entry_add_input.target = "maison"

        entry_add_body = systran_resources_api.EntryAddBody()
        entry_add_body.entry = entry_add_input

        result = self.dictionary_api.resources_dictionary_entry_add_post(dictionary_id=dictionary_id, input=entry_add_body)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test23_resources_dictionary_entry_list_post(self):
        dictionary_id = self.get_dictionary_id()
        if dictionary_id is None:
            print "No dictionary found to get the list of entry"
            return
        result = self.dictionary_api.resources_dictionary_entry_list_post(dictionary_id=dictionary_id)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test24_resources_dictionary_entry_update_post(self):
        dictionary_id = self.get_dictionary_id()
        if dictionary_id is None:
            print "No dictionary found to update an entry"
            return
        entry_update_input = systran_resources_api.EntryUpdateInput()
        entry_update_input.source_lang = "en"
        entry_update_input.target_lang = "fr"
        entry_update_input.source = "house"
        entry_update_input.target = "batiment"

        entry_list = self.dictionary_api.resources_dictionary_entry_list_post(dictionary_id=dictionary_id)
        if entry_list is None or entry_list.entries is None or entry_list.entries[0].source_id is None:
            print "No entry found to update"
            return
        entry_update_body = systran_resources_api.EntryUpdateBody()
        entry_update_body.source_id = entry_list.entries[0].source_id
        entry_update_body.target_id = entry_list.entries[0].target_id
        entry_update_body.update = entry_update_input

        result = self.dictionary_api.resources_dictionary_entry_update_post(dictionary_id=dictionary_id, input=entry_update_body)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test31_resources_dictionary_entry_delete_post(self):
        dictionary_id = self.get_dictionary_id()
        if dictionary_id is None:
            print "No dictionary found to delete an entry"
            return
        entry_list = self.dictionary_api.resources_dictionary_entry_list_post(dictionary_id=dictionary_id)
        if entry_list.entries is None or entry_list.entries[0].source_id is None:
            print "No entry found to delete"
            return
        entry_delete_input = systran_resources_api.EntryDeleteInput()
        entry_delete_input.source_id = entry_list.entries[0].source_id
        entry_delete_input.target_id = entry_list.entries[0].target_id

        entry_delete_body = systran_resources_api.EntryDeleteBody()
        entry_delete_body.entry = entry_delete_input

        result = self.dictionary_api.resources_dictionary_entry_delete_post(dictionary_id=dictionary_id, input=entry_delete_body)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test32_resources_dictionary_delete_post(self):
        match_filter = systran_resources_api.DictionariesListMatchFilter()
        match_filter.regex_name = "pythonClientTest"

        list_filters = systran_resources_api.DictionariesListFilters()
        list_filters.match = match_filter

        result = self.dictionary_api.resources_dictionary_list_post(filters=list_filters)
        if result.dictionaries is None or len(result.dictionaries) == 0:
            print "No dictionary found to delete"
            return
        for dictionary in result.dictionaries:
            if dictionary.id is not None:
                self.dictionary_api.resources_dictionary_delete_post(dictionary_id=dictionary.id)
                print "Dictionary " + dictionary.id + " has been deleted"

if __name__ == '__main__':
    unittest.main()