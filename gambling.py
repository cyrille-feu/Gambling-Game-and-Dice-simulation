import numpy as np             #imports the numpy package
b={}                           #We create an empty dictionary that will store the names and scores of the players
t=[]                           #W e crate a list to store only the names of the players
for i in range (1,3):          
	c=str(input("player %d enter your name:     "%(i)))
	b.update({c:0})                                       # This loop  introduces the two players
	t.append(c)
	
#print(b)
#d=list(b)
k=0
while(b[t[0]] != 6 and b[t[1]] != 6):          #This loop ensures that as long as the scores of each player is different from 6 it performs the operation given by 'e'
		e=np.random.randint(1,7)               # This generates a random number between 1 and 6    
		print("the result of %s is %d"%(t[0],e)) #This prints the result of the first player
		b[t[0]]=e                                # This attributes a score to the first player
		if(e!=6):                                #Here we test the score. If the score of the first player is different from 6 then the second player plays otherwise the first player wins
			e=np.random.randint(1,7)
			print("the result of %s is %d"%(t[1],e))   #This prints the result of the second player
			b[t[1]]=e
			if(e==6):                                    #Here we test the score of the second player. If the score is equal to 6 we have a winner otherwise the first player will play again
				k=k+1
				print("%s is the winner after %d attempts"%(t[1],k))
			else:
				k=k+1	
		else:
			k=k+1
			print("%s is the winner after %d attempts"% (t[0],k))
			
			
			

		


