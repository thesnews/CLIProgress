"""
 Title: CLIProgress

 File: cliprogress.py
  Provides dirt simple command line progress indicator
  
 Version:
  2010.09.01
  
 Copyright:
  2004-2011 The State News, Inc
  
 Author:
  Mike Joseph <josephm5@msu.edu>
  
 License:
  GNU GPL 2.0 - http://opensource.org/licenses/gpl-2.0.php
"""
import sys
from itertools import cycle

cyc = cycle('-\|/')
currentOut = ''

"""
 Function: start
  Begin a new indicator line
 
 Parameters:
  str - _string_
  
 Returns:
  _void_

 Namespace:
  cliprogress
"""
def start(str) :
	global currentOut
	currentOut = str
	sys.stdout.write(currentOut)


"""
 Function: tick
  Indicate forward momentum
 
 Parameters:
  _void_
  
 Returns:
  _void_

 Namespace:
  cliprogress
"""
def tick() :
	sys.stdout.write("\r%s %s" % (currentOut, cyc.next()))
	sys.stdout.flush()


"""
 Function: finish
  Finish this transaction
 
 Parameters:
  str - _string_
  
 Returns:
  _void_

 Namespace:
  cliprogress
"""
def finish(str) :
	sys.stdout.write("\r%s %s" % (currentOut, str))
	sys.stdout.flush()
	
	sys.stdout.write("\n")
