#!/usr/bin/env python3
import asyncio, random

async def wait_random(max_delay: int = 10):
    delay = random.randint(0, max_delay)

    await asyncio.sleep(delay)
    return delay
