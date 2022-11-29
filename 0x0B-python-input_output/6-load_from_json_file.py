#!/usr/bin/python3

"""a function that writes an object to
a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
	"""returns the object from its json representation to the string"""
	with open(filename, 'w', encoding="utf-8") as myfile:
		json.dump(my_obj, myfile)
