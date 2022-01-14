def custom_range(start, end):
    for _ in range(100):
        start += 1
        yield start


gen_1 = custom_range(1, 2)
for j in gen_1:
    print(j)
