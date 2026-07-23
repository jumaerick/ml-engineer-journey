#DS for mapping key value pairs

dic = dict()

dic.update({'name': 'erick', 'age': 30})

# for key, val in list(dic.items()):
#     print(key, val)

# del dic

dic['city'] = 'Nairobi'

# sorting by keys
print(dict(sorted(dic.items())))

# sorting by values
dic_two = {'a': 10, 'b': 5, 'd': 11}

print(dict(sorted(dic_two.items(), key = lambda item : item[1])))

print(dict(sorted(dic_two.items(), key = lambda item : item[1], reverse=True)))

print(dic_two['a'])

print( 'a' in dic_two)

print(len(dic_two))

del dic_two['a']

# def is_valid_zip(zip_code):
#     """Returns whether the input string is a valid (5 digit) zip code
#     """
#     valid = []
#     if len(zip_code) == 5:
#         for i in zip_code:           
#             try:
#                 valid.append(int(i))
#             except:
#                 return False
#     return len(valid) == 5

def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()

# print(is_valid_zip('1234'))/
print('1234x'.isnumeric())