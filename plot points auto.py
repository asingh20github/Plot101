import math
import matplotlib.pyplot as plt
import numpy as np
import csv
#b=math.pi
#L = 6; # link length in cms
#theta = (b/10); #theta
for theta in np.arange(18*math.pi/180,36*math.pi/180,math.pi/180):
    for L in np.arange(5.0,6.0,0.2):
        array1=[]
        array2=[]
        for i in range(11,1,-1):
                x_cord = 0
                y_cord = 0
                for j in range(1,13-i):
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
        #array1.insert(11,L*11)
        #array2.insert(11,p)
        
        #To Store points as CSV File
        with open('data.csv','a',newline='') as f:
            thewriter=csv.writer(f)
            
            thewriter.writerow(['L',"Angle"])
            thewriter.writerow([L,theta])
            thewriter.writerow(['X','Y'])
            
            for i in range(0,11):
                thewriter.writerow([array1[i],array2[i]])
        #Plot the points
        plt.plot(array1, array2)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.xlim(xmin=0)
        plt.ylim(ymin=0)
        plt.show()

