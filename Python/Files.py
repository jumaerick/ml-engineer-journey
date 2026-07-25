#open read write readwrite append
import os

filename = 'test.txt'
#open read write readwrite append

filename = 'test.txt'
print('hapa')

with open(os.path('./'+ filename) as file):
    print('hello')
    file.write('hello')
