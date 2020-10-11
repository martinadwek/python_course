def dr_lothar(number: int) -> int:
    if number <= 0:
        raise ValueError("Input must be > 0")
    steps = 0
    while number != 1:
        steps += 1
        if not number % 2:
            number = number / 2
        else:
            number = number * 3 + 1
    return steps


def dr_lothar_rec(number: int, steps: int) -> int:
    if number <= 0:
        raise ValueError("Input must be > 0")
    if number == 1:
        return steps
    if not number % 2:
        return dr_lothar_rec(int(number / 2), steps + 1)
    else:
        return dr_lothar_rec(number * 3 + 1, steps + 1)


# x = int(input(""))
# solution = dr_lothar(x)
# print(solution)
