#!/usr/bin/env python3
"""
Səhifələmə üçün köməkçi funksiya modulu.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Səhifə və səhifə ölçüsünə əsasən başlanğıc və son indeksləri qaytarır.

    Args:
        page (int): Səhifə nömrəsi (1-dən başlayır).
        page_size (int): Hər səhifədəki element sayı.

    Returns:
        Tuple[int, int]: (start_index, end_index) şəklində tuple.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
