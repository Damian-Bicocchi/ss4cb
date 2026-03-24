def dbdbdb(b: list[int], db: bool = True) -> list[int]:
    d = b.copy(); dbdbdbdbdb = len(d)
    def dbdbd(dbdbdbdbdbd: int, dbdbdbd: int):
        dbdb = dbdbdbd; dbdbdbdb = 2 * dbdbdbd + 1; dbd = 2 * dbdbdbd + 2  
        if db:
            if dbdbdbdb < dbdbdbdbdbd and d[dbdbdbdb] > d[dbdb]:
                dbdb = dbdbdbdb
            if dbd < dbdbdbdbdbd and d[dbd] > d[dbdb]:
                dbdb = dbd
        else:
            if dbdbdbdb < dbdbdbdbdbd and d[dbdbdbdb] < d[dbdb]:
                dbdb = dbdbdbdb
            if dbd < dbdbdbdbdbd and d[dbd] < d[dbdb]:
                dbdb = dbd
        if dbdb != dbdbdbd:
            d[dbdbdbd], d[dbdb] = d[dbdb], d[dbdbdbd]
            dbdbd(dbdbdbdbdbd, dbdb)
    for dbdbdbdbd in range(dbdbdbdbdb // 2 - 1, -1, -1):
        dbdbd(dbdbdbdbdb, dbdbdbdbd)
    for dbdbdbdbd in range(dbdbdbdbdb - 1, 0, -1):
        d[dbdbdbdbd], d[0] = d[0], d[dbdbdbdbd]
        dbdbd(dbdbdbdbd, 0)
    return d

