import time
import serial

serialcomm = serial.Serial('COM4', 9600)
serialcomm.timeout = 1
while True:
    e = '\n'
    serialcomm.write(e.encode())
    serialcomm.write(str(1).encode())
    time.sleep(0.2)
    serialcomm.write(e.encode())
    serialcomm.write(str(0).encode())
    time.sleep(1)


# simple code for serial

'''import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
ser.write("hello world!")'''