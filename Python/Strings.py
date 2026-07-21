#Sequence of chars enclosed with single or double quotes

#Escaping double or single quotation marks
msg = 'It\'s a sunny day today'

#Immutable datatypes cannot be modified once declared

name = 'erick juma'
name[:8:2] #step

def stringMethods(name):
    """
    This function will cover basic string operations
    """
    print('Lower', ':', name.lower(), '\n')
    print('Upper', ':', name.upper(), '\n')
    print('Is upper', ':', name.isupper(), '\n')
    print('Is lower', ':', name.islower(), '\n')
    print('Capitalize', ':', name.capitalize(), '\n')
    print('Title', ':', name.title(), '\n')
    print('Count occurence', 'j', ':', name.count('j'), '\n')
    print('Count start of substring', 'ju', ':', name.find('ju'), '\n')
    print('Strip start and end space', ':', ' juma '.strip(), '\n')
    print('Split string', ':', 'ju, ma'.split(','), '\n')
    print('Join erick juma', ':', ','.join([i for i in name.split()]), '\n')
    print('Name startswith', ':', name.startswith('e'), '\n')
    print('Name endswith', ':', name.endswith('e'), '\n')
    print('Contains substring erick', ':', 'erick' in name, '\n')
    print('Skip every second element', ':', name[::2], '\n')
    print('Skip every second element starting from the end', ':', name[-1:-4:-2], '\n')

stringMethods('erick juma')
