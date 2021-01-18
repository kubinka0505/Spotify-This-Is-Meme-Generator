Font = ImageFont.truetype("Gotham Bold.otf", 45)

Text_1 = Image.new("RGBA", (300,) * 2, (255, 255, 255, 0))	# Transparent
Draw = ImageDraw.Draw(Text_1)

Draw.text(
	xy = (0,) * 2,
	text = " ".join("THIS IS"),
	fill = (0,) * 3,
	font = Font,
	align = "center"
	)

Text_1 = Text_1.crop(Text_1.getbbox())	# Cropped Text