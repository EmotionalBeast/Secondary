# coding:utf-8

import sys, os, glob

def getLayers(path):
	layers_dic = {"aboveArrow":"", "background":"","cutout":"","foreground":"","text":"","underArrow":""}
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


	