from lib.xmlrw import xmlrw
import Image, ImageDraw, ImageFont
import os
import urllib
import etc.settings as s
import time

#TODO
# Single letter first name periods
# Relay support
# IASAS record
# OPTIMIZE

def print_debug(string):
	debug_on = 1
	if(debug_on == 1):
		print string
		
		
data = [] #zero indexed. [place][data]. 0th data index is name, 1st is school, 2nd is time
icon = [] #icon object
url = raw_input("Enter race url:\n>>> ")
if url == '':
	url = s.default_url


def get_data(row_number): # Returns 3-tuple (name, school, time)
	name = html_list[row_number][4:].partition('  ')[0] #strip four chars, remove ending whitespace

	school_time = html_list[row_number][4:].partition('  ')[2].strip(' ') #school and time - whitespace removed
	school = school_time.partition('  ')[0] #school
	
	if(school == s.ISB_ALTERNATE_NAME):
		school = 'ISB'
	if(school == s.TAS_ALTERNATE_NAME):
		school = 'TAS'
	if(school == s.ISM_ALTERNATE_NAME):
		school = 'ISM'
		
	time = school_time.partition('  ')[2].strip(' ') #remove whitespace
	time = time.split('.')[0] + '.' + time.split('.')[1][:2] #everything before millsecond + two chars
	time = time.translate(None, '! ') #remove IASAS record indicator and any whitespace
	return name, school, time #return 3-tuple
	
print_debug("\nHTTP request sent to %s..."%url)
file = urllib.urlopen(r'%s'%url) 
html = file.read() #read page source
file.close()

html = html.split('<pre>')[1] # remove all but data table
html = html.split('</pre>')[0]
html_list = html.split('\r\n')
print_debug("\nHTML response received. Parsing data...\n\n")


while True: #sort through girls and boys
	try:
		event = 'Girls ' + html_list[5].split('Girls ')[1] #name of race event
		event_race = html_list[10].strip() #race type: prelim, semi, finals, etc
		break
	except IndexError:
		event = 'Boys ' + html_list[5].split('Boys ')[1]
		event_race = html_list[10].strip()
		break
		
print_debug(event+' '+event_race+'\n')

while True: #sort data into data[] list
	try:
		for x in range(0,30): 
			data.append(get_data(x+11))
			print data[x]
			icon.append(Image.open("school_graphics/%s.png"%data[x][1].lower()))
		break
	except IndexError: #if IndexError on '=' or out of range
		break

print_debug("\n\nDrawing graphics...")

im = Image.open(r"swimming_text_removed_single.png")
draw = ImageDraw.Draw(im)

# use a bitmap font
font = ImageFont.truetype(s.font_file, 36)
draw.text((280, 225), event, font=font, fill='black') # TITLE
draw.text((277, 222), event, font=font, fill='white')
print_debug("    Title drawn")

font = ImageFont.truetype(s.font_file, 25)
draw.text((280, 264), event_race, font=font, fill='#262626') #RACE
print_debug("    Subtitle drawn")


############################## SCHOOL NAME ##########################################
font = ImageFont.truetype(s.font_file, 20)
draw.text((255-font.getsize(data[0][1])[0], 298), data[0][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[0][1])[0], 296), data[0][1], font=font, fill='white')
im.paste(icon[0], (260,298), icon[0])

draw.text((255-font.getsize(data[1][1])[0], 330), data[1][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[1][1])[0], 328), data[1][1], font=font, fill='white')
im.paste(icon[1], (260,330), icon[1])

draw.text((255-font.getsize(data[2][1])[0], 362), data[2][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[2][1])[0], 360), data[2][1], font=font, fill='white')
im.paste(icon[2], (260,362), icon[2])

draw.text((255-font.getsize(data[3][1])[0], 394), data[3][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[3][1])[0], 392), data[3][1], font=font, fill='white')
im.paste(icon[3], (260,394), icon[3])

draw.text((255-font.getsize(data[4][1])[0], 426), data[4][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[4][1])[0], 424), data[4][1], font=font, fill='white')
im.paste(icon[4], (260,426), icon[4])

draw.text((255-font.getsize(data[5][1])[0], 458), data[5][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[5][1])[0], 456), data[5][1], font=font, fill='white')
im.paste(icon[5], (260,458), icon[5])

draw.text((255-font.getsize(data[6][1])[0], 490), data[6][1], font=font, fill='black') #lane 1
draw.text((257-font.getsize(data[6][1])[0], 488), data[6][1], font=font, fill='white')
im.paste(icon[6], (260,490), icon[6])

print_debug("    School names and graphics drawn")

############################# NAMES ##################################################
font = ImageFont.truetype(s.font_file, 26)
draw.text((310, 298), data[0][0], font=font, fill='black') #lane 1 name
draw.text((312, 296), data[0][0], font=font, fill='white')

draw.text((310, 330), data[1][0], font=font, fill='black') #lane 2 name
draw.text((312, 328), data[1][0], font=font, fill='white')

draw.text((310, 362), data[2][0], font=font, fill='black') #lane 3 name
draw.text((312, 360), data[2][0], font=font, fill='white')

draw.text((310, 394), data[3][0], font=font, fill='black') #lane 4 name
draw.text((312, 392), data[3][0], font=font, fill='white')

draw.text((310, 426), data[4][0], font=font, fill='black') #lane 4 name
draw.text((312, 424), data[4][0], font=font, fill='white')

draw.text((310, 458), data[5][0], font=font, fill='black') #lane 4 name
draw.text((312, 456), data[5][0], font=font, fill='white')

draw.text((310, 490), data[6][0], font=font, fill='black') #lane 4 name
draw.text((312, 488), data[6][0], font=font, fill='white')

print_debug("    Names drawn")

##################### TIMES #################################
font = ImageFont.truetype(s.font_file, 24) # TIMES
draw.text((885-font.getsize(data[0][2])[0], 297), data[0][2], font=font, fill='black')
draw.text((883-font.getsize(data[0][2])[0], 295), data[0][2], font=font, fill='white')

draw.text((885-font.getsize(data[1][2])[0], 329), data[1][2], font=font, fill='black')
draw.text((883-font.getsize(data[1][2])[0], 327), data[1][2], font=font, fill='white')

draw.text((885-font.getsize(data[2][2])[0], 361), data[2][2], font=font, fill='black')
draw.text((883-font.getsize(data[2][2])[0], 359), data[2][2], font=font, fill='white')

draw.text((885-font.getsize(data[3][2])[0], 393), data[3][2], font=font, fill='black')
draw.text((883-font.getsize(data[3][2])[0], 391), data[3][2], font=font, fill='white')

draw.text((885-font.getsize(data[4][2])[0], 426), data[4][2], font=font, fill='black')
draw.text((883-font.getsize(data[4][2])[0], 424), data[4][2], font=font, fill='white')

draw.text((885-font.getsize(data[5][2])[0], 458), data[5][2], font=font, fill='black')
draw.text((883-font.getsize(data[5][2])[0], 456), data[5][2], font=font, fill='white')

draw.text((885-font.getsize(data[6][2])[0], 490), data[6][2], font=font, fill='black')
draw.text((883-font.getsize(data[6][2])[0], 488), data[6][2], font=font, fill='white')
print_debug("    Times drawn")

# write to stdout
im.save('helloworld.png', "PNG")
print "\n\nGraphic generated."
time.sleep(2)