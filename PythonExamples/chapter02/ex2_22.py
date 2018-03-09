for i in ['red', 'blue', 'green']:
    print(i, end=' ')
print('\nlist->', type(i), end='\n\n')
    
for i in {'one', 'two', 'three'}:
    print(i, end=' ')
print('\nset->', type(i), end='\n\n')

for i in ('house', 'mouse', 'horse'):
    print(i, end=' ')
print('\ntuple->', type(i), end='\n\n')

friends={'eliot':'35', 'sowon':'24', 'jinnam':'45'}
for i in friends:
    print(i, end=' ')
print('\ndict->', type(i), end='\n\n')

for i in friends.items():
    print(i, end=' ')
    print(i[0], ',', i[1])
print('dict->', type(i))
