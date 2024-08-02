def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 'строка',False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5, 'apple', False]
values_dict = {'a': 7, 'b': 'urban', 'c': False }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['pear', False]
print_params(*values_list_2, 42)
