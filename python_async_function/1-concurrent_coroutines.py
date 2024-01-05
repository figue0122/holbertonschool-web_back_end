#!/usr/bin/env python3
"""importing wait random from 0-basic_async_syntax"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with max_delay"""
    tasks = [wait_random(max_delay) for i in range(n)]
    # This line creates list of n tasks by spawning wait_random with max_delay.
    delay = []
    for task in asyncio.as_completed(tasks):
        delay.append(await task)
    return delay
