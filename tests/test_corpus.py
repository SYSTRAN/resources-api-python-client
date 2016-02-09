#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systran_resources_api
import systran_resources_api.configuration

class CorpusApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systran_resources_api.configuration.load_api_key(api_key_file)
        self.api_client = systran_resources_api.ApiClient()
        self.corpus_api = systran_resources_api.CorpusApi(self.api_client)

    def test11_clean_existed_corpus(self):
        corpus_ids = []
        list_corpus = self.corpus_api.resources_corpus_list_get(prefix="pythonClientTest")
        self.assertIsNotNone(list_corpus)
        if list_corpus.files is not None:
            for corpus in list_corpus.files:
                if corpus.id is not None:
                    corpus_ids.append(corpus.id)
            if len(corpus_ids) > 0:
                result = self.corpus_api.resources_corpus_delete_post(corpus_id=corpus_ids)
                self.assertIsNotNone(result)
                print result.__repr__()

    def test21_resources_corpus_add_post(self):
        lang = "en"
        name = "pythonClientTestAddCorpus"
        result = self.corpus_api.resources_corpus_add_post(name=name, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test22_resources_corpus_import_post(self):
        input = "#TM\n" \
                "#EN\tFR\n" \
                "This is a test \t Ceci est un test"
        format = "text/bitext"
        name = "pythonClientTestImportCorpus"
        result = self.corpus_api.resources_corpus_import_post(name=name, input=input, format=format)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test23_resources_corpus_import_post_with_file(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "corpus.txt")
        format = "text/bitext"
        name = "pythonClientTestFileImport"
        result = self.corpus_api.resources_corpus_import_post(name=name, input_file=input_file, format=format)
        self.assertIsNotNone(result)
        print result.__repr__()

    def get_corpus_id_by_prefix(self, prefix):
        if prefix is None:
            prefix = "pythonClientTest"
        result = self.corpus_api.resources_corpus_list_get(prefix=prefix)
        if result.files is not None and result.files[0].id is not None:
            return result.files[0].id

    def test12_resources_corpus_list_get(self):
        result = self.corpus_api.resources_corpus_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test13_resources_corpus_list_get_with_source_target(self):
        source = "en"
        target = "fr"
        result = self.corpus_api.resources_corpus_list_get(source_lang=source, target_lang=target)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test31_resources_corpus_list_get_with_prefix(self):
        prefix = "pythonClientTest"
        result = self.corpus_api.resources_corpus_list_get(prefix=prefix)
        print result.__repr__()

    def test32_resources_corpus_exists_get(self):
        name = "pythonClientTestAddCorpus"
        result = self.corpus_api.resources_corpus_exists_get(name=name)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test33_resources_corpus_details_get(self):
        corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_id is None:
            print "No corpus id found to get detail information"
            return
        result = self.corpus_api.resources_corpus_details_get(corpus_id=corpus_id)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test34_resources_corpus_export_get(self):
        corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_id is None:
            print "No corpus id found to export data"
            return
        result = self.corpus_api.resources_corpus_export_get(corpus_id=corpus_id)
        self.assertIsNotNone(result)
        output_file = os.path.join(os.path.dirname(__file__), "", "exported_corpus.xml")
        fo = open(output_file, "wb")
        fo.write(result)
        fo.close()
        print result

    def test35_resources_corpus_export_get_with_format(self):
        corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_id is None:
            print "No corpus id found to export data"
            return
        format = "text/bitext"
        result = self.corpus_api.resources_corpus_export_get(corpus_id=corpus_id, format=format)
        self.assertIsNotNone(result)
        output_file = os.path.join(os.path.dirname(__file__), "", "exported_corpus.txt")
        fo = open(output_file, "wb")
        fo.write(result)
        fo.close()
        print result

    def test36_resources_corpus_update_post(self):
        corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_id is None:
            print "No corpus id found to update data"
            return
        name = "pythonClientTestUpdatedName"
        result = self.corpus_api.resources_corpus_update_post(corpus_id=corpus_id, name=name)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test41_resources_corpus_segment_list_get(self):
        corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_id is None:
            print "No corpus id found to get segment list"
            return
        result = self.corpus_api.resources_corpus_segment_list_get(corpus_id=corpus_id)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test42_resources_corpus_segment_add_post(self):
        segment_target = systran_resources_api.CorpusAddSegmentTarget()
        segment_target.lang = "fr"
        segment_target.target = "Ceci est une belle maison"
        list_segment_targets = [segment_target]

        corpus_add_segment = systran_resources_api.CorpusAddSegment()
        corpus_add_segment.lang = "en"
        corpus_add_segment.source = "This is a beautiful house"
        corpus_add_segment.targets = list_segment_targets
        list_corpus_add_segments = [corpus_add_segment]

        corpus_segment_add_request = systran_resources_api.CorpusSegmentAddRequest()
        corpus_segment_add_request.corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_segment_add_request.corpus_id is None:
            print "No corpus id found to add a segment"
            return
        corpus_segment_add_request.segments = list_corpus_add_segments

        result = self.corpus_api.resources_corpus_segment_add_post(body=corpus_segment_add_request)
        self.assertIsNotNone(result)
        print result.__repr__()


    def test51_resources_corpus_match_get(self):
        corpus_ids = [self.get_corpus_id_by_prefix(prefix="pythonClientTest")]
        if corpus_ids[0] is None:
            print "No corpus id found for match operation"
            return
        source = "en"
        target = "fr"
        inputs = ["This is a test", "This is a beautiful house"]
        result = self.corpus_api.resources_corpus_match_get(corpus_id=corpus_ids, input=inputs, source_lang=source, target_lang=target)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test61_resources_corpus_segment_delete_post(self):
        corpus_id = self.get_corpus_id_by_prefix(prefix="pythonClientTest")
        if corpus_id is None:
            print "No corpus id found to delete a segment"
            return
        segment_list = self.corpus_api.resources_corpus_segment_list_get(corpus_id=corpus_id)
        if segment_list.segments is None or segment_list.segments[0].id:
            print "No segment id found to delete"
            return
        seg_id = [segment_list.segments[0].id]
        result = self.corpus_api.resources_corpus_segment_delete_post(corpus_id=corpus_id, seg_id=seg_id)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test62_resources_corpus_delete_get(self):
        corpus_ids = []
        list_corpus = self.corpus_api.resources_corpus_list_get(prefix="pythonClientTest")
        if list_corpus.files is None:
            print "No corpus id found to delete"
            return
        for corpus in list_corpus.files:
            if corpus.id is not None:
                corpus_ids.append(corpus.id)
        if len(corpus_ids) == 0:
            print "No corpus id found to delete"
            return
        result = self.corpus_api.resources_corpus_delete_post(corpus_id=corpus_ids)
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()


