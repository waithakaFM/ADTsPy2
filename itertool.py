# Itertool: provides various ways of handling integrators such as product, combinations, accumulate, groupby and
# infinite iterators

from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# product will computer the cartesian product of input iterable
prod = product(list1, list2)
print(list(prod))

list3 = [1, 2, 3]
list4 = [4]
prod = product(list3, list4, repeat=2)
print(list(prod))

# permutation: All possible ordering of the elements
perm = permutations(list1)
print(list(perm))

# specify the length of permutation
perm = permutations(list1, 2)
print(list(perm))

# combinations: all possible combination with specific length
a = [1, 2, 3, 4, 5]
comb = combinations(a, 2)
print(list(comb))

# combination without reception
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumulate
print("The Accumulate")
myList = [1, 2, 3, 4, 5, 6]
acc = accumulate(myList)  # compute the  sum by default
print(myList)
print(list(acc))

myList1 = [1, 2, 3, 4, 5, 6]
acc = accumulate(myList, func=operator.mul)  # compute the multiplication
print(myList)
print(list(acc))

# compute max
myNumb = [3, 13, 56, 22, 112, 1, 3, 74, 500]
acc1 = accumulate(myNumb, func=max)
print(myNumb)
print(list(acc1))


# groupby
def greater_than_18(x):
    return x > 18


myList2 = [12, 18, 19, 42, 13, 4, 56, 14, 73]
myList2.sort()
groupObj = groupby(myList2, key=greater_than_18)

for key, value in groupObj:
    print(key, list(value))

# using lambda
print("I've used lambda")
groupObj = groupby(myList2, key=lambda x: x > 18)

for key, value in groupObj:
    print(key, list(value))

persons = [{'name': 'Joy', 'age': 16}, {'name': 'John', 'age': 22},
           {'name': 'Emma', 'age': 39}, {'name': 'Mwema', 'age': 22},
           {'name': 'Mkuu', 'age': 39}, {'name': 'Karis', 'age': 9}]

persons.sort(key=lambda x: x['age'])
print("Sort list person in terms of age")
print(persons)

print("Group the dict in terms of age")
groupObj = groupby(persons, key=lambda x: x['age'])
for key, value in groupObj:
    print(key, list(value))

# infinite iterator
for i in count(10):  # infinite loop from 10
    print(i)
    if i == 16:
        break

# cycle
# num = [10, 20, 30, 40]
# for i in cycle(num, 3):  # repeat the list over and over again
#     print(i)
#
#
# for i in repeat(10): # repeat 10 till infinite
#     print(i)

for i in repeat(10, 3):  # repeat 10 3 times
    print(i)