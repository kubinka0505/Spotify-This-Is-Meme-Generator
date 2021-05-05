"""Spotify "This Is" meme generator.

Pack of scripts providing "This Is (Spotify Artist)"
meme generation, but this time You can input your
own text and picture using `Config.json` file.
"""

import os
import numpy as np
from json import load
from math import sqrt
from requests import get
from os.path import dirname
from platform import system
from string import printable
from random import choice, randint as rint
from PIL import Image, ImageDraw, ImageEnhance, ImageFile, ImageFont, PngImagePlugin

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__
__version__		= "1.1.4"
__date__		= "11.01.2021"
__status__		= "Development"
__license__		= "GPL V3"

#---#

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image_Base = Image.new(size = (1000,) * 2, mode = "RGBA", color = "white")
Draw = ImageDraw.Draw(Image_Base)

#---#

exec(open("Scripts/Utils.pyw").read())		# import Scripts/Utils.py
print("Setting up utils...")

Config = load(open("Config.json", encoding = "utf-8"))

exec(open("Scripts/Text_1.pyw").read())		# import Scripts/Text_1.py
print("Applying title...")

exec(open("Scripts/Text_2.pyw").read())		# import Scripts/Text_2.py
print("Applying artist name...")

exec(open("Scripts/Gradient.pyw").read())	# import Scripts/Gradient.py
print("Creating gradient...")

exec(open("Scripts/Paste.pyw").read())		# import Scripts/Paste.py
print("Applying artist image...")

#---#

__Path = "Images/{0}_{1}.{2}"
__Name = Config["Text"]["Content"].\
	replace(" ", "_").\
	replace("\\", "_").\
	replace("/", "_").\
	replace(":", "_").\
	replace("*", "_").\
	replace("?", "_").\
	replace('"', "_").\
	replace("<", "_").\
	replace(">", "_").\
	replace("|", "_").\
	encode().decode("utf-8", errors = "strict")

__Meta = PngImagePlugin.PngInfo()
__Meta.__dict__ = {
	"chunks":
		[
			(b"tEXt",
			bytes("Text\x00{0}".format(Config["Text"]["Content"]),
				encoding = "utf-8")
				),
			(b"tEXt",
			bytes("Image\x00{0}".format(Config["Image"]["URL / Path"]),
				encoding = "utf-8")
				)
		]
	}

#---#

__FilePath = __Path.format(__Name, Random_String(8), "png")
Text_1.convert("RGB").save(__FilePath, pnginfo = __Meta)

if Config["Settings"]["Optimize"]["Enabled"]:
	print("Optimizing...")
	exec(open("Scripts/PNGQuant_Location.pyw").read())
	os.system('{0} {1} --ext .png --force -s {2} --quality 100 --skip-if-larger "{3}"'.format(
		__PNGQuant,
		Config["Settings"]["Optimize"]["PNGQuant"]["Colors"],
		Config["Settings"]["Optimize"]["PNGQuant"]["Speed"],
		__FilePath
		)
	)

print("Done!")