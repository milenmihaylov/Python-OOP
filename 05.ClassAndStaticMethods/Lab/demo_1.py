def create_id_generator():
    x = 1_000_000

    def get_id():
        nonlocal x
        x += 1
        return x

    return get_id
