#!/usr/bin/env python3
"""
Module to measure the runtime of parallel async comprehensions.
"""
import asyncio
import time

# Import async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and
    measures the total execution time.
    """
    start_time = time.perf_counter()

    # Schedule four calls to async_comprehension to run concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
