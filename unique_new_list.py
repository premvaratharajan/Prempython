from operator import itemgetter

a = [1, 2, 3, 4, 5]
list = itemgetter(0,2,4)(a)

print list
