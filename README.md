
This repository contains C program for AVR ATMega328P microcontrollers to communitcate with MPU6050 3-axis gyro + 3-axis accelerometer IMU. Computation of orientation is done on-chip, and result is streamed out through UART as Euler angle values.

Might work on other AVR ATMega family chips, need to change hardware initialization codes.

## Source files description ##

main.c
	contains main function

i2c.h / .c
	define functions for i2c operation

mpu6050_reg.h
	defines register addresses of mpu6050

mpu6050.h / .c
	define functions to operate mpu6050

uart.h / .c
	define functions to operate UART interface, for communication with PC

python/read_orientation_Kalman_animation.py
	Python script to read euler angles from the IMU and visualize it (needs matplotlib and pySerial)
