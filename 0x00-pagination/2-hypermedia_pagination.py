#!/usr/bin/env python3
"""
    Simple pagination module using simple pagination
    parameters of page and page size
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """funtion definition"""
    start = 0 if page == 1 else page_size * (page - 1)
    end = page_size if page == 1 else start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function that get page and assert the values b4 use"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        page_index = index_range(page, page_size)
        data = self.dataset()
        return data[page_index[0]:page_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """hypermedia pagination"""
        data = self.get_page(page, page_size)
        total = len(self.dataset())/page_size
        next_page = page + 1 if page < total else None
        prev_page = page - 1 if page > 1 else None
        hyper_dict = {"page_size": page_size,
                      "page": page,
                      "data": data,
                      "next_page": next_page,
                      "prev_page": prev_page,
                      "total_pages": math.ceil(total)
                      }
        return hyper_dict
