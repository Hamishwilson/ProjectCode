import csv

import numpy as np
import matplotlib.pyplot as plt

data = []
degreeOfRotation = 0
flip = False
lengthofdata = 0
with open('../Data/DATA.csv','r' ) as csvfile: #Used to open csv file
    reader = csv.reader(csvfile) #Used to read csv file
    for row in reader:#Used to read each line
        temp = [] #List to hold all elements in line
        for element in row:
            temp.append(element)

        if temp[1] == '1':
            temp.append('H')
        elif temp[1] == '2':
            temp.append('V')

        if lengthofdata > 0:
            if data[-1][-1] == 'H' and temp[4] == 'V':
                degreeOfRotation = 180
            else:
                if temp[4] == 'H':
                    if degreeOfRotation == 0:
                        flip = False
                    elif degreeOfRotation == 180:
                        flip = True

                    if not flip:  # If flip == false
                        degreeOfRotation += 2
                    elif flip:  # If flip == true
                        degreeOfRotation -= 2

                if temp[4] == 'V':
                    if degreeOfRotation == 180:
                        flip = False
                    elif degreeOfRotation == 360:
                        flip = True

                    if not flip:  # If flip == false
                        degreeOfRotation += 2
                    elif flip:  # If flip == true
                        degreeOfRotation -= 2

        temp.append(degreeOfRotation)

        # List to hold needed elements
        temp2 = [temp[1], temp[3], temp[5], temp[4]]
        #temp2 = [temp[3], temp[5]]
        # temp2.append

        data.append(temp2)#List to hold final variables
        lengthofdata += 1


csvfile.close() #Close

setV_x = []
setV_y = []

setH_x = []
setH_y = []

for i in range(0,len(data)):
    if data[i][3] == 'V':
        setV_x.append(data[i][1])
        setV_y.append(data[i][2])
    elif data[i][3] == 'H':
        setH_x.append(data[i][1])
        setH_y.append(data[i][2])

fig = plt.figure(1)
x = setH_x
y = setH_y
u = setV_x
v = setV_y
plt.subplot(211)
plt.plot(x, y)

plt.subplot(212)
plt.subplot(u, v)

#plt.savefig('dataofdisplacement.png')
plt.show()
print(setH_x)
print(data[0])

print(data[0][0])

