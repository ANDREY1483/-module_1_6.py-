my_dict = {'Denis': 1998, 'Andrey': 1989, 'Anet': 2000}
print(my_dict)
print(my_dict ['Denis'])
print(my_dict.get ('Ket'))
my_dict.update({'Sergey': 2009, 'Dasha': 2013})
print(my_dict)
a = my_dict.pop('Andrey')
print(a)
print(my_dict)
#
my_set = {1, 4, 2, 4, 1, 'Book', 34.5}
print(my_set)
my_set.add(9)
my_set.add('Anet')
print(my_set)
my_set.discard('Book')
print(my_set)