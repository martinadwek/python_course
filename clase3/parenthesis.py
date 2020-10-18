import string

PARENTHESIS_RELATION = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def parenthesis_checker(text: string) -> bool:
    stack = list()
    for letter in text:
        if letter in {"(", "{", "["}:
            stack.append(letter)
        elif letter in {")", "}", "]"}:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if PARENTHESIS_RELATION.get(last) != letter:
                return False
    return len(stack) == 0



# x = input()
# solution = parenthesis_checker(x)
# print(solution)