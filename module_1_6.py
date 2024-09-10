my_dict = {'Marina': 1965, 'Nadezhda': 1995, 'Galina': 1983, 'Maria': 2001}
print(my_dict)
print(my_dict.get('Marina'))
print(my_dict.get('Anzhela'))
my_dict.update({'Mihail': 1999, 'Ekaterina': 1964})
a = my_dict.pop('Galina')
print(a)
print(my_dict)




my_set = {'Maria',2,3,4, True, 2,3,'Maria'}
print(my_set)
my_set.update({595, 'Katya',(12,31)})
my_set.discard('Maria')
print(my_set)