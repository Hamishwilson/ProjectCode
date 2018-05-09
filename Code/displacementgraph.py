import csv
import matplotlib.pyplot as plt
import os

data = []
print('ensure data is called DATA in the csv format and placed in same directory as code')
dpr = eval(input("enter the degree of rotation per reading: "))
tdr = eval(input("enter the total degree of rotation travelled in experiment: "))
vdr = tdr + 180
#this is used for the tracking of the degree for vertical


xv = 360 - tdr #lower bound of vertical readings
degreeOfRotation = 0
flip = False
lengthofdata = 0
script_path = os.path.abspath(__file__)
#find the directory of the code
script_dir = os.path.split(script_path)[0]
#go back in directory to find the folder the code is in
rel_path = "DATA.csv"
#add file name of code
abs_file_path = os.path.join(script_dir, rel_path)
#add firectory to file nsme
print(abs_file_path)
#print director
with open(abs_file_path,'r' ) as csvfile:
    #Used to open csv file
    reader = csv.reader(csvfile)
    #Used to select a row  csv file
    for row in reader:
        # for loop to add data to temp
        temp = []
        for element in row:
            temp.append(element)

        if temp[1] == '1':
            # if channel ID is 1 add H if 2 add V
            temp.append('H')
        elif temp[1] == '2':
            temp.append('V')

        temp.append(degreeOfRotation)
        temp2 = [temp[1], temp[3], temp[4]]
        # list to hold the data


        data.append(temp2)
        # List to hold final variables
        lengthofdata += 1
datax = []
datau = []
datah = []
datav = []
for i in range(0, len(data)):
    #for loop to split the data on whether  it is ID is 1 or 2
    if data[i][0] == '1':
        datah.append(data[i][1])
    elif data[i][0] == '2':
        datav.append(data[i][1])

for i in range(0, len(datah)):
    #for loop to set the degree of rotation for the data of horizontal
    datax.append(degreeOfRotation)
    #adds the degree of freedom in for loop to datax
    if degreeOfRotation == 0:
        #used to flip the direction when it hits 0
        flip = False
    elif degreeOfRotation == tdr:
        #used to flip the reflection once the degree of rotation is equal to max rotation distance
        flip = True

    if not flip:  # If flip == false
        degreeOfRotation += dpr
        #if flip false adds the degree of rotation per step
    elif flip:  # If flip == true
        degreeOfRotation -= dpr
        #if flip true takes away the degree of rotation per step

degreeOfRotation = 180
#set the initial degree of freedom for the vertical
flip = True
#set the flip to true to start
for i in range(0, len(datav)):
    datau.append(degreeOfRotation)
    # adds the degree of freedom in for loop to datau
    if degreeOfRotation == 180:
        if flip:
            flip = False
        elif not flip:
            flip = True
            #this if statement changes the flip once vertical equals 180
    elif degreeOfRotation == vdr:
        flip = True
        # this if statement makes flip true if the vertical degree of rotation equals the total degree of rotation
    if not flip:  # If flip == false
        degreeOfRotation += dpr
        #add the degree of rotation per step
    elif flip:  # If flip == true
        degreeOfRotation -= dpr
        # take the degree of rotation per step
y = [float(x)for x in datah]
#make datah into list of floats
v = [float(x)for x in datav]
#make datah into list of floats
for i in range(0, len(datau)): #for statement use to set angles betweeen 0-360
    if 360 < datau[i] < 720:
        datau[i] -= 360
    if datau[i] == 720:
        datau[i] -= 360
    if 720 < datau[i] < 1080:
        datau[i] -= 720
    if datau[i] == 1080:
        datau[i] -= 720
    if 1080 < datau[i] < 1440:
        datau[i] -= 1080
for i in range(0, len(datax)):
    if 360 < datax[i] < 720:
        datax[i] -= 360
    if datax[i] == 720:
        datax[i] -= 360
    if 720 < datax[i] < 1080:
        datax[i] -= 720
    if datax[i] == 1080:
        datax[i] -= 720
    if 1080 < datax[i] < 1440:
        datax[i] -= 1080

maxdatau = max(datau)
mindatau = min(datau)
maxdatax = max(datax)
mindatax = min(datax)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.scatter(datax, y)
ax1.set_xlim(mindatax, maxdatax)
ax1.set_xlabel('degree of rotation (°)')
ax1.set_ylabel('Horizontal_displacement (mm)')
plt.grid()
ax2 = fig.add_subplot(212)
ax2.scatter(datau, v)
ax2.set_xlabel('degree of rotation(°)')
ax2.set_ylabel('Vertical_displacement (mm)')
ax2.set_xlim(mindatau, maxdatau)
plt.grid()
fig.subplots_adjust(hspace=0.3)
#used this to spread the graphs out

plt.show()
fig.savefig('displacement.png', bbox_inches='tight')

csvfile.close()
#close cvs