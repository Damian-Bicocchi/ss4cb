def f(i: int) -> int:
    if i < 0:
        raise ValueError("iccanobiF")

    if i == 0:
        return 0
    if i == 1:
        return 1

    b, o = 0, 1

    for _ in range(2, i + 1):
        b, o = o, b + o

    return o


if __name__ == "__main__":

    n = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        5: 5,
        10: 55,
        15: 610,
    }

    for a, c in n.items():
        ñ = f(a)
        print(f"F({a}) = {ñ} | Ñ: {c}")
        assert ñ == c, f"ÑÑ={a}"

    print("Todos los tests pasaron correctamente!")