import csv

import matplotlib.pyplot as plt
from statistics import mean

data = []
degreeOfRotation = 0
flip = False
lengthofdata = 0
with open('../Data/DATA.csv','r' ) as csvfile:                  #Used to open csv file
    reader = csv.reader(csvfile)                                 #Used to read csv file
    for row in reader:                                            #Used to read each line
        temp = []                                                #List to hold all elements in line
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
                        degreeOfRotation += 10
                    elif flip:  # If flip == true
                        degreeOfRotation -= 10

                if temp[4] == 'V':
                    if degreeOfRotation == 180:
                        flip = False
                    elif degreeOfRotation == 360:
                        flip = True

                    if not flip:  # If flip == false
                        degreeOfRotation += 10
                    elif flip:  # If flip == true
                        degreeOfRotation -= 10

        temp.append(degreeOfRotation)

        # List to hold needed elements
        temp2 = [temp[1], temp[3], temp[5], temp[4]]
        # temp2.append

        data.append(temp2)#List to hold final variables
        lengthofdata += 1


aHdegrees = []
aVdegrees = []

#averageVat0_y = []
averageHat0_y = []
#averageVat10_y = []
averageHat10_y = []
#averageVat20_y = []
averageHat20_y = []
#averageVat30_y = []
averageHat30_y = []
#averageVat40_y = []
averageHat40_y = []
#averageVat50_y = []
averageHat50_y = []
#averageVat60_y = []
averageHat60_y = []
#averageVat70_y = []
averageHat70_y = []
#averageVat80_y = []
averageHat80_y = []
#averageVat90_y = []
averageHat90_y = []
#averageVat100_y = []
averageHat100_y = []
#averageVat110_y = []
averageHat110_y = []
#averageVat120_y = []
averageHat120_y = []
#averageVat130_y = []
averageHat130_y = []
#averageVat140_y = []
averageHat140_y = []
#averageVat150_y = []
averageHat150_y = []
#averageVat160_y = []
averageHat160_y = []
#averageVat170_y = []
averageHat170_y = []
averageVat180_y = []
averageHat180_y = []
averageVat190_y = []
#averageHat190_y = []
averageVat200_y = []
#averageHat200_y = []
averageVat210_y = []
#averageHat210_y = []
averageVat220_y = []
#averageHat220_y = []
averageVat230_y = []
#averageHat230_y = []
#averageHat240_y = []
averageVat240_y = []
#averageHat250_y = []
averageVat250_y = []
#averageHat260_y = []
averageVat260_y = []
#averageHat270_y = []
averageVat270_y = []
#averageHat280_y = []
averageVat280_y = []
#averageHat290_y = []
averageVat290_y = []
#averageHat300_y = []
averageVat300_y = []
#averageHat310_y = []
averageVat310_y = []
#averageHat320_y = []
averageVat320_y = []
#averageHat330_y = []
averageVat330_y = []
#averageHat340_y = []
averageVat340_y = []
#averageHat350_y = []
averageVat350_y = []
#averageHat360_y = []
averageVat360_y = []

aV180 = ()
aV190 = ()
aV200 = ()
aV210 = ()
aV220 = ()
aV230 = []
aV240 = []
aV250 = []
aV260 = []
aV270 = []
aV280 = []
aV290 = []
aV300 = []
aV310 = []
aV320 = []
aV330 = []
aV340 = []
aV350 = []
aV360 = []
aH0 = []
aH10 = []
aH20 = []
aH30 = []
aH40 = []
aH50 = []
aH60 = []
aH70 = []
aH80 = []
aH90 = []
aH100 = []
aH110 = []
aH120 = []
aH130 = []
aH140 = []
aH150 = []
aH160 = []
aH170 = []
aH180 = []


for i in range(0, len(data)):
    if data[i][3] == 'H':
        if data[i][2] == 0:
            averageHat0_y.append(data[i][1])
        if data[i][2] == 10:
            averageHat10_y.append(data[i][1])
        if data[i][2] == 20:
            averageHat20_y.append(data[i][1])
        if data[i][2] == 30:
            averageHat30_y.append(data[i][1])
        if data[i][2] == 40:
            averageHat40_y.append(data[i][1])
        if data[i][2] == 50:
            averageHat50_y.append(data[i][1])
        if data[i][2] == 60:
            averageHat60_y.append(data[i][1])
        if data[i][2] == 70:
            averageHat70_y.append(data[i][1])
        if data[i][2] == 80:
            averageHat80_y.append(data[i][1])
        if data[i][2] == 90:
            averageHat90_y.append(data[i][1])
        if data[i][2] == 100:
            averageHat100_y.append(data[i][1])
        if data[i][2] == 110:
            averageHat110_y.append(data[i][1])
        if data[i][2] == 120:
            averageHat120_y.append(data[i][1])
        if data[i][2] == 130:
            averageHat130_y.append(data[i][1])
        if data[i][2] == 140:
            averageHat140_y.append(data[i][1])
        if data[i][2] == 150:
            averageHat150_y.append(data[i][1])
        if data[i][2] == 160:
            averageHat160_y.append(data[i][1])
        if data[i][2] == 170:
            averageHat170_y.append(data[i][1])
        if data[i][2] == 180:
            averageHat180_y.append(data[i][1])

for i in range(0, len(data)):
    if data[i][3] == 'V':
        if data[i][2] == 180:
            averageVat180_y.append(data[i][1])
        if data[i][2] == 190:
            averageVat190_y.append(data[i][1])
        if data[i][2] == 200:
            averageVat200_y.append(data[i][1])
        if data[i][2] == 210:
            averageVat210_y.append(data[i][1])
        if data[i][2] == 220:
            averageVat220_y.append(data[i][1])
        if data[i][2] == 230:
            averageVat230_y.append(data[i][1])
        if data[i][2] == 240:
            averageVat240_y.append(data[i][1])
        if data[i][2] == 250:
            averageVat250_y.append(data[i][1])
        if data[i][2] == 260:
            averageVat260_y.append(data[i][1])
        if data[i][2] == 270:
            averageVat270_y.append(data[i][1])
        if data[i][2] == 280:
            averageVat280_y.append(data[i][1])
        if data[i][2] == 290:
            averageVat290_y.append(data[i][1])
        if data[i][2] == 300:
            averageVat300_y.append(data[i][1])
        if data[i][2] == 310:
            averageVat310_y.append(data[i][1])
        if data[i][2] == 320:
            averageVat320_y.append(data[i][1])
        if data[i][2] == 330:
            averageVat330_y.append(data[i][1])
        if data[i][2] == 340:
            averageVat340_y.append(data[i][1])
        if data[i][2] == 350:
            averageVat350_y.append(data[i][1])
        if data[i][2] == 360:
            averageVat360_y.append(data[i][1])

aV180 = mean(float(n) if n else 0 for n in averageVat180_y)
aV190 = mean(float(n) if n else 0 for n in averageVat190_y)
aV200 = mean(float(n) if n else 0 for n in averageVat200_y)
aV210 = mean(float(n) if n else 0 for n in averageVat210_y)
aV220 = mean(float(n) if n else 0 for n in averageVat220_y)
aV230 = mean(float(n) if n else 0 for n in averageVat230_y)
aV240 = mean(float(n) if n else 0 for n in averageVat240_y)
aV250 = mean(float(n) if n else 0 for n in averageVat250_y)
aV260 = mean(float(n) if n else 0 for n in averageVat260_y)
aV270 = mean(float(n) if n else 0 for n in averageVat270_y)
aV280 = mean(float(n) if n else 0 for n in averageVat280_y)
aV290 = mean(float(n) if n else 0 for n in averageVat290_y)
aV300 = mean(float(n) if n else 0 for n in averageVat300_y)
aV310 = mean(float(n) if n else 0 for n in averageVat310_y)
aV320 = mean(float(n) if n else 0 for n in averageVat320_y)
aV330 = mean(float(n) if n else 0 for n in averageVat330_y)
aV340 = mean(float(n) if n else 0 for n in averageVat340_y)
aV350 = mean(float(n) if n else 0 for n in averageVat350_y)
aV360 = mean(float(n) if n else 0 for n in averageVat360_y)

aH0 = mean(float(n) if n else 0 for n in averageHat0_y)
aH10 = mean(float(n) if n else 0 for n in averageHat10_y)
aH20 = mean(float(n) if n else 0 for n in averageHat20_y)
aH30 = mean(float(n) if n else 0 for n in averageHat30_y)
aH40 = mean(float(n) if n else 0 for n in averageHat40_y)
aH50 = mean(float(n) if n else 0 for n in averageHat50_y)
aH60 = mean(float(n) if n else 0 for n in averageHat60_y)
aH70 = mean(float(n) if n else 0 for n in averageHat70_y)
aH80 = mean(float(n) if n else 0 for n in averageHat80_y)
aH90 = mean(float(n) if n else 0 for n in averageHat90_y)
aH100 = mean(float(n) if n else 0 for n in averageHat100_y)
aH110 = mean(float(n) if n else 0 for n in averageHat110_y)
aH120 = mean(float(n) if n else 0 for n in averageHat120_y)
aH130 = mean(float(n) if n else 0 for n in averageHat130_y)
aH140 = mean(float(n) if n else 0 for n in averageHat140_y)
aH150 = mean(float(n) if n else 0 for n in averageHat150_y)
aH160 = mean(float(n) if n else 0 for n in averageHat160_y)
aH170 = mean(float(n) if n else 0 for n in averageHat170_y)
aH180 = mean(float(n) if n else 0 for n in averageHat180_y)

aH = [aH0, aH10, aH20, aH30, aH40, aH50, aH60, aH70, aH80, aH90,aH100, aH110, aH120,
      aH130, aH140, aH150, aH160, aH170, aH180]
aV = [aV180, aV190, aV200, aV210, aV220, aV230, aV240, aV250, aV260, aV270, aV280,
      aV290, aV300, aV310, aV320, aV330, aV340, aV350, aV360]
aHdegrees = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
aVdegrees = [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.scatter(aHdegrees, aH)
ax1.set_xlim(0, 180)
ax1.set_xlabel('degree of displacement/degree')
ax1.set_ylabel('Horizontal_displacement/mm')

ax2 = fig.add_subplot(212)
ax2.scatter(aVdegrees, aV)
ax2.set_xlabel('degree of displacement/degree')
ax2.set_ylabel('Vertical_displacement/mm')
ax2.set_xlim(180, 360)
#ax2.set_ylim(vmin, vmax)
#plt.yticks([v1, v2, v3, v4, v5, v6, v7, v8])

fig.subplots_adjust(hspace=0.3)
plt.show()
print(data)