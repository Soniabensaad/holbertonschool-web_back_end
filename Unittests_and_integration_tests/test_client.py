#!/usr/bin/env python3
""" Module for testing client """
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
import json
from unittest.mock import patch, PropertyMock, Mock


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Test more public repos """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()
