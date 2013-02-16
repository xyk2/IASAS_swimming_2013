import urllib2

def get_fixed_width(data, start_index, end_index):
	return data[start_index:end_index].strip()
	
def convert_school_acronym(school):
	if(school == 'Eagles'):	return 'SAS'
	if(school == 'Jis Dragons'): return 'JIS'
	return school
	
def convert_name_format(name):
	if(name != ''):
		if(len(name.split(' ')) > 2): name = name.split(' ')[0] + ' ' + name.split(' ')[1] #remove middle name initials
		return name.split(',')[1].strip().upper() + " " + name.split(',')[0].strip().upper() #reverse last-name,first-name order
	else: return ''

url = raw_input("Enter race URL:\n>>> ")
race_name = raw_input("Enter race name:\n>>> ")
race_type = raw_input("Enter race type:\n>>> ")
print '\n\n\n'
s = urllib2.urlopen(url).read()
s = s.split('<pre>')[1]
s = s.split('</pre>')[0]
s = s.split('===============================================================================')[2].strip()
print s

csv_data = ''
list = s.split("\n")

for x in list:
	lane = get_fixed_width(x, 0, 5)
	if(lane.isdigit()):
		name = get_fixed_width(x, 5, 35)
		name = convert_name_format(name)
		
		school = get_fixed_width(x, 38, 64)
		school = convert_school_acronym(school)
				
		csv_data = csv_data + lane + ',' + school + ',' + name + '\n'
		
	else: 
		csv_data = csv_data + "\n\nstart_list\n%s,%s" %(race_name, race_type) + "\n"
		
print csv_data
file = open('0_%s_H0.csv'%(race_name), 'w+')
file.write(csv_data)
file.close()

raw_input()


