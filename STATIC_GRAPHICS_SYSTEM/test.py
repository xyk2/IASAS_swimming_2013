import serial.tools.list_ports
import re
import os

data = raw_input("Enter COM port or press enter to search automatically:\n>>> ")

if(data == ''):
	com_list = list(serial.tools.list_ports.comports())
	for x in com_list:
		print x
	for x in com_list:
		if(x[2].find('FTDI') != -1):
			print int(re.sub("[^0-9]", "", x[0])) - 1
			run = r'serial2ws\serial2ws.py -p %s' %str(int(re.sub("[^0-9]", "", x[0])) - 1)
			os.system("start /wait cmd /c %s"%run)
else:
	os.system(r'serial2ws\serial2ws.py -p %s' %data)