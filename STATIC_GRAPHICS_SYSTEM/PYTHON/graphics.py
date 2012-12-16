from Tkinter import *
import numpy #sort times
import time #timestamps
from time import gmtime, strftime #timestamps
import platform #IP + computer name
import socket #IP + computer name
import tkFileDialog #import dialog
import webbrowser #open URL
import Image, ImageTk #image preview

school_name = [""]*7
swimmer_name = [""]*7
race_time = [""]*7

school_name_value = [""]*7 # value inside textbox; textvariable
swimmer_name_value = [""]*7
race_time_value = [""]*7

class edit_team_scores_dialog:
    def __init__(self, parent):
		top = self.top = Toplevel(parent)
		top.title("Team Scores")
		top.iconbitmap("img/icon.ico")

		IASAS_schools = ["TAS Tigers", "SAS Eagles", "ISB Panthers", "ISM Bearcats", "ISKL Panthers", "JIS Dragons"]
		self.team_score_value_boys = [""]*6
		self.team_score_value_girls = [""]*6
		team_score_value_boys_textvariable = [""]*6 #textvariable for internal vals
		team_score_value_girls_textvariable = [""]*6
		for x in range(0,6): #convert textVariable list to stringVars
			team_score_value_boys_textvariable[x] = StringVar()
			team_score_value_girls_textvariable[x] = StringVar()
		Label(top, text='Boys').grid(row=0,column=3,pady=(6,0))
		Label(top, text='Girls').grid(row=0,column=5,pady=(6,0))
		
		for x in range(0, 6):
			Label(top, text=IASAS_schools[x]).grid(row=x+1,column=0,columnspan=2,padx=(10,0))
			self.team_score_value_boys[x] = Entry(top,width=6,textvariable=team_score_value_boys_textvariable[x])
			self.team_score_value_boys[x].config(borderwidth=2)
			self.team_score_value_boys[x].grid(row=x+1,column=3,padx=(4,0),pady=(3,3),ipady=1)
			
			self.team_score_value_girls[x] = Entry(top,width=6,textvariable=team_score_value_girls_textvariable[x])
			self.team_score_value_girls[x].config(borderwidth=2)
			self.team_score_value_girls[x].grid(row=x+1,column=5,padx=(6,10),pady=(3,3),ipady=1)
			
		#Import file
		file = open('team_scores.csv', 'r')
		data_list = file.readlines() #read file into a list
		data_list = map(lambda s: s.rstrip(), data_list) #remove newline
		print data_list
		for x in range(2,8): #write data to Entry elements
			if(data_list[x].split(',')[0] == "TAS"): team_score_value_boys_textvariable[0].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "SAS"): team_score_value_boys_textvariable[1].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "ISB"): team_score_value_boys_textvariable[2].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "ISM"): team_score_value_boys_textvariable[3].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "ISKL"): team_score_value_boys_textvariable[4].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "JIS"): team_score_value_boys_textvariable[5].set(data_list[x].split(',')[1])
		for x in range(9,15): #write data to Entry elements
			if(data_list[x].split(',')[0] == "TAS"): team_score_value_girls_textvariable[0].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "SAS"): team_score_value_girls_textvariable[1].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "ISB"): team_score_value_girls_textvariable[2].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "ISM"): team_score_value_girls_textvariable[3].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "ISKL"): team_score_value_girls_textvariable[4].set(data_list[x].split(',')[1])
			if(data_list[x].split(',')[0] == "JIS"): team_score_value_girls_textvariable[5].set(data_list[x].split(',')[1])
		Button(top, text="Save", command=self.save).grid(row=10,column=4,ipadx=4,ipady=2,pady=(3,6),columnspan=2)
		
    def save(self):
		boys_list = [['TAS','0'],['SAS','0'],['ISB','0'],['ISM','0'],['ISKL','0'],['JIS','0']]
		girls_list = [['TAS','0'],['SAS','0'],['ISB','0'],['ISM','0'],['ISKL','0'],['JIS','0']]
		for x in range(0, 6):
			boys_list[x][1] = self.team_score_value_boys[x].get() #get values and sort into list
			girls_list[x][1] = self.team_score_value_girls[x].get()
		boys_list = sorted(boys_list, key=lambda x: x[1]) #sort lists by score
		girls_list = sorted(girls_list, key=lambda x: x[1])
		
		file = open('team_scores.csv', 'w') #rewrite csv file
		csv_string = 'team_scores\nboys\n'
		for x in reversed(range(0, 6)): #list is sorted left to right incrementing, we want it decrementing
			csv_string = csv_string + boys_list[x][0] + ','
			csv_string = csv_string + boys_list[x][1] + '\n'
		csv_string = csv_string + 'girls\n'
		for x in reversed(range(0, 6)): #list is sorted left to right incrementing, we want it decrementing
			csv_string = csv_string + girls_list[x][0] + ','
			csv_string = csv_string + girls_list[x][1] + '\n'		
		print csv_string
		file.write(csv_string) #write to team_scores
		log_to_file("logfile.log", 'team_scores', 'null', 'null') #log to logfile
		save_event_to_file('team_scores', 'team_scores', 'null', csv_string) #save event to .csv
		
		self.top.destroy()

master = Tk()
master.resizable(0,0)
master.title("IASAS Swimming 2013 Graphics Generator") #program title
master.iconbitmap('img/icon.ico')

################## MENU
mbar = Menu(master, tearoff=0) 
master.config(menu=mbar)
fileMenu = Menu(mbar,tearoff=0) 
mbar.add_cascade(label="File", menu=fileMenu) 
fileMenu.add_command(label="Open GFX Displayer", command=lambda: webbrowser.open('http://localhost', new=1)) 
editMenu = Menu(mbar,tearoff=0) 
mbar.add_cascade(label="Edit", menu=editMenu) 
editMenu.add_command(label="Edit Team Scores", command=lambda: edit_team_scores_dialog(master)) 
############## END MENU

img_list = [ImageTk.PhotoImage(Image.open('img/race_intro.png')), ImageTk.PhotoImage(Image.open('img/start_list.png')),
	ImageTk.PhotoImage(Image.open('img/nameplate.png')),ImageTk.PhotoImage(Image.open('img/winner.png')),
	ImageTk.PhotoImage(Image.open('img/results.png'))]

for x in range(0, 7): #convert datal list to string variables
	school_name_value[x] = StringVar()
	swimmer_name_value[x] = StringVar()
	race_time_value[x] = StringVar()

race_title_entry_value = StringVar()
Label(master, text='Race Title').grid(row=0,column=1,columnspan=5,sticky='w')
race_title = Entry(master, width=35, textvariable=race_title_entry_value)
race_title.config(borderwidth=2)
race_title.grid(row=1, column=1,ipady=3,columnspan=5)

match_entry_value = StringVar()
Label(master, text='Match').grid(row=2,column=1,pady=(10,0),columnspan=5,sticky='w')
match = Entry(master, width=35, textvariable=match_entry_value)
match.config(borderwidth=2)
match.grid(row=3, column=1,ipady=3,pady=(0,10),columnspan=5)

Label(master, text='School').grid(row=4,column=0,columnspan=3,sticky='e')
Label(master, text='Name').grid(row=4,column=3,padx=(5,0),sticky='w')
Label(master, text='Time').grid(row=4,column=10,padx=(5,0),sticky='w')

lane_number = IntVar()
for x in range(0, 7): #SCHOOL NAME< SWIMMER NAME, TIME
	Radiobutton(master,  variable=lane_number, value=x).grid(row=x+5,column=0,pady=2,sticky='e')
	school_name[x] = Entry(master, width=5, textvariable=school_name_value[x])
	school_name[x].config(borderwidth=2)
	school_name[x].grid(row=x+5, column=1, pady=(2,2),ipady=1, columnspan=2, sticky='w')
	swimmer_name[x] = Entry(master, width=30, textvariable=swimmer_name_value[x])
	swimmer_name[x].config(borderwidth=2)
	swimmer_name[x].grid(row=x+5, column=3, padx=(4,0),pady=(2,2),ipady=1, columnspan=4, sticky='w')
	race_time[x] = Entry(master, width=9, textvariable=race_time_value[x])
	race_time[x].config(borderwidth=2)
	race_time[x].grid(row=x+5, column=10, padx=(4,0),pady=(2,2),ipady=1,columnspan=4, sticky='w')
	
def change_img(): #change image based on gfx_type radiobutton
	int(graphic_type.get())
	image_label.config(image=img_list[int(graphic_type.get())])
	
graphic_type = IntVar() #GFX TYPE
Radiobutton(master, variable=graphic_type, text="Race Introduction", value="0", command=change_img).grid(row=5,column=14, padx=(10,15),sticky='w')
Radiobutton(master, variable=graphic_type, text="Start List", value="1", command=change_img).grid(row=6,column=14,  padx=(10,0),sticky='w')
Radiobutton(master, variable=graphic_type, text="Nameplate", value="2", command=change_img).grid(row=7,column=14, padx=(10,0), sticky='w')
Radiobutton(master, variable=graphic_type, text="Winner", value="3", command=change_img).grid(row=8,column=14, padx=(10,0), sticky='w')
Radiobutton(master, variable=graphic_type, text="Results", value="4", command=change_img).grid(row=9, column=14, padx=(10,0), sticky='w')
Radiobutton(master, variable=graphic_type, text="Team Scores", value="5", command=change_img).grid(row=10, column=14, padx=(10,0), sticky='w')


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
	gfx_type_num = ["race_intro", "start_list", "nameplate", "winner", "results", "team_scores"]
	
	gfx_type = gfx_type_num[graphic_type.get()] # graphic type; race_intro, results... etc
	if(graphic_type.get() == 1 or graphic_type.get() == 4): #if start_list or results
		if(is_relay.get() == 1): #and relay is enabled
			gfx_type = "relay_" + gfx_type 
	
	race_title_val = race_title_entry_value.get() #race title value
	match_val = match_entry_value.get() #match value
	
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
	if(gfx_type == "start_list" or gfx_type == 'relay_start_list'):
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
	if(gfx_type == 'results' or gfx_type == 'relay_results'):
		sorted_list = sort_list_by_time(dataset)
		csv_string = csv_string + race_title_val + "," + match_val + '\n' #race title + match name
		for x in range(0,7):
			csv_string = csv_string + sorted_list[x][0] + ',' + sorted_list[x][1] + ',' + sorted_list[x][2] + ',' + sorted_list[x][3] + '\n'
	if(gfx_type == 'team_scores'): 
		file = open('team_scores.csv', 'r') #read from file and append csv_string
		csv_string = file.read()
		file.close()
	file = open('../live.csv', 'w')
	file.write(csv_string)
	file.close()
	print csv_string
	log_to_file("logfile.log", gfx_type, race_title_val, match_val) #log to logfile
	save_event_to_file(gfx_type, race_title_val, match_val, csv_string) #save event to .csv
	
	
def import_file(): 
	filename = tkFileDialog.askopenfilename()
	if filename: 
		file = open(filename, 'r')
		data_list = file.readlines() #read file into a list
		data_list = map(lambda s: s.rstrip(), data_list) #remove newline
		if(data_list[0] == 'race_intro'): graphic_type.set("0")
		if(data_list[0] == 'start_list'): graphic_type.set("1")
		if(data_list[0] == 'nameplate'): 
			graphic_type.set("2")
			return
		if(data_list[0] == 'winner'): graphic_type.set("3")
		if(data_list[0] == 'results'): graphic_type.set("4")
		change_img() #change image after gfx_type is set
		race_title_entry_value.set(data_list[1].split(',')[0])  #set race title to line 2, cell 1
		match_entry_value.set(data_list[1].split(',')[1]) #set match to line 2, cell 2
		for x in range(0, 7):
			try:
				school_name_value[x].set(data_list[x+2].split(',')[1])
				swimmer_name_value[x].set(data_list[x+2].split(',')[2])
				race_time_value[x].set(data_list[x+2].split(',')[3])
			except: #if out of index (ie no time data), skip
				pass
		
def next_swimmer(): #simple function to increment lane number
		current_num = int(lane_number.get())
		if(current_num == 6): 
			lane_number.set("0")
			return
		lane_number.set(str(current_num+1))
		
#Button(master, pady=3, text="Daktronics Console").grid(row=12,column=0, columnspan=4,pady=(10,15),padx=(15,0),sticky="w")
is_relay = IntVar()
Checkbutton(master, text="Relay", variable=is_relay).grid(row=0, column=5, columnspan=2,padx=(0,10))
Button(master, pady=3, text="Import File...", command=import_file).grid(row=12,column=0, ipadx=5, columnspan=5,pady=(10,15),padx=(10,0),sticky="w")
Button(master, pady=3, text="Live", command=gfx_live_pusher).grid(row=11,column=14,ipadx=10,ipady=4, columnspan=2,rowspan=2)
Button(master, pady=3, text="Next Swimmer", command=next_swimmer).grid(row=12,column=6, columnspan=7)

image_label = Label(master, image=img_list[0]) # image preview
image_label.grid(row=0, column=10, rowspan=4, columnspan=5)

mainloop()













