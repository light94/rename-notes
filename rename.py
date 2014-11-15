import os


e = os.listdir(os.getcwd())
e.sort() #really inefficient, will improve later

a = len(e)

for i in range(0,a):
	os.rename(e[i],str(i+1)+".jpg")

