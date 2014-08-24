# improved python program, robust receiver
# will not get stuck due to accidental miss-counts

import serial
import time
import binascii
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

port = '/dev/ttyUSB0';
baud = 9600;
s0 = serial.Serial(port, baud, timeout = 1, rtscts=True, dsrdtr=True);



t = np.arange(1,100)
row = []
pitch = []

# initiate plot
plt.ion()
fig = plt.figure()
ax = p3.Axes3D(fig, xlim=[-2,2], ylim=[-2,2], zlim=[-2,2])

lineX, = ax.plot([0.,-1.],[0.,0.],[0.,0.],'r-',linewidth=2.0)
lineY, = ax.plot([0.,0.],[0.,-1.],[0.,0.],'g-',linewidth=2.0)
lineZ, = ax.plot([0.,0.],[0.,0.],[0.,-1.],'b-',linewidth=2.0)

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
		lineX.set_data([0., np.cos(theta)],[0., np.sin(theta)*np.sin(phi)])
		lineY.set_data([0., 0.],[0., np.cos(phi)])
		lineZ.set_data([0.,-1.*np.sin(theta)],[0.,np.sin(phi)*np.cos(theta)])
		lineX.set_3d_properties([0., np.sin(theta)*np.cos(phi)])
		lineY.set_3d_properties([0., -1.*np.sin(phi)])
		lineZ.set_3d_properties([0.,np.cos(phi)*np.cos(theta)])

		fig.canvas.draw()


s0.close();
