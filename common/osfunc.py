#!/usr/bin/env python
# coding=utf8
import os
import sys
import shutil
from common import log

def filename(path):
	if file_exists(path):
		return os.path.basename(path)
	return None
# 判断文件夹是否存在
def file_exists(path):
	return os.path.exists(path)

# 删除这个文件夹
def rm_file(path,logflag=True):
	if file_exists(path):
		os.remove(path)
	if logflag:	
		log.LOG.info('rm file %s suc'%(path))


# 新建文件夹
def mkdir(path):
	if not file_exists(path):
		os.makedirs(path)


# 删除文件夹
def rmdir(path):
	shutil.rmtree(path)


def read_file(filename):
	hfile = None
	try:
		hfile = open(filename)
		if hfile:
			return hfile.read()
	except IOError as e:
		print('% read failed' \
			  ', msg:%s'%(filename, e))
	finally:
		if hfile:
			hfile.close()
	return None


def write_file(filename, data, mode):
	hfile = None
	try:
		file_path = os.path.dirname(filename)
		if file_path != '' and not os.path.exists(file_path):
			os.makedirs(file_path)
		tmpname = '%s_tmp'%(filename)
		hfile = open(tmpname, mode)
		if hfile:
			hfile.write(data)
			if os.path.isfile(filename):
				os.remove(filename)
			os.rename(tmpname, filename)
			return True
	except IOError as e:
		print('%s write failed, msg:%s'%(filename, e))
	finally:
		if hfile:
			hfile.close()
	return False


def cp_file(src, dest):
	data = read_file(src)
	if data:
		write_file(dest, data, "w")
		return True
	return False


def move_file(src, dest):
	if os.path.exists(src):
		#shutil.move(src, dest)
		shutil.copy(src, dest)
		rm_file(src)


def rename_file(src, dest):		
	if os.path.exists(src):
		os.rename(src, dest)		
	return True	


def walk_dir(dir, recursion=False):
	lists = []
	for root, dirs, files in os.walk(dir):
		if (not recursion) and root != dir:
			continue
		for f in files:
			lists.append(os.path.join(root, f))
	return lists


def getsize(file):		
	if os.path.exists(file):
		return os.path.getsize(file)		
	return 0


if __name__ == "__main__":
	print(cp_file('/mnt/hgfs/share/ubuntu_code_exchange/ailife/common/00.png', '/mnt/hgfs/share/ubuntu_code_exchange/ailife/common/source/00.png'))
