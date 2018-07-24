#This function works fine, leave it alone and plug it into DarkSkyAPI script

import random
import matplotlib.pyplot as plt
import numpy as np

days = list(range(1, 366))

fakemaxtemp = []
for i in range(365):
    fakemaxtemp.append(random.gauss(75, 10))

fakemintemp = []
for i in range(365):
    fakemintemp.append(random.gauss(55, 15))

fakehumidity = []
for i in range(365):
    fakehumidity.append(random.gauss(45, 30))

fakeprecip = []
for i in range(365):
    fakeprecip.append(random.gauss(0.5, 0.05))

def make_my_DarkSky_figure(maxtemp, mintemp, hum, precip):
    plt.figure(1)
    
    plt.subplot(2,2,1)
    plt.plot(maxtemp)
    plt.xlabel('Day')
    plt.ylabel('Degrees F')
    plt.title('Max Temp')
    plt.suptitle('Selected DarkSky Weather Data')
    
    plt.subplot(2,2,2)
    plt.plot(mintemp)
    plt.xlabel('Day')
    plt.ylabel('Degrees F')
    plt.title('Min Temp')
    
    plt.subplot(2,2,3)
    plt.plot(hum)
    plt.xlabel('Day')
    plt.ylabel('Relative Humidity')
    plt.title('Humidity')
    
    plt.subplot(2,2,4)
    plt.plot(precip)
    plt.xlabel('Day')
    plt.ylabel('Inches')
    plt.title('Precipitation')
    
    plt.show()

make_my_DarkSky_figure(fakemaxtemp, fakemintemp, fakehumidity, fakeprecip)