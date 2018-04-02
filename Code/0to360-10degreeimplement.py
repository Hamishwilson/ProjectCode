import csv
import matplotlib.pyplot as plt

data = []     #list for the data
degreeOfRotation = 0    #set initial degree of rotation at 0
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
            if data[-1][-1] == 'H' and temp[4] == 'V':     #for when the last value was a H and now V set rotation at 180
                degreeOfRotation = 180
                flip = False
            else:
                if temp[4] == 'H':                         #For horizontal
                    if degreeOfRotation == 0:              #if rotation goes to zero will switch to false
                        flip = False
                    elif degreeOfRotation == 360:          #if rotation becomes 360 will switch to false
                        flip = True                        #can be set to 360 depending whether full rotation during experiment
                    if not flip:                           # If flip == false
                        degreeOfRotation += 10
                    elif flip:                             # If flip == true
                        degreeOfRotation -= 10

                if temp[4] == 'V':                          #for vertical
                    if degreeOfRotation == 0:             #if rotation goes to 180 will switch to false
                        flip = False                        #can be set to 0 depending whether full rotation during experiment
                    elif degreeOfRotation == 540:           #if the rotation is 540 will switch to true
                        flip = True

                    if not flip:                            # If flip == false
                        degreeOfRotation += 10
                    elif flip:                              # If flip == true
                        degreeOfRotation -= 10
        if lengthofdata > 0:                                #any degree between 360-540 will be made to 0-180
            if degreeOfRotation > 360:
                degreeOfRotation -= 360
        temp.append(degreeOfRotation)                       #adds the degree of rotation to the temp

        temp2 = [temp[1], temp[3], temp[5], temp[4]]        # List to hold needed elements
        #temp2.append

        data.append(temp2)                                  #List to hold final variables
        lengthofdata += 1

setV_x = []
setV_y = []
setH_x = []
setH_y = []

for i in range(0, len(data)):                   #splits the data up into v and H
    if data[i][3] == 'V':
        setV_x.append(data[i][2])               #the degree at which data was taken for V
        setV_y.append(data[i][1])               #the displacement for V
    elif data[i][3] == 'H':
        setH_x.append(data[i][2])               #the degree at which data was taken for H
        setH_y.append(data[i][1])               #the displacement for H

fig = plt.figure()

u = setV_x                                 #used to set limits in the graph
v = setV_y
umin = min(u)
umax = max(u)
vmin = min(v)
vmax = max(v)

v1 = len(v)/8                                     #used this to set the Y axis before cluttered with all data points
v2 = 2*(len(v)/8)                                  # I did this otherwise there was every data point on the y axis
v3 = 3*(len(v)/8)                                   # although this means y axis still not scaled
v4 = 4*(len(v)/8)
v5 = 5*(len(v)/8)
v6 = 6*(len(v)/8)
v7 = 7*(len(v)/8)
v8 = len(v)

x = setH_x                                         #used to set limits in the graph
y = setH_y
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

y1 = len(y)/8                                      #used this to set the Y axis before cluttered with all data points
y2 = 2*(len(y)/8)
y3 = 3*(len(y)/8)
y4 = 4*(len(y)/8)
y5 = 5*(len(y)/8)
y6 = 6*(len(y)/8)
y7 = 7*(len(y)/8)
y8 = len(y)

ax1 = fig.add_subplot(211)
ax1.scatter(x, y)
ax1.set_xlim(0, 360)
ax1.set_ylim(ymin, ymax)
ax1.set_xlabel('degree of displacement/degree')
ax1.set_ylabel('Horizontal_displacement/mm')
plt.yticks([y1, y2, y3, y4, y5, y6, y7, y8])

ax2 = fig.add_subplot(212)
ax2.scatter(u, v)
ax2.set_xlabel('degree of displacement/degree')
ax2.set_ylabel('Vertical_displacement/mm')
ax2.set_ylim(vmin, vmax)
ax2.set_xlim(0, 360)
plt.yticks([v1, v2, v3, v4, v5, v6, v7, v8])

fig.subplots_adjust(hspace=0.3)                         #used this to spread the graphs out
print(data)
plt.show()
fig.savefig('displacement.png', bbox_inches='tight')
