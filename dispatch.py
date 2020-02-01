import os
import glob
import shutil
import secrets
import schedule
import time

rand = secrets.token_hex(3)
vid_rand = secrets.token_hex(1)

a= os.getcwd()
for file in os.listdir(a):
	if file in glob.glob("*.jpg") or file in glob.glob("*.png") or file in glob.glob("*.jpeg"):
		*_, ext = os.path.splitext(file)
		nuname_img = rand + ext
		try:
			shutil.move(file, "/storage/emulated/0/Pictures/from_downloads")
		except:
			os.rename(file,nuname_img)
			shutil.move(file, "/storage/emulated/0/Pictures/feom_downloads")
			
	elif file in glob.glob("*.pdf") or file in glob.glob("*.docx"):
		_, ext = os.path.splitext(file)
		nuname_pdf = _+ rand + ext
		#shutil.move(file, "/storage/emulated/0/Download/pourleer/")
		try:
			shutil.move(file, "/storage/emulated/0/Download/for_pdf")
		#except FileNotFoundError:
#			pass
		except:
			os.rename(file, nuname_pdf)
			shutil.move(file, "/storage/emulated/0/Download/for_pdf")
			
	elif file in glob.glob("*.mp4") or file in glob.glob("*.mkv"):
		_, ext = os.path.splitext(file)
		nuname_vid = _ + vid_rand + ext
		try:
			shutil.move(file, "/storage/emulated/0/Movies")
		except:
			os.rename(file,nuname_vid)
			shutil.move(file, "/storage/emulated/0/Pictures")
		
		

			
			
		

