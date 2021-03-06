#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:post_process
   Author:jasonhaven
   date:18-11-22
-------------------------------------------------
   Change Activity:18-11-22:
-------------------------------------------------
"""
import json
import os

def get_author_with_organization(data,key):
	result = []
	global count_author_organ
	records = data[key]
	for i, record in enumerate(records):  # 关键词下的论文集合
		for r in record:  # 论文下的作者集合
			author, organs = r[0], r[1]
			result.extend([(author, organ) for organ in organs if organ != 'None'])
		[print(i,rst) for rst in result]
		count_author_organ +=len(result)


def get_author_with_coauthor(data,key):
	result = []
	global count_coauthor
	records = data[key]
	for i, record in enumerate(records):  # 关键词下的论文集合
		coauthors = set()
		for r in record:  # 每个论文下的作者集合
			coauthors.add(r[0])
		result.append(coauthors)
		[print(i,rst) for rst in result]
	count_coauthor += len(result)

def get_from_dir(dir):
	for dirpath, dirnames, filenames in os.walk(dir):
		for fname in filenames:
			fpath=dirpath+os.path.sep+fname
			keyword=fname.split('-')[0]
			with open(fpath, 'r') as f:
				data = json.load(f)
				print("\nauthor-organ\n")
				get_author_with_organization(data,keyword)
				print("\ncoauthor-coauthor\n")
				get_author_with_coauthor(data,keyword)

if __name__ == '__main__':
	# Reading data back
	input_dir = 'data/'
	count_author_organ=0
	count_coauthor=0
	get_from_dir(input_dir)
	print('total:{},{}'.format(count_author_organ,count_coauthor))
