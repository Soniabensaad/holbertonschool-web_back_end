#!/usr/bin/env python3
import asyncio
import random
import time
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

def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / n  
