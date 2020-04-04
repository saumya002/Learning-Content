import pandas as pd 
from matplotlib import pyplot as plt
data=pd.read_csv('data.csv')
l1= data[data.Label == 1]
l2= data[data.Label == 2]
plt.plot(l1.q1,l1.q2,'o')
plt.plot(l2.q1,l2.q2,'o')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

