#!/usr/bin/env python3
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> List[float]:
    tasks = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*tasks)
    return results
