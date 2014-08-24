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
row = []
pitch = []
i=0
while len(row)<99:
	s0.flush()
	c = s0.read(1)  
	
	if len(c)>0:
	    if ord(c)==10:
		phi = np.array(s0.read(4))
		theta = np.array(s0.read(4))
		dt = np.array(s0.read(4))

		phi = phi.view(np.float32)
		theta = theta.view(np.float32)
		dt = dt.view(np.float32)
        	print(dt)

		row.append(phi)
		pitch.append(theta)

		buff= []
		count = 0
        


# initiate plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot((111),ylim=(-3.5,3.5))
ax.grid()

lineRow, = ax.plot(t, row,'r-')
linePitch, = ax.plot(t, pitch, 'g-')
print("hehhhhehehhhe")
i = 0


while 1:
	s0.flush()   
	c = s0.read(1)
    
	if len(c)>0:
      	    if ord(c)==10:

		phi = np.array(s0.read(4))
		theta = np.array(s0.read(4))
		dt = np.array(s0.read(4))

		phi = phi.view(np.float32)
		theta = theta.view(np.float32)
		dt = dt.view(np.float32)
		#xxx = [ord(k) for k in dt]
		#res = res * 9.8 / 65536
	
		#update plot with new data
		row = row[1:]
		pitch = pitch[1:]
		row.append(phi)
		pitch.append(theta)

		lineRow.set_ydata(row)
		linePitch.set_ydata(pitch)
		fig.canvas.draw()

		i = 0
        	print(dt)


	if i>5:
		print("wrong")
		i = 0
		count = 0

s0.close();
