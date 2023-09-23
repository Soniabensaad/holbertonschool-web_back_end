#!/usr/bin/env python3

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    tasks = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*tasks)
    return results
