#!/usr/bin/env python

"""
Pandoc filter to convert English text to xepersian compatible format
"""

from pandocfilters import toJSONFilter, Str, RawInline
import locale
import logging
import os

log = logging.getLogger(os.path.basename(__file__))

def configure_logging():
	format_string = "%(name)s: [%(levelname)s] %(message)s"
	logging.basicConfig(format=format_string, level=logging.DEBUG)
	#log.debug("Debug logging enabled.")

def IsNumber(x):
     import re
     if re.match("^\d*.?\d*$", x) == None:
         return False
     return True
	
def behead(key, value, format, meta):

	if format == 'latex':
		if key == 'Str':
			try:
				# if there is no exception this is english text
				value.encode('ascii')
				# Just change non numeric values
				if not IsNumber(value):
					return RawInline('latex', '\\lr{'+value+'}')
			except UnicodeEncodeError:
				#log.info( "string is UTF-8")
				pass
	

if __name__ == "__main__":
	configure_logging()
	toJSONFilter(behead)
