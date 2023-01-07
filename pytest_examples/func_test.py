def our_func(a, b, c) -> int:
    if a >= b:
        return a - b + c
    return a + b + c


'''
case 1 : a = 10 b = 5 c = 3 => 8
case 2 : a = 5 b = 6 c = 2 => 12
case 3 : a = 5 b = 2 c = 2 => 2
case 3 : a = 100 b = 200 c = 0 => 300
'''


test_data = [(10, 5, 3, 8),
             (5, 6, 2, 13),
             (5, 5, 2, 2),
             (100, 200, 0, 300)]

errors = []

for data in test_data:
    a, b, c, r = data[:]
    try:
        assert our_func(a, b, c) == data[-1], f'Function works incorrectly with data {a=}' \
                                             f' {b=},' \
                                             f' {c=} return {r=}'
    except AssertionError as e:
        errors.append(e)

assert not errors, f'Errors are : {errors}'