#!/usr/bin/env python3
import asyncio, random

async def wait_random(max_delay:  float = 10.0):
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)
    return delay
    
