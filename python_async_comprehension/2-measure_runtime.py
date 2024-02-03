#!/usr/bin/env python3
"""coroutine that will execute four times in
parallel
should measure the total runtime
and return it"""
import asyncio
import time
from importlib import import_module

module_name = '1-async_comprehension'
module = import_module(module_name)
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute four times in
    parallel
    should measure the total runtime
    and return it"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
