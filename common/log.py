#!/usr/bin/env python
import logging
import logging.handlers
import os
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class Logger(object):
	def __init__(self, logname='LOG', logdir='./', bout=3):
		filename = os.path.basename(sys.argv[0])
		dotidx = filename.rfind('.')
		if dotidx != -1:
			filename = filename[:dotidx]
		self.filename = filename
		self._logger = logging.getLogger(logname)
		self._logger.setLevel(logging.DEBUG)
		self.format = logging.Formatter('[%(process)d][%(asctime)s][%(levelname)s]:%(message)s [%(filename)s:%(funcName)s:%(lineno)d]')
		self.logfile = '%s/%s_%s.log'%(logdir, self.filename, os.getpid())
		self.bout = bout
		self.init = 0
	
	def prelog(self):
		if (self.bout & 1) and not (self.init & 1):
			consolehandle = logging.StreamHandler()
			consolehandle.setFormatter(self.format)
			self._logger.addHandler(consolehandle)
			self.init |= 1
		if (self.bout & 2) and not (self.init & 2):
			filehandle = logging.handlers.TimedRotatingFileHandler(self.logfile, 'D', 1, 5)
			filehandle = logging.handlers.RotatingFileHandler(self.logfile, mode='a',maxBytes=1024*1024*50, backupCount=0)
			filehandle.setFormatter(self.format)
			self._logger.addHandler(filehandle)
			self.init |= 2
	
	def getLog(self):
		self.prelog()
		return self._logger

__single_log = Logger(logdir='../mogileserver/log/', bout=3)

LOG = __single_log.getLog()

if __name__ == "__main__":
	LOG = Logger(logdir='./', bout=3)
	# LOG.info('test')
