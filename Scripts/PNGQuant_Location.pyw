__PNGQuant = "PNGQuant"
__PNGQuant_Error_1 = "PNGQuant not found!"
__PNGQuant_Error_2 = "Image will not be optimized."

if not Config["Settings"]["Optimize"][__PNGQuant]["Location"]:
	for File in next(os.walk("."))[2]:
		if os.path.basename(File)[:6] == __PNGQuant.lower():
			try:
				__PNGQuant = os.path.abspath(File)
			except:
				pass
	else:
		__PNGQuant = VariableSearch(Content = __PNGQuant.lower())
		if __PNGQuant:
			if os.path.isfile(__PNGQuant):
				pass
			else:
				print(__PNGQuant_Error_1 + ' ("{0}")'.format(__PNGQuant) + __PNGQuant_Error_2)
else:
	__PNGQuant = os.path.abspath(Config["Settings"]["Optimize"][__PNGQuant]["Location"])
	if os.path.isfile(__PNGQuant):
		pass
	else:
		print(__PNGQuant_Error + "({0})".format(__PNGQuant))