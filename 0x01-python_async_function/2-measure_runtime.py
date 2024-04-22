#!/usr/bin/env python3
''' Create a measure_time function with integers n and max_delay as arguments '''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' This returns execution time for wait_n given n and max_delay. '''
    time_0 = time()
    run(wait_n(n, max_delay))
    time_1 = time()
    elapsed_time = time_1 - time_0
    return elapsed_time / n
