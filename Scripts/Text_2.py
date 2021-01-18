Font = ImageFont.truetype("Gotham Bold.otf", 86)

__TXT = Config["Text"]["Content"].replace("''", '"')

Text_2 = Image.new("RGBA", (
	Font.getsize(__TXT)[0],
	Font.getsize(__TXT)[1] // 2 * 3
		),
	(255, 255, 255, 0)
	)	# Transparent
Draw = ImageDraw.Draw(Text_2)

Draw.text(
	xy = (0,) * 2,
	text = __TXT,
	fill = (0,) * 3,
	font = Font,
	align = "center"
	)

Text_2 = Text_2.crop(Text_2.getbbox())	# Cropped Text