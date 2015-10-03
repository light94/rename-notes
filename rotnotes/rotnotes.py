import os
def rename(directory,rot= False):
	os.chdir(directory)
	e = os.listdir(directory)
	e.sort() 
	a = len(e)

	for i in range(0,a):
		os.rename(e[i],str(i+1)+".jpg")

	if rot:
		try:
			from PIL import Image
		except:
			return 'You have not installed all dependencies for the app. Please cd to the location where you downloaded the project and do pip install -r requirements.txt'

		files = os.listdir(os.getcwd())
		for file in files:
			im = Image.open(file)
			length,breadth = im.size
			if length>breadth :
				newimage = im.rotate(-90)
				newimage.save(file)



