#!/usr/bin/env python3
"""
Module for async comprehensions.
"""
from typing import List

# Import the async_generator coroutine from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator and returns them.
    """
    return [i async for i in async_generator()]
