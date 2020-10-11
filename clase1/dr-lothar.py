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


x = int(input("Number for Dr Lothar: "))
solution = dr_lothar(x)
print(solution)
