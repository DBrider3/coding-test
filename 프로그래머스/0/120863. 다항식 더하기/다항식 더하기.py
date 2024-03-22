def solution(polynomial):
    trans = polynomial.split(' + ')
    number = 0
    x = 0
    for t in trans:
        if t.isdigit():
            number += int(t)
        else:
            if len(t) == 1:
                x += 1
            else:
                x += int(t[:-1])

    if x == 0:
        return f"{number}"
    if x == 1:
        return f"x + {number}" if number != 0 else "x"
    else:
        return f"{x}x + {number}" if number != 0 else f"{x}x"
        