def is_valid_int(n):
    return True if n.isdigit() and int(n) > 0 else False


def print_line(i, n):
    print(f"{' '.join(['*' for _ in range(i + 1)]):^{2 * n - 1}s}")


def print_rhombus(n: int):
    for i in range(n):
        print_line(i, n)
    for j in range(n - 1, -1, -1):
        print_line(j, n)


def print_triangle(n):
    for i in range(n):
        print_line(i, n)


num = input()
if is_valid_int(num):
    print_triangle(int(num))
