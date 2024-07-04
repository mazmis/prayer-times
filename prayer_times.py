

def date_to_julian(y: int, m: int, d: int):
    return d - 32075 + 1461 * (y + 4800 + (m - 14)/12)/ 