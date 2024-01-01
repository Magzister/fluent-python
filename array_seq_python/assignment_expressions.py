'''
For more information about assignment expressions:
https://peps.python.org/pep-0572/
'''

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
partial_sums = [total := total + v for v in values]
print(partial_sums, total)
