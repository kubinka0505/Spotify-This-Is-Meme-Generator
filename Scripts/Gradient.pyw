Gradient = Image.new(size = (Image_Base.size[0], Image_Base.size[1]), mode = "RGBA")
Gradient_Draw = ImageDraw.Draw(Gradient)

R, G, B = rint(0, 255), rint(0, 255), rint(0, 255)
DR = (rint(0, 255) - R) / Gradient.size[1]
DG = (rint(0, 255) - R) / Gradient.size[1]
DB = (rint(0, 255) - B) / Gradient.size[1]

for Line in range(Image_Base.size[0]):
	R, G, B = R + DR, G + DG, B + DB
	Gradient_Draw.line((0, Line, Image_Base.size[0], Line), fill = (int(R), int(G), int(B)))

New_Size = round(Gradient.size[0] * sqrt(2)) // 2

if Config["Settings"]["Gradient Rotation"]: __Rotation = rint(1, 180)
else: __Rotation = (-360 + int(Config["Settings"]["Gradient Rotation"])) * -1

Gradient = Gradient.rotate(__Rotation, expand = True, resample = Image.BICUBIC)
Width, Height = Gradient.size

L = (Width - New_Size) // 2
T = (Height - New_Size) // 2
R = (Width + New_Size) // 2
B = (Height + New_Size) // 2

Gradient = Gradient.crop((L, T, R, B))
Gradient = Gradient.resize((Image_Base.size[0], Image_Base.size[1] // 5 * 3))