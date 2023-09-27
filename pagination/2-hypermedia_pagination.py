#!/usr/bin/env python3
"""2. Hypermedia pagination"""
import csv
import math
from typing import List, Tuple


class Server:
    """server"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """the datase"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method named get_page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page < 1 or page > total_pages:
            return []
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
       items = len(self.dataset())  # Calculate the total number of items
       current_page = (page - 1) // page_size + 1  # Calculate the current page number
       data = self.dataset()

    # Calculate next_page and prev_page based on page number validity
       next_page = current_page + 1 if current_page < (items + page_size - 1) // page_size else None
       prev_page = current_page - 1 if current_page > 1 else None

       return {
        "page_size": page_size,
        "page": current_page,
        "data": data[(current_page - 1) * page_size:current_page * page_size],
        "next_page": next_page is not None,
        "prev_page": prev_page is not None,
        "total_pages": (items + page_size - 1) // page_size
    }



    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset"""
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)
        start = (page - 1) * page_size
        end = min(start + page_size, total_rows)
        return start, end
