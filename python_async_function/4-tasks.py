#!/usr/bin/env python3
"""Let's execute multiple
coroutines at the same time with async"""


import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine"""
    delay = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrency."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n except
    task_wait_random is being called."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
