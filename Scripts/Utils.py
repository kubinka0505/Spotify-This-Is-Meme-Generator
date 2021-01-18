def Trans_Paste(Background: Image, Foreground: Image, Margin: set) -> Image:
	"""Pasting transparent `Foreground` to `Background`."""
	FRGRND_TRNS = Image.new("RGBA", Background.size)
	#---#
	FRGRND_TRNS.paste(Foreground, Margin, mask = Foreground)
	#---#
	IMG_RET = Image.alpha_composite(Background, FRGRND_TRNS)
	return IMG_RET

def Random_String(Length: int = 16) -> str:
	"""Random string creation used in saving files."""
	return "".join(choice(printable[0:62]) for String in range(Length))