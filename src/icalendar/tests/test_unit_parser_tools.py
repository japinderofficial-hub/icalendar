import unittest

from icalendar.parser_tools import _data_encode, _to_unicode, _from_unicode


class TestParserTools(unittest.TestCase):
    def test_parser_tools_to_unicode(self):
        self.assertEqual(_to_unicode(b"spam"), "spam")
        self.assertEqual(_to_unicode("spam"), "spam")
        self.assertEqual(_to_unicode(b"spam"), "spam")
        self.assertEqual(_to_unicode(b"\xc6\xb5"), "\u01b5")
        self.assertEqual(_to_unicode(b"\xc6\xb5"), "\u01b5")
        self.assertEqual(_to_unicode(b"\xc6\xb5", encoding="ascii"), "\u01b5")
        self.assertEqual(_to_unicode(1), 1)
        self.assertIsNone(_to_unicode(None))

    def test_parser_tools_from_unicode(self):
        self.assertEqual(_from_unicode("\u01b5", encoding="ascii"), b"\xc6\xb5")

    def test_parser_tools_data_encode(self):
        data1 = {
            "k1": "v1",
            "k2": "v2",
            "k3": "v3",
            "li1": ["it1", "it2", {"k4": "v4", "k5": "v5"}, 123],
        }
        res = {
            b"k3": b"v3",
            b"k2": b"v2",
            b"k1": b"v1",
            b"li1": [b"it1", b"it2", {b"k5": b"v5", b"k4": b"v4"}, 123],
        }
        self.assertEqual(_data_encode(data1), res)
