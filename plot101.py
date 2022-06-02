import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
b=math.pi
L = 5; # link length in cms
theta = (b/10); #theta
m=0
n=0
p=0
array1=[]
array2=[]
i=11
for i in range(11,1,-1):
        x_cord = 0
        y_cord = 0
        j=1
        k=13-i
        for j in range(1,k):
            if j == 12-i:
                x_cord = x_cord+((L/2)*(math.cos((j-1)*theta)))
                y_cord = y_cord+((L/2)*(math.sin((j-1)*theta)))
            else:
                x_cord = x_cord+L*(math.cos((j-1)*theta))
                y_cord = y_cord+L*(math.sin((j-1)*theta))
            
            m= (L*11)-(x_cord)
            n= y_cord
            j=j+1
    
        array1.append(m-((L/2)*math.cos(((11-i)*theta))))
        array2.append(n+((L/2)*math.sin(((11-i)*theta))))
        p=n+((L/2)*math.sin(((11-i)*theta)))

array1.insert(0, L*11)
array2.insert(0, 0)
array1.insert(11,55)
array2.insert(11,p)
a=np.array([array1,array2])
print(a)
DF = pd.DataFrame(a)
DF.to_csv("data1.csv")

plt.plot(array1, array2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.show()
