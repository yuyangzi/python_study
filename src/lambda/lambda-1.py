add_one = lambda x: x + 1
print(add_one(2))


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

print(full_name('guido', 'van rossum'))


high_ord_func = lambda x, func: x + func(x)

print(high_ord_func(3, lambda x: x * 3))