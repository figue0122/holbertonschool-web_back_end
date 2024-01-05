#!/usr/bin/env python3
"""Measures the runtime of an async comprehension"""
import asyncio
import typing

wait_random = __import__('2-measure_runtime').wait_random

async def measure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of an async comprehension"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    end = asyncio.get_event_loop().time()
    return (end - start) / n
