#!/usr/bin/env python3
"""import async_generator and write a coroutine
async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers"""
import asyncio
import random
from typing import Generator
from importlib import import_module

module_name = '0-async_generator'
module = import_module(module_name)
async_generator = module.async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """coroutine that takes no arguments"""
    return [i async for i in async_generator()]
