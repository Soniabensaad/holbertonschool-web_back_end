#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page, page_size):
    """should return a tuple of size"""
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
