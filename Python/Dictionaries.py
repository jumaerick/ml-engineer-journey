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
# print('1234x'.isnumeric())



def word_search(doc_list, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    matches = {word : [] for word in keywords}
    for word in keywords:
        print('here')
        index = word_search(doc_list, word)
        matches.update({word : index})

    return matches

doc_list=['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?']

print(multi_word_search(doc_list, ['casino', 'they']))
