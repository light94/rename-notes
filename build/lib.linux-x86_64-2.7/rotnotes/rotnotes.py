import os
def rename(directory,rot= False):
	os.chdir(directory)
	e = os.listdir(directory)
	
	e.sort() 

	a = len(e)

	for i in range(0,a):
		os.rename(e[i],str(i+1)+".jpg")

	if rot!=False:
		from PIL import Image


		files = os.listdir(os.getcwd())

		for file in files:
			im = Image.open(file)
			length,breadth = im.size
			if length>breadth :
				newimage = im.rotate(-90)
				newimage.save(file)



