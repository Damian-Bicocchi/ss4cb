def fn_01(v1: int, v2: int) -> int:
    while v1 != v2:
        if v1 > v2:
            v1 = v1 - v2
        else:
            v2 = v2 - v1
    return v1