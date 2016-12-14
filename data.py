from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from numpy import random
import numpy as np
import argparse
from random import randint
def create_image():
    	size = (72, 32)     #size of canvas
	font = ImageFont.truetype('SignPainter.ttc', 28)	
	# equation:
	num1 = "9"
	op = "-"
	num2 = "9"
	rand_x1 = randint(0, 6)
	rand_x2 = randint(42, 47)
	#initialize index of image
	n = 1
	
	#loop over rotation: num1, num2 
	for x1 in np.arange(start=rand_x1, step=5, stop=14):#3,6
		#for y1 in np.arange(start=3, step=2, stop=6):#2,5
		for y1 in np.arange(start=3, step=2, stop=6):#2,5
			for xOp in np.arange(start=28, step=2, stop=33):#30, 37
				for yOp in np.arange(start=1, step=3, stop=8):#1,8
					for x2 in np.arange(start=rand_x2, step=4, stop=55):#52, 55
						for y2 in np.arange(start=3, step=2, stop=6):#2,5
						#for y2 in np.arange(start=2, step=2, stop=5):#for 2
							for r1 in np.arange(start=-5, step=8, stop=41):#-15, 60
								for r2 in np.arange(start=-5, step=8, stop=41):
    									input_img = Image.new("RGB", size, (0, 0, 0))
    									draw_input = ImageDraw.Draw(input_img)
									draw_input.text((x1, y1), num1, (255,255,255), font=font)
									draw_input.text((xOp, yOp), op, (255,255,255), font=font)
									draw_input.text((x2, y2), num2, (255,255,255), font=font)
									input_name = str(n).zfill(7) + ".JPEG"	
									input_img.save(input_name)
									n += 1
							
									#rotate
									current_image = Image.open(input_name)	
									crop_num1 = current_image.crop((0,0,29,32)).rotate(r1)
    									current_image.paste(crop_num1, (0,0))
									current_image.save(input_name)										
									crop_num2 = current_image.crop((41, 0, 72, 32)).rotate(r2)
									current_image.paste(crop_num2, (41,0))
									current_image.save(input_name)
	
#	for x1 in np.arange(start=1, step=2, stop=2):#3,6
#		for y1 in np.arange(start=3, step=2, stop=6):#2,5
#			for xOp in np.arange(start=30, step=2, stop=31):#30, 37
#				for yOp in np.arange(start=1, step=2, stop=8):#1,8
#					for x2 in np.arange(start=54, step=2, stop=55):#52, 55
#						#for y2 in np.arange(start=2, step=2, stop=5):#for 2
#						for y2 in np.arange(start=3, step=2, stop=6):#2,5
#							for r1 in np.arange(start=-5, step=5, stop=41):#-15, 60
#								for r2 in np.arange(start=-5, step=5, stop=41):
#    									input_img = Image.new("RGB", size, (0, 0, 0))
#    									draw_input = ImageDraw.Draw(input_img)
#									draw_input.text((x1, y1), num1, (255,255,255), font=font)
#									draw_input.text((xOp, yOp), op, (255,255,255), font=font)
#									draw_input.text((x2, y2), num2, (255,255,255), font=font)
#									input_name = str(n).zfill(7) + ".JPEG"	
#									input_img.save(input_name)
#									n += 1
#							
#									#rotate
#									current_image = Image.open(input_name)	
#									crop_num1 = current_image.crop((0,0,29,32)).rotate(r1)
#    									current_image.paste(crop_num1, (0,0))
#									current_image.save(input_name)										
#									crop_num2 = current_image.crop((41, 0, 72, 32)).rotate(r2)
#									current_image.paste(crop_num2, (41,0))
#									current_image.save(input_name)
#
#	for x1 in np.arange(start=13, step=2, stop=14):#3,6
#		for y1 in np.arange(start=3, step=2, stop=6):#2,5
#			for xOp in np.arange(start=28, step=2, stop=29):#30, 37
#				for yOp in np.arange(start=1, step=2, stop=8):#1,8
#					for x2 in np.arange(start=46, step=2, stop=47):#52, 55
#						#for y2 in np.arange(start=2, step=2, stop=5):#for 2
#						for y2 in np.arange(start=3, step=2, stop=6):#2,5
#							for r1 in np.arange(start=-5, step=5, stop=41):#-15, 60
#								for r2 in np.arange(start=-5, step=5, stop=41):
#    									input_img = Image.new("RGB", size, (0, 0, 0))
#    									draw_input = ImageDraw.Draw(input_img)
#									draw_input.text((x1, y1), num1, (255,255,255), font=font)
#									draw_input.text((xOp, yOp), op, (255,255,255), font=font)
#									draw_input.text((x2, y2), num2, (255,255,255), font=font)
#									input_name = str(n).zfill(7) + ".JPEG"	
#									input_img.save(input_name)
#									n += 1
#							
#									#rotate
#									current_image = Image.open(input_name)	
#									crop_num1 = current_image.crop((0,0,29,32)).rotate(r1)
#    									current_image.paste(crop_num1, (0,0))
#									current_image.save(input_name)										
#									crop_num2 = current_image.crop((41, 0, 72, 32)).rotate(r2)
#									current_image.paste(crop_num2, (41,0))
#									current_image.save(input_name)
#	for x1 in np.arange(start=9, step=2, stop=10):#3,6
#		for y1 in np.arange(start=3, step=2, stop=6):#2,5
#			for xOp in np.arange(start=32, step=2, stop=33):#30, 37
#				for yOp in np.arange(start=1, step=2, stop=8):#1,8
#					for x2 in np.arange(start=42, step=2, stop=43):#52, 55
#						#for y2 in np.arange(start=2, step=2, stop=5):#for 2
#						for y2 in np.arange(start=3, step=2, stop=6):#2,5
#							for r1 in np.arange(start=-5, step=5, stop=41):#-15, 60
#								for r2 in np.arange(start=-5, step=5, stop=41):
#    									input_img = Image.new("RGB", size, (0, 0, 0))
#    									draw_input = ImageDraw.Draw(input_img)
#									draw_input.text((x1, y1), num1, (255,255,255), font=font)
#									draw_input.text((xOp, yOp), op, (255,255,255), font=font)
#									draw_input.text((x2, y2), num2, (255,255,255), font=font)
#									input_name = str(n).zfill(7) + ".JPEG"	
#									input_img.save(input_name)
#									n += 1
#							
#									#rotate
#									current_image = Image.open(input_name)	
#									crop_num1 = current_image.crop((0,0,29,32)).rotate(r1)
#    									current_image.paste(crop_num1, (0,0))
#									current_image.save(input_name)										
#									crop_num2 = current_image.crop((41, 0, 72, 32)).rotate(r2)
#									current_image.paste(crop_num2, (41,0))
#									current_image.save(input_name)

	print n
def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-n', '--num_samples', metavar='n', type=int, default=1, help='Number of sample')
	
	args = parser.parse_args()
	n = args.num_samples
	create_image()


if __name__ == '__main__':
	main()


