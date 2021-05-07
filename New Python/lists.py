# LISTS
import copy

myList =[10,20,30,40,50]
myListList = [["cat", "dog"], ["male", "female"]]
print(myList[4])
print(myListList[1][1])
print(myList[1:4])
print(myList[-1])
myList[1] = 25
print(myList)
myList[:3] = [15,26,35]
print(myList)
del myList[4]
print(myList)
print(len(myList))
mybigList = myList * 3
print(mybigList)
isIn = 26 in mybigList
print(isIn)
print(list(range(20)))
pets = ["cats","dogs","rat"]
for i in range(len(pets)):
    print("index " + str(i) + " in pets is: " + pets[i])

cats = ["fat","brown","cute"]
size, color, looks = cats
print(size, color, looks)

print(cats.index("brown"))
cats.append("greedy")
cats.insert(2, "male")
cats.remove("cute")
print(cats)
mybigList.sort()
print(mybigList)
mybigList.sort(reverse=True)
print(mybigList)
cats.sort(key=str.lower)
print(cats)

def eggs(param1):
    param1.append("yo")

spam = [1,2,3]
eggs(spam)
print(spam)

letters = ["a",
           "b",
           "c"]
moreletters = copy.deepcopy(letters)
moreletters[0] = "Z"
print(letters)
print(moreletters)
