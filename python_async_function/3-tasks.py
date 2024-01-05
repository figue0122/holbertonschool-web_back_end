#!/usr/bin/env python3
"""function that takes an integer"""
import asyncio
from importlib import import_module

# Importing the module dynamically
module_name = '0-basic_async_syntax'
module = import_module(module_name)
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function that takes an integer"""
    return asyncio.create_task(wait_random(max_delay))
