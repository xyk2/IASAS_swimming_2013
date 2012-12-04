import Image, ImageDraw, ImageFont
import os
import urllib #import library for HTML 


title = 'Boys 50m Freestyle'
race = 'Finals-A'
lane_one_swimmer = 'Phillip TENG'
lane_one_time = 'iasas record  23.21'
lane_two_swimmer = 'Daryl TONG'
lane_two_time = '24.94'
lane_three_swimmer = 'Justin HSU'
lane_three_time = '25.24'
lane_four_swimmer = 'Lucas LIN'
lane_four_time = '25.41'
lane_five_swimmer = 'Ryan NAM'
lane_five_time = '26.32'
lane_six_swimmer = 'Ian SILVERSTEIN'
lane_six_time = '26.57'
lane_seven_swimmer = 'Alex TAI'
lane_seven_time = ' '



im = Image.open(r"swimming_text_removed_single.png")
tas = Image.open(r"school_graphics/tas.png")
sas = Image.open(r"school_graphics/sas.png")
ism = Image.open(r"school_graphics/ism.png")
iskl = Image.open(r"school_graphics/iskl.png")
isb = Image.open(r"school_graphics/isb.png")
jis = Image.open(r"school_graphics/jis.png")

draw = ImageDraw.Draw(im)

# use a bitmap font
font = ImageFont.truetype(r"arialnbi.ttf", 36)
draw.text((280, 225), title, font=font, fill='black') # TITLE
draw.text((277, 222), title, font=font, fill='white')

font = ImageFont.truetype(r"arialnbi.ttf", 25)
draw.text((280, 264), race, font=font, fill='#262626') #RACE



######################### SCHOOL NAME ##########################################
font = ImageFont.truetype(r"arialnbi.ttf", 20)
draw.text((255-font.getsize('TAS')[0], 298), 'TAS', font=font, fill='black') #lane 1
draw.text((257-font.getsize('TAS')[0], 296), 'TAS', font=font, fill='white')
im.paste(tas, (260,298), tas)

draw.text((255-font.getsize('SAS')[0], 330), 'SAS', font=font, fill='black') #lane 1
draw.text((257-font.getsize('SAS')[0], 328), 'SAS', font=font, fill='white')
im.paste(sas, (260,330), sas)

draw.text((255-font.getsize('ISM')[0], 362), 'ISM', font=font, fill='black') #lane 1
draw.text((257-font.getsize('ISM')[0], 360), 'ISM', font=font, fill='white')
im.paste(ism, (260,362), ism)

draw.text((255-font.getsize('ISB')[0], 394), 'ISB', font=font, fill='black') #lane 1
draw.text((257-font.getsize('ISB')[0], 392), 'ISB', font=font, fill='white')
im.paste(isb, (260,394), isb)

draw.text((255-font.getsize('JIS')[0], 426), 'JIS', font=font, fill='black') #lane 1
draw.text((257-font.getsize('JIS')[0], 424), 'JIS', font=font, fill='white')
im.paste(jis, (260,426), jis)

draw.text((255-font.getsize('ISKL')[0], 458), 'ISKL', font=font, fill='black') #lane 1
draw.text((257-font.getsize('ISKL')[0], 456), 'ISKL', font=font, fill='white')
im.paste(iskl, (260,458), iskl)

draw.text((255-font.getsize('TAS')[0], 490), 'TAS', font=font, fill='black') #lane 1
draw.text((257-font.getsize('TAS')[0], 488), 'TAS', font=font, fill='white')
im.paste(tas, (260,490), tas)

############################# NAMES ##################################################
font = ImageFont.truetype(r"arialnbi.ttf", 26)
draw.text((310, 298), lane_one_swimmer, font=font, fill='black') #lane 1 name
draw.text((312, 296), lane_one_swimmer, font=font, fill='white')

draw.text((310, 330), lane_two_swimmer, font=font, fill='black') #lane 2 name
draw.text((312, 328), lane_two_swimmer, font=font, fill='white')

draw.text((310, 362), lane_three_swimmer, font=font, fill='black') #lane 3 name
draw.text((312, 360), lane_three_swimmer, font=font, fill='white')

draw.text((310, 394), lane_four_swimmer, font=font, fill='black') #lane 4 name
draw.text((312, 392), lane_four_swimmer, font=font, fill='white')

draw.text((310, 426), lane_five_swimmer, font=font, fill='black') #lane 4 name
draw.text((312, 424), lane_five_swimmer, font=font, fill='white')

draw.text((310, 458), lane_six_swimmer, font=font, fill='black') #lane 4 name
draw.text((312, 456), lane_six_swimmer, font=font, fill='white')

draw.text((310, 490), lane_seven_swimmer, font=font, fill='black') #lane 4 name
draw.text((312, 488), lane_seven_swimmer, font=font, fill='white')


##################### TIMES #################################
font = ImageFont.truetype(r"arialnbi.ttf", 24) # TIMES
draw.text((885-font.getsize(lane_one_time)[0], 297), lane_one_time, font=font, fill='black')
draw.text((883-font.getsize(lane_one_time)[0], 295), lane_one_time, font=font, fill='white')

draw.text((885-font.getsize(lane_two_time)[0], 329), lane_two_time, font=font, fill='black')
draw.text((883-font.getsize(lane_two_time)[0], 327), lane_two_time, font=font, fill='white')

draw.text((885-font.getsize(lane_three_time)[0], 361), lane_three_time, font=font, fill='black')
draw.text((883-font.getsize(lane_three_time)[0], 359), lane_three_time, font=font, fill='white')

draw.text((885-font.getsize(lane_four_time)[0], 393), lane_four_time, font=font, fill='black')
draw.text((883-font.getsize(lane_four_time)[0], 391), lane_four_time, font=font, fill='white')

draw.text((885-font.getsize(lane_five_time)[0], 426), lane_five_time, font=font, fill='black')
draw.text((883-font.getsize(lane_five_time)[0], 424), lane_five_time, font=font, fill='white')

draw.text((885-font.getsize(lane_six_time)[0], 458), lane_six_time, font=font, fill='black')
draw.text((883-font.getsize(lane_six_time)[0], 456), lane_six_time, font=font, fill='white')

draw.text((885-font.getsize(lane_seven_time)[0], 490), lane_seven_time, font=font, fill='black')
draw.text((883-font.getsize(lane_seven_time)[0], 488), lane_seven_time, font=font, fill='white')
del draw



# write to stdout
im.save('helloworld.png', "PNG")
raw_input("Graphic generated.")
