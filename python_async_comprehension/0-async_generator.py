#!/usr/bin/env python3
"""coroutine that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator():
    """coroutine that takes no arguments"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
