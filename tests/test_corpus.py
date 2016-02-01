#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systranResourcesApi
import systranResourcesApi.configuration

class CorpusApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systranResourcesApi.configuration.load_api_key(api_key_file)
        self.api_client = systranResourcesApi.ApiClient()
        self.corpus_api = systranResourcesApi.CorpusApi(self.api_client)

    def test_resources_corpus_list_get(self):
        result = self.corpus_api.resources_corpus_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_corpus_list_get_with_source_target(self):
        source = "en"
        target = "fr"
        result = self.corpus_api.resources_corpus_list_get(source_lang=source, target_lang=target)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_corpus_list_get_with_prefix(self):
        prefix = "testImport"
        result = self.corpus_api.resources_corpus_list_get(prefix=prefix)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_corpus_add_post(self):
        lang = "en"
        name = "testAddCorpus"
        print 'Enter a new corpus name and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_add_post(name=name, lang=lang)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_import_post(self):
        input = "#TM\n" \
                "#EN\tFR\n" \
                "This is a test \t Ceci est un test"
        format= "text/bitext"
        name = "testImport"
        print 'Enter a new corpus name and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_import_post(name=name, input=input, format=format)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_import_post_with_file(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "corpus.txt")
        format = "text/bitext"
        name = "testFileImport"
        print 'Enter a new corpus name and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_import_post(name=name, input_file=input_file, format=format)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_exists_get(self):
        name = "testImport"
        result = self.corpus_api.resources_corpus_exists_get(name=name)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_resources_corpus_details_get(self):
        corpus_id = "55b62288158ad061c6aaa509"
        print 'Use a valid "corpus_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_details_get(corpus_id=corpus_id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_export_get(self):
        corpus_id = "55b62288158ad061c6aaa509"
        print 'Use a valid "corpus_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_export_get(corpus_id=corpus_id)
        # self.assertIsNotNone(result)
        # output_file = os.path.join(os.path.dirname(__file__), "", "exported_corpus.xml")
        # fo = open(output_file, "wb")
        # fo.write(result)
        # fo.close()
        # print result

    def test_resources_corpus_export_get_with_format(self):
        corpus_id = "55b62288158ad061c6aaa509"
        format = "text/bitext"
        print 'Use a valid "corpus_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_export_get(corpus_id=corpus_id, format=format)
        # self.assertIsNotNone(result)
        # output_file = os.path.join(os.path.dirname(__file__), "", "exported_corpus.txt")
        # fo = open(output_file, "wb")
        # fo.write(result)
        # fo.close()
        # print result

    def test_resources_corpus_update_post(self):
        corpus_id = "55b62288158ad061c6aaa509"
        name = "testImportPythonClient"
        print 'Use a valid "corpus_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_update_post(corpus_id=corpus_id, name=name)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_segment_list_get(self):
        corpus_id = "55b62288158ad061c6aaa509"
        print 'Use a valid "corpus_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_segment_list_get(corpus_id=corpus_id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_segment_add_post(self):
        segment_target = systranResourcesApi.CorpusAddSegmentTarget()
        segment_target.lang = "fr"
        segment_target.target = "Ceci est une belle maison"
        list_segment_targets = [segment_target]

        corpus_add_segment = systranResourcesApi.CorpusAddSegment()
        corpus_add_segment.lang = "en"
        corpus_add_segment.source = "This is a beautiful house"
        corpus_add_segment.targets = list_segment_targets
        list_corpus_add_segments = [corpus_add_segment]

        corpus_segment_add_request = systranResourcesApi.CorpusSegmentAddRequest()
        corpus_segment_add_request.corpus_id = "55b62288158ad061c6aaa509"
        corpus_segment_add_request.segments = list_corpus_add_segments

        print 'Use a valid "corpus_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_segment_add_post(body=corpus_segment_add_request)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_segment_delete_post(self):
        corpus_id = "55b62288158ad061c6aaa509"
        seg_id = ["55b62288158ad061c6aaa508.55c0dda6fd400171d6f8428d"]
        print 'Use a valid "corpus_id", "seg_id" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_segment_delete_post(corpus_id=corpus_id, seg_id=seg_id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_delete_get(self):
        corpus_ids = ["55b6311d158ad061c6aaa519", "55b633c4158ad061c6aaa51b"]
        print 'Use a valid list of "corpus_ids" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_delete_post(corpus_id=corpus_ids)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_resources_corpus_match_get(self):
        corpus_ids = ["55b62288158ad061c6aaa509"]
        source = "en"
        target = "fr"
        inputs = ["This is a test", "This is a beautiful house"]
        print 'Use a valid list of "corpus_ids" and uncomment below codes to test'
        # result = self.corpus_api.resources_corpus_match_get(corpus_id=corpus_ids, input=inputs, source_lang=source, target_lang=target)
        # self.assertIsNotNone(result)
        # print result.__repr__()

if __name__ == '__main__':
    unittest.main()


