from Tkinter import *
from lib.functions import *

team_one = [0]*15 #row data
team_two = [0]*15
strikes = [0]*5
balls=[0]*5
outs = [0]*5

### TEAM 1 INFO ###
lineup = [0]*15
position = [0]*15
number = [0]*15

### TEAM 2 INFO ###
lineup_two = [0]*15
position_two = [0]*15
number_two = [0]*15


def update_data():
	total_team_one = 0
	total_team_two = 0
	for x in range(7):
		if(team_one[x].get() != ''): #if not blank
			total_team_one = total_team_one + int(team_one[x].get()) #increment data
		else:
			continue
	team_one[9].delete(0, END)
	team_one[9].insert(0, total_team_one) #replace field with total
	
	for x in range(7):
		if(team_two[x].get() != ''): #if not blank
			total_team_two = total_team_two + int(team_two[x].get())  #increment data
		else:
			continue
	team_two[9].delete(0, END)
	team_two[9].insert(0, total_team_two) #replace field with total
	print inning_half.get()
	
	

def advance_baserunner(base):
	if(base==1):
		data = first.get()
		first.delete(0, END)
		second.delete(0, END)
		second.insert(0, data)
	if(base==2):
		data = second.get()
		second.delete(0, END)
		third.delete(0, END)
		third.insert(0, data)
	if(base==3):
		third.delete(0, END)

def advance_all():
	data1 = first.get()
	data2 = second.get()
	data3 = third.get()
	first.delete(0, END)
	second.delete(0, END)
	third.delete(0, END)
	second.insert(0, data1)
	third.insert(0, data2)

def next_batter():	
	if(batter_number.get() < 23):
		batter_number.set(batter_number.get()+1)
		return
	batter_number.set(0)
	

master = Tk()
master.resizable(0,0)
master.wm_title("IASAS Swimming 2013 Graphics Console") #program title
master.wm_iconbitmap('icon.ico')



Label(master, text="Nameplate").grid(row=1, column=0, padx=(10,0))




######################### NAMEPLATE ENTRY ##################################
team_one[9] = Entry(master, width=30) #team one runs
team_one[9].config(borderwidth=2, justify=LEFT)
team_one[9].grid(row=2, column=3, padx=3, ipadx=3, ipady=3)
team_one[9].insert(0, "") #set 0

inning_value = StringVar()
inning_value.set("1") # initial value
OptionMenu(master, inning_value, "TAS", "SAS", "ISB", "ISM", "ISKL", "JIS").grid(row=2,column=0,columnspan=2)


######################### INNING ##########################################
inning_half = IntVar()
Radiobutton(master, text="T", variable=inning_half, value='0').grid(row=3,column=3,columnspan=2,sticky='w')
Radiobutton(master, text="B", variable=inning_half, value='1').grid(row=3,column=4,columnspan=2,sticky='w')
Label(master, text='Inning:').grid(row=3,column=0,columnspan=1,sticky='e')


###################### STRIKES AND BALLS ##############################
Label(master, text='Strikes').grid(row=3,column=5,sticky='e',pady=10, columnspan=2) # strikes 
strikes[0] = IntVar()
strikes[1] = IntVar()
strikes[2] = IntVar()
Checkbutton(master, variable=strikes[0]).grid(row=3,column=7,padx=0)
Checkbutton(master, variable=strikes[1]).grid(row=3,column=8, padx=0)
Checkbutton(master, variable=strikes[2]).grid(row=3,column=9, padx=0)

Label(master, text='Balls').grid(row=4,column=5,sticky='e',columnspan=2) #balls
balls[0] = IntVar()
balls[1] = IntVar()
balls[2] = IntVar()
balls[3] = IntVar()
Checkbutton(master, variable=balls[0]).grid(row=4, column=7, padx=0)
Checkbutton(master, variable=balls[1]).grid(row=4, column=8, padx=0)
Checkbutton(master, variable=balls[2]).grid(row=4, column=9, padx=0)
Checkbutton(master, variable=balls[3]).grid(row=4, column=10, padx=0)

######################## OUTS ####################################

Label(master, text='Outs').grid(row=4,column=1,sticky='w', columnspan=2) # strikes 
outs[0] = IntVar()
outs[1] = IntVar()
outs[2] = IntVar()
Checkbutton(master, variable=outs[0]).grid(row=4,column=2,padx=0)
Checkbutton(master, variable=outs[1]).grid(row=4,column=3, padx=0)
Checkbutton(master, variable=outs[2]).grid(row=4,column=4, padx=0)

######################### BASE RUNNERS ################################
Label(master, text='1B').grid(row=1,column=10,sticky='e',padx=(10,0)) #label 
first = Entry(master, width=15) #1B
first.config(borderwidth=2, justify=LEFT)
first.grid(row=1, column=11, padx=3, ipadx=1, ipady=1) 
Button(master, text="C", command=lambda:first.delete(0, END)).grid(row=1,column=12,padx=(0,10)) 
Button(master, text="Advance", command=lambda:advance_baserunner(1)).grid(row=1,column=13,padx=(0,10)) 

Label(master, text='2B').grid(row=2,column=10,sticky='e',padx=(10,0))
second = Entry(master, width=15) #2B
second.config(borderwidth=2, justify=LEFT)
second.grid(row=2, column=11, padx=3, ipadx=1, ipady=1)
Button(master, text="C", command=lambda:second.delete(0, END)).grid(row=2,column=12,padx=(0,10))
Button(master, text="Advance", command=lambda:advance_baserunner(2)).grid(row=2,column=13,padx=(0,10)) 

Label(master, text='3B').grid(row=3,column=10,sticky='e',padx=(10,0))
third = Entry(master, width=15) #3B
third.config(borderwidth=2, justify=LEFT)
third.grid(row=3, column=11, padx=3, ipadx=1, ipady=1)
Button(master, text="C", command=lambda:third.delete(0, END)).grid(row=3,column=12,padx=(0,10))
Button(master, text="Advance", command=lambda:advance_baserunner(3)).grid(row=3,column=13,padx=(0,10)) 

Button(master, text="Advance All", command=lambda:advance_all()).grid(row=4,column=12,padx=(0,10),columnspan=2) 




######################## LINEUPS #############################################
Label(master, text='Lineups').grid(row=5,column=1,columnspan=2,sticky='w')

for x in range(0, 12): #12 man lineup
	lineup[x] = Entry(master, width=15)
	lineup[x].config(borderwidth=2)
	lineup[x].grid(row=x+7, column=1, padx=1, pady=0, columnspan=4, sticky='w')
	position[x] = Entry(master, width=2)
	position[x].config(borderwidth=2, justify=CENTER)
	position[x].grid(row=x+7, column=4, padx=1, pady=0, ipadx=2, sticky='e')
	number[x] = Entry(master, width=2)
	number[x].config(borderwidth=2, justify=CENTER)
	number[x].grid(row=x+7, column=5, padx=1, pady=0, ipadx=2, sticky='w')
	
Label(master, text='Name').grid(row=6, column=1, sticky='w', columnspan=2)
Label(master, text='Pos.').grid(row=6, column=4, columnspan=2, sticky='w', padx=(5,0))
Label(master, text='#').grid(row=6, column=5, columnspan=2, sticky='w', padx=(5,0))


for x in range(0, 12): #12 man lineup 2
	lineup_two[x] = Entry(master, width=15)
	lineup_two[x].config(borderwidth=2)
	lineup_two[x].grid(row=x+7, column=7, padx=1, pady=0, columnspan=4, sticky='w')
	position_two[x] = Entry(master, width=2)
	position_two[x].config(borderwidth=2, justify=CENTER)
	position_two[x].grid(row=x+7, column=10, padx=12, pady=0, ipadx=2, columnspan=2, sticky='w')
	number_two[x] = Entry(master, width=2)
	number_two[x].config(borderwidth=2, justify=CENTER)
	number_two[x].grid(row=x+7, column=11, padx=(7,0), pady=0, ipadx=2, sticky='w')
	
Label(master, text='Name').grid(row=6, column=7, sticky='w', columnspan=2)
Label(master, text='Pos.').grid(row=6, column=10, columnspan=2, sticky='w', padx=(5,0))
Label(master, text='#').grid(row=6, column=11, columnspan=2, sticky='w', padx=(5,0))


batter_number = IntVar()
for x in range(7, 19):
	Radiobutton(master,  variable=batter_number, value=x-7).grid(row=x,column=0,columnspan=1,sticky='e')
for x in range(19, 31):
	Radiobutton(master,  variable=batter_number, value=x-7).grid(row=x-12,column=6,columnspan=1,sticky='e')

	
def update_1B(): #increment singles
	batter = batter_number.get()
	old_singles = int(xml.singles(batter))
	xml.singles_w(batter, str(old_singles+1)) # write new value
	string = 'Single for %s - %s total' %(xml.name(batter), str(old_singles+1))
	console_log.set(string) #console log

def update_2B():
	batter = batter_number.get()
	old_doubles = int(xml.doubles(batter))
	xml.doubles_w(batter, str(old_doubles+1))
	string = 'Double for %s - %s total' %(xml.name(batter), str(old_doubles+1))
	console_log.set(string) #console log
	
def update_3B(): 
	batter = batter_number.get()
	old_triples = int(xml.triples(batter))
	xml.triples_w(batter, str(old_triples+1))
	string = 'Triple for %s - %s total' %(xml.name(batter), str(old_triples+1))
	console_log.set(string) #console log

def update_HR():
	batter = batter_number.get()
	old_homeruns = int(xml.homeruns(batter))
	xml.homeruns_w(batter, str(old_homeruns+1))
	string = 'Home run for %s - %s total' %(xml.name(batter), str(old_homeruns+1))
	console_log.set(string) #console log
	
	
################### ALL BUTTONS ######################
Button(master, text="Next Batter", command=next_batter).grid(row=19,column=0,columnspan=3, padx=(10,0),sticky='w')
Button(master, text="1B", command=update_1B).grid(row=19,column=2,columnspan=1, padx=(10,0))
Button(master, text="2B", command=update_2B).grid(row=19,column=3,columnspan=1)
Button(master, text="3B", command=update_3B).grid(row=19,column=4,columnspan=1)
Button(master, text="HR", command=update_HR).grid(row=19,column=5,columnspan=1)
Button(master, text="BB").grid(row=19,column=6,columnspan=1)
Button(master, text="SO").grid(row=19,column=7,columnspan=1)
Button(master, text="OUT").grid(row=19,column=8,columnspan=2, sticky='w')




###################### PBP and YouTube Highlights #############################
Label(master, text='Play-by-Play').grid(row=6, column=14, columnspan=3, sticky='w')
pbp=Text(master, width=35, height=3, borderwidth=2)
pbp.grid(row=7, column=14, rowspan=3,columnspan=10, sticky='nw', ipady=10)
new_pbp = IntVar()
Checkbutton(master, variable=new_pbp, text='New').grid(row=6, column=14, columnspan=2)


Label(master, text='New Highlight').grid(row=10, column=14, columnspan=3, sticky='w')
video_highlight = Entry(master, width=47)
video_highlight.config(borderwidth=2)
video_highlight.grid(row=11, column=14, columnspan=10, sticky='nw')
new_video = IntVar()
Checkbutton(master, variable=new_video, text='New').grid(row=10, column=14, sticky='w')


######################## SUBMIT BUTTONS #####################################
def xml_test():
	xml.write('output.xml')
	console_log.set('Data written to output.xml')

	
console_log = StringVar()
Label(master, textvariable=console_log).grid(row=101, column=0, columnspan=10, sticky='w')
Button(master, pady=3, text="Update XML", command=xml_test).grid(row=100,column=12,pady=5,padx=5, columnspan=2)
Button(master, pady=3, text="Upload FTP", command=update_data).grid(row=100,column=10,pady=5,padx=5, columnspan=2, sticky='e')

mainloop()












