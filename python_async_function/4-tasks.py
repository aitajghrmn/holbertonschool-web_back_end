#!/usr/bin/env python3
"""Execute multiple tasks concurrently using task_wait_random."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return delays in ascending order."""
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
