# coding:utf-8

import sys, os, glob, json

def getLayers(path):
	layers_dic = {}
	for root,dirs,files in os.walk(path):
		if root[-17:] == "aboveArrow/images":
			layers_dic["aboveArrow"] = len(glob.glob(root + "/*.png"))
		if root[-17:] == "background/images":
			layers_dic["background"] = len(glob.glob(root + "/*.png"))
		if root[-13:] == "cutout/images":
			layers_dic["cutout"] = len(glob.glob(root + "/*.png"))
		if root[-17:] == "foreground/images":
			layers_dic["foreground"] = len(glob.glob(root + "/*.png"))
		if root[-11:] == "text/images":
			layers_dic["text"] = len(glob.glob(root + "/*.png"))
		if root[-17:] == "underArrow/images":
			layers_dic["underArrow"] = len(glob.glob(root + "/*.png"))
	return layers_dic

def getFonts():
	with open("./resources/json/font.json","r") as lf:
		jsonStr = lf.read()
		dic = json.loads(jsonStr, strict = False)
		list = dic.keys()
	return list

def writeJson(path, dic):
	with open(path, "w") as df:
		jsonStr = json.dumps(dic, sort_keys=True, indent=2, ensure_ascii=False)
		df.write(jsonStr)





	