import json
import unittest

from linkml_solr.utils.solr_bulkload import _solr_value


class SolrValueTestCase(unittest.TestCase):
    """Nested records are serialized to JSON strings for Solr (no service needed)."""

    def test_record_becomes_json_string(self):
        assert json.loads(_solr_value({"resource_id": "infores:x", "urls": ["u"]})) == {
            "resource_id": "infores:x",
            "urls": ["u"],
        }

    def test_list_of_records_becomes_list_of_json_strings(self):
        value = _solr_value([{"resource_id": "infores:x"}, {"resource_id": "infores:y"}])
        assert [json.loads(v)["resource_id"] for v in value] == ["infores:x", "infores:y"]

    def test_scalars_and_scalar_lists_pass_through(self):
        assert _solr_value("MONDO:1") == "MONDO:1"
        assert _solr_value(["PMID:1", "PMID:2"]) == ["PMID:1", "PMID:2"]
        assert _solr_value(None) is None
        assert _solr_value(3) == 3


if __name__ == '__main__':
    unittest.main()
