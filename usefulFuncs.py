import numpy as np

def check_float(val: str):
    try:
        float(val)
        return True
    except ValueError:
        return False
    
def check_int(val: str):
    try:
        int(val)
        return True
    except ValueError:
        return False