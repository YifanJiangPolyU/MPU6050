# improved python program, robust receiver
# will not get stuck due to accidental miss-counts

import serial
import time
import binascii
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

port = '/dev/ttyUSB0';
baud = 9600;
s0 = serial.Serial(port, baud, timeout = 1, rtscts=True, dsrdtr=True);



t = np.arange(1,100)
count = 0
TimeOutCount = 0
buff = []
x = []
y = []
z = []
i=0
while len(y)<99:
	s0.flush()
	c = s0.read(1)  
	
	if len(c)>0:
	    if ord(c)==10:
		resX = np.array(s0.read(2))
		resY = np.array(s0.read(2))
		resZ = np.array(s0.read(2))

		dt = np.array(s0.read(4))
		dt = dt.view(np.float32)
        	print(dt)

        	resX = resX.view(np.int16)
        	resY = resY.view(np.int16)
        	resZ = resZ.view(np.int16)
		#res = res * 9.8 / 65536
		x.append(resX*9.8*2/32768)
		y.append(resY*9.8*2/32768)
		z.append(resZ*9.8*2/32768)

		buff= []
		count = 0
        


# initiate plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot((111),ylim=(-12,12))
ax.grid()

line, = ax.plot(t, y,'r-')
print("hehhhhehehhhe")
i = 0


while 1:
	s0.flush()   
	c = s0.read(1)
    
	if len(c)>0:
      	    if ord(c)==10:


		resX = np.array(s0.read(2))
		resY = np.array(s0.read(2))
		resZ = np.array(s0.read(2))
		dt = np.array(s0.read(4))
		resX = resX.view(np.int16)
		resY = resY.view(np.int16)
		resZ = resZ.view(np.int16)
		dt = dt.view(np.float32)
		#xxx = [ord(k) for k in dt]
		#res = res * 9.8 / 65536
	
		#update plot with new data
		x = x[1:]
		y = y[1:]
		z = z[1:]
		x.append(resX*9.8*2/32768)
		y.append(resY*9.8*2/32768)
		z.append(resZ*9.8*2/32768)
		line.set_ydata(x)
		fig.canvas.draw()

		i = 0
		prev_t = t
        	print(dt)


	if i>5:
		print("wrong")
		i = 0
		count = 0

s0.close();
