#Collection of items of same or different datatypes
#Mutable

def listMethods(name):
    print('Length', ':', len(name), '\n')
    print('Min Max', ':', min(name), max(name), '\n')
    print('Concat', ':',  name + name, ':', '\n')
    name.append('james')
    print('Append', ':', name, '\n')
    print('Pop', ':',  name.pop(), '\n')
    name.insert(0, 'james')
    print('Inserted', ':',  name, '\n')
    print('Slice', ':',  name[1:-1], '\n')
    del name[0]
    print('Delete', ':',  name, '\n')
    print('Search', ':',  name.index('erick'), '\n')
    print('Membership', ':',  'erick' in name, '\n')
    print('Sort', ':',  sorted(name), '\n')
    print('Reverse', ':',  list(reversed(name)), '\n')
    pass

listMethods(['erick', 'juma'])