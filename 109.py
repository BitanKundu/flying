diceresult=[]
for i in range(0,1000):
 dice1=random.randint(1,6)
 dice2=random.randint(1,6)
 diceresult.append(dice1+dice2)
import statistics
mean=sum(diceresult)/len(diceresult)
