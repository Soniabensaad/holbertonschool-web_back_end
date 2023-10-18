#!/usr/bin/env python3
""" Module for testing client """
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
import json
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """the client.GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, input_org, mock_get_json):
        """Parameterize and patch as decorators"""
        class_test = GithubOrgClient(input_org)
        class_test.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{input_org}")
