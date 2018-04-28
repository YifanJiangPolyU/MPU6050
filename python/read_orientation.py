
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
s0 = serial.Serial(port, baud, timeout = 0.5, rtscts=True, dsrdtr=True);


# initialize orientation transform matrix
T = np.array([ [1.,0.,0.],[0.,1.,0.],[0.,0.,1.] ])

# time step
dt = 0.02


# initiate plot
plt.ion()
fig = plt.figure()
ax = p3.Axes3D(fig, xlim=[-2,2], ylim=[-2,2], zlim=[-2,2])


lineX, = ax.plot([0.,-1.],[0.,0.],[0.,0.],'r-',linewidth=2.0)
lineY, = ax.plot([0.,0.],[0.,-1.],[0.,0.],'g-',linewidth=2.0)
lineZ, = ax.plot([0.,0.],[0.,0.],[0.,-1.],'b-',linewidth=2.0)




# calibrate sensor: find bias
i = 0
cal_x=[]
cal_y=[]
cal_z=[]
while i<99:
	s0.flush()
	c = s0.read(1)

	if len(c)>0:
      	    if ord(c)==10:
		res_accel_X = np.array(s0.read(2))
		res_accel_Y = np.array(s0.read(2))
		res_accel_Z = np.array(s0.read(2))

		res_accel_X = res_accel_X.view(np.int16)
		res_accel_Y = res_accel_Y.view(np.int16)
		res_accel_Z = res_accel_Z.view(np.int16)

		cal_x.append(res_accel_X)
		cal_y.append(res_accel_Y)
		cal_z.append(res_accel_Z)

		i = i+1



i = 0


while 1:
	s0.flush()
	c = s0.read(1)

	if len(c)>0:
      	    if ord(c)==10:

		# data acquisition
		res_accel_X = np.array(s0.read(2))
		res_accel_Y = np.array(s0.read(2))
		res_accel_Z = np.array(s0.read(2))

		res_accel_X = res_accel_X.view(np.int16)
		res_accel_Y = res_accel_Y.view(np.int16)
		res_accel_Z = res_accel_Z.view(np.int16)

		aX = (res_accel_X) * 9.8*2/32768
		aY = (res_accel_Y) * 9.8*2/32768
		aZ = (res_accel_Z) * 9.8*2/32768

		#cal_x = cal_x[1:]
		#cal_y = cal_y[1:]
		#cal_z = cal_z[1:]
		#cal_x.append(aX)
		#cal_y.append(aY)
		#cal_z.append(aZ)

		phi = np.arctan2(aY, aZ) # row
		theta = np.arctan2(-aX, np.sqrt(aY*aY+aZ*aZ)) # pitch
		#theta = np.arcsin(-1.*aX/9.8)

		#update plot with new data
		# assume yaw is always 0
		lineX.set_data([0., np.cos(theta)],[0., np.sin(theta)*np.sin(phi)])
		lineY.set_data([0., 0.],[0., np.cos(phi)])
		lineZ.set_data([0.,-1.*np.sin(theta)],[0.,np.sin(phi)*np.cos(theta)])
		lineX.set_3d_properties([0., np.sin(theta)*np.cos(phi)])
		lineY.set_3d_properties([0., -1.*np.sin(phi)])
		lineZ.set_3d_properties([0.,np.cos(phi)*np.cos(theta)])

		#accX.set_ydata(cal_x)
		#accY.set_ydata(cal_y)
		#accZ.set_ydata(cal_z)

		fig.canvas.draw()
		#fig2.canvas.draw()
		i = 0


	if i>5:
		print("wrong")
		i = 0
		count = 0

s0.close();
