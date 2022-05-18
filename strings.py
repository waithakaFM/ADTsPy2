from timeit import default_timer as timer

# Strings: ordered, immutable, text representation

# declaration
myString = "Hello Frank!"
print(myString)
myString1 = """Hello
I'm fine thank you!"""
print(myString1)

# access characters
char = myString[1]
print(char)
substring = myString1[1:5]
print(substring)

# reverse the string
substring1 = myString[::-1]
print(substring1)

# concatenate
sentence = myString + " " +myString1
print(sentence)

# loop through the string
for c in myString:
    print(c)

# check a character
if 'f' in myString:
    print("yes")
else:
    print("no")

# remove the white space
myString2 = "    franco313mwas@gmail.com   "
print(myString2)
myString2 = myString2.strip()
print(myString2)

# convert every character to uppercase
print(myString2.upper())
print(myString2.lower())
print(myString2.startswith('f'))
print(myString2.endswith('o'))

# find the index of the character
print("Index of 'o' in hello")
print(myString.find('o'))
print("Character 'p' not found in myString, returns -1")
print(myString.find('p'))

# count the instance of a char
print("How many 'l' are found in hello word: ", myString.count('l'))

# replace a string
print(myString.replace('Frank', 'Judy'))

# convert a string to list
myString3 = "I love tech food and money"
myList = myString3.split() # default argument is space, it splint words whenever there is space
print(myList)

myString4 = "I love,tech,food,money"
myList1 = myString4.split(",")
print(myList1)

# convert a list to a string
myList2 = ["Franco", "313", "Mwas", "@gmail.com"] * 100000

# bad, expensive method
start = timer()
newMyEmail = ''
for i in myList2:
    newMyEmail += i
stop = timer()
print(stop-start)

# correct method
start = timer()
myEmail = ''.join(myList2)
stop = timer()
print(stop-start)

myName = ["Franco", "Mwas", "from Kenya"]
newString = ' '.join(myName) # if you put spaces in between quotes the words separates
print(newString)

# format strings: with %, .format(), f-string
var = " Njoki"
myString5 = "the varible is %s"%var # after % we put the data type Old:(
print(myString5)

var2 = 3.12345
myVar = "The variable is {}".format(var2)
print(myVar)

myVar2 = "The variable is {:.2f}".format(var2)
print(myVar2)

myVar3 = "The variable is {} and {}".format(var2, var)
print(myVar3)

# newer and more efficient format
myVar4 = f"The variable is {var} and {var2*2}"
print(myVar4)
