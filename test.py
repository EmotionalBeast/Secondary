# coding: utf-8
import glob, os

num = glob.glob("./workspace/test/in/10011/aboveArrow/images/*.png")
# print(len(num))

layers = ()
# for root,dirs,files in os.walk("./workspace/test/in/10011"):
# 	if root[-17:] == "aboveArrow/images":
# 		layers += (len(glob.glob(root + "/*.png")),)
# 	if root[-17:] == "background/images":
# 		layers += (len(glob.glob(root + "/*.png")),)
# 	if root[-13:] == "cutout/images":
# 		layers += (len(glob.glob(root + "/*.png")),)
# 	if root[-17:] == "foreground/images":
# 		layers += (len(glob.glob(root + "/*.png")),)
# 	if root[-14:] == "sticker/images":
# 		layers += (len(glob.glob(root + "/*.png")),)
# 	if root[-11:] == "text/images":
# 		layers += (len(glob.glob(root + "/*.png")),)
# 	if root[-17:] == "underArrow/images":
# 		layers += (len(glob.glob(root + "/*.png")),)

layers_dic = {"aboveArrow":"", "background":"", "cutout":"", "foreground":"", "sticker":"", "text":"", "underArrow":""}

for root,dirs,files in os.walk("./workspace/test/in/10011"):
	if root[-17:] == "aboveArrow/images":
		layers_dic["aboveArrow"] = len(glob.glob(root + "/*.png"))
	if root[-17:] == "background/images":
		layers_dic["background"] = len(glob.glob(root + "/*.png"))
	if root[-13:] == "cutout/images":
		layers_dic["cutout"] = len(glob.glob(root + "/*.png"))
	if root[-17:] == "foreground/images":
		layers_dic["foreground"] = len(glob.glob(root + "/*.png"))
	if root[-14:] == "sticker/images":
		layers_dic["sticker"] = len(glob.glob(root + "/*.png"))
	if root[-11:] == "text/images":
		layers_dic["text"] = len(glob.glob(root + "/*.png"))
	if root[-17:] == "underArrow/images":
		layers_dic["underArrow"] = len(glob.glob(root + "/*.png"))

print(layers_dic)