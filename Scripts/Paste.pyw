Text_1 = Trans_Paste(Image_Base, Text_1, (392, 147))

#---#

if Config["Settings"]["Spotify Logo"]:
	Logo = Image.open(get("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/75px-Spotify_logo_without_text.svg.png", stream = True).raw)
	Logo = Logo.convert("RGBA")
	Logo = ImageEnhance.Color(Logo).enhance(0)
	Logo = ImageEnhance.Brightness(Logo).enhance(1.5)
	Text_1 = Trans_Paste(Text_1, Logo, (38, 38))

#---#

Text_1 = Trans_Paste(Text_1, Text_2, ((Image_Base.size[0] - Text_2.size[0]) // 2, 225))

Artist = Image.open(get(Config["Image"]["URL / Path"], stream = True).raw)
Artist = Artist.convert(mode = "RGBA")

# Remove Background #

if Config["Image"]["Background Color to Remove"] != None:
	Color = tuple(int(Config["Image"]["Background Color to Remove"][1:].upper()[x:x+2], 16) for x in (0, 2, 4))
	Data = Artist.getdata()
	Data_New = []

	for Element in Data:
		if Element[0] == Color[0] and Element[1] == Color[1] and Element[2] == Color[2]:
			Data_New.append((Color[0], Color[1], Color[2], 0))
		else:
			Data_New.append(Element)

	Artist.putdata(Data_New)

# Crop Transparent Pixels #
Artist = Artist.crop(Artist.getbbox())

# Fix resizing #
if Artist.size[0] > Artist.size[1]:
	Size = (Artist.size[0], Artist.size[0])
if Artist.size[0] < Artist.size[1]:
	Size = (Artist.size[1], Artist.size[1])
elif Artist.size[0] == Artist.size[0]:
	Size = (Artist.size[0], Artist.size[0])

Background = Image.new("RGBA", Size, (0,) * 4)
Background = Trans_Paste(Background, Artist, ((Background.size[0] - Artist.size[0]) // 2, Background.size[1] - Artist.size[1]))
Background = Background.resize((Config["Image"]["Max Image Height"],) * 2, Image.LANCZOS)
Background = Background.crop(Background.getbbox())

#---#

Text_1 = Trans_Paste(Text_1, Gradient, (0, - Gradient.size[1] + Image_Base.size[0]))
Text_1 = Trans_Paste(Text_1, Background, ((Image_Base.size[0] - Background.size[0]) // 2, - Background.size[1] + Config["Image"]["Bottom Offset"] + Image_Base.size[0]))