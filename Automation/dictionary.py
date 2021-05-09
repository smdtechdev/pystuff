#dictionariess
#test

mydict = {'size':'fat', 'color':'black'}
print(mydict['size'])

print('size' in mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())

for k in mydict.keys():
    print(k)

for i,j in mydict.items():
    print(i,j)

print(mydict.get('color', 0))
print(mydict.get('gender', 0))

mydict.setdefault('gender', 'male')
print(mydict)

message = 'This is a random bit of text'
count = {}

for chars in message.upper():
    count.setdefault(chars, 0)
    count[chars] = count[chars] + 1

print(count)