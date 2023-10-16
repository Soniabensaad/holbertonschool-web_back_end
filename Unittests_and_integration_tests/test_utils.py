#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from utils import access_nested_map
from parameterized import parameterized, parameterized_class

class TestAccessNestedMap(unittest.TestCase):
    """ unit test"""
    @parameterized.expand([
    ({"a": 1}, ("a",), 1),
    ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ({"a": {"b": 2}}, ("a", "b"), 2)
])


    def test_access_nested_map(self, nested_map, path, result):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), result)


    @parameterized.expand([
    ({}, ("a",), "Key 'a' not found in the nested_map"),
    ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested_map")
])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """test exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(result, e.exception)
