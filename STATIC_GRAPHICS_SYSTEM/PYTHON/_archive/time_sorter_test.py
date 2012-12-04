test_list = [['1', 'SAS', 'BUSTER POSEY', '55.9'], ['2', 'TAS', 'HUNTER PENCE', '58.2'], ['3', 'ISKL', 'ANGEL PAGAN', '1:01.2'], ['4', 'ISB', 'GREGOR BLANCO', '1:03.2'], ['5', 'JIS', 'BRANDON BELT', '12:13.1'], ['6', 'ISM', 'MARCO SCUTARO', '2:03.1'],['7', 'TAS', 'BRANDON CRAWFORD', '1:34.7']]

def sort_list_by_time(list):
	for x in range(0,7): #convert time str to float
		if(len(list[x][3])>0 and list[x][3].find(":") == -1 and list[x][3].find(".") != -1): #skip empty times, >1 min times, and DNFs
			list[x][3] = float(list[x][3])
		elif(list[x][3].find(":") != -1):
			min_in_sec =  float(list[x][3].split(':')[0])*60+float(list[x][3].split(':')[1])
			list[x][3] = min_in_sec
	list = sorted(list, key=lambda a_entry: a_entry[3])
	for x in range(0,7): #convert float back to string
		if(list[x][3] >= 60):
			min, sec = divmod(list[x][3], 60)
			list[x][3] = "%02d:%02d.%s" %(min,sec,str(sec).split('.')[1])
		list[x][3] = str(list[x][3])
		#print list[x][3]
	return list
	
print sort_list_by_time(test_list)
raw_input()
