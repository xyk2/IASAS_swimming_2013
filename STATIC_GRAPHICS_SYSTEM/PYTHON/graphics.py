from Tkinter import *
import numpy #sort times
import time
from time import gmtime, strftime
import platform
import socket

school_name = [""]*7
swimmer_name = [""]*7
race_time = [""]*7


master = Tk()
master.resizable(0,0)
master.wm_title("IASAS Swimming 2013 Graphics Generator") #program title
master.wm_iconbitmap('icon.ico')


Label(master, text='Race Title').grid(row=0,column=1,columnspan=5,sticky='w')
race_title = Entry(master, width=35)
race_title.config(borderwidth=2)
race_title.grid(row=1, column=1,ipady=3,columnspan=5)


Label(master, text='Match').grid(row=2,column=1,pady=(10,0),columnspan=5,sticky='w')
match = Entry(master, width=35)
match.config(borderwidth=2)
match.grid(row=3, column=1,ipady=3,pady=(0,10),columnspan=5)

Label(master, text='School').grid(row=4,column=0,columnspan=3,sticky='e')
Label(master, text='Name').grid(row=4,column=3,padx=(5,0),sticky='w')
Label(master, text='Time').grid(row=4,column=10,padx=(5,0),sticky='w')

lane_number = IntVar()
for x in range(0, 7):
	Radiobutton(master,  variable=lane_number, value=x).grid(row=x+5,column=0,pady=2,sticky='e')
	school_name[x] = Entry(master, width=5)
	school_name[x].config(borderwidth=2)
	school_name[x].grid(row=x+5, column=1, pady=(2,2),ipady=1, columnspan=2, sticky='w')
	swimmer_name[x] = Entry(master, width=30)
	swimmer_name[x].config(borderwidth=2)
	swimmer_name[x].grid(row=x+5, column=3, padx=(4,0),pady=(2,2),ipady=1, columnspan=4, sticky='w')
	race_time[x] = Entry(master, width=9)
	race_time[x].config(borderwidth=2)
	race_time[x].grid(row=x+5, column=10, padx=(4,0),pady=(2,2),ipady=1,columnspan=4, sticky='w')
	
graphic_type = IntVar()
Radiobutton(master,  variable=graphic_type, text="Race Introduction", value="0").grid(row=5,column=14, padx=(10,15),sticky='w')
Radiobutton(master,  variable=graphic_type, text="Start List", value="1").grid(row=6,column=14,  padx=(10,0),sticky='w')
Radiobutton(master,  variable=graphic_type, text="Nameplate", value="2").grid(row=7,column=14, padx=(10,0), sticky='w')
Radiobutton(master,  variable=graphic_type, text="Winner", value="3").grid(row=8,column=14, padx=(10,0), sticky='w')
Radiobutton(master,  variable=graphic_type, text="Results", value="4").grid(row=9, column=14, padx=(10,0), sticky='w')


def log_to_file(filename, gfx_type, race_title_val, match_val): #logfile function; logs to file with ip, network name, race title, type, and match
	current_time = strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	ip_address = socket.gethostbyname(socket.gethostname())
	network_name = platform.node()
	csv_string = ip_address + "," + network_name + "," + current_time + ',' + gfx_type + "," + race_title_val + "," + match_val + '\n'
	file = open(filename, 'a') #open logfile in append mode
	file.write(csv_string)
	file.close()

	
def save_event_to_file(gfx_type, race_title_val, match_val, csv_string): #saves all live.csv files in timestamped files
	filename = strftime("%Y-%m-%d-%H_%M_%S", time.localtime()) + "_" + gfx_type + "_" + race_title_val + "_" + match_val + ".csv"
	print filename
	file = open(r"logs/%s"%filename, "w+")
	file.write(csv_string)
	file.close()
	
def sort_list_by_time(list):
	for x in range(0,7): #convert time str to float
		if(len(list[x][3])>0 and list[x][3].find(":") == -1 and list[x][3].find(".") != -1): #skip empty times, >1 min times, and DNFs
			list[x][3] = float(list[x][3])
		elif(list[x][3].find(":") != -1): #if colon is present; >1 min
			min_in_sec =  float(list[x][3].split(':')[0])*60+float(list[x][3].split(':')[1])
			list[x][3] = min_in_sec
	list = sorted(list, key=lambda a_entry: a_entry[3])
	for x in range(0,7): #convert float back to string
		if(len(str(list[x][3]))>0 and list[x][3] >= 60):
			min, sec = divmod(list[x][3], 60)
			if(min<10):
				list[x][3] = "%01d:%02d.%s" %(min,sec,str(sec).split('.')[1])
			else:
				list[x][3] = "%02d:%02d.%s" %(min,sec,str(sec).split('.')[1])
		list[x][3] = str(list[x][3])
		#print list[x][3]
	return list
	
	
def gfx_live_pusher():
	csv_string = "" #complete csv string to be appended
	gfx_type_num = ["race_intro", "start_list", "nameplate", "winner", "results"]
	
	gfx_type = gfx_type_num[graphic_type.get()] # graphic type; race_intro, results... etc
	race_title_val = race_title.get() #race title value
	match_val = match.get() #match value
	
	dataset = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
	for x in range(0,7):
		dataset[x][0] = str(x+1)
		dataset[x][1] = school_name[x].get()
		dataset[x][2] = swimmer_name[x].get()
		dataset[x][3] = race_time[x].get()
	print dataset
	csv_string = csv_string + gfx_type + '\n' #line 1, gfx type command
	
	if(gfx_type == "race_intro"):
		csv_string = csv_string + race_title_val + "," + match_val #race title + match name
	if(gfx_type == "start_list"):
		csv_string = csv_string + race_title_val + "," + match_val + '\n' #race title + match name
		for x in range(0,7):
			csv_string = csv_string + dataset[x][0] + ',' + dataset[x][1] + ',' + dataset[x][2] + '\n'
	if(gfx_type == "nameplate"): #lane_number, school_name, swimmer_name
		index = lane_number.get()
		csv_string = csv_string + dataset[index][0] + ',' + dataset[index][1] + ',' + dataset[index][2]
	if(gfx_type == "winner"):
		sorted_list = sort_list_by_time(dataset)
		csv_string = csv_string + race_title_val + "," + match_val + '\n' #race title + match name
		csv_string = csv_string + sorted_list[0][0] + ',' + sorted_list[0][1] 
		csv_string = csv_string + ',' + sorted_list[0][2] + ',' + sorted_list[0][3] 
	if(gfx_type == 'results'):
		sorted_list = sort_list_by_time(dataset)
		csv_string = csv_string + race_title_val + "," + match_val + '\n' #race title + match name
		for x in range(0,7):
			csv_string = csv_string + sorted_list[x][0] + ',' + sorted_list[x][1] + ',' + sorted_list[x][2] + ',' + sorted_list[x][3] + '\n'
	
	
	file = open('../live.csv', 'w')
	file.write(csv_string)
	file.close()
	print csv_string
	log_to_file("logfile.log", gfx_type, race_title_val, match_val) #log to logfile
	save_event_to_file(gfx_type, race_title_val, match_val, csv_string) #save event to .csv
	
Button(master, pady=3, text="Daktronics Console").grid(row=12,column=0, columnspan=4,pady=(10,15),padx=(15,0),sticky="w")
Button(master, pady=3, text="Open GFX Displayer").grid(row=12,column=4, ipadx=5, columnspan=2,pady=(10,15),padx=(15,0),sticky="w")
Button(master, pady=3, text="Live", command=gfx_live_pusher).grid(row=10,column=14,ipadx=10,ipady=4, columnspan=2,rowspan=2)

mainloop()













