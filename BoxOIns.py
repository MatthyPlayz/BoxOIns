import urllib

def download_file(url, filename):
	testfile = urllib.URLopener()
	testfile.retrieve(url, filename)

def webIns(insName, insLocationList, filenameList, insDescList):
	defMinPercent = 100 / len(insLocationList)
	print("\n" * 100)
	for i in range(0, len(insLocationList)):
		download_file(insLocationList[i], filenameList[i])
		print("Installing " + insName + ", " + str(defMinPercent) + "% done")
