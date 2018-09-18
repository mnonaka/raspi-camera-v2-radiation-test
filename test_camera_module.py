import picamera
import picamera.array
import numpy as np
import serial
import time
import signal

def get_seu(arg1, arg2):
	global total_seu_num 
	current_time = time.time()
	print('time:'+str(current_time))
	
	camera = picamera.PiCamera()
	output = picamera.array.PiBayerArray(camera, output_dims = 2)
	camera.capture(output, 'jpeg', bayer = True)
	camera.close()
	#print("output2:")
	b = output.array
	b = b.astype('int16') #cast uint16 -> int16 for sub
	#print(b)
	
	#|b - a| (absolute of sub of PiBayerArrray B - PiBayerArray A 
	sub_ab = abs(b - a)
	#print("sub_ab:")
	#print(sub_ab)
	
	#SEU detection
	judge = 50#judgement value of SEU happeed or not
	seu = sub_ab >judge
	#print('seu:')
	#print(seu)
	
	seu_num =seu.sum()
	print('seu_num:'+str(seu_num))

	total_seu_num += seu_num
	print('total_seu_num:'+str(total_seu_num))
	
	seu_index = np.where(seu)
	#print('seu_index'+str(seu_index)
	
	#	print('time:'+str(time.time()-current_time))

num = 0
total_seu_num = 0
#total_seu_num = 0 #total seu number @ whole program
#ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) # for serial

camera = picamera.PiCamera()
output = picamera.array.PiBayerArray(camera, output_dims = 2)
#capture first raw bayer data(2-dimensional PiBayerArray)
camera.capture(output, 'jpeg', bayer = True)
camera.close()
#print("output1:")
a = output.array
a = a.astype('int16') #cast uint16 -> int16 for sub
#print(a)

current_time = time.time()
signal.signal(signal.SIGALRM, get_seu)
signal.setitimer(signal.ITIMER_REAL, 2, 2)

while 1:
	continue
	#print("num:", num)
	#print(str(num) + ':' + str(time.time() - current_time))
	#num  += 1

# *****for serial*****     
#    ser.write(chr(seu_num).encode())
#    ser.write(chr(total_seu_num).encode())  
#    r_seu_num = ser.read()
#    r_total_seu_num = ser.read()
#    print("seu number per loop:", r_seu_num)
#    print("total number of seu]:", r_total_seu_num)
