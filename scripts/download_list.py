"""Script to download the list of black-listed websites from

https://github.com/MassMove/AttackVectors/raw/master/LocalJournals/fake-local-journals-list.txt
"""
from urllib import request


URL = ('https://github.com/MassMove/AttackVectors/raw/master/'
        'LocalJournals/fake-local-journals-list.txt')
print(f'Downloading fake local journals list from {URL}')

response = request.urlopen(URL)
print('RESPONSE:', response)
print('URL     :', response.geturl())

headers = response.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)

data = response.read().decode('utf-8')
data = data.split('\n')
del data[0]
print('LENGTH  :', len(data))
print('DATA    :') # 1st 10 entries
print('---------')
print('\n'.join(data[:10]))


data_to_write = str.encode('\n'.join(data))

with open('list.txt', 'wb') as f:
    f.write(data_to_write)
