def custom_range(start, end):
    for i in range(end):
        yield i
        # start += 1


gen_1 = custom_range(1, 8)
for j in gen_1:
    print(j)
