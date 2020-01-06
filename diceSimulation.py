import matplotlib.pyplot as plt
import numpy as np


c=list(np.random.randint(1,7,100))      #This generates randomly a list of numbers between 1 and 6 after throwing a dice 100 times
b=c.count(6)                            # This counts the number of times 6 appears in our list c
print(b)
l1=[]                            #l1 creates an empty list to stores the number of time 6 appears 
for i in range(1,1001):          #This loop repeats the process 1000times and count the number of times 6 
	c=list(np.random.randint(1,7,100))
	b=c.count(6)
	l1.append(b)
plt.figure(figsize=(15,15))            
plt.hist(l1,color=['blue'])  # This plots a histogram of distribution of 6
plt.title('Histogram of distribution of the number of times face number 6 appear')
plt.xlabel('number of time we obtain face 6 in a process')
plt.ylabel('number of time that number appear after 1000 repeating process')
plt.show()

l1.sort()
tt1=[]                        # empty list to save number of time we obtain face 6 in a process
tt=[]                         # empty list to save number of time that number appear after 1000 repeating process
for i in l1:                  # this loop fills tt1 and tt
    if i not in tt1:
        tt1.append(i)
        tt.append(l1.count(i))

                # to arange elements in tt1 in ascending order
i =0
while i<len(tt):
    print(tt1[i], "*"*tt[i])
    i = i+1
