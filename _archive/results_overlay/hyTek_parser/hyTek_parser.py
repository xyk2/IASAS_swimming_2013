import urllib #import library for HTML 
from xmlrw import xmlrw

#TODO
# Single letter first name periods
# Relay support
# IASAS record
# OPTIMIZE

data = [] #zero indexed. [place][data]. 0th data index is name, 1st is school, 2nd is time

def get_data(row_number): # Returns 3-tuple (name, school, time)
	global name
	global school
	global time
	name = html_list[row_number][4:].partition('  ')[0] #strip four chars, remove ending whitespace

	school_time = html_list[row_number][4:].partition('  ')[2].strip(' ') #school and time - whitespace removed
	school = school_time.partition('  ')[0] #school

	time = school_time.partition('  ')[2].strip(' ') #remove whitespace
	time = time.split('.')[0] + '.' + time.split('.')[1][:2] #everything before millsecond + two chars
	time = time.translate(None, '! ') #remove IASAS record indicator and any whitespace
	return name, school, time #return 3-tuple

	
file = urllib.urlopen("http://iasas.tas.edu.tw/track/iasas12/120412F009.htm") 
html = file.read() #read page source
file.close()

html = html.split('<pre>')[1] # remove all but data table
html = html.split('</pre>')[0]
html_list = html.split('\r\n')


while True: #sort through girls and boys
	try:
		event = 'Girls ' + html_list[5].split('Girls ')[1] #name of race event
		event_race = html_list[10].strip() #race type: prelim, semi, finals, etc
		get_data(11)
		break
	except IndexError:
		event = 'Boys ' + html_list[5].split('Boys ')[1]
		event_race = html_list[10].strip()
		get_data(11)
		break
		

while True: #sort data into data[] list
	try:
		for x in range(11,30): 
			data.append(get_data(x))
			print data[x-11]
		break
	except IndexError: #if IndexError on '=' or out of range
		break

print event
print event_race

print '\n\n'
print data

xml = xmlrw(r'XML/Girls_400_Meter_Hurdles_Preliminaries.xml')
while True: #sort data into data[] list
	try:
		for x in range(0,30): 
			xml.rewrite_tag('<name>', x, data[x][0])
			xml.rewrite_tag('<school>', x, data[x][1])
			xml.rewrite_tag('<time>', x, data[x][2])

		break
	except IndexError: #if IndexError on '=' or out of range
		break
		



