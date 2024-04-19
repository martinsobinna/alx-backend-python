#!/usr/bin/env python3
''' takes a float multiplier as argument and returns a function that multiplies a float by multiplier '''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' return function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier
