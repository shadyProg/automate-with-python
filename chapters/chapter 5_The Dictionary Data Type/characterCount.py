import pprint
message = 'It was a bright cold day in April, and the clocks were striking \
thirteen.'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character]+=1

newList=list(count.keys())
newList.sort()
print(newList)
print()
print()
print()
for key in newList:
    print("key: "+key+" value is  "+ str(count[key]))
print()
print()


pprint.pprint (count)