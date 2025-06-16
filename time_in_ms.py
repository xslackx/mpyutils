import time

def in_ms() -> int:
    return time.ticks_ms()

def diff_in_ms(t1) -> int: 
    return time.ticks_diff(in_ms(), t1)