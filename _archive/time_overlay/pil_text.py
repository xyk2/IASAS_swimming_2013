import Image, ImageDraw, ImageFont
import os






for x in range(0, 3000):
	text = float(x)*0.02 #50fps, 0.02s per frame
	im = Image.open(r"C:\Users\Xiaoyang\Desktop\Dropbox\IASAS_swim_graphics\time_overlay\test.png")
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(r"C:\Users\Xiaoyang\Desktop\Dropbox\IASAS_swim_graphics\time_overlay\arialnbi.ttf", 27)
	if(text < 10):
		draw.text((869-font.getsize(str('%.2f'%text)[:1]+'.')[0], 582), str('%.2f'%text)[:1]+'.', font=font, fill='black')
	else:
		draw.text((869-font.getsize(str('%.2f'%text)[:2]+'.')[0], 582), str('%.2f'%text)[:2]+'.', font=font, fill='black')

	draw.text((893-font.getsize(str('%.2f'%text)[2:])[0], 582), str('%.2f'%text)[2:], font=font, fill='black')
	im.save(r'C:\Users\Xiaoyang\Desktop\Dropbox\IASAS_swim_graphics\time_overlay\frames\%s.png'%str(x).zfill(4), "PNG")
	#print str(x).zfill(4)
	print str('%.2f'%text)[:1]+'.' + str('%.2f'%text)[2:]
	del draw



# write to stdout
#im.save(r'D:\Dropbox\IASAS_swim_graphics\time_overlay\helloworld.png', "PNG")
#os.system('start %s'%r'D:\Dropbox\IASAS_swim_graphics\time_overlay\helloworld.png')
