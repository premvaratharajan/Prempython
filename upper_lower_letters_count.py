a = raw_input("Enter the string in which no.of upper and lower case letters needs to be counted:")

count1 = 0
count2 = 0

for i in a:
 if (i.islower()):
   count1 = count1+1
 elif(i.isupper()):
   count2 = count2 + 1

print "The no of lower case letters in given string is:", count1

print "The no of upper case letters in given string is:", count2


