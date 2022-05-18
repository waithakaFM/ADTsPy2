# collections:(containers for storing data) Counter, namedtuple, orderdict, defaultdict, deque

# counter collection: stores the element as dict keys and counts as dict values

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

myString = "aaabbbbcccdd"
my_counter = Counter(myString)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# check the most common
print("Most common: ", my_counter.most_common(1))
print("The two most common ", my_counter.most_common(2))
print("The most common element ", my_counter.most_common(1)[0][0])

# list with all the different element
print(list(my_counter.elements()))

# namedtuple
print("Namedtuple")
points = namedtuple('points', 'x,y')
pt = points(1, -8)
print(pt)
print(f"value for x = {pt.x} and y = {pt.y}")

# orderded dict: remember the order--old :(
orderedDict = OrderedDict()
orderedDict['a'] = 1
orderedDict['b'] = 2
orderedDict['c'] = 3
orderedDict['d'] = 4
print(orderedDict)

# defaultDict: have default value if the key not set yet
dd = defaultdict(int)
dd['a'] = 1
dd['b'] = 2
dd['c'] = 3
print(dd['c'])
print("Default key of value 'd'", dd['d'])

# Deque: double ended queue, used to add or remove element from both end
dQ = deque([1, 2, 3, 4, 5])
dQ.append('a')
dQ.append('b')
print(dQ)

dQ.appendleft('leftside')
print(dQ)

# remove element
dQ.pop()
print(dQ)

dQ.popleft()
print(dQ)

dQ.extend([11, 12, 13, 20])
print(dQ)

dQ.extendleft([0, -1, -2])
print(dQ)

# rotate elements
dQ.rotate(1)
print(dQ)

dQ.rotate(2)
print(dQ)

dQ.rotate(-1) # rotate to the left
print(dQ)