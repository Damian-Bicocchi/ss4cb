def fn_01(v1: int, v2: int) -> int:
    if v1 <= 0 or v2 <= 0:
        raise ValueError(f"v1 and v2 must be strictly positive (> 0). Got: v1={v1}, v2={v2}.")
    while v1 != v2:
        if v1 > v2:
            v1 = v1 - v2
        else:
            v2 = v2 - v1
    return v1