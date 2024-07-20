#!/usr/bin/env python3
"""
    Simple pagination module using simple pagination
    parameters of page and page size
"""


def index_range(page: int, page_size: int) -> tuple:
    """funtion definition"""
    start = 0 if page == 1 else page_size * (page - 1)
    end = page_size if page == 1 else start + page_size
    return (start, end)
