# Contains unsorted, positive and negative integers.
#elements = [100, 200, 0, -100]

# Sort from low to high.
#elements.sort()
#print(elements)

l = [1, 2, 10,-1, 0, 9, 7, 8]

l.sort()

print l

#print reversed(sorted(l))


elements = [22, 333, 0, -22, 1000]

# Use a reversed, sorted view: a descending view.
#view = reversed(sorted(elements))
elements.sort(reverse=True) 

print elements
