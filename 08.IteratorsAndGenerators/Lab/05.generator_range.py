def genrange(start, end):
    return (i for i in range(start, end + 1))


print(list(genrange(1, 10)))
