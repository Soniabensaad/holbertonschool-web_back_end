#!/usr/bin/env python3
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine"""
    delay = random.uniform(0, float(max_delay))

    await asyncio.sleep(delay)
    return delay

"""Let's execute multiple
coroutines at the same time with async"""

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
