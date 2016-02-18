#!/usr/bin/env python
# Mac Clayton 2016

import os
import shutil
import subprocess
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))


def installGdbHelpersOnLinux():
   gdb_dotfile_path = os.path.join(base_dir, 'gdbinit')
   gdb_path = os.path.join(os.environ['HOME'], '.gdbinit')
   if os.path.exists(gdb_path):
      print 'Removing Existing .gdbinit symlink: %s' % gdb_path
      os.unlink(gdb_path)
   os.symlink(gdb_dotfile_path, gdb_path)

if __name__ == '__main__':
   if sys.platform.startswith('win'):
      print "Windows not supported!"
   elif sys.platform.startswith('linux'):
      installGdbHelpersOnLinux()
      print "Finished!"
   else:
      print 'OS %s not supported' % sys.platform